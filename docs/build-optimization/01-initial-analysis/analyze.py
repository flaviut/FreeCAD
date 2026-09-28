import collections
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parent
repo = root.parent.parent
log = root / '.ninja_log'

entries = {}
for line in log.read_text().splitlines()[1:]:
    fields = line.split('\t')
    if len(fields) < 4:
        continue
    start, end, _, output = fields[:4]
    entries[output] = (int(start), int(end))

units = []
headers = collections.Counter()
templates = collections.Counter()
phase_sum = collections.Counter()
for output, (start, end) in entries.items():
    if not output.endswith(('.cpp.o', '.cxx.o', '.cc.o', '.c.o')):
        continue
    trace = root / (output[:-2] + 'json')
    if not trace.is_file():
        # Clang names the trace after the source suffix: foo.cpp.json.
        trace = root / (output[:-1] + 'json')
    if not trace.is_file():
        continue
    try:
        events = json.loads(trace.read_text())['traceEvents']
    except (OSError, ValueError, KeyError):
        continue
    phases = {}
    local_headers = collections.Counter()
    local_templates = collections.Counter()
    starts = {}
    for event in events:
        name = event.get('name', '')
        ph = event.get('ph')
        if name.startswith('Total ') and ph == 'X':
            phases[name[6:]] = event['dur'] / 1e6
        if name not in ('Source', 'InstantiateFunction', 'InstantiateClass'):
            continue
        if ph == 'b':
            starts[(name, event.get('id'))] = event
            continue
        if ph == 'e':
            begin = starts.pop((name, event.get('id')), None)
            if begin is None:
                continue
            duration = (event['ts'] - begin['ts']) / 1e6
            detail = begin.get('args', {}).get('detail', '')
        elif ph == 'X':
            duration = event.get('dur', 0) / 1e6
            detail = event.get('args', {}).get('detail', '')
        else:
            continue
        if not detail:
            continue
        if name == 'Source':
            local_headers[detail] += duration
        else:
            local_templates[detail] += duration
    headers.update(local_headers)
    templates.update(local_templates)
    phase_sum.update(phases)
    units.append({
        'output': output,
        'ninja_s': (end - start) / 1000,
        'trace_s': phases.get('ExecuteCompiler', 0),
        'frontend_s': phases.get('Frontend', 0),
        'backend_s': phases.get('Backend', 0),
        'source_s': phases.get('Source', 0),
        'instantiate_function_s': phases.get('InstantiateFunction', 0),
        'instantiate_class_s': phases.get('InstantiateClass', 0),
        'optimizer_s': phases.get('Optimizer', 0),
        'codegen_s': phases.get('CodeGenPasses', 0),
        'top_headers': local_headers.most_common(10),
        'top_templates': local_templates.most_common(10),
    })

units.sort(key=lambda row: row['ninja_s'], reverse=True)
groups = collections.defaultdict(lambda: [0.0, 0])
for row in units:
    parts = row['output'].split('/')
    if parts[0] == 'src' and parts[1] == 'Mod':
        group = 'Mod/' + parts[2]
    elif parts[0] == 'src':
        group = 'src/' + parts[1]
    elif parts[0] == 'tests':
        group = 'tests'
    else:
        group = parts[0]
    groups[group][0] += row['trace_s']
    groups[group][1] += 1
with (root / 'translation-units.csv').open('w', newline='') as file:
    fields = [key for key in units[0] if not key.startswith('top_')]
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows({key: row[key] for key in fields} for row in units)

def shortened(path):
    return str(path).replace(str(repo) + '/', '')

lines = [
    '# Clang build profile',
    '',
    f'* Build wall time from Ninja log: {max(end for _, end in entries.values()) / 1000:.1f} s',
    f'* Translation units with traces: {len(units)}',
    f'* Sum of traced compiler time: {phase_sum["ExecuteCompiler"]:.1f} s',
    '* Release build, Clang 21.1.8, `BUILD_ENABLE_TIME_TRACE=ON`, ccache off, 8 compile jobs.',
    '* Ninja durations are elapsed times under parallel load. Trace durations are compiler events; child events overlap parents.',
    '',
    '## Top 25 translation units by Ninja elapsed time',
    '',
    '| Ninja s | Trace s | Frontend s | Backend s | Source s | Function instantiation s | Output |',
    '|---:|---:|---:|---:|---:|---:|---|',
]
for row in units[:25]:
    lines.append('| ' + ' | '.join([
        *(f'{row[key]:.1f}' for key in ('ninja_s', 'trace_s', 'frontend_s', 'backend_s', 'source_s', 'instantiate_function_s')),
        row['output'],
    ]) + ' |')
lines += ['', '## Compiler phase totals', '',
          '| Phase | Sum of TU seconds |', '|---|---:|']
for key in ('ExecuteCompiler', 'Frontend', 'Backend', 'Source', 'InstantiateFunction', 'InstantiateClass', 'Optimizer', 'CodeGenPasses'):
    lines.append(f'| {key} | {phase_sum[key]:.1f} |')
lines += ['', '## Largest source areas', '',
          '| Area | Compiler s | Translation units |', '|---|---:|---:|']
for group, (seconds, count) in sorted(groups.items(), key=lambda item: -item[1][0])[:20]:
    lines.append(f'| {group} | {seconds:.1f} | {count} |')
lines += ['', '## Included files with greatest cumulative trace time', '',
          'These are inclusive header parsing times summed across translation units; nested includes may overlap.', '',
          '| Inclusive s | Header |', '|---:|---|']
for path, seconds in headers.most_common(25):
    lines.append(f'| {seconds:.1f} | {shortened(path)} |')
lines += ['', '## Template instantiations with greatest cumulative trace time', '',
          'These are inclusive event times summed across translation units.', '',
          '| Inclusive s | Template |', '|---:|---|']
for name, seconds in templates.most_common(25):
    lines.append(f'| {seconds:.1f} | {name.replace("|", "\\|")} |')
for row in units[:5]:
    lines += ['', f'## {row["output"]}', '',
              f'Ninja {row["ninja_s"]:.1f} s; compiler {row["trace_s"]:.1f} s; frontend {row["frontend_s"]:.1f} s; backend {row["backend_s"]:.1f} s.',
              '', 'Top included files:', '']
    for name, seconds in row['top_headers'][:10]:
        lines.append(f'* {seconds:.2f} s — {shortened(name)}')
    lines += ['', 'Top template instantiations:', '']
    for name, seconds in row['top_templates'][:10]:
        lines.append(f'* {seconds:.2f} s — {name}')
(root / 'analysis.md').write_text('\n'.join(lines) + '\n')
print('wrote', root / 'analysis.md', 'and', root / 'translation-units.csv')
