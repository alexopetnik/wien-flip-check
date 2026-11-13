# Erzeugt index.html aus app.src.html + data-wien-2025.json (Statistik Austria Immobilien-Durchschnittspreise 2025)
s=open('app.src.html').read(); open('index.html','w').write(s.replace('__DATA__',open('data-wien-2025.json').read()))
