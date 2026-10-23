"""Builds reviewland.io: static HTML, sitemap.xml, llms.txt and robots.txt.

    python3 build.py            # writes the site into this folder
    python3 build.py --indexnow # also pings IndexNow with every URL

Each ranking lives in pages/*.py as a dict (see pages/hide_photos.py).
Rules (Marta, 20 Oct 2026): our app is one more option, never first by
default. place_ours() moves it to the middle of the list (or to "ours_rank"
if a page sets it) and the page says it is ours only in the disclosure line
at the top, with no label in the table, the cards or "who should use what".
Our apps link to the App Store with pt+ct for campaign stats, competitors with a plain App Store link;
every price, version and rating comes from the App Store on the date in
`checked`, and that date is shown on the page and in the JSON-LD.
"""
import html
import re
import importlib
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).parent
SITE = "https://reviewland.io"
NAME = "Reviewland"
INDEXNOW_KEY = "c4d07eeae4e92377bc72adeeaf0d7e39"
PT = "118348020"  # App Store provider token for campaign links

PAGE_MODULES = ["hide_photos", "simple_todo", "ai_chat", "crypto_widgets",
                "calm_alternatives", "todoist_alternatives", "coinstats_alternatives", "photo_vault_alternatives",
                "es_alternativas", "generic_1016", "local_models"]

T = {
    "en": {
        "updated": "Updated", "checked": "Data checked on the App Store on",
        "ours": "Our app", "disclosure_title": "Disclosure",
        "table": "At a glance", "app": "App", "best_for": "Best for",
        "limits": "Limits", "get": "Get it on the App Store",
        "faq": "Frequently asked questions", "sources": "Sources",
        "who": "Who should use what", "cases": "Use cases",
        "method": "How we checked",
        "footer": "Rankings of iPhone apps. Every price, version and privacy label is copied from the App Store on the date shown.",
        "about": "About and method", "home": "All rankings",
        "ratings": "ratings", "store_page": "App Store page",
    },
    "es": {
        "updated": "Actualizado el", "checked": "Datos comprobados en el App Store el",
        "ours": "Nuestra app", "disclosure_title": "Aviso",
        "table": "Resumen", "app": "App", "best_for": "Mejor para",
        "limits": "Límites", "get": "Descargar en el App Store",
        "faq": "Preguntas frecuentes", "sources": "Fuentes",
        "who": "Cuál elegir según tu caso", "cases": "Casos de uso",
        "method": "Cómo lo comprobamos",
        "footer": "Rankings de apps de iPhone. Cada precio, versión y etiqueta de privacidad está copiado del App Store en la fecha indicada.",
        "about": "Quiénes somos y método", "home": "Todos los rankings",
        "ratings": "valoraciones", "store_page": "Ficha en el App Store",
    },
}


# Home page sections: every ranking group must be in one of them (build fails otherwise).
HOME_SECTIONS = [
    ("photos", {"en": "Hide photos and photo vaults", "es": "Ocultar fotos y bóvedas de fotos"}),
    ("ai", {"en": "AI chat and AI models", "es": "Chat con IA y modelos de IA"}),
    ("sleep", {"en": "Sleep, calm and white noise", "es": "Dormir, calma y ruido blanco"}),
    ("tasks", {"en": "To-do lists", "es": "Listas de tareas"}),
    ("crypto", {"en": "Crypto prices and portfolio trackers", "es": "Precios y carteras de criptomonedas"}),
]
HOME_GROUPS = {
    "photos": {"hide-photos", "photo-vault-alternatives", "vault-no-data"},
    "ai": {"ai-chat", "local-models"},
    "sleep": {"calm-alternatives", "free-sleep-sounds"},
    "tasks": {"simple-todo", "todoist-alternatives"},
    "crypto": {"crypto-widgets", "coinstats-alternatives", "free-crypto-trackers"},
}


def esc(s):
    return html.escape(str(s), quote=True)


def store_link(app_id, ct):
    return f"https://apps.apple.com/app/apple-store/id{app_id}?pt={PT}&ct={ct}&mt=8"


