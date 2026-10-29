# Build the static site from content.py into site/.
import html, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content import PROFILE, CASES, SIDE, SITE_URL  # noqa: E402

SITE = f"{ROOT}/site"


class Sizes(dict):
    def __missing__(self, key):
        from PIL import Image
        self[key] = Image.open(f"{SITE}/img/{key}.webp").size
        return self[key]


SIZES = Sizes()
e = html.escape


def img(key, alt="", cls="", crop=None, eager=False, prefix=""):
    w, h = SIZES[key]
    style = f' style="aspect-ratio:{crop}"' if crop else ""
    load = "eager" if eager else "lazy"
    return (f'<img src="{prefix}img/{key}.webp" width="{w}" height="{h}" alt="{e(alt)}" '
            f'loading="{load}" decoding="async" class="{cls}"{style} data-zoom>')


def figure(item, prefix, cls=""):
    cap = item.get("cap", "")
    body = img(item["src"], cap, crop=item.get("crop"), prefix=prefix)
    capt = f"<figcaption>{e(cap)}</figcaption>" if cap else ""
    return f'<figure class="{cls}">{body}{capt}</figure>'


def block(b, prefix):
    t = b["t"]
    if t == "text":
        ps = "".join(f"<p>{e(p)}</p>" for p in b["p"])
        return f'<section class="prose"><h2>{e(b["h"])}</h2>{ps}</section>'
    if t == "img":
        return f'<div class="media">{figure(b, prefix)}</div>'
    if t == "grid":
        items = "".join(figure(i, prefix) for i in b["items"])
        return f'<div class="media grid cols-{b["cols"]}">{items}</div>'
    if t == "scroll":
        w, h = SIZES[b["src"]]
        return (f'<div class="media"><figure><div class="scroller" tabindex="0" aria-label="{e(b.get("cap", ""))} Scrollable.">'
                f'<img src="{prefix}img/{b["src"]}.webp" width="{w}" height="{h}" alt="{e(b.get("cap", ""))}" loading="lazy" decoding="async">'
                f'</div><figcaption>{e(b.get("cap", ""))} Scroll inside the frame.</figcaption></figure></div>')
    if t == "phones":
        out = []
        for i in b["items"]:
            w, h = SIZES[i["src"]]
            out.append(f'<figure class="phone"><div class="scroller phone-screen" tabindex="0" aria-label="{e(i.get("cap", ""))} Scrollable.">'
                       f'<img src="{prefix}img/{i["src"]}.webp" width="{w}" height="{h}" alt="{e(i.get("cap", ""))}" loading="lazy" decoding="async">'
                       f'</div><figcaption>{e(i.get("cap", ""))}</figcaption></figure>')
        return f'<div class="media phones">{"".join(out)}</div>'
    raise ValueError(t)


def page(title, desc, body, prefix=""):
    p = PROFILE
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE_URL}/img/og-bw.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<link rel="preload" href="{prefix}fonts/KibernetykMono-Light.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefix}fonts/KibernetykMono-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
<header class="top wrap">
  <a class="brand" href="{prefix}index.html">{e(p["name"])}<span class="handle">@{e(p["handle"])}</span></a>
  <nav><a href="{prefix}index.html#work">Work</a><a href="{prefix}index.html#about">About</a><a href="{prefix}index.html#contact">Contact</a></nav>
