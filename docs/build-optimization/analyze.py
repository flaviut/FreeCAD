#!/usr/bin/env python3
"""Summarize Clang time traces for ordinary compilations and PCH builds."""

import argparse
import collections
import csv
import json
from pathlib import Path


PHASES = (
    'ExecuteCompiler', 'Frontend', 'Backend', 'Source',
    'InstantiateFunction', 'InstantiateClass', 'Optimizer', 'CodeGenPasses',
)
CSV_FIELDS = (
    'output', 'ninja_s', 'trace_s', 'frontend_s', 'backend_s', 'source_s',
    'instantiate_function_s', 'instantiate_class_s', 'optimizer_s', 'codegen_s',
)
PHASE_FIELDS = {
    'ExecuteCompiler': 'trace_s',
    'Frontend': 'frontend_s',
    'Backend': 'backend_s',
    'Source': 'source_s',
    'InstantiateFunction': 'instantiate_function_s',
    'InstantiateClass': 'instantiate_class_s',
    'Optimizer': 'optimizer_s',
    'CodeGenPasses': 'codegen_s',
}


def job_kind(output):
    if output.endswith(('cmake_pch.hxx.pch', 'cmake_pch.hxx.gch')):
        return 'pch'
    if output.endswith(('.cpp.o', '.cxx.o', '.cc.o', '.c.o')):
        return 'translation_unit'
    return None


def trace_candidates(build_dir, output):
    path = Path(output)
    if not path.is_absolute():
        path = build_dir / path
    if output.endswith('.o'):
        return (Path(str(path)[:-1] + 'json'), Path(str(path) + '.json'))
    return (Path(str(path) + '.json'), path.with_suffix('.json'),
            Path(str(path).removesuffix('.pch').removesuffix('.gch') + '.json'))


def read_log(path):
    entries = {}
    duplicate_count = 0
    malformed_count = 0
    starts = []
    ends = []
    for line in path.read_text().splitlines():
        if line.startswith('#'):
            continue
        fields = line.split('\t')
        if len(fields) < 4:
            malformed_count += 1
            continue
        try:
            start, end = int(fields[0]), int(fields[1])
        except ValueError:
            malformed_count += 1
            continue
        if end < start:
            malformed_count += 1
            continue
        output = fields[3]
        starts.append(start)
        ends.append(end)
        if output in entries:
            duplicate_count += 1
        entries[output] = (start, end)
    return entries, {
        'recorded_start_ms': min(starts) if starts else None,
        'recorded_end_ms': max(ends) if ends else None,
        'recorded_span_s': (max(ends) - min(starts)) / 1000 if starts else None,
        'duplicate_output_entries': duplicate_count,
        'malformed_entries': malformed_count,
    }


def read_trace(path):
    data = json.loads(path.read_text())
    events = data['traceEvents']
    if not isinstance(events, list):
        raise ValueError('traceEvents is not a list')
    phases = {}
    sources = collections.Counter()
    templates = collections.Counter()
    begins = {}
    for event in events:
        name = event.get('name', '')
        phase = event.get('ph')
        if name.startswith('Total ') and phase == 'X':
            phases[name[6:]] = event['dur'] / 1e6
        if name not in ('Source', 'InstantiateFunction', 'InstantiateClass'):
            continue
        if phase == 'b':
            begins[(name, event.get('id'))] = event
            continue
        if phase == 'e':
            begin = begins.pop((name, event.get('id')), None)
            if begin is None:
                continue
            duration = (event['ts'] - begin['ts']) / 1e6
            detail = begin.get('args', {}).get('detail', '')
        elif phase == 'X':
            duration = event.get('dur', 0) / 1e6
            detail = event.get('args', {}).get('detail', '')
        else:
            continue
        if detail:
            (sources if name == 'Source' else templates)[detail] += duration
    return phases, sources, templates


def area(output):
    parts = Path(output).parts
    if len(parts) >= 3 and parts[:2] == ('src', 'Mod'):
        return 'Mod/' + parts[2]
    if len(parts) >= 2 and parts[0] == 'src':
        return 'src/' + parts[1]
    if parts and parts[0] == 'tests':
        return 'tests'
    return parts[0] if parts else '(unknown)'


