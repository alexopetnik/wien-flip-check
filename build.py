# Erzeugt index.html aus app.src.html + Daten + Logo
import base64,json,urllib.parse
from logo_svg import icon
s=open('app.src.html').read()
s=s.replace('__DATA__',open('data-wien-2025.json').read()).replace('__MAP__',open('data-wien-map.json').read()).replace('__DEMAND__',open('data-wien-demand.json').read())
s=s.replace('__LOGOJSON__',json.dumps(icon()))
s=s.replace('__LOGO_HTML__',icon(40).replace('<svg ','<svg class="logo" aria-hidden="true" ',1))
s=s.replace('__FAVICON__','data:image/svg+xml,'+urllib.parse.quote(icon()))
s=s.replace('__TOUCHICON__','data:image/png;base64,'+base64.b64encode(open('icon-180.png','rb').read()).decode())
open('index.html','w').write(s)
