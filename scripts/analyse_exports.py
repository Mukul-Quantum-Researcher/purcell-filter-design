"""Inspect original HFSS CSV exports without requiring HFSS."""
from pathlib import Path
import csv
import json
import os
os.environ.setdefault('MPLCONFIGDIR',str(Path(__file__).resolve().parents[1]/'.mpl-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
out=root/'analysis';out.mkdir(exist_ok=True)
summary=[]
fig,axes=plt.subplots(2,1,figsize=(9,7),layout='constrained')
for ax,path in zip(axes,sorted((root/'data').glob('*.csv'))):
    with path.open(encoding='utf-8-sig',newline='') as f:
        r=csv.reader(f);columns=next(r);rows=[[float(x) for x in row] for row in r if row]
    item={'source':path.name,'rows':len(rows),'frequency_range_GHz':[rows[0][0],rows[-1][0]],'minima':[]}
    assert len(rows)==1601 and rows[0][0]==4 and rows[-1][0]==15
    for j,column in enumerate(columns[1:],1):
        p=min(rows,key=lambda v:v[j]);ax.plot([r[0] for r in rows],[r[j] for r in rows],label=column)
        item['minima'].append({'column':column,'frequency_GHz':p[0],'value':p[j]})
    ax.set(xlabel='Frequency (GHz)',ylabel='Original HFSS exported quantity',title=path.name)
    ax.legend(fontsize=7);ax.grid(alpha=.2);summary.append(item)
fig.savefig(out/'exported-sweeps.png',dpi=160)
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
