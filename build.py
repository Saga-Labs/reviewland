"""Builds reviewland.io: static HTML, sitemap.xml, llms.txt and robots.txt.

    python3 build.py            # writes the site into this folder
    python3 build.py --indexnow # also pings IndexNow with every URL

Each ranking lives in pages/*.py as a dict (see pages/hide_photos.py).
Rules (Marta, 20 Oct 2026): our app is one more option, never first by
default. place_ours() moves it to the middle of the list (or to "ours_rank"
if a page sets it) and articles do not mention ownership (Marta, 2 Nov 2026): that stays in the
footer, About and llms.txt, with no label in the table, the cards or "who should use what".
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
                "es_alternativas", "generic_1016", "local_models", "chatgpt_apps", "nov02_video", "nov02_dora5", "nov02_chatgpt_video", "nov03_video_models", "nov03_text_video", "nov03_habits", "nov03_crypto_alerts", "nov03_photo_enhancer", "nov03_homework", "nov03_video_sound", "nov03_deepseek_alt", "nov03_video_ipad", "nov03_trend_video", "nov03_video_sound_es", "nov03_poe_alt", "nov03_grok_alt", "nov03_videogpt_alt", "nov03_calculator_vault_alt", "nov03_pocketpal_alt", "nov03_crypto_no_connect", "nov04_higgsfield_alt", "nov04_vault_backup", "nov04_pdf_offline", "nov04_pollo_alt", "nov04_hide_it_pro_alt", "nov04_binaural", "nov08_wlfi_trump",
                "tr_ru", "tr_de", "tr_ja", "tr_ptbr", "tr_fr", "tr_ar"]

from langs import LANGS  # one table of languages: prefix, html lang, dir, date format, UI strings

T = {code: L["ui"] for code, L in LANGS.items()}
ACTIVE = []  # languages that have pages, in LANGS order (filled in main)


def prefix_of(lang):
    """URL folder of a language with a trailing slash ("" for English)."""
    pre = LANGS[lang]["prefix"]
    return f"{pre}/" if pre else ""


def about_path(lang):
    return {"en": "about/", "es": "es/acerca/"}.get(lang) or f"{prefix_of(lang)}about/"


# Home page sections: every ranking group must be in one of them (build fails otherwise).
HOME_SECTIONS = [(sec, sec) for sec in ("photos", "ai", "study", "ai-video", "photo-editing", "sleep", "tasks", "habits", "crypto")]
HOME_GROUPS = {
    "photos": {"hide-photos", "photo-vault-alternatives", "vault-no-data", "calculator-vault-alternatives", "vault-backup", "hide-it-pro-alternatives"},
    "ai": {"ai-chat", "local-models", "chatgpt-apps", "chatgpt-video", "deepseek-alternatives", "poe-alternatives", "pocketpal-alternatives", "pdf-offline"},
    "ai-video": {"make-video", "free-video", "capcut-alt", "reels-apps", "photo-talk-family", "sora-alt", "text-video", "video-models", "text-video-list", "video-sound", "video-ipad", "trend-video", "grok-imagine-alternatives", "videogpt-alternatives", "higgsfield-alternatives", "pollo-alternatives"},
    "photo-editing": {"photo-enhancer"},
    "sleep": {"calm-alternatives", "free-sleep-sounds", "binaural-beats"},
    "tasks": {"simple-todo", "todoist-alternatives"},
    "habits": {"habit-trackers"},
    "study": {"homework-helpers"},
    "crypto": {"crypto-widgets", "coinstats-alternatives", "free-crypto-trackers", "crypto-alerts", "crypto-no-connect", "wlfi-trump-trackers"},
}


def esc(s):
    return html.escape(str(s), quote=True)


def store_link(app_id, ct):
    extra = f"&ppid={askai_ppid(ct)}" if str(app_id) == ASKAI_ID else ""
    return f"https://apps.apple.com/app/apple-store/id{app_id}?pt={PT}&ct={ct}&mt=8" + extra


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


# Ask AI: Custom Product Pages aprobadas el 7 nov 2026 (#80). Cada enlace va a la página de su tema.
ASKAI_ID = "1662608035"
ASKAI_PPID = {
    "fotos": "2275a5f5-5264-4ade-98ab-7f7ca0ccdb1a",
    "modelo": "420fcaf3-b818-460e-a74f-1cb8fe2a787a",
    "traducir": "735d27ce-2811-4b20-9d3c-7bfad431030d",
}


def askai_ppid(ct):
    """Tema de la página (por su ct): imágenes -> fotos; traducir -> traducir; lo demás (chat, modelos) -> modelo."""
    c = (ct or "").lower()
    if re.search(r"translat|tradu|uebersetz|ubersetz|perevod", c):
        return ASKAI_PPID["traducir"]
    if re.search(r"image|photo|picture|imagen|imagem|bild|foto|画像", c):
        return ASKAI_PPID["fotos"]
    return ASKAI_PPID["modelo"]


def tag_ours(url, ct):
    """Enlace a una app nuestra: le pone pt y el ct de la pagina (max 40). Los de otros, sin tocar."""
    m = re.search(r"/id(\d+)", url)
    if not m or m.group(1) not in OUR_IDS:
        return url
    extra = f"&ppid={askai_ppid(ct)}" if m.group(1) == ASKAI_ID and "ppid=" not in url else ""
    if "ct=" in url:
        return url + extra
    return url + ("&" if "?" in url else "?") + f"pt={PT}&ct={ct[:40]}" + extra


def cover_of(p):
    """Cover image name, or None. A page without group (home, about) or with "cover": None has no image."""
    if not p.get("group") or ("cover" in p and not p["cover"]):
        return None
    return p.get("cover", p["group"])


def page_url(p):
    return f"{SITE}/{p['path']}"


def last_change(url):
    """Date the built HTML of a URL last changed: today if the build just changed it, else its last commit.
    The visible "Updated" date stays the data-check date; the sitemap lastmod also moves when the page text changes."""
    import subprocess, datetime
    rel = url[len(SITE) + 1:] + "index.html"
    try:
        if subprocess.run(["git", "-C", str(ROOT), "diff", "--quiet", "HEAD", "--", rel]).returncode == 1:
            return datetime.date.today().isoformat()
        out = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%cs", "--", rel],
                             capture_output=True, text=True).stdout.strip()
        return out or None
    except OSError:
        return None


def lastmod(url, updated):
    dates = [d for d in (updated, last_change(url)) if d]
    return max(dates) if dates else None


def human_date(iso, lang):
    y, m, d = iso.split("-")
    L = LANGS[lang]
    return L["date"].format(d=int(d), m=L["months"][int(m) - 1], y=y)


def hl(code):
    """hreflang / html lang value for a language code (x-default stays as is)."""
    return LANGS[code]["html"] if code in LANGS else code


def head(p, alternates, extra_ld):
    t = T[p["lang"]]
    alt = "".join(
        f'<link rel="alternate" hreflang="{hl(l)}" href="{esc(u)}">' for l, u in alternates
    )
    lds = "".join(
        f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
        for ld in extra_ld
    )
    return f"""<!doctype html>
