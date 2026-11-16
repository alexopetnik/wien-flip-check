# Erzeugt data-wien-demand.json aus Stadt Wien OGD (Registerzählung 2023, Bevölkerungsprognose 2023–2043)
import csv,io,json,os,urllib.request
SRC={"wohn":"https://www.wien.gv.at/data/ogd/ma23/vie-404-2023.csv",
     "pop":"https://www.wien.gv.at/data/ogd/ma23/vie-405-2023.csv",
     "prog":"https://www.wien.gv.at/data/ogd/ma23/vie-bez-proj-pop-sex-age5-geo2-2023.csv"}
def get(k):
  f=f"raw/{os.path.basename(SRC[k])}"
  if not os.path.exists(f):
    os.makedirs("raw",exist_ok=True); urllib.request.urlretrieve(SRC[k],f)
  b=open(f,'rb').read()
  try: t=b.decode('utf-8-sig')
  except UnicodeDecodeError: t=b.decode('latin-1')
  r=list(csv.reader(io.StringIO(t),delimiter=';')); return [dict(zip(r[1],x)) for x in r[2:] if len(x)>5]
n=lambda v: float(v.replace(',','.')) if v not in('','.') else 0.0
agg={i:{} for i in range(1,24)}
def add(rows,cols,key):
  for x in rows:
    b=int(x["DISTRICT_CODE"][1:3]); d=agg[b].setdefault(key,{})
    for c in cols: d[c]=d.get(c,0)+n(x[c])
add(get("wohn"),["WHG_TOTAL","WHG_WSA_0","WHG_NOC_1","WHG_NOC_2","WHG_NOC_3","WHG_NOC_4"]+[f"WHG_NTZFL_{i}" for i in range(1,6)],"w")
add(get("pop"),["WHG_POP_TOTAL","WHG_RECHTSVERH_2","WHG_DFS_1","WHG_DFS_2","HST_1"],"p")
prog={}
for x in get("prog"):
  b=int(x["DISTRICT_CODE"][1:3]); y=int(x["REF_YEAR"]); a=int(x["AGE5"]); v=n(x["AUT"])+n(x["FOR"])
  d=prog.setdefault(b,{}).setdefault(y,[0]*18); d[a]+=v
out={}
for b in range(1,24):
  w,p=agg[b]["w"],agg[b]["p"]; hh=[w[f"WHG_NOC_{i}"] for i in range(1,5)]; H=sum(hh)
  st=[w[f"WHG_NTZFL_{i}"] for i in range(1,6)]; S=sum(st)
  y25,y35=prog[b][2025],prog[b][2035]
  out[b]={"hh":[round(v/H,3) for v in hh],"stock":[round(v/S,3) for v in st],"nHH":int(H),
    "leer":round(w["WHG_WSA_0"]/w["WHG_TOTAL"],3),
    "eig":round(p["WHG_RECHTSVERH_2"]/p["WHG_POP_TOTAL"],3),
    "eng":round((p["WHG_DFS_1"]+p["WHG_DFS_2"])/p["WHG_POP_TOTAL"],3),
    "fam":round(p["HST_1"]/p["WHG_POP_TOTAL"],3),
    "grow":round(sum(y35)/sum(y25)-1,4),
    "a2544":round(sum(y25[6:10])/sum(y25),3),"kids":round(sum(y25[1:4])/sum(y25),3)}
json.dump(out,open("data-wien-demand.json","w"),separators=(",",":"))
for b,v in out.items(): print(b,v)
