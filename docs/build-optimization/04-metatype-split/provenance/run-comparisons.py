import json
from pathlib import Path
import subprocess
import sys
p=Path(__file__).resolve().parent
paths=json.loads((p/'source-paths.json').read_text())
for label,revision in [('candidate-1','mzktnxlp'),('baseline-2','vpmkvoxr'),('candidate-2','mzktnxlp'),('baseline-3','vpmkvoxr'),('candidate-3','mzktnxlp')]:
    subprocess.run(['jj','restore','--from',revision,*paths],check=True)
    subprocess.run([sys.executable,str(p/'measure.py'),label+'-prepare','Materials','MatGui','Part','SketcherGui'],check=True)
    subprocess.run([sys.executable,str(p/'run-series.py'),label],check=True)
