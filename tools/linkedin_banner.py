# LinkedIn cover 1584x396: text kept on the right, clear of the profile photo on the left.
import sys, subprocess
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from github_banner import text_path  # noqa: E402  (reuses the outline renderer)

OUT = sys.argv[2]
W, H = 1584, 396


def width(text, weight, size, tracking):
    _, end = text_path(text, weight, size, 0, 0, tracking)
    return end


def cover(fg, bg, name):
    right = W - 96
    lines = [
        ("design / code", "Light", 104, -0.06, 196, 1),
        ("vladimir vizhunov  ·  almaty", "Regular", 26, 0, 258, .6),
        ("rockstaneverdie.github.io/portfolio", "Regular", 26, 0, 300, .6),
    ]
    paths = []
    for text, wt, size, tr, y, op in lines:
        x = right - width(text, wt, size, tr)
        d, _ = text_path(text, wt, size, x, y, tr)
        paths.append(f'<path d="{d}" opacity="{op}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
           f'<rect width="{W}" height="{H}" fill="{bg}"/><g fill="{fg}">{"".join(paths)}</g></svg>')
    open(f"{OUT}/{name}.svg", "w").write(svg)
    subprocess.run(["rsvg-convert", "-w", str(W * 2), f"{OUT}/{name}.svg", "-o", f"{OUT}/{name}.png"], check=True)


cover("#ffffff", "#000000", "linkedin-cover-dark")
cover("#000000", "#ffffff", "linkedin-cover-light")
print("ok")
