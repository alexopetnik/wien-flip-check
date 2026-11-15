# Erzeugt Logo-SVGs (Umriss Wien aus den 23 Bezirksgrenzen + Donau) -> logo.json
import json,re,math
m=json.load(open('data-wien-map.json')); B=m['b']
def pts(d): return [tuple(map(float,p)) for p in re.findall(r'(-?[\d.]+),(-?[\d.]+)',d)]
P={k:pts(v['d']) for k,v in B.items()}
def dseg(p,a,b):
    ax,ay=a;bx,by=b;dx,dy=bx-ax,by-ay;L=dx*dx+dy*dy or 1
    t=max(0,min(1,((p[0]-ax)*dx+(p[1]-ay)*dy)/L));return math.hypot(p[0]-ax-t*dx,p[1]-ay-t*dy)
def dpoly(p,k): r=P[k]; return min(dseg(p,r[i],r[(i+1)%len(r)]) for i in range(len(r)))
def chain(a,others,t=3):
    ring=P[a]; f=[min(dpoly(p,o) for o in others)<t for p in ring]; n=len(ring)
    best=(0,0)
    for s in range(n):
        if f[s] and not f[s-1]:
            l=0
            while l<n and f[(s+l)%n]: l+=1
            if l>best[1]: best=(s,l)
    s,l=best; return [ring[(s+i)%n] for i in range(l)]
c21=chain('21',['20','19']); c22=chain('22',['2','11'])
def join(a,b):
    # Richtung NW->SO
    if a and a[0][1]>a[-1][1]: a=a[::-1]
    if b and b[0][1]>b[-1][1]: b=b[::-1]
    return a+b
don=join(c21,c22)
print(len(c21),len(c22),don[:2],don[-2:])
xs=[x for r in P.values() for x,_ in r]; ys=[y for r in P.values() for _,y in r]
bb=(min(xs),min(ys),max(xs),max(ys)); print(bb)
D="".join(v['d'] for v in B.values())
dpath="M"+" L".join(f"{x:.1f},{y:.1f}" for x,y in don)
json.dump({'all':D,'d1':B['1']['d'],'donau':dpath,'bb':bb},open('logo.json','w'))
