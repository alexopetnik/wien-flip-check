import json
L=json.load(open('logo.json'))
def icon(size=None, bg="#1d2330", fg="#c8102e", lines="#1d2330", don="#7fc4ff", c1="#ffffff", rx=120, pad=0.10):
    W,H=600,466; s=600*(1-2*pad)/W; ty=(600-H*s)/2; tx=600*pad
    sz=f' width="{size}" height="{size}"' if size else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"{sz}><rect width="600" height="600" rx="{rx}" fill="{bg}"/><g transform="translate({tx:.1f},{ty:.1f}) scale({s:.4f})" stroke-linejoin="round"><path d="{L['all']}" fill="{fg}" stroke="{fg}" stroke-width="6"/><path d="{L['all']}" fill="none" stroke="{lines}" stroke-opacity=".35" stroke-width="2.2"/><path d="{L['donau']}" fill="none" stroke="{don}" stroke-width="13" stroke-linecap="round"/><path d="{L['d1']}" fill="{c1}"/></g></svg>'''