def ranks(counter, repo_root, limit=100):
    prefix = str(repo_root) + '/'
    return [{'name': name.removeprefix(prefix), 'seconds': seconds}
            for name, seconds in counter.most_common(limit)]


def aggregate(rows, sources, templates, repo_root):
    totals = {phase: sum(row[PHASE_FIELDS[phase]] for row in rows) for phase in PHASES}
    return {
        'count': len(rows),
        'phase_seconds': totals,
        'source_ranking': ranks(sources, repo_root),
        'template_ranking': ranks(templates, repo_root),
    }


def markdown_table(lines, heading, items, label, limit=25):
    lines.extend(['', heading, '', f'| Inclusive s | {label} |', '|---:|---|'])
    for item in items[:limit]:
        lines.append(f"| {item['seconds']:.1f} | {item['name'].replace('|', chr(92) + '|')} |")


def write_report(output_dir, summary, rows_by_kind, local_details):
    tu = rows_by_kind['translation_unit']
    pch = rows_by_kind['pch']
    log = summary['ninja_log']
    diagnostics = summary['diagnostics']
    if log['recorded_span_s'] is None:
        span = 'No timed entries were found in the Ninja log.'
    else:
        span = (f"Recorded Ninja log timestamp span: {log['recorded_span_s']:.1f} s "
                f"({log['recorded_start_ms']}–{log['recorded_end_ms']} ms). "
                'This span is not a complete build wall time if the log contains multiple builds.')
    lines = [
        '# Clang build profile', '',
        f'* {span}',
        f'* Ordinary translation units with traces: {len(tu)}; PCH jobs with traces: {len(pch)}.',
        f"* Missing traces: {len(diagnostics['missing_traces'])}; "
        f"invalid traces: {len(diagnostics['invalid_traces'])}.",
        '* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.',
        '* Source and template rankings sum inclusive event durations. Nested events can overlap, so these totals are not additive.',
        '', '## Compiler phase totals', '',
        '| Phase | Ordinary TU s | PCH s | Combined s |', '|---|---:|---:|---:|',
    ]
    aggregates = summary['aggregates']
    for phase in PHASES:
        vals = [aggregates[kind]['phase_seconds'][phase]
                for kind in ('translation_unit', 'pch', 'combined')]
        lines.append(f'| {phase} | ' + ' | '.join(f'{value:.1f}' for value in vals) + ' |')
    for kind, title in (('translation_unit', 'translation units'), ('pch', 'PCH jobs')):
        lines.extend(['', f'## {title.capitalize()} by Ninja elapsed time', '',
                      '| Ninja s | Compiler s | Frontend s | Backend s | Source s | Output |',
                      '|---:|---:|---:|---:|---:|---|'])
        for row in rows_by_kind[kind][:25]:
            values = (row['ninja_s'], row['trace_s'], row['frontend_s'],
                      row['backend_s'], row['source_s'])
            lines.append('| ' + ' | '.join(f'{value:.1f}' for value in values)
                         + f" | {row['output']} |")
    groups = collections.defaultdict(lambda: [0.0, 0])
    for row in tu:
        group = groups[area(row['output'])]
        group[0] += row['trace_s']
        group[1] += 1
    lines.extend(['', '## Largest ordinary compilation areas', '',
                  '| Area | Compiler s | Translation units |', '|---|---:|---:|'])
    for name, (seconds, count) in sorted(groups.items(), key=lambda item: -item[1][0])[:20]:
        lines.append(f'| {name} | {seconds:.1f} | {count} |')
    for kind, title in (('translation_unit', 'ordinary translation units'),
                        ('pch', 'PCH jobs'), ('combined', 'all traced jobs')):
        aggregate_data = aggregates[kind]
        markdown_table(lines, f'## Included files in {title}',
                       aggregate_data['source_ranking'], 'Source')
        markdown_table(lines, f'## Template instantiations in {title}',
                       aggregate_data['template_ranking'], 'Template')
    lines.extend(['', '## Trace coverage', '',
                  f"* Ninja log entries overwritten for repeated outputs: {log['duplicate_output_entries']}.",
                  f"* Malformed Ninja log entries: {log['malformed_entries']}."])
    for label, key in (('Missing', 'missing_traces'), ('Invalid', 'invalid_traces')):
        items = diagnostics[key]
        lines.extend(['', f'### {label} traces', ''])
        lines.extend(f'* `{item["output"]}`' +
                     (f': {item["error"]}' if 'error' in item else '')
                     for item in items)
        if not items:
            lines.append('None.')
    for row in tu[:5]:
        details = local_details[row['output']]
        lines.extend(['', f'## {row["output"]}', '',
                      f'Ninja {row["ninja_s"]:.1f} s; compiler {row["trace_s"]:.1f} s; '
                      f'frontend {row["frontend_s"]:.1f} s; backend {row["backend_s"]:.1f} s.',
                      '', 'Top included files:', ''])
        lines.extend(f'* {item["seconds"]:.2f} s — {item["name"]}'
                     for item in details['sources'][:10])
        lines.extend(['', 'Top template instantiations:', ''])
        lines.extend(f'* {item["seconds"]:.2f} s — {item["name"]}'
                     for item in details['templates'][:10])
    (output_dir / 'analysis.md').write_text('\n'.join(lines) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build-dir', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--repo-root', type=Path,
                        default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    build_dir = args.build_dir.resolve()
    repo_root = args.repo_root.resolve()
    output_dir = args.output_dir.resolve()
    entries, log_summary = read_log(build_dir / '.ninja_log')
    rows_by_kind = {'translation_unit': [], 'pch': []}
    counters = {kind: (collections.Counter(), collections.Counter())
                for kind in ('translation_unit', 'pch', 'combined')}
    diagnostics = {'missing_traces': [], 'invalid_traces': []}
    local_details = {}
    for output, (start, end) in entries.items():
        kind = job_kind(output)
        if kind is None:
            continue
        candidates = trace_candidates(build_dir, output)
        trace = next((path for path in candidates if path.is_file()), None)
        if trace is None:
            diagnostics['missing_traces'].append({'kind': kind, 'output': output,
                                                  'expected': [str(path) for path in candidates]})
            continue
        try:
            phases, sources, templates = read_trace(trace)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            diagnostics['invalid_traces'].append({'kind': kind, 'output': output,
                                                  'trace': str(trace), 'error': str(exc)})
            continue
        row = {'output': output, 'ninja_s': (end - start) / 1000}
        row.update({field: phases.get(phase, 0.0)
                    for phase, field in PHASE_FIELDS.items()})
        rows_by_kind[kind].append(row)
        for counter_kind in (kind, 'combined'):
            counters[counter_kind][0].update(sources)
            counters[counter_kind][1].update(templates)
        local_details[output] = {'sources': ranks(sources, repo_root),
                                 'templates': ranks(templates, repo_root)}
    for rows in rows_by_kind.values():
        rows.sort(key=lambda row: row['ninja_s'], reverse=True)
    aggregates = {
        kind: aggregate(rows, *counters[kind], repo_root)
        for kind, rows in (*rows_by_kind.items(),
                           ('combined', rows_by_kind['translation_unit'] + rows_by_kind['pch']))
    }
    summary = {'build_dir': str(build_dir), 'repo_root': str(repo_root),
               'ninja_log': log_summary, 'aggregates': aggregates,
               'diagnostics': diagnostics}
    output_dir.mkdir(parents=True, exist_ok=True)
    for kind, filename in (('translation_unit', 'translation-units.csv'),
                           ('pch', 'pch.csv')):
        with (output_dir / filename).open('w', newline='') as file:
            writer = csv.DictWriter(file, CSV_FIELDS)
            writer.writeheader()
            writer.writerows(rows_by_kind[kind])
    (output_dir / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    write_report(output_dir, summary, rows_by_kind, local_details)
    print(f'Wrote analysis.md, summary.json, translation-units.csv, and pch.csv to {output_dir}')


if __name__ == '__main__':
    main()