<html lang="{hl(p['lang'])}"{' dir="rtl"' if LANGS[p['lang']]['dir'] == 'rtl' else ''}>
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
{f'<meta property="og:image" content="{SITE}/img/{cover_of(p)}.jpg"><meta name="twitter:card" content="summary_large_image">' if cover_of(p) else ""}
<meta name="robots" content="index, follow, max-snippet:-1">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<link rel="stylesheet" href="/style.css">
<script src="/umami.js" defer></script>
{lds}
</head>
<body>
<header class="top"><a class="brand" href="/{prefix_of(p['lang'])}"><img src="/favicon.svg" alt="" width="28" height="28">{NAME}</a>
<nav><a href="/{prefix_of(p['lang'])}">{t['home']}</a> · <a href="/{about_path(p['lang'])}">{t['about']}</a></nav></header>
<main>
"""


def lang_switch():
    return " · ".join(f'<a href="/{prefix_of(c)}">{LANGS[c]["name"]}</a>' for c in ACTIVE)


def foot(lang):
    t = T[lang]
    return f"""</main>
<footer><p>{esc(t['footer'])}</p>
<p>{lang_switch()} · <a href="/{about_path(lang)}">{t['about']}</a> · <a href="/llms.txt">llms.txt</a></p></footer>
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
                    "operatingSystem": p.get("os", "iOS"),
                    "applicationCategory": p.get("category", "UtilitiesApplication"),
                    **({"url": a["url"]} if a.get("url") else {"url": f"https://apps.apple.com/app/id{a['id']}"} if a.get("id") else {}),
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
        "headline": p["h1"], "description": p["description"], **({"image": f"{SITE}/img/{cover_of(p)}.jpg"} if cover_of(p) else {}),
        "inLanguage": hl(lang), "datePublished": p["published"], "dateModified": p["updated"],
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
            {"@type": "ListItem", "position": 1, "name": NAME, "item": f"{SITE}/{prefix_of(lang)}"},
            {"@type": "ListItem", "position": 2, "name": p["h1"], "item": page_url(p)},
        ],
    }

    out = [head(p, alternates, [article, item_list, faq, crumbs])]
    out.append(f'<article>\n<div class="hero"><p class="kicker">{esc(p.get("kicker", f"{len(apps)} apps · Ranking"))}</p><h1>{esc(p["h1"])}</h1>\n')
    out.append(f'<p class="meta">{t["updated"]} <time datetime="{p["updated"]}">{upd}</time> · {p.get("checked_label", t["checked"])} {chk}</p></div>\n')
    if cover_of(p):
        out.append(f'<figure class="cover"><img src="/img/{cover_of(p)}.jpg" alt="" width="1200" height="675" fetchpriority="high"></figure>\n')
    out.append('<div class="answer">' + "".join(f"<p>{x}</p>\n" for x in p["answer"]) + "</div>\n")
    if p.get("cta"):  # download button(s) right after the answer, with one line on which complaint they fix
        c = p["cta"]
        btns = ""
        for label, app_id in c["buttons"]:
            href = store_link(app_id, p["ct"]) if str(app_id) in OUR_IDS else f"https://apps.apple.com/{p['store']}/app/id{app_id}"
            btns += f'<a class="cta" href="{esc(href)}">{esc(label)}</a> '
        out.append(f'<div class="cta-box"><p>{c["line"]}</p><p>{btns}</p></div>\n')
    for cp in p.get("complaints", []):  # one section per repeated 1-2 star complaint, with the fix
        out.append(f'<h2 id="{cp["id"]}">{esc(cp["h2"])}</h2>\n' + "".join(f"<p>{x}</p>\n" for x in cp["body"]))
    if p.get("context_html"):  # news pages: dated context and a small data table before the ranking
        out.append(p["context_html"])

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
        if a.get("url"):
            out.append(f'<p><a class="link" href="{esc(a["url"])}">{esc(p.get("link_label", t["store_page"]))} →</a></p>\n')
        elif a.get("ours"):
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
    out.append(related_html(p))
    out.append(guide_links_html(p))
    out.append(f'<h2 id="sources">{t["sources"]}</h2>\n<ul class="sources">')
    for label, url, *_ in p["sources"]:
        out.append(f'<li>{esc(label)}: <a href="{esc(tag_ours(url, p["ct"]))}">{esc(url)}</a> ({chk})</li>')
    out.append("</ul>\n</article>\n")
    out.append(foot(lang))
    return "".join(out)


