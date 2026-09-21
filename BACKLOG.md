> Tracked in Linear: project **rmj** — https://linear.app/fabled-cat/project/rmj-81ca62a90a57
> Repo: https://github.com/fabled-murk/rmj-zombie-site

# fabled-zombie-site — backlog

Proposed Jira project: **ZMB** — "Zombie Site". Epic + 14 issues. Anything
already done in the demo build is marked DONE so you can close it on import
instead of re-doing it.

`jira-import.csv` next to this file is the same list in Jira's CSV import
format (Summary, Issue Type, Priority, Description, Labels, Parent).

## Epic: ZMB — Zombie site (neobrutalist, orange)

| # | Type | Issue | Priority | Status |
|---|---|---|---|---|
| 1 | Task | Decide what the site is actually for — audience, one primary action, who signs off | Highest | **Blocking everything below** |
| 2 | Task | Create GitHub repo and push the existing build | Highest | Blocked on repo access |
| 3 | Story | Neobrutalist design system: tokens, borders, hard shadows, orange scale | High | DONE (demo) |
| 4 | Story | Hero, marquee, stats band | High | DONE (demo) |
| 5 | Story | Zombie gallery, 12 freely licensed Commons images, lightbox | High | DONE (demo) |
| 6 | Story | Attribution: per-image captions, footer list, generated CREDITS.md | High | DONE (demo) |
| 7 | Story | Feature cards, survival tiers, FAQ, CTA band, footer | Medium | DONE (demo) |
| 8 | Story | Real copy to replace the placeholder text | High | Todo — needs #1 |
| 9 | Story | Mobile pass at 360 / 768 / 1024 on a real device | High | Todo |
| 10 | Story | Accessibility pass: contrast audit, keyboard order, screen-reader run | High | Partly — needs a real audit |
| 11 | Task | Self-host Archivo Black + Space Grotesk, drop the Google Fonts request | Medium | Todo |
| 12 | Task | Performance: responsive `srcset`, WebP/AVIF variants, budget under 1 MB first load | Medium | Todo |
| 13 | Task | Legal review of the image set — licences are free but check brand/likeness comfort | Medium | Todo |
| 14 | Task | Hosting and domain: where this lives, TLS, deploy on merge to `main` | High | Todo |
| 15 | Task | SEO and share cards: OG image, meta description, sitemap, favicon set | Low | Partly — favicon only |

## Notes

- **#1 is not a formality.** The current copy is written against a brief that
  said "zombie pictures". It looks finished and says nothing.
- **#13 is the one that bites.** CC BY-SA means derivative works of those images
  inherit the licence; the photos themselves are fine to use with attribution,
  but do not crop one into a logo.
- **#11 and #12** are the difference between "looks fast on our laptops" and
  "is fast".