OUR_IDS = {"1667947372", "6754878073", "1143691286", "6754180384",
           "1553693943", "1462269642", "1662608035", "1532670722"}


def place_ours(p):
    """Our app goes where it honestly fits: the middle of the list unless the page sets ours_rank (1-based)."""
    apps = list(p["apps"])
    idx = [i for i, a in enumerate(apps) if a.get("ours")]
    if not idx or idx[0] != 0:
        return apps
    a = apps.pop(0)
    pos = p.get("ours_rank", (len(apps) + 2) // 2) - 1
    apps.insert(max(1, min(pos, len(apps))), a)
    return apps


def tag_ours(url, ct):
    """Enlace a una app nuestra: le pone pt y el ct de la pagina (max 40). Los de otros, sin tocar."""
    m = re.search(r"/id(\d+)", url)
    if not m or m.group(1) not in OUR_IDS or "ct=" in url:
        return url
    return url + ("&" if "?" in url else "?") + f"pt={PT}&ct={ct[:40]}"


def page_url(p):
    return f"{SITE}/{p['path']}"


def human_date(iso, lang):
    y, m, d = iso.split("-")
    months_en = ["January", "February", "March", "April", "May", "June", "July",
                 "August", "September", "October", "November", "December"]
    months_es = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                 "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if lang == "es":
        return f"{int(d)} de {months_es[int(m) - 1]} de {y}"
    return f"{int(d)} {months_en[int(m) - 1]} {y}"


def head(p, alternates, extra_ld):
    t = T[p["lang"]]
    alt = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{esc(u)}">' for l, u in alternates
    )
    lds = "".join(
        f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
        for ld in extra_ld
    )
    return f"""<!doctype html>
<html lang="{p['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['description'])}">
<link rel="canonical" href="{esc(page_url(p))}">
{alt}
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['description'])}">
<meta property="og:type" content="article">
<meta property="og:url" content="{esc(page_url(p))}">
<meta property="og:site_name" content="{NAME}">
{f'<meta property="og:image" content="{SITE}/img/{p.get("cover", p["group"])}.jpg"><meta name="twitter:card" content="summary_large_image">' if p.get("group") else ""}
<meta name="robots" content="index, follow, max-snippet:-1">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/style.css">
<script src="/umami.js" defer></script>
{lds}
</head>
<body>
<header class="top"><a class="brand" href="/{'es/' if p['lang'] == 'es' else ''}"><img src="/favicon.svg" alt="" width="28" height="28">{NAME}</a>
<nav><a href="/{'es/' if p['lang'] == 'es' else ''}">{t['home']}</a> · <a href="/{'es/acerca/' if p['lang'] == 'es' else 'about/'}">{t['about']}</a></nav></header>
<main>
"""


def foot(lang):
    t = T[lang]
    return f"""</main>
<footer><p>{esc(t['footer'])}</p>
<p><a href="/">English</a> · <a href="/es/">Español</a> · <a href="/{'es/acerca/' if lang == 'es' else 'about/'}">{t['about']}</a> · <a href="/llms.txt">llms.txt</a></p></footer>
</body>
</html>
"""