# Guias paso a paso de aisagalab.com que tratan lo mismo (enlaces entre los tres sitios, 23 oct 2026).
GUIDE_LINKS = {'sora-alternatives-by-use-iphone/': [('Best Sora app alternatives for iPhone, with more detail on each app', 'https://reditor.cloud/sora-app-alternatives-iphone/'), ('The same prompt in 8 AI video models', 'https://doravideo.com/blog/8-ai-video-models-same-prompt-test')], 'how-to-turn-text-into-video-iphone/': [('The same prompt in 8 AI video models', 'https://doravideo.com/blog/8-ai-video-models-same-prompt-test'), ('Turn a story or script into an AI video series', 'https://doravideo.com/blog/turn-a-story-script-into-an-ai-video-series')], 'best-apps-to-hide-photos-iphone/': [('What to do before lending your iPhone or taking it to repair', 'https://aisagalab.com/photo-vault/before-lending-iphone-or-taking-it-to-repair.html'), ('How to hide photos on iPhone without installing an app', 'https://aisagalab.com/photo-vault/hide-photos-iphone-without-an-app.html'), ('How to move a photo vault to a new iPhone without losing photos', 'https://aisagalab.com/blog/move-photo-vault-to-new-iphone.html')], 'private-photo-vault-alternatives-iphone/': [('What to do before lending your iPhone or taking it to repair', 'https://aisagalab.com/photo-vault/before-lending-iphone-or-taking-it-to-repair.html'), ('How to hide photos on iPhone without installing an app', 'https://aisagalab.com/photo-vault/hide-photos-iphone-without-an-app.html'), ('How to move a photo vault to a new iPhone without losing photos', 'https://aisagalab.com/blog/move-photo-vault-to-new-iphone.html')], 'best-photo-vault-apps-no-data-collection-iphone/': [('What to do before lending your iPhone or taking it to repair', 'https://aisagalab.com/photo-vault/before-lending-iphone-or-taking-it-to-repair.html'), ('How to hide photos on iPhone without installing an app', 'https://aisagalab.com/photo-vault/hide-photos-iphone-without-an-app.html'), ('How to move a photo vault to a new iPhone without losing photos', 'https://aisagalab.com/blog/move-photo-vault-to-new-iphone.html')], 'es/mejores-apps-para-ocultar-fotos-iphone/': [('Qué hacer antes de prestar el iPhone o llevarlo a reparar', 'https://aisagalab.com/photo-vault/es/antes-de-prestar-el-iphone-o-llevarlo-a-reparar.html'), ('Cómo ocultar fotos en el iPhone sin instalar ninguna app', 'https://aisagalab.com/photo-vault/es/ocultar-fotos-iphone-sin-instalar-app.html'), ('Cómo pasar una bóveda de fotos a un iPhone nuevo sin perderlas', 'https://aisagalab.com/blog/es/pasar-boveda-de-fotos-a-iphone-nuevo.html')], 'es/alternativas-a-private-photo-vault-iphone/': [('Qué hacer antes de prestar el iPhone o llevarlo a reparar', 'https://aisagalab.com/photo-vault/es/antes-de-prestar-el-iphone-o-llevarlo-a-reparar.html'), ('Cómo ocultar fotos en el iPhone sin instalar ninguna app', 'https://aisagalab.com/photo-vault/es/ocultar-fotos-iphone-sin-instalar-app.html'), ('Cómo pasar una bóveda de fotos a un iPhone nuevo sin perderlas', 'https://aisagalab.com/blog/es/pasar-boveda-de-fotos-a-iphone-nuevo.html')], 'es/mejores-apps-bovedas-fotos-sin-recoger-datos-iphone/': [('Qué hacer antes de prestar el iPhone o llevarlo a reparar', 'https://aisagalab.com/photo-vault/es/antes-de-prestar-el-iphone-o-llevarlo-a-reparar.html'), ('Cómo ocultar fotos en el iPhone sin instalar ninguna app', 'https://aisagalab.com/photo-vault/es/ocultar-fotos-iphone-sin-instalar-app.html'), ('Cómo pasar una bóveda de fotos a un iPhone nuevo sin perderlas', 'https://aisagalab.com/blog/es/pasar-boveda-de-fotos-a-iphone-nuevo.html')], 'calm-alternatives-iphone/': [('Brown noise vs pink noise vs white noise: which one for sleep, focus or a baby', 'https://aisagalab.com/drop/brown-noise-vs-pink-noise-vs-white-noise.html'), ('How to use white noise to fall asleep on iPhone', 'https://aisagalab.com/drop/white-noise-to-fall-asleep-iphone.html')], 'best-free-sleep-sound-apps-iphone/': [('Brown noise vs pink noise vs white noise: which one for sleep, focus or a baby', 'https://aisagalab.com/drop/brown-noise-vs-pink-noise-vs-white-noise.html'), ('How to use white noise to fall asleep on iPhone', 'https://aisagalab.com/drop/white-noise-to-fall-asleep-iphone.html')], 'es/alternativas-a-calm-iphone/': [('Ruido marrón, rosa o blanco: cuál para dormir, concentrarse o para un bebé', 'https://aisagalab.com/drop/es/ruido-marron-rosa-o-blanco.html'), ('Cómo usar ruido blanco para dormirte con el iPhone', 'https://aisagalab.com/drop/es/ruido-blanco-para-dormir-iphone.html')], 'es/mejores-apps-gratis-sonidos-para-dormir-iphone/': [('Ruido marrón, rosa o blanco: cuál para dormir, concentrarse o para un bebé', 'https://aisagalab.com/drop/es/ruido-marron-rosa-o-blanco.html'), ('Cómo usar ruido blanco para dormirte con el iPhone', 'https://aisagalab.com/drop/es/ruido-blanco-para-dormir-iphone.html')], 'best-simple-to-do-list-apps-iphone/': [('The 3-task method (Ivy Lee and the Rule of 3): how to plan your day with only 3 tasks', 'https://aisagalab.com/3-tasks/3-task-method-ivy-lee-rule-of-3.html')], 'todoist-alternatives-iphone/': [('The 3-task method (Ivy Lee and the Rule of 3): how to plan your day with only 3 tasks', 'https://aisagalab.com/3-tasks/3-task-method-ivy-lee-rule-of-3.html')], 'es/mejores-apps-de-tareas-sencillas-iphone/': [('El método de las 3 tareas (Ivy Lee y la regla de 3)', 'https://aisagalab.com/3-tasks/es/metodo-de-3-tareas-ivy-lee-regla-de-3.html')], 'es/alternativas-a-todoist-iphone/': [('El método de las 3 tareas (Ivy Lee y la regla de 3)', 'https://aisagalab.com/3-tasks/es/metodo-de-3-tareas-ivy-lee-regla-de-3.html')], 'best-apps-run-open-source-ai-models-iphone/': [('Is it safe to tell ChatGPT private things? What AI chat apps keep, and how to keep it on your phone', 'https://aisagalab.com/pinku/is-it-safe-to-tell-chatgpt-private-things.html'), ('How to use AI on iPhone without internet', 'https://aisagalab.com/pinku/use-ai-on-iphone-without-internet.html'), ('How to check whether an AI chat app really keeps your chats on your iPhone', 'https://aisagalab.com/pinku/check-ai-chat-app-keeps-chats-on-iphone.html')], 'best-ai-chat-apps-iphone-no-account/': [('Is it safe to tell ChatGPT private things? What AI chat apps keep, and how to keep it on your phone', 'https://aisagalab.com/pinku/is-it-safe-to-tell-chatgpt-private-things.html')], 'es/mejores-apps-chat-ia-sin-cuenta-iphone/': [('¿Es seguro contarle cosas privadas a ChatGPT?', 'https://aisagalab.com/pinku/es/es-seguro-contarle-cosas-privadas-a-chatgpt.html')]}


