"""Grok Imagine alternatives for iPhone. EN. Our app: Dora (id6754180384), 4th of 6.
Checked 2026-11-03 (JST): iTunes lookup and US App Store pages; Grok Imagine API specs from docs.x.ai; Gemini Omni from gemini.google; Kling 4.0 from klingai.com.
Dora also lists Grok among its models (doravideo.com/models: 480p, 6 s, 10 credits). No Veo for Dora."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
MODELS = '<a href="/seedance-2-mini-vs-veo-3-1-vs-kling/">Seedance 2 Mini vs Kling vs Veo vs Grok Imagine</a>'
SOUND = '<a href="/best-ai-video-generator-apps-with-sound-iphone/">AI video apps with sound</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, makes, sound, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, makes, sound, labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 32838, "3.9.32", "2 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $10, Pro $37, Premier $92 a month; one week from $1.19; credits from $1.49", "Text or image to video, up to 15 s in 1080p or 4K", "Kling 4.0, per Kling's site; not in the listing",
        "4K clips, and extending a clip up to 3 minutes.",
        ["Its listing says text and images become video, up to 15 seconds in native 1080p or 4K, and Video Extension takes a clip up to 3 minutes.", "Kling's website presents Kling 4.0 as making picture and sound together."],
        "the listing does not say how many credits a video costs or mention sound."),
    app("Google Gemini", 6477489729, "gemini", "Google LLC", 4.73, 2394514, "1.2026.4262206", "29 Oct 2026", LINKED,
        "Google AI Plus $4.99, Pro $19.99, Ultra $199.99 a month", "Gemini Omni: video from text or up to 5 photos, edited by chat", "Native audio, per Google's site",
        "a chat app like Grok, with video you edit by asking, if you pay for Google AI.",
        ["Its listing says Gemini Omni makes video for Google AI Plus, Pro and Ultra users; Google's site lists 10-second clips with native audio and editing in the chat.", "The only privacy label here without Data Used to Track You."],
        "video needs a paid plan, and Google's site says it is for users 18 and over."),
    app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19176, "103.0.0", "1 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $14.99 a month or $143.99 a year, Pro $35, Max $95; credits $10 to $100", "Text, image or video to video; an agent that plans the shots", "Not stated",
        "choosing among several companies' video models and planning multi-shot videos.",
        ["Its listing names Seedance 2.5, Kling 3 Pro and Gen-4.5 among its video models.", "Runway Agent turns a plain description into several shots and assembles them."],
        "English only, no iPad version, and the listing gives no clip length or sound."),
    app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16, "1.4.2", "26 Oct 2026", label(TRACK, NOTLINKED),
        "Pro weekly $4.99 or $6.99, Pro yearly $119.99; coins $4.99 (300) to $224.99 (25,000)", "Text or photo to a short clip; templates; several models", "On the models that support it, per listing",
        "keeping Grok as one option and trying other models from the same coins.",
        ["Dora's models page lists Grok (480p, 6 seconds, 10 credits) next to Seedance 2 Mini (8 seconds with sound for 31 credits) and Kling 2.6.", "The coin cost shows before you generate and failed generations give the coins back, per its listing.", "Templates put you in another era or place, and Motion Control copies a dance onto your photo."],
        "a subscription with no free video, and short clips only.", True),
    app("Pollo AI: AI Video & Image", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.47, 13581, "4.3.1", "30 Oct 2026", label(TRACK, LINKED),
        "$5.99 a week, $99.99 a year; Lite $15 or Pro $29 a month; credits $6.99 to $164.99", "Many video models in one app, plus effects and avatars", "Some models, \"native audio\"",
        "trying many models, including Veo 3.1, in one app.",
        ["Its listing names Seedance, Veo 3.1, Kling, Hailuo, Vidu and PixVerse, and multi-scene videos with audio."],
        "English only, and the listing does not say what each model costs."),
    app("Hula AI: Trend Video Generator", 6739294055, "hula", "Prequel Inc.", 4.59, 13551, "2.20.0", "28 Oct 2026", label(TRACK, NOTLINKED),
        "Premium $6.99 or $9.99 a week, $39.99 a year; packs $2.99 to $4.99", "Selfie to animated video, era and anime styles", "Not stated",
        "fun selfie clips without a chat app.",
        ["Turns selfies into animated videos and shows you in other eras or anime styles, per its listing.", "Makes sticker packs from the same selfie."],
        "the listing does not say how long a video is, and it is not for clips from text."),
]

PAGES = [{
    "group": "grok-imagine-alternatives", "lang": "en", "store": "us", "path": "grok-imagine-alternatives-iphone/", "ct": "rl-grok-imagine-alt",
    "category": "PhotoVideoApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best Grok Imagine Alternatives for iPhone (2026)", "h1": "Grok Imagine alternatives for iPhone",
    "description": "Six iPhone apps to make AI video instead of, or as well as, Grok Imagine, compared by US price, clip length, sound, privacy label and rating on 3 November 2026.",
    "llms": "Six Grok Imagine alternatives for iPhone: Kling AI, Google Gemini, Runway, Dora, Pollo AI, Hula AI. What each makes, sound, price, privacy label, rating. Grok Imagine API specs from xAI.",
    "answer": [
        "Grok Imagine lives inside the Grok app (SuperGrok from $10 a month) and, on xAI's API, makes up to 15 seconds at up to 1080p with lip-synced speech. For 4K, or a clip extended up to 3 minutes, <strong>Kling AI</strong>. For video you edit by chatting, if you pay for Google AI, <strong>Gemini</strong>. To keep Grok as one option and add Seedance 2 Mini and Kling from the same coins, <strong>Dora</strong>.",
        "All six are free to download and sell subscriptions or credits; none of these listings promises free video. Sound depends on the model, so check it before you generate.",
    ],
    "columns": ["App", "Price (US)", "What it makes, per listing", "Sound", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases on each US App Store page on 3 November 2026; pages list only some. For comparison, Grok 1.4.61: SuperGrok Lite $10, SuperGrok $30, Plus $100, Heavy $300; its listing says Grok Imagine makes short videos with sound.",
    "apps": APPS,
    "who": ["<strong>4K and longer edits:</strong> Kling AI.", "<strong>Editing video by chat:</strong> Gemini.", "<strong>Several models and multi-shot videos:</strong> Runway.",
            "<strong>Grok plus other models from one balance:</strong> Dora.", "<strong>The most models:</strong> Pollo AI.", "<strong>Selfie fun:</strong> Hula AI."],
    "cases": ["A 4K product shot: Kling AI.", "A talking clip with sound: Gemini, or Seedance 2 Mini in Dora.", "The same prompt on several models: Pollo AI, Runway or Dora."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data, xAI's API documentation for Grok Imagine, and Google's and Kling's sites for sound. We generated nothing and did not compare quality.",
               "Order: first the apps whose listing says most plainly what video they make, then the many-model apps and the selfie app. For the models side by side, see " + MODELS + "; for sound, " + SOUND + "."],
    "faq": [
        ("What is the best alternative to Grok Imagine?", "For quality settings, Kling AI (up to 4K). Inside a chat app, Gemini with a Google AI plan. To keep Grok and add other models, Dora or Pollo AI."),
        ("Is Grok Imagine free?", "The Grok app sells SuperGrok plans from $10 and extra credits; its listing does not say how many free videos you get. On xAI's API, Grok Imagine Video 1.5 costs $0.08 to $0.25 per second, and the Lite version from $0.02."),
        ("Which alternatives make video with sound?", "Gemini (Gemini Omni), Kling 4.0 per Kling's site, Dora on the models that support it, and some models in Pollo AI."),
        ("Can I still use Grok's video model in another app?", "Yes. Dora's models page lists Grok at 480p and 6 seconds for 10 credits."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("Grok (App Store)", "https://apps.apple.com/us/app/id6670324846"), ("xAI: video generation guide", "https://docs.x.ai/docs/guides/video-generation"), ("xAI: pricing", "https://docs.x.ai/docs/pricing"),
        ("Gemini Omni (Google)", "https://gemini.google/overview/video-generation/"), ("Kling AI", "https://klingai.com/global/"), ("Dora: models and coins", "https://doravideo.com/models")],
}]
