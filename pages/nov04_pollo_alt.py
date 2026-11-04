"""Pollo AI alternatives for iPhone. EN. Our app: Dora (id6754180384), 4th of 6.
Checked 2026-11-04 (JST): iTunes lookup and US App Store pages. Pollo AI (COCOSOFT, id6740024098): 4.3.1 (30 Oct 2026),
4.5 from 13,603 ratings, English only, label Data Used to Track You and Data Linked to You; weekly $5.99, annual $99.99,
Lite $15 and Pro $29 a month, credits $6.99 to $164.99; an all-in-one app for ads, UGC and product videos, with many
models. Dora models from doravideo.com/models (Seedance 2 Mini default, Kling 2.6, Gemini Omni, Grok).
Reserved in ios-playbook/references/temas-webs.md (7f3b413)."""

DAY = "2026-11-04"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
HIGGS = '<a href="/higgsfield-alternatives-iphone/">Higgsfield alternatives</a>'
TREND = '<a href="/best-ai-trend-video-apps-iphone/">trend video apps</a>'
SOUND = '<a href="/best-ai-video-generator-apps-with-sound-iphone/">AI video apps with sound</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, does, langs, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, does, langs, labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19332, "103.0.0", "1 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $14.99 a month or $143.99 a year, Pro $35, Max $95; credits $10 to $100", "Many models in one app (Seedance 2.5, Kling 3 Pro, Gen-4.5) and an agent", "1",
        "the closest to Pollo's many-models idea, with an agent that plans the shots.",
        ["Its listing names Seedance 2.5, Kling 3 Pro, Gen-4.5, Nano Banana Pro and Nano Banana 2.", "Runway Agent builds a whole video from a description; consistent characters across shots."],
        "English only, like Pollo, and no ad templates in the listing."),
    app("invideo: AI Video Editor", 6471394316, "invideo", "Invideo Inc", 4.55, 28037, "4.5.63", "27 Oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Plus $24 to $30, Max $72, Generative $143.99; Ads Pack $25 or $50", "Ads and whole videos with 200+ models, on a timeline editor", "1",
        "ads you can edit afterwards: an agent builds them and you fix every cut.",
        ["Its listing says Agent Two turns an idea, a script or your footage into a video, with 200+ models for image, video, voice and music.", "Sells an Ads Pack; edits on a timeline with your team."],
        "the most expensive plans here, and English only."),
    app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 32949, "3.9.32", "2 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $10, Pro $37, Premier $92 a month; one week from $1.19; credits $1.49 to $50", "Cinematic clips up to 4K, extendable to 3 minutes", "5",
        "the sharpest single clips, from the company that makes the Kling models Pollo also offers.",
        ["Its listing says text and images become video, up to 15 seconds in native 1080p or 4K, extendable to 3 minutes.", "Updated on 2 November 2026; about 33,000 ratings."],
        "one family of models only, and no ad maker."),
    app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16, "1.4.2", "26 Oct 2026", label(TRACK, NOTLINKED),
        "Pro $4.99 or $6.99 a week, $119.99 a year; coin packs $4.99 (300) to $224.99 (25,000)", "Short clips from a photo, an idea or a template; product and app ads per listing", "11",
        "a short clip from a photo or an idea, with the coin cost shown before you tap, in 11 languages.",
        ["Its listing says you pick a template or write an idea, add a photo, and get a video in about two minutes, including ads for a shop or an app.", "Dora's site lists Seedance 2 Mini as the default model, plus Kling 2.6, Gemini Omni and Grok.", "Failed generations give the coins back, per its listing."],
        "short clips only, no timeline editor or ad variations, and no free video."),
    app("PixVerse Lite", 6767802142, "pixverse", "AIVORA PTE. LTD.", 4.32, 2623, "0.8.1", "21 Sep 2026", label(TRACK, LINKED, NOTLINKED),
        "Elite $5.99 a week or $49.99 a year; credit packs $5 to $100", "PixVerse V6 plus other models; effects, talking avatars", "14",
        "the same weekly price as Pollo, with effects and talking avatars.",
        ["Its listing says it runs PixVerse V6 plus external models, with trending effects, lip-sync avatars and sound effects."],
        "a version below 1.0 and last updated in September."),
    app("Hula AI: Trend Video Generator", 6739294055, "hula", "Prequel Inc.", 4.59, 13554, "2.20.0", "28 Oct 2026", label(TRACK, NOTLINKED),
        "Premium $6.99 to $9.99 a week or $39.99 a year; packs from $2.99", "Trend effects and avatars on your photos", "7",
        "trend clips of yourself, paid by small packs.",
        ["Its listing says it makes avatars, animated videos for Reels, photo-to-video effects, remixes and stickers.", "Sells packs of 2 or 5 creations as well as Premium."],
        "built for effects on photos, not for ads or scenes from a script."),
]

