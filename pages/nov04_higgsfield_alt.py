"""Higgsfield alternatives for iPhone. EN. Our app: Dora (id6754180384), 4th of 6.
Checked 2026-11-04 (JST): a US App Store search for "higgsfield" returns no Higgsfield app, and higgsfield.ai links no
App Store app; its home page names Cinema Studio, Shorts ("hundreds of viral presets"), Ads Studio, Effects, AI Influencer,
Seedance 2.5, a ChatGPT plugin and an MCP for Claude. Its pricing page needs JavaScript, so no Higgsfield prices here.
Apps: iTunes lookup and US App Store pages the same day. Dora models from doravideo.com/models (Seedance 2 Mini default,
Kling 2.6, Gemini Omni, Grok; no Veo since 3 Nov). Reserved in ios-playbook/references/temas-webs.md (4e4b0a3)."""

DAY = "2026-11-04"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
TREND = '<a href="/best-ai-trend-video-apps-iphone/">trend video apps</a>'
MODELS = '<a href="/seedance-2-mini-vs-veo-3-1-vs-kling/">Seedance 2 Mini vs Kling vs Veo vs Grok Imagine</a>'
PLUGINS = '<a href="/chatgpt-video-generator-plugins/">ChatGPT video plugins</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, like, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, like, labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 32949, "3.9.32", "2 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $10, Pro $37, Premier $92 a month; one week from $1.19; credits $1.49 to $50", "Cinematic clips (like Cinema Studio)",
        "cinematic clips in 1080p or 4K, and scenes extended up to 3 minutes.",
        ["Its listing says text and images become video, up to 15 seconds in native 1080p or 4K, extendable to 3 minutes.", "A community feed to reuse other creators' ideas; updated on 2 November 2026."],
        "one family of models (Kling's own), 5 languages, and the listing does not say how many credits a clip costs."),
    app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19332, "103.0.0", "1 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $14.99 a month or $143.99 a year, Pro $35, Max $95; credits $10 to $100", "Many models in one app, and an agent",
        "the closest to Higgsfield's many-models idea: Seedance 2.5, Kling 3 Pro and Gen-4.5 in one app.",
        ["Its listing names Seedance 2.5, Kling 3 Pro, Gen-4.5, Nano Banana Pro and Nano Banana 2.", "Runway Agent builds a whole video from a description; consistent characters across shots."],
        "English only, and the plans start higher than the weekly apps here."),
    app("Pollo AI: AI Video & Image", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.47, 13603, "4.3.1", "30 Oct 2026", label(TRACK, LINKED),
        "$5.99 a week, $99.99 a year; Lite $15, Pro $29 a month; credits $6.99 to $164.99", "Ads and product videos (like Ads Studio)",
        "product ads and marketing videos from a photo, a script or a URL.",
        ["Its listing says ideas, scripts, photos, product images, URLs or reference videos become ads and social videos.", "An AI ad maker and design tools in the same app, for online sellers and small businesses."],
        "English only, and the listing does not say what each model costs."),
    app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16, "1.4.2", "26 Oct 2026", label(TRACK, NOTLINKED),
        "Pro $4.99 or $6.99 a week, $119.99 a year; coin packs $4.99 (300) to $224.99 (25,000)", "Templates and short clips from a photo or an idea",
        "a short clip from a photo or a written idea, with the coin cost shown before you tap.",
        ["Its listing says you pick a template or write an idea, add a photo, and get a video in about two minutes; it can copy a dance onto the person in your photo.", "Dora's site lists Seedance 2 Mini as the default model, plus Kling 2.6, Gemini Omni and Grok.", "Failed generations give the coins back, per its listing."],
        "short clips only, no ad studio or story editor, and no free video."),
    app("PixVerse Lite", 6767802142, "pixverse", "AIVORA PTE. LTD.", 4.32, 2623, "0.8.1", "21 Sep 2026", label(TRACK, LINKED, NOTLINKED),
        "Elite $5.99 a week or $49.99 a year; credit packs $5 to $100", "Trending effects and talking avatars (like Effects)",
        "trending effects, talking avatars and music videos in one toolbox.",
        ["Its listing says it runs PixVerse V6 plus external models, with trending effects, lip-sync avatars and sound effects."],
        "a version below 1.0, last updated in September, and no clip length in the listing."),
    app("Hula AI: Trend Video Generator", 6739294055, "hula", "Prequel Inc.", 4.59, 13554, "2.20.0", "28 Oct 2026", label(TRACK, NOTLINKED),
        "Premium $6.99 to $9.99 a week or $39.99 a year; packs from $2.99", "Viral presets for Reels (like Shorts)",
        "viral presets and photo effects for Reels, with packs instead of a plan.",
        ["Its listing says it makes avatars, animated videos for Reels, photo-to-video effects, remixes and stickers.", "Sells small packs (2 or 5 AI creations) as well as Premium."],
        "built for effects on your photos, not for writing a scene from scratch."),
]

