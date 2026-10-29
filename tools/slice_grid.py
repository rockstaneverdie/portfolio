# Cut individual slides out of a Figma Slides grid render.
import sys, os
from PIL import Image
import numpy as np
Image.MAX_IMAGE_PIXELS = None

src, outdir, minw = sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 300
os.makedirs(outdir, exist_ok=True)
im = Image.open(src).convert("RGB")
k = 8
small = np.asarray(im.resize((im.width // k, im.height // k), Image.NEAREST)).astype(int)
bg = small[0, 0]
mask = np.abs(small - bg).sum(axis=2) > 12

def runs(v, minlen):
    out, start = [], None
    for i, x in enumerate(list(v) + [False]):
        if x and start is None: start = i
        if not x and start is not None:
            if i - start >= minlen: out.append((start, i))
            start = None
    return out

n = 0
for y0, y1 in runs(mask.any(axis=1), minw // k // 2):
    for x0, x1 in runs(mask[y0:y1].any(axis=0), minw // k):
        n += 1
        box = (x0 * k, y0 * k, x1 * k, y1 * k)
        im.crop(box).save(f"{outdir}/{n:02d}.jpg", quality=88)
print(n, "slides; bg", bg.tolist())
