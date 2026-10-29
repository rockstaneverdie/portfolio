# Portfolio content. Edit text here, then run `python3 tools/build.py`.

SITE_URL = "https://rockstaneverdie.github.io/portfolio"

PROFILE = {
    "name": "vladimir vizhunov",
    "handle": "stillrocksta",
    "role": "design / code · almaty",
    "email": "",  # optional; footer CTA falls back to Telegram
    "telegram": "stillrocksta",
    "instagram": "stillrocksta",
    "github": "rockstaneverdie",
    "linkedin": "https://www.linkedin.com/in/vladimir-vizhunov-5964213b5/",
    "intro": "I design brands, interfaces and the tools around them — and I build them too.",
    "description": "Designer and web developer in Almaty. Design systems, product UI, internal tools and web front-end: 8 case studies.",
    "about": [
        "I work across identity, interfaces and marketing. Most of the work here was made for MIREX, "
        "an exhibition-stand builder: a web design system, a homepage redesign, internal tools, "
        "sales decks, social campaigns and print. On the side I build KoKo, my iOS app for "
        "learning Russian Sign Language.",
        "I like systems: tokens instead of hex codes, components instead of copies, a script instead "
        "of fifty manual exports. When a tool doesn't exist, I design it and ship it myself — "
        "mostly for the web with Next.js and TypeScript, sometimes for iOS in Swift.",
        "I use AI image models as a production tool, with art direction and clean-up on top. "
        "Where a visual is AI-assisted, the case says so.",
    ],
    "skills": [
        ("Design", "Design systems, UI/UX, web, identity, presentations, social, print"),
        ("Tools", "Figma (variables, components, Slides), Figma API, Photoshop, ChatGPT/Gemini image models"),
        ("Code", "TypeScript, React, Next.js, Svelte, HTML/CSS · Swift and SwiftUI for iOS · Python for asset pipelines"),
    ],
}

