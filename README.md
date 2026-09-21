# fabled-zombie-site

Neobrutalist one-page site — near-black ink on warm paper, one very loud orange
(`--orange: #ff5a1f`), 3px borders, 6px hard shadows, no gradients. Twelve
freely licensed zombie photographs from Wikimedia Commons.

## Layout

```
src/                  source
  index.template.html  page, with __GALLERY__ / __CREDITS__ / __HERO_*__ slots
  styles.css           all styling; design tokens are custom properties at the top
  app.js               lightbox, year stamp, marquee pause on hidden tab
  server.js            static file server on $PORT
  build.py             src/ + img/ -> dist/ (also regenerates CREDITS.md)
img/                  downloaded images + credits.json (source of truth for attribution)
dist/                 build output — deployable as-is, do not edit by hand
CREDITS.md            generated attribution list
```

## Build and run

```bash
python3 src/build.py          # writes dist/ and CREDITS.md
PORT=8099 node dist/server.js # http://localhost:8099
```

No dependencies, no bundler, no npm install. The only runtime requirements are
Python 3 (build) and Node (serve).

## Conventions

- **Alt text is hand-written**, in the `ALT` map in `build.py`. Add an entry
  whenever you add an image; generated alt text is worse than none.
- **Attribution is not optional.** Every image is CC BY, CC BY-SA, public domain
  or Free Art License. `img/credits.json` drives the per-image caption, the
  footer list and `CREDITS.md`. Remove an image from `credits.json` and it
  disappears from all three.
- **Motion respects `prefers-reduced-motion`** — keep it that way.
- Copy in the template is placeholder, written against a brief that said
  "zombie pictures". Replace it when there is a real brief.

## Known gaps

- Google Fonts (Archivo Black, Space Grotesk) load from the CDN; self-host them
  if the site must work offline or without third-party requests.
- No analytics, no cookie banner, no forms — the CTA is a `mailto:`.
- Single page. Multi-page needs a router or a second HTML file plus a nav state.
