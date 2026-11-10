"""Best text-to-video AI apps for iPhone. EN. Criterion: the App Store listing says it makes video from text alone (no photo needed).
Checked 2026-11-02 (JST night); ratings, versions and prices re-checked 2026-11-07: iTunes lookup and US App Store pages. No quality test, nothing generated.
Dora cost: Seedance 2 Mini, 31 coins for 8 s (doravideo.com/models and Dora list_models, 2 Nov); in 1.4.2 the picker still says "SeeDance 1.5 Pro".
Excluded: Google Gemini (listing does not mention video), CapCut and Filmora (editors first)."""

DAY = "2026-11-02"
CHECKED = "2026-11-07"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
HOWTO = '<a href="/how-to-turn-text-into-video-iphone/">how to turn text into a video on iPhone</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, does, length, best, facts, limits, ours=False):
    if anchor in ("kling", "runway", "invideo"):
        facts = list(facts) + ["Also works inside ChatGPT as an app, per its ChatGPT listing."]
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, does, length, labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 33339, "3.10.10", "4 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $10, Pro $37, Premier $92 a month; one week from $1.19; credits from $1.49 (100)",
        "Text or image to video", "Up to 15 s in 1080p or 4K, extendable to 3 minutes",
        "the longest and sharpest single clips from a text prompt.",
        ["Its listing says text and images become video, up to 15 seconds in native 1080p or 4K.", "Video Extension takes a clip up to 3 minutes.", "A community feed lets you copy the prompt behind other people's videos."],
        "the listing does not say how many credits a video costs, and it does not mention sound."),
    app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19662, "103.0.0", "1 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $14.99 a month or $143.99 a year, Pro $35, Max $95; credits $10 to $100",
        "Text, image or video to video; an agent that plans the shots", "Not stated",
        "choosing the model, or letting an agent turn a description into several shots.",
        ["The listing names Seedance 2.5, Kling 3 Pro and Gen-4.5 among its video models.", "Runway Agent plans the shots, generates them and assembles the video from a plain description.", "It says the first generation takes about two minutes."],
        "English only, and the listing gives no clip length or cost per video."),
    app("Grok", 6670324846, "grok", "X Corp.", 4.87, 1582846, "1.4.62", "6 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "SuperGrok Lite $10, SuperGrok $30, Plus $100, Heavy $300; extra credits $5 to $100",
        "Chat assistant with Grok Imagine: text or photo to video", "Short videos with sound, per its listing",
        "people who already pay for Grok and want a short clip with sound.",
        ["Its listing says Grok Imagine makes images from text, short videos with sound, and videos from photos.", "38 languages, the most of any app here."],
        "video is one feature of a chat app, and the listing gives no length or cost per video."),
    app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.12, 17, "1.4.2", "26 Oct 2026", label(TRACK, NOTLINKED),
        "Pro weekly $4.99 or $6.99, Pro yearly $119.99; coins $4.99 (300) to $224.99 (25,000)",
        "Text or photo to a short clip, several models", "8 s with sound for 31 coins on the default model",
        "one short clip from a description, with the coin cost shown before you tap.",
        ["Type what happens in the shot, choose 9:16 and generate; the coin cost shows before you tap. In version 1.4.2 the default model is still named \"SeeDance 1.5 Pro\" in the picker; Dora's site says those requests now run on Seedance 2 Mini, at 31 coins for 8 seconds with sound.",
         "At the 300-coin pack price that is about $0.52 per 8-second clip.",
         "Videos up to 1080p on some models, no watermark, about two minutes per video, per its listing.", "The same account also works in a browser at <a href=\"https://doravideo.com/?utm_source=reviewland&amp;utm_medium=guide&amp;utm_campaign=best-text-to-video-ai-apps-iphone\">doravideo.com</a>.", "Dora also works inside ChatGPT as an app: <a href=\"https://doravideo.com/chatgpt?utm_source=reviewland&amp;utm_campaign=chatgpt_cta\">how to connect it</a>."],
        "short clips only, and no free video.", True),
    app("invideo: AI Video Editor", 6471394316, "invideo", "Invideo Inc", 4.55, 28062, "4.5.63", "27 Oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Plus $24 to $30, Max $72, Generative $143.99; add-ons from $12",
        "Agent plus timeline editor; script to finished video", "Not stated; voice, sound and music included",
        "turning a long script into an edited video with voice and music.",
        ["Start from an idea, a script or your own footage, and Agent Two develops it into a video, per its listing.", "200+ models for image, video, voice, sound and music, and a timeline editor."],
        "English only, the most expensive plans here, and more editing than most people need for one clip."),
    app("Faceless - AI Video Generator", 6742199664, "faceless", "Yildirimhan Atcioglu", 4.55, 1174, "1.34", "4 Sep 2026", NOTLINKED,
        "Weekly $6.99, monthly $19.99, yearly $79.99; credits $3.99 to $24.99",
        "Text or script to a vertical reel", "Short reels with music, per its listing",
        "a faceless reel for TikTok or Shorts straight from a script.",
        ["Its listing says you paste text or a script and it picks visuals, music and transitions.", "33 languages, and the only app here whose privacy label has no tracking or linked data."],
        "a small developer, and the look comes from its own templates."),
    app("VideoGPT - AI Video Generator", 6451396274, "videogpt", "ElevenThirteen LLC", 4.76, 56005, "4.7", "8 Oct 2025", label(TRACK, NOTLINKED),
        "Unlimited $6.99 a week or $69.99 a year, Premium $19.99 a month, Pro $14.99 a week; credits $2.99 to $9.99",
        "Text or story to an animated video in styles such as Cinematic or Anime", "Not stated",
        "a story told in one visual style, such as anime.",
        ["Its listing says you type a story and pick a style, from Cinematic to Anime.", "Many ratings for its size: 4.8 from about 56,000."],
        "its last update was in October 2025, over a year before we checked, so newer video models may be missing."),
]