ALL_PAGES = []


def related_html(p):
    """Links to the other rankings of the same home section and language, so no page is a dead end."""
    groups = next((g for g in HOME_GROUPS.values() if p["group"] in g), set())
    # hide_from_related: la página sale en la portada pero aún no en «Related» de las demás (protegidas fijas hasta la lectura del 10 nov)
    rel = [q for q in ALL_PAGES if q["lang"] == p["lang"] and q["group"] in groups and q["path"] != p["path"] and not q.get("hide_from_related")]
    if not rel:
        return ""
    h = T[p["lang"]]["related"]
    items = "".join(f'<li><a href="/{q["path"]}">{esc(q["h1"])}</a></li>' for q in rel[:5])
    return f'<h2 id="related">{h}</h2>\n<ul>{items}</ul>\n'


def guide_links_html(p):
    links = GUIDE_LINKS.get(p["path"])
    if not links:
        return ""
    h = T[p["lang"]]["guides"]
    items = "".join(f'<li><a href="{esc(u)}">{esc(t)}</a> ({u.split("/")[2]})</li>' for t, u in links)
    return f'<h2 id="guides">{h}</h2>\n<ul>{items}</ul>\n'


def simple_page(lang, path, title, description, body_html, alternates=(), ld=()):
    p = {"lang": lang, "path": path, "title": title, "description": description}
    return head(p, alternates, list(ld)) + body_html + foot(lang)