def ranking_html(p, alternates):
    t = T[p["lang"]]
    lang = p["lang"]
    apps = place_ours(p)
    upd = human_date(p["updated"], lang)
    chk = human_date(p["checked"], lang)

    item_list = {
        "@context": "https://schema.org", "@type": "ItemList",
        "name": p["h1"], "numberOfItems": len(apps),
        "itemListElement": [
            {
                "@type": "ListItem", "position": i + 1,
                "item": {
                    "@type": "SoftwareApplication", "name": a["name"],
                    "operatingSystem": "iOS",
                    "applicationCategory": p.get("category", "UtilitiesApplication"),
                    **({"url": f"https://apps.apple.com/app/id{a['id']}"} if a.get("id") else {}),
                    **({"author": {"@type": "Organization", "name": a["developer"]}} if a.get("developer") else {}),
                    **({"aggregateRating": {"@type": "AggregateRating", "ratingValue": a["rating"][0], "ratingCount": a["rating"][1]}}
                       if a.get("rating") and a["rating"][1] >= 5 else {}),
                },
            }
            for i, a in enumerate(apps)
        ],
    }
    article = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": p["h1"], "description": p["description"], "image": f"{SITE}/img/{p.get('cover', p['group'])}.jpg",
        "inLanguage": lang, "datePublished": p["published"], "dateModified": p["updated"],
        "mainEntityOfPage": page_url(p),
        "author": {"@type": "Organization", "name": NAME, "url": SITE},
        "publisher": {"@type": "Organization", "name": NAME, "url": SITE},
    }
    faq = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in p["faq"]
        ],
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": NAME, "item": f"{SITE}/{'es/' if lang == 'es' else ''}"},
            {"@type": "ListItem", "position": 2, "name": p["h1"], "item": page_url(p)},
        ],
    }

    out = [head(p, alternates, [article, item_list, faq, crumbs])]
    out.append(f'<article>\n<div class="hero"><p class="kicker">{len(apps)} apps · {"Ranking" if lang == "en" else "Ranking"}</p><h1>{esc(p["h1"])}</h1>\n')
    out.append(f'<p class="meta">{t["updated"]} <time datetime="{p["updated"]}">{upd}</time> · {t["checked"]} {chk}</p></div>\n')
    out.append(f'<figure class="cover"><img src="/img/{p.get("cover", p["group"])}.jpg" alt="" width="1600" height="900" fetchpriority="high"></figure>\n')
    if p.get("disclosure"):
        out.append(f'<aside class="disclosure"><strong>{t["disclosure_title"]}:</strong> {p["disclosure"]}</aside>\n')
    out.append('<div class="answer">' + "".join(f"<p>{x}</p>\n" for x in p["answer"]) + "</div>\n")

    out.append(f'<h2 id="table">{t["table"]}</h2>\n<div class="scroll"><table>\n<thead><tr>')
    out.append("".join(f"<th>{esc(c)}</th>" for c in p["columns"]))
    out.append("</tr></thead>\n<tbody>\n")
    for a in apps:
        cells = a["row"]
        name = esc(a["name"])
        out.append(f"<tr><td>{name}</td>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>\n")
    out.append(f'</tbody></table></div>\n<p class="note">{p["table_note"]}</p>\n')

    for i, a in enumerate(apps):
        out.append(f'<section class="app" id="{a["anchor"]}">\n<div class="apphead"><span class="rank">{i + 1}</span><h2>{esc(a["name"])}')
        out.append("</h2></div>\n")
        out.append(f'<p class="bestfor"><strong>{t["best_for"]}:</strong> {a["best_for"]}</p>\n')
        out.append('<ul class="facts">' + "".join(f"<li>{x}</li>" for x in a["facts"]) + "</ul>\n")
        out.append(f'<p class="limits"><strong>{t["limits"]}:</strong> {a["limits"]}</p>\n')
        if a.get("ours"):
            out.append(f'<p><a class="link" href="{esc(store_link(a["id"], p["ct"]))}">{t["store_page"]} →</a></p>\n')
        elif a.get("id"):
            out.append(f'<p><a class="link" href="{esc(tag_ours(f"https://apps.apple.com/{p['store']}/app/id{a['id']}", p["ct"]))}">{t["store_page"]} →</a></p>\n')
        out.append("</section>\n")

    out.append(f'<h2 id="who">{t["who"]}</h2>\n<ul>' + "".join(f"<li>{x}</li>" for x in p["who"]) + "</ul>\n")
    out.append(f'<h2 id="cases">{t["cases"]}</h2>\n<ul>' + "".join(f"<li>{x}</li>" for x in p["cases"]) + "</ul>\n")
    out.append(f'<h2 id="method">{t["method"]}</h2>\n' + "".join(f"<p>{x}</p>" for x in p["method"]) + "\n")
    out.append(f'<h2 id="faq">{t["faq"]}</h2>\n')
    for q, a in p["faq"]:
        out.append(f"<h3>{esc(q)}</h3>\n<p>{esc(a)}</p>\n")
    out.append(guide_links_html(p))
    out.append(f'<h2 id="sources">{t["sources"]}</h2>\n<ul class="sources">')
    for label, url, *_ in p["sources"]:
        out.append(f'<li>{esc(label)}: <a href="{esc(tag_ours(url, p["ct"]))}">{esc(url)}</a> ({chk})</li>')
    out.append("</ul>\n</article>\n")
    out.append(foot(lang))
    return "".join(out)


