# Wien Flip-Check

Investment-Rechner für sanierungsbedürftige Wohnungen in Wien (alle 23 Bezirke): Kauf, Finanzierung, Sanierung, Verkauf, Steuer, Risiko, Vermietung nach Sanierung und PDF-Bericht.

**App öffnen:** https://alexopetnik.github.io/wien-flip-check/ – am iPhone in Safari öffnen → Teilen → „Zum Home-Bildschirm“.

- Reine statische Web-App (`index.html`), keine Server-Daten; gespeicherte Objekte bleiben lokal im Browser.
- Quellcode: `app.src.html`; `python3 build.py` erzeugt `index.html` (Daten + Logo eingebettet).
- Icons neu rendern: `python3 make_icons.py` (benötigt Playwright + Chrome).
- Referenzdaten: Statistik Austria (Immobilien-Durchschnittspreise 2025), Stadt Wien OGD (Bezirksgrenzen), Richtwert Wien 2026, Angebotsmieten je Bezirk (mietdaten.at, rentradar.rentals).

Keine Rechts- oder Steuerberatung.