def card_img(p):
    return f'<img src="/img/{cover_of(p)}.jpg" alt="" width="1200" height="675" loading="lazy">' if cover_of(p) else ""


def write(path, text):
    f = ROOT / path
    if path.endswith("/") or path == "":
        f = f / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def write_404():
    links = " · ".join(f'<a href="/{prefix_of(c)}">{T[c]["home"]}</a>' for c in ACTIVE)
    body = ('<div class="hero home"><h1>Page not found</h1><p>That page does not exist or has moved. '
            + links + '</p></div>')
    html_404 = simple_page("en", "", "Page not found: Reviewland", "This page does not exist.", body)
    html_404 = html_404.replace('content="index, follow, max-snippet:-1"', 'content="noindex"')
    html_404 = re.sub(r'<link rel="canonical"[^>]*>\n', "", html_404)
    (ROOT / "404.html").write_text(html_404, encoding="utf-8")


def main():
    pages = []
    for mod in PAGE_MODULES:
        pages += importlib.import_module(f"pages.{mod}").PAGES
    ALL_PAGES[:] = pages
    ACTIVE[:] = [c for c in LANGS if any(p["lang"] == c for p in pages)]
    for p in pages:
        assert p["lang"] in LANGS, p["path"]
        assert len(p["ct"]) <= 40, f"ct too long: {p['ct']}"
        assert p["path"].startswith(prefix_of(p["lang"])), f"{p['path']} is not under /{prefix_of(p['lang'])}"
    by_group = {}
    for p in pages:
        by_group.setdefault(p["group"], []).append(p)

    for p in pages:
        alts = [(q["lang"], page_url(q)) for q in by_group[p["group"]]]
        assert len({l for l, _ in alts}) == len(alts), f"duplicate language in group {p['group']}"
        alts.append(("x-default", page_url(next(q for q in by_group[p["group"]] if q["lang"] == "en"))))
        write(p["path"], ranking_html(p, alts))

    # Home pages
    home_alts = [(c, f"{SITE}/{prefix_of(c)}") for c in ACTIVE] + [("x-default", f"{SITE}/")]
    for lang in ACTIVE:
        path = prefix_of(lang)
        own = [p for p in pages if p["lang"] == lang]
        title, desc = T[lang]["home_title"], T[lang]["home_desc"]
        intro = f'<h1>{T[lang]["home_h1"]}</h1><p>{T[lang]["home_p"]}</p>'
        sections = ""
        for sec_id, _ in HOME_SECTIONS:
            group_pages = [p for p in own if p["group"] in HOME_GROUPS[sec_id]]
            if not group_pages:
                continue
            cards = "".join(
                f'<li><a href="/{p["path"]}">{card_img(p)}<span class="cardtitle">{esc(p["h1"])}</span><span class="meta">{len(p["apps"])} {p.get("count_word", "apps")} · {T[lang]["updated"]} {human_date(p["updated"], lang)}</span></a></li>'
                for p in group_pages
            )
            sections += f'<h2 id="{sec_id}">{esc(LANGS[lang]["sections"][sec_id])} <span class="meta">({len(group_pages)})</span></h2><ul class="cards">{cards}</ul>'
        missing = [p["path"] for p in own if not any(p["group"] in g for g in HOME_GROUPS.values())]
        assert not missing, f"home: add these groups to HOME_GROUPS: {missing}"
        write(path, simple_page(lang, path, title, desc, '<div class="hero home">' + intro + f'</div>{sections}',
                                home_alts,
                                [{"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": f"{SITE}/", "inLanguage": hl(lang),
                                  "publisher": {"@type": "Organization", "name": NAME, "url": SITE, "parentOrganization": {"@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com"}}}]))

    about_en = """<h1>About Reviewland and how we check</h1>
<p>Reviewland is made by a small team that also builds iPhone apps.</p>
<h2>Our apps are one more option</h2>
<p>When one of our apps fits a question, it is included as one more option, placed where it fits rather than first, and the footer of every page says that we also make some of the apps listed. Competitors are linked to their normal App Store pages and shown with their real data, including where they are better than ours.</p>
<h2>What we check</h2>
<ul><li>Price and in-app purchases, version and release date, rating, languages, minimum iOS: from the App Store listing (US store unless the page says otherwise) on the date shown.</li>
<li>Privacy: the App Store privacy label as published by each developer.</li>
<li>Features: only what the developer states on its App Store listing or official site. We do not invent reviews or scores.</li></ul>
<h2>Updates</h2>
<p>We recheck each page about once a month. The "Updated" date only changes when the data has actually been checked again.</p>
"""
    about_es = """<h1>Quiénes somos y cómo comprobamos</h1>
<p>Reviewland lo hace un equipo pequeño que también hace apps de iPhone.</p>
<h2>Nuestras apps son una opción más</h2>
<p>Cuando una de nuestras apps encaja, aparece como una opción más, en el puesto que le corresponde y no primera, y el pie de cada página dice que también hacemos algunas de las apps de las listas. Las demás llevan enlace a su ficha normal del App Store y aparecen con sus datos reales, también donde son mejores que la nuestra.</p>
<h2>Qué comprobamos</h2>
<ul><li>Precio y compras dentro de la app, versión y fecha, valoración, idiomas e iOS mínimo: de la ficha del App Store (la de España en las páginas en español) en la fecha indicada.</li>
<li>Privacidad: la etiqueta de privacidad del App Store que publica cada desarrollador.</li>
<li>Funciones: solo lo que el desarrollador dice en su ficha o en su web oficial. No inventamos reseñas ni puntuaciones.</li></ul>
<h2>Actualizaciones</h2>
<p>Revisamos cada página más o menos una vez al mes. La fecha de "Actualizado" solo cambia cuando de verdad se han vuelto a comprobar los datos.</p>
"""
    about_alts = [(c, f"{SITE}/{about_path(c)}") for c in ACTIVE] + [("x-default", f"{SITE}/about/")]
    about_html = {"en": about_en, "es": about_es}
    for c in ACTIVE:
        body = about_html[c] if c in about_html else LANGS[c]["about_html"]
        write(about_path(c), simple_page(c, about_path(c), T[c]["about_title"], T[c]["about_desc"], body, about_alts))

    write_404()

    # sitemap
    urls = [(f"{SITE}/{prefix_of(c)}", max(p["updated"] for p in pages)) for c in ACTIVE]
    urls += [(f"{SITE}/{about_path(c)}", None) for c in ACTIVE]
    urls += [(page_url(p), p["updated"]) for p in pages]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, d in urls:
        d = lastmod(u, d)
        sm.append(f"<url><loc>{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    # llms.txt
    lines = ["# Reviewland", "",
             "> Rankings of iPhone apps by task, with prices, versions and privacy labels copied from the App Store on a stated date. When one of our own apps is ranked it is one more option, not first by default, and the footer of every page says we make some of the apps listed.", "",
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