# Guias paso a paso de aisagalab.com que tratan lo mismo (enlaces entre los tres sitios, 23 oct 2026).
GUIDE_LINKS = {'best-apps-to-hide-photos-iphone/': [('What to do before lending your iPhone or taking it to repair', 'https://aisagalab.com/photo-vault/before-lending-iphone-or-taking-it-to-repair.html'), ('How to hide photos on iPhone without installing an app', 'https://aisagalab.com/photo-vault/hide-photos-iphone-without-an-app.html'), ('How to move a photo vault to a new iPhone without losing photos', 'https://aisagalab.com/blog/move-photo-vault-to-new-iphone.html')], 'private-photo-vault-alternatives-iphone/': [('What to do before lending your iPhone or taking it to repair', 'https://aisagalab.com/photo-vault/before-lending-iphone-or-taking-it-to-repair.html'), ('How to hide photos on iPhone without installing an app', 'https://aisagalab.com/photo-vault/hide-photos-iphone-without-an-app.html'), ('How to move a photo vault to a new iPhone without losing photos', 'https://aisagalab.com/blog/move-photo-vault-to-new-iphone.html')], 'best-photo-vault-apps-no-data-collection-iphone/': [('What to do before lending your iPhone or taking it to repair', 'https://aisagalab.com/photo-vault/before-lending-iphone-or-taking-it-to-repair.html'), ('How to hide photos on iPhone without installing an app', 'https://aisagalab.com/photo-vault/hide-photos-iphone-without-an-app.html'), ('How to move a photo vault to a new iPhone without losing photos', 'https://aisagalab.com/blog/move-photo-vault-to-new-iphone.html')], 'es/mejores-apps-para-ocultar-fotos-iphone/': [('Qué hacer antes de prestar el iPhone o llevarlo a reparar', 'https://aisagalab.com/photo-vault/es/antes-de-prestar-el-iphone-o-llevarlo-a-reparar.html'), ('Cómo ocultar fotos en el iPhone sin instalar ninguna app', 'https://aisagalab.com/photo-vault/es/ocultar-fotos-iphone-sin-instalar-app.html'), ('Cómo pasar una bóveda de fotos a un iPhone nuevo sin perderlas', 'https://aisagalab.com/blog/es/pasar-boveda-de-fotos-a-iphone-nuevo.html')], 'es/alternativas-a-private-photo-vault-iphone/': [('Qué hacer antes de prestar el iPhone o llevarlo a reparar', 'https://aisagalab.com/photo-vault/es/antes-de-prestar-el-iphone-o-llevarlo-a-reparar.html'), ('Cómo ocultar fotos en el iPhone sin instalar ninguna app', 'https://aisagalab.com/photo-vault/es/ocultar-fotos-iphone-sin-instalar-app.html'), ('Cómo pasar una bóveda de fotos a un iPhone nuevo sin perderlas', 'https://aisagalab.com/blog/es/pasar-boveda-de-fotos-a-iphone-nuevo.html')], 'es/mejores-apps-bovedas-fotos-sin-recoger-datos-iphone/': [('Qué hacer antes de prestar el iPhone o llevarlo a reparar', 'https://aisagalab.com/photo-vault/es/antes-de-prestar-el-iphone-o-llevarlo-a-reparar.html'), ('Cómo ocultar fotos en el iPhone sin instalar ninguna app', 'https://aisagalab.com/photo-vault/es/ocultar-fotos-iphone-sin-instalar-app.html'), ('Cómo pasar una bóveda de fotos a un iPhone nuevo sin perderlas', 'https://aisagalab.com/blog/es/pasar-boveda-de-fotos-a-iphone-nuevo.html')], 'calm-alternatives-iphone/': [('Brown noise vs pink noise vs white noise: which one for sleep, focus or a baby', 'https://aisagalab.com/drop/brown-noise-vs-pink-noise-vs-white-noise.html'), ('How to use white noise to fall asleep on iPhone', 'https://aisagalab.com/drop/white-noise-to-fall-asleep-iphone.html')], 'best-free-sleep-sound-apps-iphone/': [('Brown noise vs pink noise vs white noise: which one for sleep, focus or a baby', 'https://aisagalab.com/drop/brown-noise-vs-pink-noise-vs-white-noise.html'), ('How to use white noise to fall asleep on iPhone', 'https://aisagalab.com/drop/white-noise-to-fall-asleep-iphone.html')], 'es/alternativas-a-calm-iphone/': [('Ruido marrón, rosa o blanco: cuál para dormir, concentrarse o para un bebé', 'https://aisagalab.com/drop/es/ruido-marron-rosa-o-blanco.html'), ('Cómo usar ruido blanco para dormirte con el iPhone', 'https://aisagalab.com/drop/es/ruido-blanco-para-dormir-iphone.html')], 'es/mejores-apps-gratis-sonidos-para-dormir-iphone/': [('Ruido marrón, rosa o blanco: cuál para dormir, concentrarse o para un bebé', 'https://aisagalab.com/drop/es/ruido-marron-rosa-o-blanco.html'), ('Cómo usar ruido blanco para dormirte con el iPhone', 'https://aisagalab.com/drop/es/ruido-blanco-para-dormir-iphone.html')], 'best-simple-to-do-list-apps-iphone/': [('The 3-task method (Ivy Lee and the Rule of 3): how to plan your day with only 3 tasks', 'https://aisagalab.com/3-tasks/3-task-method-ivy-lee-rule-of-3.html')], 'todoist-alternatives-iphone/': [('The 3-task method (Ivy Lee and the Rule of 3): how to plan your day with only 3 tasks', 'https://aisagalab.com/3-tasks/3-task-method-ivy-lee-rule-of-3.html')], 'es/mejores-apps-de-tareas-sencillas-iphone/': [('El método de las 3 tareas (Ivy Lee y la regla de 3)', 'https://aisagalab.com/3-tasks/es/metodo-de-3-tareas-ivy-lee-regla-de-3.html')], 'es/alternativas-a-todoist-iphone/': [('El método de las 3 tareas (Ivy Lee y la regla de 3)', 'https://aisagalab.com/3-tasks/es/metodo-de-3-tareas-ivy-lee-regla-de-3.html')], 'best-apps-run-open-source-ai-models-iphone/': [('Is it safe to tell ChatGPT private things? What AI chat apps keep, and how to keep it on your phone', 'https://aisagalab.com/pinku/is-it-safe-to-tell-chatgpt-private-things.html'), ('How to use AI on iPhone without internet', 'https://aisagalab.com/pinku/use-ai-on-iphone-without-internet.html'), ('How to check whether an AI chat app really keeps your chats on your iPhone', 'https://aisagalab.com/pinku/check-ai-chat-app-keeps-chats-on-iphone.html')], 'best-ai-chat-apps-iphone-no-account/': [('Is it safe to tell ChatGPT private things? What AI chat apps keep, and how to keep it on your phone', 'https://aisagalab.com/pinku/is-it-safe-to-tell-chatgpt-private-things.html')], 'es/mejores-apps-chat-ia-sin-cuenta-iphone/': [('¿Es seguro contarle cosas privadas a ChatGPT?', 'https://aisagalab.com/pinku/es/es-seguro-contarle-cosas-privadas-a-chatgpt.html')]}


