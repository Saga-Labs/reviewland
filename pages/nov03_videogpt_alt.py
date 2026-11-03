"""VideoGPT alternatives for iPhone. EN. Our app: Dora (id6754180384), 4th of 6.
Checked 2026-11-03 (JST): iTunes lookup and US App Store pages. VideoGPT (ElevenThirteen LLC, id6451396274):
4.7, last updated 8 Oct 2025, text to video stories in styles from Cinematic to Anime.
Criterion: updated in the last 30 days and the listing says it makes video from text. Not on reditor, aisagalab
or doravideo.com (checked 3 Nov); reserved in ios-playbook/references/temas-webs.md.
Dora's US page listed coin packs from $4.99 (300) that day. No Veo for Dora."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
TEXT = '<a href="/best-text-to-video-ai-apps-iphone/">text-to-video apps</a>'
SOUND = '<a href="/best-ai-video-generator-apps-with-sound-iphone/">AI video apps with sound</a>'
GROK = '<a href="/grok-imagine-alternatives-iphone/">Grok Imagine alternatives</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, makes, sound, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, makes, sound, labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("invideo: AI Video Editor", 6471394316, "invideo", "Invideo Inc", 4.55, 28034, "4.5.63", "27 Oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Plus $24 to $30, Max $72, Generative $143.99; add-on packs $12 to $60", "Whole videos from an idea or a script, edited on a timeline", "Voice, sound and music, per listing",
        "a story told from start to finish, with narration and music, closest to what VideoGPT promises.",
        ["Its listing says you can start from an idea, a script or your own footage, and an AI agent (Agent Two) builds and edits the video.", "Generates images, video, voice, sound and music with 200+ AI models, on a timeline editor."],
        "the plans cost more than a weekly clip app, and the app is English only."),
    app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 32921, "3.9.32", "2 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $10, Pro $37, Premier $92 a month; one week from $1.19; credits from $1.49", "Text or image to video, up to 15 s in 1080p or 4K, extendable to 3 min", "Kling 4.0, per Kling's site; not in the listing",
        "sharp clips from a prompt, and longer scenes by extending a clip.",
        ["Its listing says text and images become video, up to 15 seconds in native 1080p or 4K, and Video Extension takes a clip up to 3 minutes.", "Updated on 2 November 2026, the most recent here."],
        "the listing does not say how many credits a video costs, and it is in 5 languages."),
    app("Grok", 6670324846, "grok", "X Corp.", 4.87, 1572298, "1.4.61", "1 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "SuperGrok Lite $10, SuperGrok $30, Plus $100, Heavy $300; extra credits $5 to $100", "Short videos from text or a photo, inside a chat app", "Yes, \"short videos with sound\", per listing",
        "a quick clip with sound inside a chat app you may already pay for.",
        ["Its listing says Grok Imagine makes short videos with sound and turns photos into videos.", "The most ratings here, about 1.57 million, and 38 languages."],
        "video is one feature of a chat app, and the listing gives no clip length or cost per video."),
    app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16, "1.4.2", "26 Oct 2026", label(TRACK, NOTLINKED),
        "Pro weekly $4.99 or $6.99, Pro yearly $119.99; coin packs from $4.99 (300) to $224.99 (25,000)", "Text or photo to a short clip; templates; several models", "On the models that support it, per listing",
        "short clips from a written idea or a photo, with the coin cost shown before you tap.",
        ["Its listing says you write an idea or add a photo and get a video back in about two minutes.", "The coin cost shows before you generate, and failed generations give the coins back, per its listing.", "Dora's site lists Seedance 2 Mini as the default model: 8 seconds with sound for 31 coins; Kling 2.6 and Grok are also there."],
        "short clips only, no story editor, and a subscription with no free video."),
    app("Pollo AI: AI Video & Image", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.47, 13588, "4.3.1", "30 Oct 2026", label(TRACK, LINKED),
        "$5.99 a week, $99.99 a year; Lite $15 or Pro $29 a month; credits $6.99 to $164.99", "Video from ideas, scripts, photos or URLs; many models; ads", "Some models, \"native audio\"",
        "trying many video models, including Veo 3.1, from one app.",
        ["Its listing says ideas, scripts, photos, product images, URLs or reference videos become finished videos for ads, social media and stories.", "Names Seedance, Veo 3.1, Kling, Hailuo, Vidu and PixVerse among its models."],
        "English only, and the listing does not say what each model costs."),
    app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19308, "103.0.0", "1 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $14.99 a month or $143.99 a year, Pro $35, Max $95; credits $10 to $100", "Text, image or video to video; an agent that plans the shots", "Not stated",
        "describing a video in plain words and letting an agent plan several shots.",
        ["Its listing names Seedance 2.5, Kling 3 Pro and Gen-4.5 among its models, and says the first generation takes about two minutes.", "Runway Agent turns a description into several shots and assembles them."],
        "English only, no iPad version, and the listing gives no clip length or sound."),
]

PAGES = [{
    "group": "videogpt-alternatives", "lang": "en", "store": "us", "path": "videogpt-alternatives-iphone/", "ct": "rl-videogpt-alt",
    "category": "PhotoVideoApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best VideoGPT Alternatives for iPhone (2026)", "h1": "VideoGPT alternatives for iPhone",
    "description": "VideoGPT has not been updated since October 2025. Six iPhone AI video apps updated this month, compared by US price, sound, privacy label and rating on 3 November 2026.",
    "llms": "Six VideoGPT alternatives for iPhone, all updated in October or November 2026: invideo, Kling AI, Grok, Dora, Pollo AI, Runway. What each makes from text, sound, price, privacy label, rating. VideoGPT's last update: 8 October 2025.",
    "answer": [
        "VideoGPT (by ElevenThirteen) turns a written story into a video in styles from Cinematic to Anime, but its last App Store update was version 4.7 on 8 October 2025. All six apps here were updated in the last month. For a whole story with narration and music, <strong>invideo</strong>. For sharp clips up to 4K and scenes extended to 3 minutes, <strong>Kling AI</strong>. For a quick clip with sound inside a chat app, <strong>Grok</strong>. For short clips from a written idea or a photo, with the cost shown first, <strong>Dora</strong>.",
        "All six are free to download and sell subscriptions or credits; none of these listings promises free video. VideoGPT itself lists Unlimited at $6.99 a week or $69.99 a year and Pro at $14.99 a week.",
    ],
    "columns": ["App", "Price (US)", "What it makes, per listing", "Sound", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases on each US App Store page on 3 November 2026; pages list only some. For comparison, VideoGPT 4.7 (8 October 2025): Unlimited $6.99 a week or $69.99 a year (promo $34.99), Premium $19.99 a month, Pro $14.99 a week or $39.99 a month, credits $2.99 to $9.99; privacy label Data Used to Track You and Data Not Linked to You; rated 4.8 from 55,766 ratings.",
    "apps": APPS,
    "who": ["<strong>A whole story with narration and music:</strong> invideo.", "<strong>Sharp clips and longer scenes:</strong> Kling AI.", "<strong>A clip with sound from a chat:</strong> Grok.",
            "<strong>Short clips from an idea or a photo, cost shown first:</strong> Dora.", "<strong>Many models in one app:</strong> Pollo AI.", "<strong>Several shots planned for you:</strong> Runway."],
    "cases": ["A bedtime story or a short tale as a video with a narrator: invideo.", "An anime or cinematic scene from one prompt: Kling AI, Dora or Pollo AI; name the style in the prompt.", "A product clip for social media: Pollo AI or Dora."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data, and for Kling and Dora the company's own site. An app is here only if its listing says it makes video from text and it was updated in the last 30 days. We generated nothing and did not compare quality.",
               "Order: first the apps that make longer or more finished videos, then the clip apps. See also " + TEXT + ", " + SOUND + " and " + GROK + "."],
    "faq": [
        ("Is VideoGPT still updated?", "Its App Store page shows version 4.7, released on 8 October 2025, and nothing newer on 3 November 2026. The app is still on sale."),
        ("What is the best alternative to VideoGPT?", "For whole story videos with narration, invideo. For the sharpest clips, Kling AI. For short clips with the cost shown before you tap, Dora."),
        ("Is there a free alternative to VideoGPT?", "None of these listings promises free video. They sell subscriptions, weekly plans or credits; Grok's video comes with its SuperGrok plans."),
        ("Which alternatives make video with sound?", "Grok and invideo say so in their listings, Dora on the models that support it, and Pollo AI on some models. Kling's site says Kling 4.0 makes sound; its listing does not."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("VideoGPT (App Store)", "https://apps.apple.com/us/app/id6451396274"), ("Kling AI", "https://klingai.com/global/"), ("Dora: models and coins", "https://doravideo.com/models")],
}]