# Block types: text, img, grid (cols, items), scroll (long page in a frame), phones (narrow scroll frames)
CASES = [
    {
        "slug": "design-system",
        "title": "MIREX Web Design System",
        "summary": "A token-driven design system for a B2B website: one set of components, light and dark themes.",
        "cover": "design-system/cover",
        "cover_crop": "left",
        "tags": ["Design system", "Figma variables", "Web"],
        "meta": [("Role", "Sole designer"), ("Client", "MIREX"), ("Year", "2026"), ("Tools", "Figma, CSS")],
        "blocks": [
            {"t": "text", "h": "Context", "p": [
                "MIREX builds exhibition stands. Its print and social work already had a recognisable look, "
                "but the website had nothing to stand on: no tokens, no components, no rules. The team liked a "
                "series of greeting cards I had made, so the brief was simple: the same visual language, "
                "without the holiday theme, as a system the website can be built from."]},
            {"t": "img", "src": "design-system/cover", "cap": "File cover. Pages: Foundations, Tone of voice, Brand, Icons, Controls, Content, Layout, Pages."},
            {"t": "text", "h": "Foundations", "p": [
                "82 variables in four collections. Primitive palettes (green 50–950, neutrals, red, amber) are never "
                "used directly — components only reference 25 semantic colour tokens such as bg/surface, "
                "text/brand or action/primary-hover.",
                "Each semantic token has a Light and a Dark mode. Switching the mode on a parent frame re-themes a "
                "whole page, so there is not a single duplicated component for dark mode. Spacing runs on a 4 px "
                "scale (4–128), radii from 0 to pill, and 13 text styles pair Affect for headlines with Montserrat "
                "for everything else."]},
            {"t": "img", "src": "design-system/palette", "cap": "Primitive palettes. Components never reference these directly."},
            {"t": "grid", "cols": 2, "items": [
                {"src": "design-system/tokens", "cap": "Semantic tokens with their CSS names."},
                {"src": "design-system/type", "cap": "Type scale: Affect for headlines, Montserrat for text and UI."},
            ]},
            {"t": "text", "h": "Components", "p": [
                "Buttons come in five variants — Primary, Secondary, Ghost, Link and Glass — three sizes and six "
                "states, including focus and loading: 90 variants with label and icon exposed as properties. Icon "
                "buttons, inputs, tags, cards, header, hero, CTA banner and footer are built the same way, and the "
                "example pages are assembled only from these parts."]},
            {"t": "img", "src": "design-system/buttons", "cap": "The full button matrix in both themes — same components, different variable mode."},
            {"t": "text", "h": "Brand pattern", "p": [
                "The brand's arc pattern used to end in a dense block with a hard diagonal cut. I regenerated the "
                "geometry with code from a single Bézier spine and wrote usage rules: the arc always runs off the "
                "edge of a block, its ends are never visible, and a page uses it at most twice."]},
            {"t": "img", "src": "design-system/arc-usage", "cap": "Arc usage: in a corner, behind a dark block, next to a key number."},
            {"t": "text", "h": "Handoff", "p": [
                "Every variable carries a CSS code-syntax name, and the tokens are exported as a tokens.css file "
                "with the same names — light theme in :root, dark under [data-theme=\"dark\"]. Developers read "
                "var(--color-action-primary) in Figma and type the same thing in code."]},
        ],
    },
    {
        "slug": "website",
        "title": "mir-ex.ru homepage redesign",
        "summary": "Three art directions for a B2B homepage; the chosen one taken to a full desktop page and a 390 px mobile version.",
        "cover": "website/bento",
        "cover_crop": "top",
        "tags": ["Web design", "Art direction", "Responsive"],
        "meta": [("Role", "Lead designer"), ("Client", "MIREX"), ("Year", "2026"), ("Built with", "MIREX Web Design System")],
        "blocks": [
            {"t": "text", "h": "Brief", "p": [
                "The company asked for a homepage that feels more modern and more like them. Instead of one "
                "mock-up I proposed three clearly different directions, all built from the same design system "
                "components, so the choice was about tone and structure, not about buttons."]},
            {"t": "grid", "cols": 2, "items": [
                {"src": "website/bento", "cap": "B · Bento — everything is a tile; a quick stand-cost calculator sits in the first screen.", "crop": 1.25},
                {"src": "website/cinema", "cap": "C · Cinema — dark and immersive: full-bleed photography, big type, almost no frames.", "crop": 1.25},
            ]},
            {"t": "text", "h": "Direction A · Architectural bureau", "p": [
                "The direction the team chose treats the site like an architect's portfolio: a light editorial "
                "layout, hairline rules, dimension lines drawn over photos, an index-style list of services with "
                "hover previews and an editorial grid of projects.",
                "I developed it into a complete page of 17 blocks — from the announcement bar and hero through "
                "numbers, clients, services and formats to the final CTA and footer — and adapted every block "
                "for a 390 px mobile layout. Scroll inside the frames to see the full pages."]},
            {"t": "scroll", "src": "website/desktop-full", "cap": "Desktop, 1440 px."},
            {"t": "phones", "items": [{"src": "website/mobile-full", "cap": "Mobile, 390 px."}]},
        ],
    },
    {
        "slug": "design-hub",
        "title": "Design Hub",
        "summary": "An internal portal where designers and managers find logos, templates, decks and brand rules in seconds.",
        "cover": "design-hub/home",
        "tags": ["Product design", "Internal tool", "Next.js"],
        "meta": [("Role", "Designer & developer"), ("Client", "MIREX"), ("Year", "2026"), ("Stack", "Next.js, Yandex Cloud")],
        "blocks": [
            {"t": "text", "h": "Problem", "p": [
                "Brand files lived in chats, shared folders and people's downloads. Every new deck started with "
                "\"where is the latest logo?\" and the answer was often an outdated PNG."]},
            {"t": "img", "src": "design-hub/home", "cap": "Home: search first, then sections and recently added files."},
            {"t": "text", "h": "Solution", "p": [
                "One portal with one search. Assets show a live preview and copy or download in one click; "
                "company materials are grouped by purpose — presentations, social templates, documents; the brand "
                "rules are a readable page instead of a PDF nobody opens."]},
            {"t": "grid", "cols": 2, "items": [
                {"src": "design-hub/search", "cap": "Global search across files and pages."},
                {"src": "design-hub/assets", "cap": "Asset library with filters by type."},
                {"src": "design-hub/company", "cap": "Company materials, ready to download."},
                {"src": "design-hub/rules", "cap": "Brand guidelines as a web page."},
            ]},
            {"t": "text", "h": "Shipping it", "p": [
                "I designed the interface and built the app myself: Next.js in a serverless container on Yandex "
                "Cloud, with an admin area for adding files and automatic deploys from GitHub. To get people to "
                "actually use it, I also produced a short animated walkthrough of the main scenarios."]},
            {"t": "grid", "cols": 3, "items": [
                {"src": "design-hub/mobile", "cap": "Mobile layout."},
            ]},
        ],
    },
    {
        "slug": "proposal-platform",
        "title": "Proposal landing platform",
        "summary": "A service that turns a sales proposal into a personal web page for every client — editor, landing and dashboard.",
        "cover": "proposal-platform/hero-dark",
        "tags": ["Product design", "SaaS", "Prototype"],
        "meta": [("Role", "Product designer"), ("Client", "MIREX"), ("Year", "2026"), ("Stage", "Spec + clickable prototype")],
        "blocks": [
            {"t": "text", "h": "Idea", "p": [
                "Stand proposals were sent as heavy PDFs: no way to know if the client opened them, and every "
                "change meant a new file. The platform gives each client a personal landing page — renders of "
                "their future stand, project stages, estimate and a direct line to the manager. Client names "
                "in the screens are fictional."]},
            {"t": "img", "src": "proposal-platform/hero-dark", "cap": "Client landing: the stand, the show dates and the manager one tap away."},
            {"t": "img", "src": "proposal-platform/gallery-dark", "cap": "Stand gallery, the four goals the stand works on, and a fly-through video."},
            {"t": "img", "src": "proposal-platform/stages-dark", "cap": "\"From design to show day\": the six stages of the project."},
            {"t": "text", "h": "For managers", "p": [
                "Managers fill a form-based editor with a live preview next to it. The editor warns about what is "
                "still missing before publishing, and the dashboard shows every proposal with its status and views."]},
            {"t": "grid", "cols": 2, "items": [
                {"src": "proposal-platform/editor-light", "cap": "Editor with live preview."},
                {"src": "proposal-platform/dashboard-dark", "cap": "\"My proposals\" dashboard."},
            ]},
            {"t": "text", "h": "Status", "p": [
                "I wrote the product spec together with the client, then built a clickable prototype in "
                "Next.js so the team could test real flows before development."]},
        ],
    },
    {
        "slug": "presentations",
        "title": "Sales presentation system",
        "summary": "A 62-slide company deck and a 19-slide proposal template, rebuilt in Figma Slides on one shared grid.",
        "cover": "presentations/company-01",
        "tags": ["Presentations", "Figma Slides", "Layout systems"],
        "meta": [("Role", "Designer"), ("Client", "MIREX"), ("Year", "2026"), ("Tools", "Figma Slides, PowerPoint")],
        "blocks": [
            {"t": "text", "h": "Context", "p": [
                "Sales used a long PowerPoint deck that had grown slide by slide. I rebuilt it in Figma Slides "
                "against one reference style: 1920×1080, 80 px margins, three 520 px columns, a fixed header "
                "(eyebrow, two-colour headline, rule) and a footer with page number."]},
            {"t": "grid", "cols": 2, "items": [
                {"src": "presentations/company-01"}, {"src": "presentations/company-04"},
                {"src": "presentations/company-05"}, {"src": "presentations/company-07"},
            ]},
            {"t": "text", "h": "51 case slides that don't look the same", "p": [
                "Most of the deck is a portfolio of 51 stands. Four photo layouts — two equal photos, narrow + "
                "wide, wide + narrow, one panorama — alternate through the deck, picked per case by how many good "
                "photos it had. Section dividers group the stands by size."]},
            {"t": "grid", "cols": 2, "items": [
                {"src": "presentations/company-14"}, {"src": "presentations/company-24"},
                {"src": "presentations/company-39"}, {"src": "presentations/company-51"},
            ]},
            {"t": "text", "h": "Proposal template", "p": [
                "The 19-slide proposal is a template managers fill in themselves. Image placeholders show the "
                "exact size they need, the \"how we work\" chapter uses tab navigation across eight slides, and "
                "full-bleed render slides ship with two overlay versions — for light and for dark renders. "
                "The template is also delivered as an editable PowerPoint file."]},
            {"t": "grid", "cols": 2, "items": [
                {"src": "presentations/kp-01"}, {"src": "presentations/kp-02"},
                {"src": "presentations/kp-09"}, {"src": "presentations/kp-12"},
            ]},
        ],
    },
    {
        "slug": "social",
        "title": "Social media campaigns",
        "summary": "Seminar launch across Instagram, stories, Telegram and email, plus a monthly exhibitions carousel.",
        "cover": "social/expo-01",
        "tags": ["Social media", "Campaign", "AI-assisted imagery"],
        "meta": [("Role", "Designer"), ("Client", "MIREX"), ("Year", "2026"), ("Formats", "4:5, 9:16, 1:1, email")],
        "blocks": [
            {"t": "text", "h": "Seminar launch", "p": [
                "An online seminar on exhibiting at medical trade shows needed a full announcement pack: an "
                "Instagram carousel, stories, Telegram squares and email banners. Each format got its own grid "
                "and safe zones, but the same typography, speaker photo and decor, so the campaign reads as one "
                "voice wherever people meet it. Texts follow the client's brief word for word."]},
            {"t": "grid", "cols": 4, "items": [
                {"src": "social/seminar-post-1"}, {"src": "social/seminar-post-2"},
                {"src": "social/seminar-post-3"}, {"src": "social/seminar-post-4"},
            ]},
            {"t": "grid", "cols": 4, "items": [
                {"src": "social/seminar-story-1"}, {"src": "social/seminar-story-2"},
                {"src": "social/seminar-story-3"}, {"src": "social/seminar-story-4"},
            ]},
            {"t": "img", "src": "social/seminar-mail", "cap": "Email banner."},
            {"t": "text", "h": "Exhibitions of the month", "p": [
                "A recurring carousel: one slide per trade show with dates, venue and the show's own logo, "
                "taken from its official site and cleaned up. The cover and the final slide use 3D glass objects "
                "for each industry — generated with an image model, art-directed over several rounds and composed "
                "in Figma. Two earlier cover ideas were rejected along the way."]},
            {"t": "grid", "cols": 5, "items": [{"src": f"social/expo-{i:02d}"} for i in range(1, 11)]},
        ],
    },
    {
        "slug": "print",
        "title": "New Year cards",
        "summary": "Branded New Year cards, chosen from 23 concepts over six rounds.",
        "cover": "print/ny-tree",
        "cover_crop": "top",
        "tags": ["Print", "Illustration", "AI-assisted imagery"],
        "meta": [("Role", "Designer"), ("Client", "MIREX"), ("Year", "2026"), ("Output", "Print-ready PDF, 90×90 mm")],
        "blocks": [
            {"t": "text", "h": "New Year cards", "p": [
                "Six rounds and 23 concepts — frosted-glass scenes, flat illustration drawn in Figma, ring and "
                "garland variations — until the client picked three. The brand arc pattern became the decoration "
                "on the baubles and the tree. Scenes are AI-generated; I extended the top of each scene for "
                "headline space and prepared files with 3 mm bleed."]},
            {"t": "grid", "cols": 3, "items": [
                {"src": "print/ny-baubles"}, {"src": "print/ny-tree"}, {"src": "print/ny-snowflake"},
            ]},
        ],
    },
    {
        "slug": "koko",
        "title": "KoKo — sign language app",
        "summary": "My iOS app for learning Russian Sign Language: a mascot, an illustrated alphabet and on-device gesture recognition.",
        "cover": "koko/cover",
        "tags": ["iOS app", "Illustration", "Swift"],
        "meta": [("Role", "Designer & developer"), ("Client", "Own product"), ("Year", "2026"), ("Stack", "Swift, SwiftUI, Vision, Create ML")],
        "blocks": [
            {"t": "text", "h": "Idea", "p": [
                "KoKo is my Duolingo-style iOS app for Russian Sign Language. Instead of watching videos, you "
                "sign in front of the camera and the app checks the hand shape on device, with Vision and a "
                "Create ML model. Lessons are led by Koko, a monkey in a blue hoodie.",
                "That meant every letter of the fingerspelling alphabet had to be drawn with the mascot — and "
                "the hand shapes had to be correct, not just cute."]},
            {"t": "img", "src": "koko/concept", "cap": "Character sheet: turnaround, palette, details and emotions."},
            {"t": "grid", "cols": 6, "items": [{"src": f"koko/letter-{c}"} for c in ("a", "v", "l", "o", "p", "u")]},
            {"t": "text", "h": "Process", "p": [
                "33 letters; the nine that involve movement get start, end and path frames, 51 images in total, "
                "plus a second set of 42 hand-only images. Images were generated with a strict reference sheet "
                "to keep the character consistent, then cleaned by a Python pipeline: background removal, "
                "artifact clean-up, resizing. Letters where the model kept getting the gesture wrong were "
                "flagged for manual review instead of being shipped."]},
            {"t": "img", "src": "koko/letters-grid", "cap": "The full letter set, А to Я, with start and end frames for moving letters."},
            {"t": "img", "src": "koko/hands-grid", "cap": "Hand-only set for exercises."},
            {"t": "text", "h": "Code", "p": [
                "The app is written in Swift and SwiftUI. Source: github.com/rockstaneverdie/koko-sign-app."]},
        ],
    },
]

SIDE = [
    {
        "title": "Audit — product identity",
        "text": "Identity for an AI service that checks accounting reports: three logo concepts, a walnut-and-brass palette, and a serif + sans type pairing tested on real UI.",
        "img": "audit-identity/logo-concepts",
    },
    {
        "title": "WhatchaSay?",
        "text": "My Firefox extension: a karaoke-style subtitle panel over any video, with AI that explains slang and references in the context of the scene. Brand, UI and code.",
        "img": "whatchasay/preview",
        "link": ("GitHub", "https://github.com/rockstaneverdie/whatchasay"),
    },
]
