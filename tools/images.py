# Copy and compress case images into site/img/<case>/ as WebP.
import os, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

H = os.path.expanduser("~")
D, P, R = f"{H}/Downloads", f"{H}/Projects", f"{H}/Projects/portfolio/raw/figma"
OUT = f"{H}/Projects/portfolio/site/img"

CASES = {
    "design-system": [
        ("cover", f"{R}/ds-cover.png"),
        ("buttons", f"{R}/ds-buttons.png"),
        ("arc-usage", f"{R}/ds-arc-usage.png"),
    ],
    "website": [
        ("desktop-full", f"{R}/site-a-desktop.png"),
        ("mobile-full", f"{R}/site-a-mobile.png"),
        ("bento", f"{R}/site-b-bento.png"),
        ("cinema", f"{R}/site-c-kino.png"),
    ],
    "design-hub": [
        ("home", f"{P}/design-hub-video/shots/01-home.png"),
        ("search", f"{P}/design-hub-video/shots/03-search-open.png"),
        ("company", f"{P}/design-hub-video/shots/06-company.png"),
        ("assets", f"{P}/design-hub-video/shots/10-assets.png"),
        ("rules", f"{P}/design-hub-video/shots/18-rules.png"),
        ("mobile", f"{P}/design-hub-video/shots/22-mobile-home.png"),
    ],
    "proposal-platform": [
        ("hero-light", f"{P}/kp-platform/docs/screens-v2/01-lending-hero-svetlaya.jpg"),
        ("hero-dark", f"{P}/kp-platform/docs/screens-v2/02-lending-hero-temnaya.jpg"),
        ("gallery-dark", f"{P}/kp-platform/docs/screens-v2/03-lending-galereya-temnaya.jpg"),
        ("editor-light", f"{P}/kp-platform/docs/screens-v2/04-redaktor-svetlaya.png"),
        ("editor-dark", f"{P}/kp-platform/docs/screens-v2/05-redaktor-temnaya.png"),
        ("dashboard-dark", f"{P}/kp-platform/docs/screens-v2/06-moi-kp-temnaya.png"),
        ("stages-light", f"{P}/kp-platform/docs/screens-v2/08-lending-etapy-svetlaya.jpg"),
        ("estimate-light", f"{P}/kp-platform/docs/screens-v2/09-lending-smeta-svetlaya.jpg"),
        ("phone-dark", f"{P}/kp-platform/docs/screens-v2/10-lending-telefon-temnaya.jpg"),
    ],
    "audit-identity": [
        ("logo-concepts", f"{P}/report-audit/brand/logo-concepts/концепты-логотипа.png"),
        ("type-options", f"{P}/report-audit/brand/шрифты-варианты.png"),
    ],
    "presentations": [(f"company-{n}", f"{R}/slides-company/{n}.jpg") for n in ("01", "04", "05", "07", "14", "24", "39", "51")]
    + [(f"kp-{n}", f"{R}/slides-kp/{n}.jpg") for n in ("01", "02", "09", "11", "12", "15")],
    "social": [
        ("seminar-post-1", f"{D}/СЕМИНАР МЕДИЦИНА/ИНСТА-ПОСТ/01 — обложка.png"),
        ("seminar-post-2", f"{D}/СЕМИНАР МЕДИЦИНА/ИНСТА-ПОСТ/02 — никакой воды.png"),
        ("seminar-post-3", f"{D}/СЕМИНАР МЕДИЦИНА/ИНСТА-ПОСТ/03 — кому подойдёт.png"),
        ("seminar-post-4", f"{D}/СЕМИНАР МЕДИЦИНА/ИНСТА-ПОСТ/04 — регистрация.png"),
        ("seminar-story-1", f"{D}/СЕМИНАР МЕДИЦИНА/СТОРИС/обложка.png"),
        ("seminar-story-2", f"{D}/СЕМИНАР МЕДИЦИНА/СТОРИС/02 — никакой воды.png"),
        ("seminar-story-3", f"{D}/СЕМИНАР МЕДИЦИНА/СТОРИС/03 — кому подойдёт.png"),
        ("seminar-story-4", f"{D}/СЕМИНАР МЕДИЦИНА/СТОРИС/04 — регистрация.png"),
        ("seminar-mail", f"{D}/СЕМИНАР МЕДИЦИНА/РАССЫЛКА/mail.mix.1-optimized.jpg"),
    ] + [(f"expo-{i:02d}", f"{D}/Выставки ноябрь 2026/Instagram 1080x1350/{n}.png") for i, n in enumerate([
        "01 — обложка", "02 — Химия-2026", "03 — MITEX 2026", "04 — Мир Климата. Осень", "05 — CleanExpo Moscow",
        "06 — БИОТ 2026", "07 — Мебель-2026", "08 — Электроника России 2026", "09 — Pharmtech & Ingredients 2026", "10 — финал"], 1)],
    "print": [
        ("ny-baubles", f"{D}/ny-cards/otkrytki-jpeg/21_ИИ_шары_узор_на_игрушках.jpg"),
        ("ny-tree", f"{D}/ny-cards/otkrytki-jpeg/22_ИИ_ёлка_узор_на_ярусах.jpg"),
        ("ny-snowflake", f"{D}/ny-cards/otkrytki-jpeg/23_ИИ_снежинка_узор_в_лучах.jpg"),
    ],
    "koko": [
        ("letters-sheet", f"{D}/koko-letters/koko-letters-contact-sheet.jpg"),
        ("hands-sheet", f"{D}/koko-hands/koko-hands-contact-sheet.jpg"),
        ("concept", f"{D}/koko-letters/koko-concept.png"),
    ] + [(f"letter-{c}", f"{D}/koko-letters/koko-letter-{c}.png") for c in ("А", "В", "Л", "О", "П", "У")],
    "whatchasay": [("preview", f"{P}/whatchasay/brand/preview.png")],
}

ASCII = {"А": "a", "В": "v", "Л": "l", "О": "o", "П": "p", "У": "u"}

def save(src, dst, maxw):
    im = Image.open(src)
    alpha = im.mode in ("RGBA", "LA") or "transparency" in im.info
    im = im.convert("RGBA" if alpha else "RGB")
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(dst, "WEBP", quality=82, method=6)
    return im.size

sizes = {}
for case, items in CASES.items():
    os.makedirs(f"{OUT}/{case}", exist_ok=True)
    for name, src in items:
        for k, v in ASCII.items(): name = name.replace(k, v)
        if not os.path.exists(src):
            print("MISSING", src); continue
        maxw = 1440 if name.endswith("-full") and "mobile" not in name else (780 if "mobile-full" in name else 2400)
        w, h = save(src, f"{OUT}/{case}/{name}.webp", maxw)
        sizes[f"{case}/{name}"] = (w, h)
print(len(sizes), "images")
