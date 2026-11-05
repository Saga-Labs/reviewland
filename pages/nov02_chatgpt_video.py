"""ChatGPT video generator plugins. EN. Listings read 2 Nov 2026 in the browser: public OpenAI plugin pages and the ChatGPT directory listing for Dora.
Prices and free plans re-read on each vendor's own pricing page on 2 Nov 2026 (JST night). Kling: its web plans need sign-in, so the App Store
in-app price is used and labelled. Nothing was installed, generated or paid for. Visla: no listing found at the slugs tried.
Title starts with «Make videos in ChatGPT» since 5 Nov (#187); the h1 stays the same: it appears in the Related block of protected pages, which must not change until 11 Nov."""

DAY = "2026-11-02"
OA = "https://openai.com/business/plugins/"
DORA = "https://chatgpt.com/plugins/plugin_asdk_app_6ac7e595853c8191baefac6a3a2b9c24"
GUIDE = '<a href="/best-chatgpt-apps-plugins/">our wider guide to ChatGPT plugins</a>'


def app(name, anchor, dev, url, makes, free, cheapest, price_url, best, facts, limits, ours=False):
    d = {"name": name, "anchor": anchor, "developer": dev, "url": url, "best_for": best, "facts": facts, "limits": limits,
         "price_url": price_url, "row": [dev, makes, free, cheapest]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Runway", "runway", "Runway AI, Inc.", OA + "runway/", "Video, images, audio, multi-shot stories and ads",
        "Yes: 125 one-time credits", "Standard $15 a month, or $12 a month billed yearly", "https://runway.com/pricing",
        "generating and also editing video from one chat.",
        ["The listing covers animating images, targeted edits to footage, new aspect ratios, multi-shot story videos and localising ads.", "It also lists music, sound effects, voiceover, and a check of remaining credits and plan.", "Runway's pricing page: Free with 125 credits once; Standard 625 credits a month; Pro $35, Max $95 a month."],
        "you need a Runway account, and the free credits are a one-off, not monthly."),
    app("OpenArt", "openart", "OpenArt Inc", OA + "openart/", "Images and video from a choice of models",
        "No free plan on the pricing page", "Starter $14 a month, or $13 a month billed yearly", "https://openart.ai/pricing",
        "picking a specific model, such as Seedance or Wan.",
        ["The listing names Seedance 2.5 and 2.0, Minimax H3, Gemini Omni Flash and Wan 3.0, among others.", "OpenArt's pricing page: Starter 4,000 credits a month, Plus $34, Pro $56, Wonder $240 a month.", "The result comes back into the chat, and past work stays in projects."],
        "no editing tools: the listing says none are required, and it does not describe any."),
    app("Higgsfield", "higgsfield", "Higgsfield AI, Inc.", OA + "higgsfield/", "Images, videos, product ads, voiceovers",
        "Yes, with limited use", "Starter $19 a month (same monthly or yearly)", "https://higgsfield.ai/pricing",
        "short ads made from a product photo.",
        ["Marketing Studio presets turn product photos into promotional visuals and short video ads.", "Genjutsu transfers motion from a reference video, or replaces a subject in a clip.", "Higgsfield's pricing page: Starter 270 credits a month; Plus $47 and Ultra $99 a month billed yearly."],
        "built mostly around marketing, and it needs a connected account."),
    app("invideo", "invideo", "Invideo Inc", OA + "invideo/", "Finished videos with script, visuals, voiceover and music",
        "No free plan on the pricing page", "Starter $20 a month, or $10 a month billed yearly", "https://invideo.io/pricing",
        "a longer video from one prompt.",
        ["Its tagline is \"Create videos of any length\", and its sample prompt asks for a 5-minute video.", "invideo's pricing page: Starter 400 credits a month; Plus $60 a month ($30 yearly); Max $250 a month."],
        "the listing does not state a maximum length, and the cheapest plan has 400 credits a month."),
    app("Dora AI Video", "dora", "Saga Labs", DORA, "Short videos and images",
        "No free plan", "Pro $2.99 for the first week, then $4.99 a week; or $119.99 a year", "https://doravideo.com/pricing",
        "a short vertical clip from a photo.",
        ["The listing says videos arrive in about two minutes and images in about one.", "Vertical, horizontal or square, and the same character across a series of clips.", "Dora's pricing page (re-read 4 Nov 2026): Pro weekly or yearly, both with 150 coins a week, and top-up packs when you need more."],
        "short clips only, and no free plan. It does not publish to social networks for you. We found no OpenAI business page for it, so we read its ChatGPT directory listing instead.", True),
    app("VEED Video Generator", "veed", "VEED", OA + "veed-video-generator/", "Videos with a character and a voice",
        "Yes (\"Start for free\")", "Creator $20 a month, or $10 a month billed yearly", "https://www.veed.io/pricing",
        "a presenter video with no camera.",
        ["You choose from a library of characters and voices.", "VEED's pricing page: Creator 6,000 credits a month with no watermark; Pro $44 and Studio $70 a month ($21 and $35 yearly)."],
        "the listing does not describe other video styles, and the pricing page does not say what the free plan includes."),
    app("HeyGen", "heygen", "HeyGen Technology Inc.", OA + "heygen/", "Talking-avatar videos and general AI clips",
        "Yes: 3 videos a month, up to 1 minute, watermarked", "Creator $29 a month, or $24 a month billed yearly", "https://www.heygen.com/pricing",
        "talking avatars and translated videos from a script.",
        ["Clips can open in a player in the chat, on supported hosts.", "You can manage videos, avatars, voices, translations, templates and brand assets from the chat.", "HeyGen's pricing page: Pro $49 a month; Business $149 a month plus $20 per seat."],
        "features depend on your plan, and the listing says creating an avatar or voice requires the appropriate rights and consent."),
    app("Descript", "descript", "Descript", OA + "descript/", "Edits of existing video; can also create one from a prompt",
        "Yes: 60 media minutes a month, 720p, watermarked", "Hobbyist $24 a month, or $16 a month billed yearly", "https://www.descript.com/pricing",
        "editing a recording rather than generating new footage.",
        ["Transcription, filler word removal, Studio Sound, captions, B-roll and clips.", "Descript's pricing page: the free plan also has 100 AI credits once; Creator $35 a month ($24 yearly)."],
        "it is a video editor first, so it is not the obvious choice for generating scenes."),
    app("Kling AI", "kling", "KLING AI", OA + "kling-ai/", "Images and video, single or multi-shot",
        "Not shown without signing in", "Standard $10 a month (App Store price; web plans need sign-in)", "https://apps.apple.com/us/app/id6738049229",
        "technical users who already work in Codex.",
        ["Text to video, image to video, motion control and reusable character Elements, through the official Kling CLI.", "Kling's web plan page asks you to sign in, so the price here is from its App Store page: Standard $10, Pro $37, Premier $92 a month."],
        "the listing requires a local Codex environment with Node.js 18+, Kling CLI 0.2.0+ and shell access, so it is not a simple option for most people."),
]

