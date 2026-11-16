"""Best AI dance video apps for iPhone. EN. No app of ours is listed (none of ours is on sale in this category yet).

Checked 2026-11-16 (JST): iTunes lookup (US) for the five apps (name, seller, price, rating, version, date, minimum iOS
and description) and the iTunes search (US) for "ai dance video", "dance video ai" and "photo dance ai".
Features, limits and prices come only from each listing's own text. In-app purchase prices were not readable without a
browser, so the page gives none and says "subscription inside" only where the listing says it.
"""

DAY = "2026-11-16"
AS_OF = "Nov 16, 2026"


def src(cc="us"):
    return [
        ("Ai Dance Generator: Make Video (App Store)", f"https://apps.apple.com/{cc}/app/id6752712092"),
        ("Dance AI - Video Generator (App Store)", f"https://apps.apple.com/{cc}/app/id6758041184"),
        ("Viggle AI: Meme & Dance Maker (App Store)", f"https://apps.apple.com/{cc}/app/id6503272013"),
        ("Photo Dance: AI Baby Dance (App Store)", f"https://apps.apple.com/{cc}/app/id6474650062"),
        ("DanceHit: AI Dance Generator (App Store)", f"https://apps.apple.com/{cc}/app/id6761751034"),
    ]


EN = {
    "group": "dance-video", "lang": "en", "store": "us", "cover": None,
    "path": "best-ai-dance-video-apps-iphone/",
    "ct": "rl-ai-dance-video-apps",
    "category": "PhotoVideo",
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Best AI Dance Video Apps for iPhone (2026)",
    "h1": "Best AI dance video apps for iPhone (2026)",
    "description": "Five AI dance video apps for iPhone compared: how each turns a photo into a dance, what it costs to use fully, its rating and what its listing says about privacy. Checked on the App Store on 16 November 2026.",
    "llms": "Compares five AI dance video apps for iPhone (Ai Dance Generator, Dance AI, Viggle AI, Photo Dance and DanceHit) by how they turn one photo into a dance video, what the listing says about subscriptions and credits, rating, version and what each says about keeping photos. Checked on the App Store on Nov 16, 2026.",
    "answer": [
        "The best AI dance video app for one photo depends on how you want to pay: Ai Dance Generator (4.8) sells credit packs that never expire as well as a membership, and Dance AI (4.6) works from a style library with weekly or yearly plans. Viggle AI (4.8) is the one to open if you want memes and scenes beyond dancing. We checked five apps on the App Store on Nov 16, 2026.",
        "All five are free to download. Four of them list a subscription or credit packs for full use, while Viggle AI says it is free to start with five generations a day. Check the price on Apple's payment sheet before you buy, and read the privacy section of any app before you upload a photo of someone else.",
    ],
    "columns": ["App", "Works with", "Price (US)", "Rating (US)", "Best for"],
    "table_note": "Price and rating are from the US App Store as of Nov 16, 2026. \"Free\" means free to download. Works with and the price notes come from each app's own description. Ratings are rounded to one decimal.",
    "apps": [
        {
            "name": "Ai Dance Generator: Make Video", "id": 6752712092, "anchor": "ai-dance-generator",
            "developer": "Eray YAVUZ",
            "row": ["One photo, dance styles and choreography", "Free; Pro membership and credit packs inside", "4.8", "Short clips from one photo"],
            "best_for": "people who want credits that do not expire, or a weekly membership, for short clips from one photo.",
            "facts": [
                "Pick a dance style, upload one photo and the app generates the video; the listing says no green screen or special equipment is needed.",
                "The listing describes a Pro membership with up to four AI dance videos a week, and credit packs that never expire and need no subscription.",
                "It says the photo is sent only to its AI generation partner and is not stored on its servers.",
                "Version 2.0.6 (15 Sep 2026), iOS 16.6 or later.",
            ],
            "limits": "the listing gives a weekly limit on the membership, so heavy use means buying credit packs.",
        },
        {
            "name": "Dance AI - Video Generator", "id": 6758041184, "anchor": "dance-ai",
            "developer": "Deepix AI Yazilim Teknolojileri",
            "row": ["Photos of people, kids and pets; a growing library of dance styles", "Free; subscription for all styles", "4.6", "Realistic motion from one photo"],
            "best_for": "a simple one-photo dance video with a style library, for TikTok, Reels or Shorts.",
            "facts": [
                "Upload a photo, choose a dance style and get a video in seconds, per the listing.",
                "The listing says photos are used only to make your video and are not stored permanently afterwards.",
                "Full access to all styles, effects and tools needs a subscription, with weekly and yearly plans.",
                "Version 1.1.1 (19 Oct 2026), iOS 15.1 or later.",
            ],
            "limits": "unused trial time is lost when you subscribe, according to the listing's subscription terms.",
        },
        {
            "name": "Viggle AI: Meme & Dance Maker", "id": 6503272013, "anchor": "viggle",
            "developer": "WarpEngine Canada",
            "row": ["Any photo put into a video clip; memes, scenes and dance trends", "Free to start; 5 free generations a day", "4.8", "Memes and scenes, not only dance"],
            "best_for": "memes and viral clips where your photo sits inside a famous scene or a trend.",
            "facts": [
                "Motion-controlled video: the listing says you can put your photo into any video clip, from a dance to a sports scene.",
                "The listing says it is free to start and gives up to five free video generations per day.",
                "It is built around memes and trends, so the library and the templates are wider than dance alone.",
                "Version 2.1.1 (2 Nov 2026), iOS 16.0 or later.",
            ],
            "limits": "the listing does not say what the paid plan adds, so check the price before you rely on it for daily use.",
        },
        {
            "name": "Photo Dance: AI Baby Dance", "id": 6474650062, "anchor": "photo-dance",
            "developer": "SPARKHUB PTE. LTD.",
            "row": ["Faces, full bodies, pets and anime characters", "Free to try; weekly and yearly subscriptions", "4.4", "500+ templates, per the listing"],
            "best_for": "photos of babies, pets and anime characters, with a large template list.",
            "facts": [
                "The listing says it animates faces, full bodies, pets and anime characters from one photo.",
                "The listing says 500+ dance templates and TikTok trends updated weekly.",
                "Subscriptions are weekly or yearly and renew automatically unless turned off 24 hours before the period ends, per the listing.",
                "Version 2.1.8 (9 Oct 2026), iOS 15.6 or later.",
            ],
            "limits": "the listing mixes dance with other AI video features, so read the template list before you subscribe.",
        },
        {
            "name": "DanceHit: AI Dance Generator", "id": 6761751034, "anchor": "dancehit",
            "developer": "SCALEUP YAZILIM HIZMETLERI",
            "row": ["Selfies, portraits and pet photos with dance templates", "Free to download; subscription for premium features", "4.4", "Pet and selfie clips"],
            "best_for": "pet and selfie dance clips with a template you pick in a few taps.",
            "facts": [
                "Upload a picture, choose a dance template and generate a video to save and share, per the listing.",
                "The listing says optional auto-renewing subscriptions unlock premium features.",
                "It says payment is charged to your Apple ID at purchase and can be cancelled in your App Store account settings.",
                "Version 1.1.2 (9 Nov 2026), iOS 16.0 or later.",
            ],
            "limits": "the listing says features may require a paid subscription, and it does not list which ones are free.",
        },
    ],
    "who": [
        "<strong>You want to pay for credits, not a subscription:</strong> Ai Dance Generator.",
        "<strong>You want a style library and a photo of a person or a pet:</strong> Dance AI or Photo Dance.",
        "<strong>You want memes and scenes, not only dance:</strong> Viggle AI, free to start.",
        "<strong>You want a quick pet or selfie clip:</strong> DanceHit.",
    ],
    "cases": [
        "A birthday clip of a grandparent with a dance from a template library (Dance AI, Photo Dance).",
        "A pet dance video for TikTok or Reels (Photo Dance, DanceHit, Ai Dance Generator).",
        "A meme that puts your face into a trending scene (Viggle AI).",
        "A few short clips a month, paid as credits rather than a subscription (Ai Dance Generator).",
    ],
    "method": [
        "On 16 November 2026 we searched the US App Store for \"ai dance video\", \"dance video ai\" and \"photo dance ai\", kept the apps whose own description says they turn a photo into a dance video, and looked up five with Apple's lookup data for name, seller, price, rating, version, date and description.",
        "We did not test the apps ourselves. Everything in the table comes from each listing; prices inside the app were not readable without a browser, so we give none. Apps are ordered by rating, highest first.",
        "We do not list apps that were not on the App Store that day, and we do not compare features that a listing does not state.",
    ],
    "faq": [
        ("What is the best AI dance video app for iPhone?",
         "For one photo with a choice of dance styles, Ai Dance Generator (4.8) and Dance AI (4.6) are the most direct. For memes and scenes beyond dancing, Viggle AI (4.8) is free to start. All five are free to download."),
        ("Can I make a dance video from one photo?",
         "Yes. Ai Dance Generator, Dance AI, Photo Dance and DanceHit each ask for one photo and a dance style or template. Viggle AI puts your photo into a video clip you choose."),
        ("Are AI dance video apps free?",
         "All five are free to download. Four list a subscription or credit packs for full use. Viggle AI says it is free to start with five generations a day."),
        ("Do these apps keep my photos?",
         "Dance AI says photos are used only to make your video and are not stored permanently afterwards. Ai Dance Generator says the photo goes only to its AI partner and is not stored on its servers. Read each app's privacy policy before you upload a photo of someone else."),
    ],
    "sources": src("us"),
}

PAGES = [EN]