PAGES = [{
    "group": "text-video-list", "lang": "en", "store": "us", "path": "best-text-to-video-ai-apps-iphone/", "ct": "rl-text-video-list",
    "category": "PhotoVideoApplication", "published": DAY, "updated": CHECKED, "checked": CHECKED, "cover": None,
    "title": "Best Text-to-Video AI Apps for iPhone (2026)", "h1": "Best text-to-video AI apps for iPhone",
    "description": "Seven iPhone apps that make a video from text alone, no photo needed, compared by US price, clip length, sound, privacy label and rating on 7 November 2026.",
    "llms": "Seven iPhone apps that turn text alone into video: Kling AI, Runway, Grok, Dora, invideo, Faceless, VideoGPT. Price, clip length, sound, privacy label, rating. No quality test.",
    "answer": [
        "If you have a script or a description and no photo, these seven iPhone apps say they turn text alone into video. For one sharp clip, <strong>Kling AI</strong> (up to 15 seconds in 1080p or 4K). To pick the model or let an agent plan several shots, <strong>Runway</strong>. For a whole edited video with voice and music from a long script, <strong>invideo</strong>, or <strong>Faceless</strong> for a quick vertical reel. For one short clip with sound where the cost shows before you tap, <a href=\"#dora\"><strong>Dora</strong></a>: about $0.52 per 8-second clip, in the <a href=\"https://apps.apple.com/us/app/id6754180384?pt=118348020&amp;ct=rl-text-video-list\">iPhone app</a> or in the browser at <a href=\"https://doravideo.com/?utm_source=reviewland&amp;utm_medium=guide&amp;utm_campaign=best-text-to-video-ai-apps-iphone\">doravideo.com</a>.",
        "None of them makes video free in its listing, and most do not say what one video costs. Paste one shot at a time, choose 9:16 for a phone, and look at the cost before you generate. For the steps, see " + HOWTO + ".",
    ],
    "columns": ["App", "Price (US)", "From text", "Clip length and sound, per listing", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases on each US App Store page on 7 November 2026; pages list only some. All are free to download. \"Not stated\" means the listing does not say.",
    "apps": APPS,
    "who": ["<strong>One sharp clip:</strong> Kling AI.", "<strong>Choosing the model, or several shots from one description:</strong> Runway.", "<strong>You already pay for Grok:</strong> Grok Imagine.",
            "<strong>One short clip with the cost shown first:</strong> Dora.", "<strong>A long script with voice and music:</strong> invideo.", "<strong>A vertical reel from a script:</strong> Faceless.", "<strong>A story in one style, such as anime:</strong> VideoGPT."],
    "cases": ["A 30-second explainer from a written script: invideo or Faceless split it into scenes.", "One cinematic shot from a sentence: Kling AI, Runway or Dora.", "A clip with sound from a chat: Grok."],
    "method": ["On 2 November 2026 we read each app's US App Store page and Apple's lookup data, and re-checked ratings, versions and prices on 7 November. An app is on this list only if its listing says it makes video from text alone. What each one does, how long a clip is and whether there is sound come from the listing; we generated nothing and ran no quality test.",
               "Google Gemini is left out because its listing does not mention video. CapCut and Filmora are editors first, so they are not here. The list is ordered by how directly each listing describes text to video, not by quality. For apps compared on sound, see <a href=\"/best-ai-video-generator-apps-with-sound-iphone/\">AI video generator apps with sound</a>."],
    "faq": [
        ("Which app turns a script into a video on iPhone?", "For a long script with voice and music, invideo; for a short vertical reel, Faceless. For one scene at a time, Kling AI, Runway or Dora."),
        ("Can I make a video from text without a photo?", "Yes. All seven apps here say they accept text alone. Kling AI, Runway, Grok and Dora also accept a photo if you have one."),
        ("Is there a free text-to-video app?", "All are free to download, but none of these listings promises free videos. They sell subscriptions or credits."),
        ("How long can the video be?", "Kling AI lists up to 15 seconds per clip, extendable to 3 minutes. Dora's default model makes 8 seconds. The others do not state a length."),
        ("Which apps add sound?", "Grok says its short videos have sound, invideo generates voice, sound and music, Faceless adds music, and Dora's default model includes sound. Kling AI's listing does not mention sound."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [("Dora: models and coins", "https://doravideo.com/models")],
}]
