"""Best AI video generator apps for iPad. EN. Criterion: universal app with iPad screenshots on its US App Store page (built for iPad).
Our app: Dora (id6754180384), 4th of 7. Checked 2026-11-03 (JST): iTunes lookup (features "iosUniversal", ipadScreenshotUrls, minimumOsVersion)
and US App Store pages. Not built for iPad on 3 Nov: Runway (1665024375), VideoGPT, Flashloop, VideoMax, "AI Video" by HUBX (0 iPad screenshots, not universal)."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
SOUND = '<a href="/best-ai-video-generator-apps-with-sound-iphone/">AI video apps with sound</a>'
TEXT = '<a href="/best-text-to-video-ai-apps-iphone/">text-to-video apps</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, makes, ipad, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, makes, ipad, labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 32838, "3.9.32", "2 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $10, Pro $37, Premier $92 a month; one week from $1.19; credits from $1.49",
        "Text or image to video, up to 15 s in 1080p or 4K", "Yes, 10 iPad screenshots; iPadOS 14 or later",
        "sharp clips on a big screen, even on an older iPad.",
        ["Its listing says text and images become video, up to 15 seconds in native 1080p or 4K, and Video Extension takes a clip up to 3 minutes.", "Runs on the oldest iPadOS of any app here (14), and shows the most iPad screenshots."],
        "the listing does not say how many credits a video costs, and it is in 5 languages."),
    app("Google Gemini", 6477489729, "gemini", "Google LLC", 4.73, 2394514, "1.2026.4262206", "29 Oct 2026", LINKED,
        "Google AI Plus $4.99, Pro $19.99, Ultra $199.99 a month", "Gemini Omni: video from text or up to 5 photos, with sound", "Yes, 8 iPad screenshots; iPadOS 18.2 or later",
        "people with a Google AI plan who want video, chat and editing in one iPad app.",
        ["Its listing says Gemini Omni makes video for Google AI Plus, Pro and Ultra users; Google's site lists 10-second clips with native audio.", "70 languages, and the only privacy label here without Data Used to Track You."],
        "video needs a paid Google AI plan, and Google's site says it is for users 18 and over."),
    app("Grok", 6670324846, "grok", "X Corp.", 4.87, 1570441, "1.4.61", "1 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "SuperGrok Lite $10, SuperGrok $30, Plus $100, Heavy $300; credits $5 to $100", "Grok Imagine: short videos with sound, from text or a photo", "Yes, 5 iPad screenshots; iPadOS 17 or later",
        "a quick clip with sound inside a chat app.",
        ["Its listing says Grok Imagine creates short videos with sound and turns photos into videos.", "38 languages."],
        "video is one feature of a chat app, and the listing gives no length or cost per video."),
    app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16, "1.4.2", "26 Oct 2026", label(TRACK, NOTLINKED),
        "Pro weekly $4.99 or $6.99, Pro yearly $119.99; coins $3.99 (300) to $224.99 (25,000)", "Text or photo to a short clip, several models", "Yes, 6 iPad screenshots; iPadOS 18.6 or later",
        "short clips with the coin cost shown first, and the same account on the web.",
        ["The coin cost shows before you generate, and failed generations give the coins back, per its listing.", "Dora's site says the default model, Seedance 2 Mini, makes 8 seconds with sound for 31 coins, about $0.41 at the 300-coin pack price.",
         "The same account and coins work on doravideo.com and in Claude and ChatGPT, its listing says."],
        "it needs iPadOS 18.6, the newest requirement here, it is a subscription, and there is no free video.", True),
    app("invideo: AI Video Editor", 6471394316, "invideo", "Invideo Inc", 4.55, 28028, "4.5.63", "27 Oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Plus $24 to $30, Max $72, Generative $143.99; add-ons from $12", "Script to a finished, edited video with voice and music", "Yes, 6 iPad screenshots; iPadOS 16 or later",
        "editing a whole video on the iPad's larger screen, with a timeline.",
        ["Its listing says an agent develops an idea or script into a video, and a timeline editor lets you refine layers, transitions, captions and sound.", "200+ models for image, video, voice, sound and music."],
        "English only, and the most expensive plans here."),
    app("Pollo AI: AI Video & Image", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.47, 13581, "4.3.1", "30 Oct 2026", label(TRACK, LINKED),
        "$5.99 a week, $99.99 a year; Lite $15 or Pro $29 a month; credits $6.99 to $164.99", "Many video models in one app, plus effects", "Yes, 9 iPad screenshots; iPadOS 15.6 or later",
        "trying many video models from one iPad app.",
        ["Its listing names models such as Seedance, Veo 3.1, Kling, Hailuo, Vidu and PixVerse.", "Text, photo, reference and video to video, plus effects and AI avatars."],
        "English only, and the listing does not say what each model costs."),
    app("Faceless - AI Video Generator", 6742199664, "faceless", "Yildirimhan Atcioglu", 4.55, 1169, "1.34", "4 Sep 2026", NOTLINKED,
        "Weekly $6.99, monthly $19.99, yearly $79.99; credits $3.99 to $24.99", "Text or script to a vertical reel with music", "Yes, 8 iPad screenshots; iPadOS 16.4 or later",
        "a faceless reel from a script, typed on an iPad keyboard.",
        ["Its listing says you paste text or a script and it picks visuals, music and transitions.", "33 languages, and the only privacy label here with no tracking or linked data."],
        "a small developer, and its last update was on 4 September 2026."),
]

PAGES = [{
    "group": "video-ipad", "lang": "en", "store": "us", "path": "best-ai-video-generator-apps-ipad/", "ct": "rl-video-ipad",
    "category": "PhotoVideoApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best AI Video Generator Apps for iPad (2026)", "h1": "Best AI video generator apps for iPad",
    "description": "Seven AI video apps built for iPad, not iPhone apps in a small window, compared by US price, iPadOS version, privacy label and rating on 3 November 2026.",
    "llms": "Seven AI video generator apps built for iPad (universal, with iPad screenshots): Kling AI, Google Gemini, Grok, Dora, invideo, Pollo AI, Faceless. Runway and VideoGPT have no iPad version. Price, iPadOS, privacy label, rating.",
    "answer": [
        "Some popular AI video apps, such as Runway and VideoGPT, have no iPad version on the US App Store: on an iPad they open as an iPhone app in a small window. These seven are built for iPad. For sharp clips, even on an older iPad, <strong>Kling AI</strong>. With a Google AI plan, <strong>Gemini</strong>. For a clip with sound in a chat app, <strong>Grok</strong>. To edit a whole video on a timeline, <strong>invideo</strong>.",
        "All are free to download and sell subscriptions or credits. Check the iPadOS version first: they range from iPadOS 14 to 18.6.",
    ],
    "columns": ["App", "Price (US)", "What it makes, per listing", "Built for iPad", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "\"Built for iPad\" means the US App Store lists the app as universal and shows iPad screenshots, on 3 November 2026; the version is the minimum the listing requires. Prices are in-app purchases on each page that day; pages list only some.",
    "apps": APPS,
    "who": ["<strong>Older iPad:</strong> Kling AI (iPadOS 14).", "<strong>You pay for Google AI:</strong> Gemini.", "<strong>A clip from a chat:</strong> Grok.",
            "<strong>Cost shown first, same account on the web:</strong> Dora.", "<strong>Editing on a timeline:</strong> invideo.", "<strong>Many models:</strong> Pollo AI.", "<strong>Reels from a script:</strong> Faceless."],
    "cases": ["A class or work presentation clip: Kling AI or Gemini, in 16:9 for the iPad screen.", "A family video from a photo: Dora or Grok.", "A YouTube video from a script, edited: invideo."],
    "method": ["On 3 November 2026 we read Apple's lookup data and each app's US App Store page. An app is here only if Apple lists it as universal and its page shows iPad screenshots; Runway, VideoGPT, Flashloop and VideoMax do not, so they are left out. We did not install the apps on an iPad or compare video quality.",
               "Order: first the apps whose listing says most plainly what video they make and at what quality, then the editor and the template apps. See also " + SOUND + " and " + TEXT + "."],
    "faq": [
        ("Does Runway work on iPad?", "On 3 November 2026 Runway's US App Store page shows no iPad version, so on an iPad it opens as an iPhone app in a smaller window."),
        ("Which AI video app works on an older iPad?", "Kling AI needs iPadOS 14 or later, the oldest here; Pollo AI needs 15.6. Dora needs 18.6 and Gemini 18.2."),
        ("Is there a free AI video app for iPad?", "All seven are free to download, but none of these listings promises free videos; they sell subscriptions or credits."),
        ("Can I use the same account on iPhone and iPad?", "These are universal apps, so one purchase covers both. Dora's listing also says the same account works on the web."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("Runway (App Store)", "https://apps.apple.com/us/app/id1665024375"), ("Gemini Omni (Google)", "https://gemini.google/overview/video-generation/"), ("Dora: models and coins", "https://doravideo.com/models")],
}]
