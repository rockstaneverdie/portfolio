# Link-preview image (og:image) 1200x630 in the site style: Kibernetyk Mono outlines, black on white is inverted here.
import sys, subprocess
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from github_banner import text_path  # noqa: E402

OUT = sys.argv[2]
W, H = 1200, 630
lines = [
    ("design / code", "Light", 112, -0.06, 300, 1),
    ("vladimir vizhunov  ·  almaty", "Regular", 30, 0, 384, .6),
    ("portfolio  ·  8 case studies", "Regular", 30, 0, 430, .6),
]
paths = "".join(f'<path d="{text_path(t, w, s, 72, y, tr)[0]}" opacity="{op}"/>' for t, w, s, tr, y, op in lines)
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
       f'<rect width="{W}" height="{H}" fill="#000"/><g fill="#fff">{paths}</g></svg>')
open(f"{OUT}/og.svg", "w").write(svg)
subprocess.run(["rsvg-convert", "-w", str(W), f"{OUT}/og.svg", "-o", f"{OUT}/og.png"], check=True)
print("ok")