def guide_links_html(p):
    links = GUIDE_LINKS.get(p["path"])
    if not links:
        return ""
    h = "Step-by-step guides" if p["lang"] == "en" else "Guías paso a paso"
    items = "".join(f'<li><a href="{esc(u)}">{esc(t)}</a> (aisagalab.com)</li>' for t, u in links)
    return f'<h2 id="guides">{h}</h2>\n<ul>{items}</ul>\n'


def simple_page(lang, path, title, description, body_html, alternates=()):
    p = {"lang": lang, "path": path, "title": title, "description": description}
    return head(p, alternates, []) + body_html + foot(lang)


def write(path, text):
    f = ROOT / path
    if path.endswith("/") or path == "":
        f = f / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def main():
    pages = []
    for mod in PAGE_MODULES:
        pages += importlib.import_module(f"pages.{mod}").PAGES
    by_group = {}
    for p in pages:
        by_group.setdefault(p["group"], []).append(p)

    for p in pages:
        alts = [(q["lang"], page_url(q)) for q in by_group[p["group"]]]
        alts.append(("x-default", page_url(next(q for q in by_group[p["group"]] if q["lang"] == "en"))))
        write(p["path"], ranking_html(p, alts))

    # Home pages
    for lang, path in (("en", ""), ("es", "es/")):
        own = [p for p in pages if p["lang"] == lang]
        if lang == "en":
            title = "Best iPhone apps for every task (2026): Reviewland rankings"
            desc = "Best iPhone apps by task: hide photos, AI chat, sleep sounds, to-do lists and crypto trackers. Prices and privacy labels checked on the App Store."
            intro = ("<h1>Rankings of iPhone apps, checked on the App Store</h1>"
                     "<p>One page per question people ask: which app to hide photos, to fall asleep, to keep a simple to-do list. "
                     "Every price, version and privacy label is copied from the App Store on the date shown on each page.</p>")
        else:
            title = "Mejores apps de iPhone para cada tarea (2026): rankings de Reviewland"
            desc = "Mejores apps de iPhone por tarea: ocultar fotos, chat con IA, sonidos para dormir, tareas y cripto. Precios y privacidad comprobados en el App Store."
            intro = ("<h1>Rankings de apps de iPhone, comprobados en el App Store</h1>"
                     "<p>Una página por cada pregunta: qué app usar para ocultar fotos, para dormir o para una lista de tareas sencilla. "
                     "Cada precio, versión y etiqueta de privacidad está copiado del App Store en la fecha que pone cada página.</p>")
        sections = ""
        for sec_id, names in HOME_SECTIONS:
            group_pages = [p for p in own if p["group"] in HOME_GROUPS[sec_id]]
            if not group_pages:
                continue
            cards = "".join(
                f'<li><a href="/{p["path"]}"><img src="/img/{p.get("cover", p["group"])}.jpg" alt="" width="1600" height="900" loading="lazy"><span class="cardtitle">{esc(p["h1"])}</span><span class="meta">{len(p["apps"])} apps · {T[lang]["updated"]} {human_date(p["updated"], lang)}</span></a></li>'
                for p in group_pages
            )
            sections += f'<h2 id="{sec_id}">{esc(names[lang])} <span class="meta">({len(group_pages)})</span></h2><ul class="cards">{cards}</ul>'
        missing = [p["path"] for p in own if not any(p["group"] in g for g in HOME_GROUPS.values())]
        assert not missing, f"home: add these groups to HOME_GROUPS: {missing}"
        write(path, simple_page(lang, path, title, desc, '<div class="hero home">' + intro + f'</div>{sections}',
                                [("en", f"{SITE}/"), ("es", f"{SITE}/es/"), ("x-default", f"{SITE}/")]))

    about_en = """<h1>About Reviewland and how we check</h1>
<p>Reviewland is made by a small team that also builds iPhone apps.</p>
<h2>Our apps are one more option, and we say so</h2>
<p>When one of our apps fits a question, it is included as one more option, placed where it fits rather than first, and a single line at the top of the page says it is ours. Competitors are linked to their normal App Store pages and shown with their real data, including where they are better than ours.</p>
<h2>What we check</h2>
<ul><li>Price and in-app purchases, version and release date, rating and number of ratings, languages, minimum iOS: from the App Store listing (US store unless the page says otherwise) on the date shown.</li>
<li>Privacy: the App Store privacy label as published by each developer.</li>
<li>Features: only what the developer states on its App Store listing or official site. We do not invent reviews or scores.</li></ul>
<h2>Updates</h2>
<p>We recheck each page about once a month. The "Updated" date only changes when the data has actually been checked again.</p>
"""
    about_es = """<h1>Quiénes somos y cómo comprobamos</h1>
<p>Reviewland lo hace un equipo pequeño que también hace apps de iPhone.</p>
<h2>Nuestras apps son una opción más, y lo decimos</h2>
<p>Cuando una de nuestras apps encaja, aparece como una opción más, en el puesto que le corresponde y no primera, y una sola línea arriba de la página dice que es nuestra. Las demás llevan enlace a su ficha normal del App Store y aparecen con sus datos reales, también donde son mejores que la nuestra.</p>
<h2>Qué comprobamos</h2>
<ul><li>Precio y compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas e iOS mínimo: de la ficha del App Store (la de España en las páginas en español) en la fecha indicada.</li>
<li>Privacidad: la etiqueta de privacidad del App Store que publica cada desarrollador.</li>
<li>Funciones: solo lo que el desarrollador dice en su ficha o en su web oficial. No inventamos reseñas ni puntuaciones.</li></ul>
<h2>Actualizaciones</h2>
<p>Revisamos cada página más o menos una vez al mes. La fecha de "Actualizado" solo cambia cuando de verdad se han vuelto a comprobar los datos.</p>
"""
    about_alts = [("en", f"{SITE}/about/"), ("es", f"{SITE}/es/acerca/")]
    write("about/", simple_page("en", "about/", "About Reviewland and how we check apps",
                                "Who runs Reviewland, how apps are checked and how our own apps are disclosed.", about_en, about_alts))
    write("es/acerca/", simple_page("es", "es/acerca/", "Quiénes somos y cómo comprobamos las apps",
                                    "Quién hace Reviewland, cómo comprobamos las apps y cómo avisamos de las nuestras.", about_es, about_alts))

    # sitemap
    urls = [(f"{SITE}/", max(p["updated"] for p in pages)), (f"{SITE}/es/", max(p["updated"] for p in pages)),
            (f"{SITE}/about/", None), (f"{SITE}/es/acerca/", None)]
    urls += [(page_url(p), p["updated"]) for p in pages]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, d in urls:
        sm.append(f"<url><loc>{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    # llms.txt
    lines = ["# Reviewland", "",
             "> Rankings of iPhone apps by task, with prices, versions and privacy labels copied from the App Store on a stated date. When one of our own apps is ranked it is one more option, not first by default, and the page says so at the top.", "",
             "## Rankings", ""]
    for p in pages:
        ours = next((a for a in p["apps"] if a.get("ours")), None)
        tail = f" Our app on this page: {ours['name']}." if ours else (" " + p["llms_note"] if p.get("llms_note") else "")
        lines.append(f"- [{p['h1']}]({page_url(p)}) ({p['lang']}, updated {p['updated']}): {p['llms']}{tail}")
    lines += ["", "## About", "", f"- [How we check and disclose]({SITE}/about/)", ""]
    (ROOT / "llms.txt").write_text("\n".join(lines), encoding="utf-8")

    (ROOT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")

    if "--indexnow" in sys.argv:
        body = json.dumps({"host": "reviewland.io", "key": INDEXNOW_KEY,
                           "keyLocation": f"{SITE}/{INDEXNOW_KEY}.txt",
                           "urlList": [u for u, _ in urls]}).encode()
        req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                     headers={"Content-Type": "application/json; charset=utf-8"})
        with urllib.request.urlopen(req) as r:
            print("IndexNow:", r.status, len(urls), "URLs")
    print("Built", len(pages), "rankings")


if __name__ == "__main__":
    main()