PAGES = [{
    "group": "higgsfield-alternatives", "lang": "en", "store": "us", "path": "higgsfield-alternatives-iphone/", "ct": "rl-higgsfield-alt",
    "category": "PhotoVideoApplication", "cover": None,
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Higgsfield on iPhone? Best Higgsfield Alternatives (2026)", "h1": "Higgsfield alternatives for iPhone",
    "description": "Higgsfield has no App Store app. Six iPhone apps that do what it does: cinematic clips, many models, ads, effects and viral presets. Prices and ratings on 4 November 2026.",
    "llms": "Higgsfield has no iPhone app on the US App Store (4 November 2026); it works in a browser. Six iPhone alternatives by what you use Higgsfield for: Kling AI (cinematic clips), Runway (many models and an agent), Pollo AI (ads), Dora (short clips from a photo or idea), PixVerse Lite (effects), Hula AI (viral presets). Price, privacy label, version and rating.",
    "llms_note": "Dora, one of the six, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "Higgsfield has no app on the App Store: a search for it on the US store on 4 November 2026 found none, and higgsfield.ai links to no iPhone app. You can use it in Safari. If you want an app, pick by what you use Higgsfield for. For cinematic clips like Cinema Studio, <strong>Kling AI</strong>. For many models in one place, including Seedance 2.5, <strong>Runway</strong>. For product ads like Ads Studio, <strong>Pollo AI</strong>. For a short clip from a photo or an idea, with the cost shown first, <strong>Dora</strong>. For viral presets like Higgsfield Shorts, <strong>Hula AI</strong> or <strong>PixVerse Lite</strong>.",
        "All six are free to download and sell plans, credits or coins; none of these listings promises free video.",
    ],
    "columns": ["App", "Price (US)", "Closest to Higgsfield's", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases on each US App Store page on 4 November 2026; pages list only some. Higgsfield's own plans are on higgsfield.ai/pricing, which needs JavaScript; we did not copy them.",
    "apps": APPS,
    "who": ["<strong>Cinematic clips:</strong> Kling AI.", "<strong>Many models and an agent:</strong> Runway.", "<strong>Product ads:</strong> Pollo AI.",
            "<strong>A short clip from a photo or an idea:</strong> Dora.", "<strong>Effects and talking avatars:</strong> PixVerse Lite.", "<strong>Viral presets on your photos:</strong> Hula AI."],
    "cases": ["You used Higgsfield on a computer and want to keep going on the phone: Safari works; for an app, Runway has the most models in one place.",
              "A product video from a photo or a link: Pollo AI.",
              "A trend clip of yourself for Reels or TikTok: Hula AI or Dora; see " + TREND + "."],
    "method": ["On 4 November 2026 we searched the US App Store for Higgsfield, read higgsfield.ai, and read each app's US App Store page and Apple's lookup data. We generated nothing and did not compare quality.",
               "Order: by how close each app is to Higgsfield's main tools, from cinematic clips to presets. See also " + MODELS + " and " + PLUGINS + "."],
    "faq": [
        ("Does Higgsfield have an iPhone app?", "Not on the App Store: on 4 November 2026 a search on the US store found no Higgsfield app, and higgsfield.ai links to none. It works in Safari on iPhone."),
        ("What is the best Higgsfield alternative on iPhone?", "For many models in one app, Runway. For cinematic clips, Kling AI. For viral presets, Hula AI. For a short clip from a photo with the cost shown first, Dora."),
        ("Which app has Seedance on iPhone?", "Runway's listing names Seedance 2.5, Pollo AI's names Seedance, and Dora's site lists Seedance 2 Mini as its default model."),
        ("Is there a free Higgsfield alternative?", "All six are free to download, but none of these listings promises free video; they sell plans, credits or coins. Hula AI and Dora also sell small packs instead of a plan."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("Higgsfield", "https://higgsfield.ai/"), ("Dora: models and coins", "https://doravideo.com/models")],
}]
