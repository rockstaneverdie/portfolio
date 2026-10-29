# Render the GitHub profile banner: Kibernetyk Mono text converted to SVG paths (no font loading needed).
import os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONTS = sys.argv[1]  # folder with KibernetykMono-*.ttf
OUT = sys.argv[2]


def text_path(text, weight, size, x, y, tracking=0.0):
    f = TTFont(f"{FONTS}/KibernetykMono-{weight}.ttf")
    gs, cmap, upm = f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm
    s = size / upm
    pen = SVGPathPen(gs)
    cx = x
    for ch in text:
        g = cmap.get(ord(ch))
        if g is None:
            continue
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, cx, y)))
        cx += gs[g].width * s + tracking * size
    return pen.getCommands(), cx


def banner(fg, bg, name):
    W, H = 1200, 240
    d1, _ = text_path("vladimir vizhunov", "Light", 84, 48, 132, -0.06)
    d2, _ = text_path("@stillrocksta   design / code   almaty", "Regular", 22, 52, 188, 0)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
           f'<rect width="{W}" height="{H}" fill="{bg}"/>'
           f'<g fill="{fg}"><path d="{d1}"/><path d="{d2}" opacity=".5"/></g></svg>')
    open(f"{OUT}/{name}", "w").write(svg)


if __name__ == "__main__":
    banner("#000000", "#ffffff", "banner-light.svg")
    banner("#ffffff", "#0d1117", "banner-dark.svg")
    print("ok")
