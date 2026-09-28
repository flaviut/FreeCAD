import json
from pathlib import Path
import subprocess
import sys
root=Path.cwd()
build=root/'build/clang-profile'
prov=root/'docs/build-optimization/03-material-headers/provenance'
label=sys.argv[1]
targets=['Materials','Part','SketcherGui']
def measure(suffix):
    subprocess.run([sys.executable,str(prov/'measure.py'),label+'-'+suffix,*targets],check=True)
with (prov/(label+'-deps.txt')).open('w') as stream:
    subprocess.run(['ninja','-C',str(build),'-t','deps'],stdout=stream,check=True)
removed=[]
for target in targets:
    for directory in build.glob('src/**/CMakeFiles/'+target+'.dir'):
        for path in directory.rglob('*'):
            if path.suffix in ('.o','.pch'):
                removed.append(str(path.relative_to(build)))
                path.unlink()
(prov/(label+'-removed.json')).write_text(json.dumps(removed,indent=2)+'\n')
measure('targets')
for header,name in [('src/App/Application.h','application-touch'),('src/Gui/MetaTypes.h','metatypes-touch')]:
    (root/header).touch()
    measure(name)
