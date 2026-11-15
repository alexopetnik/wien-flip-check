# Rendert App-Icons (PNG) + icon.svg aus logo_svg.icon()
import asyncio,os,json
from logo_svg import icon
from playwright.async_api import async_playwright
open('icon.svg','w').write(icon())
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path=os.path.realpath("/home/ubuntu/.local/bin/google-chrome"))
    for s,rx in [(180,0),(192,0),(512,0),(1024,0)]:
      pg=await b.new_page(viewport={"width":s,"height":s})
      await pg.set_content(f"<body style='margin:0'>{icon(s,rx=rx)}</body>"); await pg.screenshot(path=f"icon-{s}.png",omit_background=True); await pg.close()
    await b.close()
asyncio.run(main())
json.dump({"name":"Wien Flip-Check","short_name":"Flip-Check","start_url":"./","scope":"./","display":"standalone","background_color":"#1d2330","theme_color":"#1d2330","lang":"de-AT",
  "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},open('manifest.webmanifest','w'),ensure_ascii=False,indent=1)

# Favicon: transparente Ecken, wenig Rand, ohne Bezirkslinien (bei 16–48 px lesbarer)
from PIL import Image
fav=icon(256,rx=56,pad=0.05,lines="none")
open('favicon.svg','w').write(icon(rx=130,pad=0.05,lines="none"))
async def fav_png():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path=os.path.realpath("/home/ubuntu/.local/bin/google-chrome"))
    pg=await b.new_page(viewport={"width":256,"height":256})
    await pg.set_content(f"<body style='margin:0;background:transparent'>{fav}</body>")
    await pg.screenshot(path="favicon-256.png",omit_background=True); await b.close()
asyncio.run(fav_png())
im=Image.open('favicon-256.png').convert('RGBA')
im.resize((32,32),Image.LANCZOS).save('favicon-32.png')
im.resize((16,16),Image.LANCZOS).save('favicon-16.png')
im.save('favicon.ico',sizes=[(16,16),(32,32),(48,48)])
