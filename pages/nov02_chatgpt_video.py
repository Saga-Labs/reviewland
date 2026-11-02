"""ChatGPT video generator plugins. EN. Read 2 Nov 2026 in the browser: public OpenAI listings and the ChatGPT directory listing for Dora.
Nothing was installed, generated or paid for. Visla: no listing found at the slugs tried."""

DAY = "2026-11-02"
OA = "https://openai.com/business/plugins/"
DORA = "https://chatgpt.com/plugins/plugin_asdk_app_6ac7e595853c8191baefac6a3a2b9c24"
GUIDE = '<a href="/best-chatgpt-apps-plugins/">our wider guide to ChatGPT plugins</a>'


def app(name, anchor, dev, url, makes, start, cost, best, facts, limits, ours=False):
    d = {"name": name, "anchor": anchor, "developer": dev, "url": url, "best_for": best, "facts": facts, "limits": limits,
         "row": [makes, start, cost, dev]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Runway", "runway", "Runway AI, Inc.", OA + "runway/", "Video, images, audio, multi-shot stories and ads", "Text, a photo or existing footage", "Runway account; credits; purchases on runway.com",
        "generating and also editing video from one chat.",
        ["The listing covers animating images, targeted edits to footage, new aspect ratios, multi-shot story videos and localising ads.", "It also lists music, sound effects, voiceover, and a check of remaining credits and plan.", "Results are stored in your Runway workspace and shown in a viewer in the chat."],
        "you need a Runway account, and the listing gives no prices."),
    app("OpenArt", "openart", "OpenArt Inc", OA + "openart/", "Images and video from a choice of models", "Text, with optional reference images", "Credits; the listing gives no prices",
        "picking a specific model, such as Seedance or Wan.",
        ["The listing names Seedance 2.5 and 2.0, Minimax H3, Gemini Omni Flash and Wan 3.0, among others.", "The result comes back into the chat, and past work stays in projects."],
        "no editing tools: the listing says none are required, and it does not describe any."),
    app("Higgsfield", "higgsfield", "Higgsfield AI, Inc.", OA + "higgsfield/", "Images, videos, product ads, voiceovers", "Text, a product photo or reference media", "Higgsfield account; the listing gives no prices",
        "short ads made from a product photo.",
        ["Marketing Studio presets turn product photos into promotional visuals and short video ads.", "Genjutsu transfers motion from a reference video, or replaces a subject in a clip.", "It can also create a recurring AI character to use as a reference."],
        "built mostly around marketing, and it needs a connected account."),
    app("invideo", "invideo", "Invideo Inc", OA + "invideo/", "Finished videos with script, visuals, voiceover and music", "Text prompt", "Not stated on the listing",
        "a longer video from one prompt.",
        ["Its tagline is \"Create videos of any length\", and its sample prompt asks for a 5-minute video.", "It handles the script, visuals, voiceovers and music from your text."],
        "the listing does not state a maximum length, a price or the account you need."),
    app("Dora AI Video", "dora", "Saga Labs", DORA, "Short videos and images", "A photo or a description", "Dora account; no free tier; prices on doravideo.com/pricing",
        "a short vertical clip from a photo.",
        ["The listing says videos arrive in about two minutes and images in about one.", "Vertical, horizontal or square, and the same character across a series of clips.", "Work is also saved to your gallery at doravideo.com and in the Dora iPhone app."],
        "short clips only, and no free tier, according to doravideo.com/llms.txt. It does not publish to social networks for you. We found no OpenAI business page for it, so we read its ChatGPT directory listing instead.", True),
    app("VEED Video Generator", "veed", "VEED", OA + "veed-video-generator/", "Videos with a character and a voice", "Your idea, then a chosen character and voice", "Not stated on the listing",
        "a presenter video with no camera.",
        ["You choose from a library of characters and voices.", "Sample prompts are a narrated product explainer and an onboarding video."],
        "the listing does not describe other video styles, and it gives no price or length limit."),
    app("HeyGen", "heygen", "HeyGen Technology Inc.", OA + "heygen/", "Talking-avatar videos and general AI clips", "A script, text, images or references", "Connected account; uses your HeyGen allowance",
        "talking avatars and translated videos from a script.",
        ["Clips can open in a player in the chat, on supported hosts.", "You can manage videos, avatars, voices, translations, templates and brand assets from the chat."],
        "features depend on your entitlements, and the listing says creating an avatar or voice requires the appropriate rights and consent."),
    app("Descript", "descript", "Descript", OA + "descript/", "Edits of existing video; can also create one from a prompt", "A recording, or a prompt", "Not stated on the listing",
        "editing a recording rather than generating new footage.",
        ["Transcription, filler word removal, Studio Sound, captions, B-roll and clips.", "Sample prompts include dubbing a video into Spanish, French and Japanese."],
        "it is a video editor first, so it is not the obvious choice for generating scenes."),
    app("Kling AI", "kling", "KLING AI", OA + "kling-ai/", "Images and video, single or multi-shot", "Text or images, in local Codex tasks", "Credits; the listing gives no prices",
        "technical users who already work in Codex.",
        ["Text to video, image to video, motion control and reusable character Elements, through the official Kling CLI."],
        "the listing requires a local Codex environment with Node.js 18+, Kling CLI 0.2.0+ and shell access, so it is not a simple option for most people."),
]