</header>
{body}
{footer(prefix)}
<div class="lightbox" hidden><img alt=""><button type="button" aria-label="Close">×</button></div>
<script src="{prefix}main.js" defer></script>
</body>
</html>
"""


def footer(prefix):
    p = PROFILE
    tg = f"https://t.me/{p['telegram']}"
    cta = f"mailto:{p['email']}" if p["email"] else tg
    links = []
    if p["email"]:
        links.append(f'<a href="mailto:{e(p["email"])}">{e(p["email"])}</a>')
    links.append(f'<a href="{e(tg)}">Telegram @{e(p["telegram"])}</a>')
    links.append(f'<a href="https://instagram.com/{e(p["instagram"])}">Instagram @{e(p["instagram"])}</a>')
    links.append(f'<a href="https://github.com/{e(p["github"])}">GitHub</a>')
    if p.get("linkedin"):
        links.append(f'<a href="{e(p["linkedin"])}">LinkedIn</a>')
    return f"""<footer id="contact" class="foot wrap">
  <p class="foot-lead">Have a project or a role in mind?</p>
  <a class="foot-mail" href="{e(cta)}">Let's talk →</a>
  <div class="foot-links">{"".join(links)}</div>
  <p class="foot-small">© 2026 {e(p["name"])} · Set in <a href="https://pavlokilko.github.io/KibernetykMono/">Kibernetyk Mono</a></p>
</footer>"""


def tags(t):
    return "".join(f"<li>{e(x)}</li>" for x in t)


def index():
    p = PROFILE
    cards = []
    for i, c in enumerate(CASES):
        cls = "card wide" if i in (0, 3) else "card"
        cards.append(f"""<a class="{cls}" href="work/{c['slug']}.html">
  <div class="card-img{' pin-' + c['cover_crop'] if c.get('cover_crop') else ''}">{img(c['cover'], c['title'], eager=i < 2)}</div>
  <div class="card-text"><h3>{e(c['title'])}</h3><p>{e(c['summary'])}</p><ul class="tags">{tags(c['tags'])}</ul></div>
</a>""")
    side = []
    for s in SIDE:
        link = f'<a class="more" href="{e(s["link"][1])}">{e(s["link"][0])} →</a>' if s.get("link") else ""
        side.append(f'<article class="side"><div class="side-img">{img(s["img"], s["title"])}</div>'
                    f'<div><h3>{e(s["title"])}</h3><p>{e(s["text"])}</p>{link}</div></article>')
    about = "".join(f"<p>{e(x)}</p>" for x in p["about"])
    skills = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in p["skills"])
    body = f"""<main>
<section class="hero wrap">
  <p class="eyebrow">{e(p["role"])}</p>
  <h1>{e(p["intro"]).replace("— and I build them too.", "— <em>and I build them too.</em>")}</h1>
</section>
<section id="work" class="wrap">
  <div class="section-head"><h2>Selected work</h2><span>{len(CASES)} case studies · 2026</span></div>
  <div class="cards">{"".join(cards)}</div>
</section>
<section class="wrap">
  <div class="section-head"><h2>More</h2></div>
  <div class="sides">{"".join(side)}</div>
</section>
<section id="about" class="wrap about">
  <div class="section-head"><h2>About</h2></div>
  <div class="about-grid"><div class="prose">{about}</div><dl class="skills">{skills}</dl></div>
</section>
</main>"""
    return page(f'{p["name"]} — {p["role"]}', p["description"], body)


def case(c, i):
    prefix = "../"
    meta = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in c["meta"])
    blocks = "".join(block(b, prefix) for b in c["blocks"])
    nxt = CASES[(i + 1) % len(CASES)]
    body = f"""<main class="case">
<section class="case-head wrap">
  <a class="back" href="../index.html#work">← All work</a>
  <h1>{e(c['title'])}</h1>
  <p class="lead">{e(c['summary'])}</p>
  <dl class="meta">{meta}</dl>
</section>
<div class="case-body wrap">{blocks}</div>
<a class="next wrap" href="{nxt['slug']}.html"><span>Next case</span><strong>{e(nxt['title'])} →</strong></a>
</main>"""
    return page(f"{c['title']} — {PROFILE['name']}", c["summary"], body, prefix)


os.makedirs(f"{SITE}/work", exist_ok=True)
open(f"{SITE}/index.html", "w").write(index())
for i, c in enumerate(CASES):
    open(f"{SITE}/work/{c['slug']}.html", "w").write(case(c, i))
print("built", 1 + len(CASES), "pages")