PAGES = [{
    "group": "pollo-alternatives", "lang": "en", "store": "us", "path": "pollo-ai-alternatives-iphone/", "ct": "rl-pollo-alt",
    "category": "PhotoVideoApplication", "cover": None,
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Best Pollo AI Alternatives for iPhone (2026)", "h1": "Pollo AI alternatives for iPhone",
    "description": "Six iPhone apps instead of Pollo AI: many models, ads, cinematic clips or short clips from a photo. US prices, languages, privacy labels and ratings on 4 November 2026.",
    "llms": "Six alternatives to Pollo AI on iPhone: Runway, invideo, Kling AI, Dora, PixVerse Lite, Hula AI. Price, what each makes, languages, privacy label, version and rating on 4 November 2026.",
    "llms_note": "Dora, one of the six, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "Pollo AI puts many video models and an ad maker in one app, but it is English only, sells weekly, monthly and credit plans side by side, and its privacy label includes data used to track you. For many models in one place, <strong>Runway</strong>. For ads you can edit on a timeline, <strong>invideo</strong>. For the sharpest single clips, <strong>Kling AI</strong>. For a short clip from a photo or an idea in 11 languages, with the cost shown first, <strong>Dora</strong>.",
        "All six are free to download and sell plans, credits or coins; none of these listings promises free video.",
    ],
    "columns": ["App", "Price (US)", "What it makes, per listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases on each US App Store page on 4 November 2026; pages list only some. For comparison, Pollo AI 4.3.1 (30 October 2026): $5.99 a week or $99.99 a year, Lite $15 or Pro $29 a month, credits $6.99 to $164.99; English only; Data Used to Track You and Data Linked to You; rated 4.5 from 13,603 ratings.",
    "apps": APPS,
    "who": ["<strong>Many models in one app:</strong> Runway.", "<strong>Ads with a timeline editor:</strong> invideo.", "<strong>Cinematic clips:</strong> Kling AI.",
            "<strong>Short clips from a photo, in your language:</strong> Dora.", "<strong>Effects and talking avatars:</strong> PixVerse Lite.", "<strong>Trend clips of yourself:</strong> Hula AI."],
    "cases": ["A product ad for a small shop: invideo or Dora.", "Trying Seedance and Kling side by side: Runway.", "A trend clip for Reels: Hula AI or PixVerse Lite; see " + TREND + "."],
    "method": ["On 4 November 2026 we read each app's US App Store page and Apple's lookup data, and Dora's own site for its models. We generated nothing and did not compare quality.",
               "Order: first the apps closest to Pollo's all-in-one idea, then the clip and effect apps. See also " + HIGGS + " and " + SOUND + "."],
    "faq": [
        ("What is the best alternative to Pollo AI?", "For many models in one app, Runway. For ads you can edit, invideo. For the sharpest clips, Kling AI. For short clips from a photo with the cost shown first, Dora."),
        ("Is there a Pollo AI alternative in other languages?", "Pollo, Runway and invideo are English only on the App Store. Dora is in 11 languages, PixVerse Lite in 14, Hula AI in 7 and Kling AI in 5."),
        ("Which Pollo alternative has Seedance?", "Runway's listing names Seedance 2.5, and Dora's site lists Seedance 2 Mini as its default model."),
        ("Is there a free Pollo AI alternative?", "None of these listings promises free video. They sell plans, credits, coins or small packs."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("Pollo AI (App Store)", "https://apps.apple.com/us/app/id6740024098"), ("Dora: models and coins", "https://doravideo.com/models")],
}]