PAGES = [{
    "group": "chatgpt-video", "lang": "en", "store": "us", "path": "chatgpt-video-generator-plugins/", "ct": "rl-chatgpt-video",
    "category": "MultimediaApplication", "os": "ChatGPT", "link_label": "Plugin listing",
    "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "ChatGPT Video Generator Plugins Compared (Nov 2026)", "h1": "ChatGPT video generator plugins compared",
    "description": "Nine ChatGPT plugins that make or edit video, from their public listings on 2 November 2026: Runway, OpenArt, Higgsfield, invideo, Dora, VEED, HeyGen, Descript, Kling.",
    "llms": "Nine ChatGPT video plugins compared from their public listings: Runway, OpenArt, Higgsfield, invideo, Dora AI Video, VEED, HeyGen, Descript, Kling AI. None was tested.",
    "answer": [
        "We read the listings of nine plugins that make or edit video from ChatGPT. For general text to video, start with Runway or OpenArt. For a longer video from one prompt, invideo. For a presenter, HeyGen or VEED. To edit a recording, Descript. <strong>We did not install or run any of them, so this page says what each listing claims, not how good the videos are.</strong>",
        "Each one uses its own account, and the ones that state a cost charge through their own credits or allowance. OpenAI says availability depends on the plugin, your plan and your workspace settings, so check the listing from your own account. This page covers plugins only; for other kinds, see " + GUIDE + ".",
    ],
    "columns": ["Plugin", "Makes", "Starts from", "Account and cost, per listing", "Developer"],
    "table_note": "Read on 2 November 2026. \"Not stated\" means the listing does not say, not that it is free.",
    "apps": APPS,
    "who": ["<strong>General text to video, plus editing:</strong> Runway.", "<strong>Choosing the model:</strong> OpenArt.", "<strong>Product ads:</strong> Higgsfield.", "<strong>A longer video from one prompt:</strong> invideo.", "<strong>A short clip from a photo:</strong> Dora AI Video.", "<strong>A presenter with no camera:</strong> VEED or HeyGen.", "<strong>Editing a recording:</strong> Descript.", "<strong>Working in Codex:</strong> Kling AI."],
    "cases": ["A product clip from one photo.", "A narrated explainer from a written brief.", "Cleaning up and dubbing a recorded webinar."],
    "method": ["On 2 November 2026 we read each plugin's public listing on openai.com, and for Dora AI Video its ChatGPT directory listing plus doravideo.com/llms.txt. We did not install a plugin, generate a video or pay for anything, and we have no output or speed results of our own.",
               "The order follows how directly each listing describes making video from a prompt in the chat, ending with an editor and a plugin that needs a local setup. It is not a quality ranking. We looked for Visla and found no listing at the addresses we tried; that does not prove it is absent from the directory."],
    "faq": [
        ("How do I make a video in ChatGPT?", "Install a video plugin, connect its account, and start a chat asking it to use the plugin. OpenAI's listings describe these steps, and some connections need admin approval."),
        ("Are ChatGPT video plugins free?", "We cannot say that for any of them. Runway, OpenArt, Kling AI and HeyGen mention credits or an allowance, Dora AI Video has no free tier, and the others do not state a cost on their listing."),
        ("Which plugin makes the best videos?", "We do not know, because we did not test them. Try the same short prompt in two plugins, on the smallest paid option each offers."),
        ("Do I need a ChatGPT Business plan?", "The pages we read are on OpenAI's business site and mention ChatGPT Work and Codex. They say availability depends on the plugin, your plan and your workspace settings, without listing plans per plugin."),
    ],
    "sources": [(a["name"] + " listing", a["url"]) for a in APPS] + [("OpenAI: Plugins overview", OA), ("Dora llms.txt", "https://doravideo.com/llms.txt"), ("Dora on the App Store", "https://apps.apple.com/us/app/id6754180384")],
}]