PAGES = [{
    "group": "chatgpt-video", "lang": "en", "store": "us", "path": "chatgpt-video-generator-plugins/", "ct": "rl-chatgpt-video",
    "category": "MultimediaApplication", "os": "ChatGPT", "link_label": "Plugin listing", "kicker": "9 plugins · Last verified 2 Nov 2026",
    "checked_label": "Plugins and prices last verified",
    "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Make Videos in ChatGPT: 9 Video Generator Plugins Compared (Nov 2026)", "h1": "ChatGPT video generator plugins compared",
    "description": "How to make videos in ChatGPT: nine plugins that make or edit video, last verified 2 November 2026: who makes each, what it does, free plan and cheapest price from each vendor's site.",
    "llms": "Nine ChatGPT video plugins compared, last verified 2 Nov 2026: Runway, OpenArt, Higgsfield, invideo, Dora AI Video, VEED, HeyGen, Descript, Kling AI. Developer, what it makes, free plan, cheapest plan from each vendor's pricing page. None was tested.",
    "answer": [
        "<strong>Last verified 2 November 2026.</strong> We read the listings of nine plugins that make or edit video from ChatGPT, and each vendor's own pricing page. For general text to video, start with Runway or OpenArt. For a longer video from one prompt, invideo. For a presenter, HeyGen or VEED. To edit a recording, Descript. <strong>We did not install or run any of them, so this page says what each listing and pricing page claims, not how good the videos are.</strong>",
        "Free plans: Runway (125 credits once), Higgsfield, VEED, HeyGen (3 watermarked videos a month) and Descript. The cheapest paid plans start at $10 a month billed yearly (invideo, VEED). Each plugin uses its own account; OpenAI says availability depends on the plugin, your plan and your workspace settings. For other kinds of plugins, see " + GUIDE + ".",
    ],
    "columns": ["Plugin (as named in ChatGPT)", "Developer", "Makes", "Free plan (vendor site)", "Cheapest paid plan (vendor site)"],
    "table_note": "Listings and prices verified on 2 November 2026. Prices are in US dollars from each vendor's pricing page, except Kling (App Store, because its web plans need sign-in). \"No free plan on the pricing page\" means the page shows none, not that sign-up costs money.",
    "apps": APPS,
    "who": ["<strong>General text to video, plus editing:</strong> Runway.", "<strong>Choosing the model:</strong> OpenArt.", "<strong>Product ads:</strong> Higgsfield.", "<strong>A longer video from one prompt:</strong> invideo.", "<strong>A short clip from a photo:</strong> Dora AI Video.", "<strong>A presenter with no camera:</strong> VEED or HeyGen.", "<strong>Editing a recording:</strong> Descript.", "<strong>Working in Codex:</strong> Kling AI."],
    "cases": ["A product clip from one photo.", "A narrated explainer from a written brief.", "Cleaning up and dubbing a recorded webinar."],
    "method": ["On 2 November 2026 we read each plugin's public listing on openai.com, and for Dora AI Video its ChatGPT directory listing. The same day we read each vendor's pricing page for the free plan and the cheapest paid plan, in US dollars; for Kling, whose web plans need sign-in, we used its App Store page. We did not install a plugin, generate a video or pay for anything.",
               "We re-check this page every month against the listings and pricing pages and change the date at the top when we do. The order follows how directly each listing describes making video from a prompt in the chat, ending with an editor and a plugin that needs a local setup. It is not a quality ranking. We looked for Visla and found no listing at the addresses we tried."],
    "faq": [
        ("How do I make a video in ChatGPT?", "Install a video plugin, connect its account, and start a chat asking it to use the plugin. OpenAI's listings describe these steps, and some connections need admin approval."),
        ("Are ChatGPT video plugins free?", "Some have free plans on their own sites: Runway (125 credits once), Higgsfield, VEED, HeyGen (3 watermarked videos a month) and Descript. OpenArt, invideo and Dora AI Video show no free plan."),
        ("What is the cheapest ChatGPT video plugin?", "On 2 November 2026 the lowest paid plans were invideo Starter and VEED Creator at $10 a month billed yearly ($20 monthly), then Runway Standard at $12 a month billed yearly."),
        ("Which plugin makes the best videos?", "We do not know, because we did not test them. Try the same short prompt in two plugins, on the free plan or the smallest paid option each offers."),
        ("Do I need a ChatGPT Business plan?", "The pages we read are on OpenAI's business site and mention ChatGPT Work and Codex. They say availability depends on the plugin, your plan and your workspace settings, without listing plans per plugin."),
    ],
    "sources": [(a["name"] + " listing", a["url"]) for a in APPS]
               + [(a["name"] + " pricing", a["price_url"]) for a in APPS]
               + [("OpenAI: Plugins overview", OA), ("Dora llms.txt", "https://doravideo.com/llms.txt"), ("Dora on the App Store", "https://apps.apple.com/us/app/id6754180384")],
}]
