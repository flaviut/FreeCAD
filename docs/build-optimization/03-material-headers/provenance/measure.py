import datetime
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import time

label, *targets = sys.argv[1:]
root = Path.cwd()
out = root / 'docs/build-optimization/03-material-headers'
prov = out / 'provenance'
command = ['fc-build'] + (['--target', *targets] if targets else [])
env = os.environ | {'FREECAD_BUILD_DIR': str(root / 'build/clang-profile'), 'FREECAD_BUILD_JOBS': '8'}
build = root / 'build/clang-profile'
def log_entries():
    path = build / '.ninja_log'
    return {line.split('\t')[3]: line for line in path.read_text().splitlines()
            if not line.startswith('#') and len(line.split('\t')) >= 4} if path.exists() else {}
before = log_entries()
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
start = time.monotonic()
with (prov / f'{label}.log').open('w') as stream:
    result = subprocess.run(command, env=env, stdout=stream, stderr=subprocess.STDOUT)
after = log_entries()
changed = {output: line for output, line in after.items() if before.get(output) != line}
dataset = prov / label
dataset.mkdir(exist_ok=True)
(dataset / '.ninja_log').write_text('# ninja log v5\n' + '\n'.join(changed.values()) + '\n')
for output in changed:
    artifact = build / output
    if output.endswith('.o'):
        candidates = [Path(str(artifact)[:-1] + 'json')]
    elif output.endswith('.pch'):
        candidates = [artifact.with_suffix('.json')]
    else:
        continue
    for trace in candidates:
        if trace.is_file():
            dest = dataset / trace.relative_to(build)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(trace, dest)
usage = resource.getrusage(resource.RUSAGE_CHILDREN)
metrics = {'label': label, 'command': command, 'started_utc': started,
           'elapsed_s': time.monotonic() - start, 'exit_code': result.returncode,
           'jobs': 8, 'changed_ninja_outputs': len(changed), 'build_dir': env['FREECAD_BUILD_DIR'],
           'children_user_s': usage.ru_utime, 'children_system_s': usage.ru_stime,
           'max_child_rss_kib': usage.ru_maxrss,
           'memory_note': 'Largest individual child RSS, not aggregate concurrent build memory.'}
(out / f'{label}-metrics.json').write_text(json.dumps(metrics, indent=2) + '\n')
print(json.dumps(metrics, indent=2), flush=True)
sys.exit(result.returncode)
