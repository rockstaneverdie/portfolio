# Numbered contact sheet of images in a folder, for picking frames.
import sys, glob
from PIL import Image, ImageDraw
files = sorted(glob.glob(sys.argv[1] + "/*.jpg")) + sorted(glob.glob(sys.argv[1] + "/*.png"))
cols, tw = int(sys.argv[3]) if len(sys.argv) > 3 else 8, 320
th = int(tw * 9 / 16)
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw, rows * (th + 18)), "white")
d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB"); im.thumbnail((tw - 6, th - 6))
    x, y = (i % cols) * tw, (i // cols) * (th + 18)
    sheet.paste(im, (x + 3, y + 3)); d.text((x + 4, y + th), f.split("/")[-1], fill="black")
sheet.save(sys.argv[2], quality=80)
