import csv
import json
from pathlib import Path
import statistics
import subprocess
import sys
out=Path(__file__).resolve().parent.parent
prov=out/'provenance'
comparison={}
for case in ['targets','documentobject-touch','documentobserver-touch','metatypes-touch']:
    result={}
    sets={}
    for variant in ['baseline','candidate']:
        runs=[]
        sets[variant]=[]
        for i in range(1,4):
            label=f'{variant}-{i}-{case}'
            destination=out/label
            subprocess.run([sys.executable,'docs/build-optimization/analyze.py','--build-dir',str(prov/label),'--output-dir',str(destination)],check=True)
            summary=json.loads((destination/'summary.json').read_text())
            metrics=json.loads((out/(label+'-metrics.json')).read_text())
            aggregates=summary['aggregates']
            rows=list(csv.DictReader((destination/'translation-units.csv').open()))
            sets[variant].append(set(row['output'] for row in rows))
            counts={}
            for row in rows:
                target=row['output'].split('/CMakeFiles/')[1].split('.dir/')[0]
                counts[target]=counts.get(target,0)+1
            runs.append({'label':label,'elapsed_s':metrics['elapsed_s'],'translation_units':len(rows),'pch':aggregates['pch']['count'],
              'compiler_s':aggregates['combined']['phase_seconds'].get('ExecuteCompiler',0),
              'frontend_s':aggregates['combined']['phase_seconds'].get('Frontend',0),
              'counts_by_target':counts,'diagnostics':summary['diagnostics']})
        result[variant]={'runs':runs,'identical_tu_sets_across_repeats':all(x==sets[variant][0] for x in sets[variant]),
          'statistics':{key:{'median':statistics.median(r[key] for r in runs),'min':min(r[key] for r in runs),'max':max(r[key] for r in runs)} for key in ['elapsed_s','compiler_s','frontend_s']}}
    result['removed_translation_units']=sorted(sets['baseline'][0]-sets['candidate'][0])
    result['added_translation_units']=sorted(sets['candidate'][0]-sets['baseline'][0])
    result['median_change_percent']={key:100*(result['candidate']['statistics'][key]['median']/result['baseline']['statistics'][key]['median']-1) for key in ['elapsed_s','compiler_s','frontend_s']}
    comparison[case]=result
(out/'comparison.json').write_text(json.dumps(comparison,indent=2)+'\n')
