#!/usr/bin/env python3
"""Build the static site into dist/ from src/ + img/ + img/credits.json."""
import json, shutil, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, IMG, DIST = ROOT / "src", ROOT / "img", ROOT / "dist"

# Hand-written alt text, keyed by file name. Machine-generated alt text is worse than none.
ALT = {
    "zombie-walk-paris-2017-36862101084.jpg": "Participants in heavy undead make-up shambling down a Paris street at a zombie walk",
    "zombie-walk-2013-11054080926.jpg": "A zombie-walk participant with bloodied face staring into the camera",
    "zombie-fest-2009-4003566266.jpg": "A costumed zombie with grey skin and torn clothing at a zombie festival",
    "crazy-zombie-boy-in-the-studio.jpg": "Studio portrait of a young man in zombie make-up, mouth open mid-snarl",
    "the-walking-dead-cosplay.jpg": "Cosplayers dressed as walkers from The Walking Dead",
    "zombie-sculpture-niagara-falls-zombie-at.jpg": "A large zombie sculpture on display at a Niagara Falls zombie event",
    "zombie-walk-2016-29560783686.jpg": "A crowd of made-up zombies walking a city street in daylight",
    "zombie-walk-2015-21149793606.jpg": "Close-up of a zombie-walk participant with prosthetic wounds",
    "2015-richmond-zombie-walk-time-lapse-sti.jpg": "Time-lapse still of the Richmond zombie walk, figures blurred in motion",
    "zombie-haiti-ill-artlibre-jnl.jpg": "Illustration of a Haitian zombie figure, ink and wash",
    "groupofzombiesjoelf.jpg": "A group of costumed zombies posed together outdoors",
    "hallween-tumble-2012-zombie-shamble.jpg": "New Orleans Halloween parade zombie shamble, costumed crowd in the street",
}
HERO = "zombie-walk-paris-2017-36862101084.jpg"

credits = json.loads((IMG / "credits.json").read_text())
by_file = {pathlib.Path(c["file"]).name: c for c in credits}


def artist(c):
    return " ".join(c["artist"].split())[:80] or "Unknown"


def shot(c):
    name = pathlib.Path(c["file"]).name
    alt = ALT.get(name, "Zombie photograph")
    cap = f'{artist(c)} — {c["license"]}'
    return (
        f'    <figure class="shot" data-caption="{html.escape(cap)}" tabindex="0" role="button">\n'
        f'      <img src="img/{name}" alt="{html.escape(alt)}" loading="lazy" decoding="async">\n'
        f'      <figcaption><span>{html.escape(artist(c))}</span>'
        f'<span class="lic">{html.escape(c["license"])}</span></figcaption>\n'
        f"    </figure>"
    )


order = [HERO] + [n for n in by_file if n != HERO]
gallery = "\n".join(shot(by_file[n]) for n in order)

credit_lis = "\n".join(
    f'      <li><a href="{html.escape(by_file[n]["page"])}">{html.escape(by_file[n]["title"].replace("File:", ""))}</a>'
    f' — {html.escape(artist(by_file[n]))}, {html.escape(by_file[n]["license"])}, via Wikimedia Commons</li>'
    for n in order
)

hero = by_file[HERO]
page = (SRC / "index.template.html").read_text()
page = (
    page.replace("__GALLERY__", gallery)
    .replace("__CREDITS__", credit_lis)
    .replace("__HERO_IMG__", f"img/{HERO}")
    .replace("__HERO_ALT__", html.escape(ALT[HERO]))
    .replace("__HERO_CAP__", html.escape(f"{artist(hero)} — {hero['license']} — Wikimedia Commons"))
)

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()
(DIST / "index.html").write_text(page)
shutil.copy(SRC / "styles.css", DIST / "styles.css")
shutil.copy(SRC / "app.js", DIST / "app.js")
shutil.copy(SRC / "server.js", DIST / "server.js")
shutil.copytree(IMG, DIST / "img", ignore=shutil.ignore_patterns("credits.json"))

(ROOT / "CREDITS.md").write_text(
    "# Image credits\n\nAll photographs come from Wikimedia Commons under free licences. "
    "Keep these attributions if you keep the images.\n\n"
    + "\n".join(
        f'- [{by_file[n]["title"].replace("File:", "")}]({by_file[n]["page"]}) — {artist(by_file[n])} — {by_file[n]["license"]}'
        for n in order
    )
    + "\n"
)
print(f"built dist/ — {len(order)} images")
