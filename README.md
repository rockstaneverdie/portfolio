# Portfolio

Static portfolio site. No framework: `content.py` holds all text, `tools/build.py` renders HTML into `site/`.

```bash
python3 tools/images.py   # re-export case images from Downloads/Figma renders into site/img (WebP)
python3 tools/build.py    # rebuild site/*.html from content.py
python3 -m http.server 4321 --directory site
```

- `raw/` — full-size Figma renders (not deployed, git-ignored).
- `tools/slice_grid.py` — cuts single slides out of a Figma Slides grid render.
- Deploy: GitHub Pages via `.github/workflows/pages.yml` — every push to main publishes `site/` to https://rockstaneverdie.github.io/portfolio/

TODO before publishing: real name and contacts in `PROFILE` (content.py), permission to show client work.
