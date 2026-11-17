"""Best Bible apps with videos for iPhone. EN. No app of ours is listed (none of ours is on sale in this category yet).

Checked 2026-11-17 (UTC): iTunes lookup (US) for the five apps (name, seller, price, rating, version, date, minimum iOS
and description) and the iTunes search (US) for "bible videos", "bible stories videos" and "bible app for kids".
Features, limits and prices come only from each listing's own text. In-app purchase prices were not readable without a
browser, so the page gives none and says "subscription" only where the listing says it.
"""

DAY = "2026-11-17"
AS_OF = "Nov 17, 2026"


def src(cc="us"):
    return [
        ("Video Bible (App Store)", f"https://apps.apple.com/{cc}/app/id1660831327"),
        ("Faithe: Bible Videos & Stories (App Store)", f"https://apps.apple.com/{cc}/app/id6736618823"),
        ("Sacred Shorts: Bible Videos (App Store)", f"https://apps.apple.com/{cc}/app/id6759298323"),
        ("Bible - Audio & Video Bibles (App Store)", f"https://apps.apple.com/{cc}/app/id378075859"),
        ("Superbook Kids Bible (App Store)", f"https://apps.apple.com/{cc}/app/id606378030"),
    ]


EN = {
    "group": "bible-video", "lang": "en", "store": "us", "cover": None,
    "path": "best-bible-apps-with-videos-iphone/",
    "ct": "rl-bible-video-apps",
    "category": "Reference",
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Best Bible Apps with Videos for iPhone (2026)",
    "h1": "Best Bible apps with videos for iPhone (2026)",
    "description": "Five Bible apps with videos compared for iPhone: what each video collection contains, what it costs to use fully, its rating and who it suits, including a free one for children. Checked on the App Store on 17 November 2026.",
    "llms": "Compares five Bible apps with videos for iPhone (Video Bible, Faithe, Sacred Shorts, Bible - Audio & Video Bibles and Superbook Kids Bible) by what each video collection contains, what its listing says about subscriptions, rating, version and who it suits. Checked on the App Store on Nov 17, 2026.",
    "answer": [
        "The best Bible app with videos depends on what you want to watch: Video Bible (4.9) pairs guided videos with study tools for each verse, Faithe and Sacred Shorts (4.8 each) are built around Bible videos and sell a subscription, and Superbook Kids Bible (4.8) is free and has 68 full-length episodes for children. We checked five apps on the App Store on Nov 17, 2026.",
        "Video Bible, Superbook Kids Bible and Bible - Audio & Video Bibles are free to download, and their descriptions name no subscription. Faithe and Sacred Shorts need a subscription for their premium content. Check the price on Apple's payment sheet before you buy.",
    ],
    "columns": ["App", "Works with", "Price (US)", "Rating (US)", "Best for"],
    "table_note": "Price and rating are from the US App Store as of Nov 17, 2026. \"Free\" means free to download. Works with and the price notes come from each app's own description. Ratings are rounded to one decimal.",
    "apps": [
        {
            "name": "Video Bible", "id": 1660831327, "anchor": "video-bible",
            "developer": "The Video Bible LLC",
            "row": ["Guided Bible videos with a verse-by-verse text", "Free to download; in-app prices not checked", "4.9", "Videos plus study tools for each verse"],
            "best_for": "reading one chapter at a time with a video, verse meanings, notes and a dictionary.",
            "facts": [
                "The listing describes a growing Video Bible of guided videos, with new content added regularly.",
                "Tap any verse to see its meaning, per the listing; it also lists commentary, chapter summaries, a dictionary, Bible characters and maps.",
                "The listing names no subscription in its description.",
                "Version 6.21.1 (11 May 2026), iOS 15.1 or later.",
            ],
            "limits": "the listing does not say how much of the video library is free, so check it in the App Store before you rely on it.",
        },
        {
            "name": "Faithe: Bible Videos & Stories", "id": 6736618823, "anchor": "faithe",
            "developer": "Tightrope Interactive",
            "row": ["Curated Bible video collections, with the full passages", "Free; Premium subscription", "4.8", "Video collections by theme or in order"],
            "best_for": "watching Bible stories by theme, with prayers and reminders added.",
            "facts": [
                "The listing says you can watch Bible videos in curated collections, such as the life and miracles of Jesus, Job and Esther, or the Old and New Testaments in order.",
                "It lets you ask about any passage and get an explanation, per the listing.",
                "Premium unlocks the full app. The listing says the subscription renews unless you turn off auto-renew at least 24 hours before the period ends.",
                "Version 1.21 (10 Nov 2026), iOS 16.0 or later.",
            ],
            "limits": "the listing says unused free-trial time is lost when you switch to a paid plan.",
        },
        {
            "name": "Sacred Shorts: Bible Videos", "id": 6759298323, "anchor": "sacred-shorts",
            "developer": "Ian Marco Rodriguez",
            "row": ["Cinematic short films of Bible stories, with a Study Bible", "Subscription required", "4.8", "Short films, released every week"],
            "best_for": "a short Bible film each day, with a study Bible and devotionals in the same app.",
            "facts": [
                "The listing describes cinematic short films, from the story of Creation to the journeys of Paul, with new episodes every week.",
                "The listing says a subscription is required to access Sacred Shorts, including Bible reading.",
                "Per the listing, the subscription covers the full catalog, the Bible with audio, an AI Bible chat, daily devotionals and guided prayer.",
                "Version 3.6.3 (3 Nov 2026), iOS 15.1 or later.",
            ],
            "limits": "the listing gives no free tier, so every use needs the subscription.",
        },
        {
            "name": "Bible - Audio & Video Bibles", "id": 378075859, "anchor": "bible-is",
            "developer": "Faith Comes By Hearing",
            "row": ["Bible text, audio and video in many languages", "Free; donations are accepted", "4.8", "Many languages, audio first"],
            "best_for": "a Bible in your own language, with audio for the car or video as one option.",
            "facts": [
                "The listing says you can hear, watch, read and share the Bible in many languages, and that it detects the language your phone uses.",
                "It includes the Gospel Films and the JESUS film, per the listing.",
                "You can make plans and playlists, bookmark, highlight and add notes, per the listing.",
                "The listing says it is free and that donations are tax-deductible. Version 3.14.12 (25 Aug 2026), iOS 13.4 or later.",
            ],
            "limits": "the listing leads with audio, so video is one of several formats here, not the main feature.",
        },
        {
            "name": "Superbook Kids Bible", "id": 606378030, "anchor": "superbook",
            "developer": "The Christian Broadcasting Network, Inc",
            "row": ["Full children's Bible with 68 animated episodes", "Free; the listing names no subscription", "4.8", "Children's Bible episodes and games"],
            "best_for": "children who want Bible stories as episodes, with games and trivia.",
            "facts": [
                "The listing says the app has 68 full-length, free episodes from the Superbook series, such as David and Goliath, Daniel and the Lions' Den and The First Christmas.",
                "It has more than 20 Bible games, a trivia game and over 80 topics for children, per the listing.",
                "Videos and interactive content sit inside each chapter of the children's Bible, per the listing.",
                "Version 3.1.1 (28 Oct 2026), iOS 15.3 or later.",
            ],
            "limits": "the listing is written for children; its features are episodes, games, trivia and a children's Bible.",
        },
    ],
    "who": [
        "<strong>You want a free Bible with videos for children:</strong> Superbook Kids Bible.",
        "<strong>You want a Bible you can read, hear and watch in your own language:</strong> Bible - Audio & Video Bibles.",
        "<strong>You want videos with a study tool for each verse:</strong> Video Bible.",
        "<strong>You want a daily Bible film with a subscription:</strong> Sacred Shorts or Faithe.",
    ],
    "cases": [
        "A bedtime Bible story for a child, one episode at a time (Superbook Kids Bible).",
        "A short Bible film on your phone each morning (Sacred Shorts, Faithe).",
        "Reading one chapter with a video, verse meanings and a dictionary (Video Bible).",
        "Listening to the Bible in your language on the drive to work (Bible - Audio & Video Bibles).",
    ],
    "method": [
        "On 17 November 2026 we searched the US App Store for \"bible videos\", \"bible stories videos\" and \"bible app for kids\", kept the apps whose own description says they show Bible videos, and looked up five with Apple's lookup data for name, seller, price, rating, version, date and description.",
        "We did not test the apps ourselves. Everything in the table comes from each listing; prices inside the app were not readable without a browser, so we give none. Apps are ordered by rating, highest first.",
        "We do not list apps that were not on the App Store that day, and we do not compare features that a listing does not state.",
    ],
    "faq": [
        ("What is the best Bible app with videos?",
         "Video Bible (4.9) pairs guided videos with study tools for each verse. Faithe and Sacred Shorts (4.8 each) add Bible video series to a subscription. For children, Superbook Kids Bible (4.8) is free."),
        ("Are Bible video apps free?",
         "Video Bible, Superbook Kids Bible and Bible - Audio & Video Bibles are free to download, and their descriptions name no subscription. Faithe and Sacred Shorts need a subscription for premium content, and Sacred Shorts needs one for everything."),
        ("Which Bible video app is good for kids?",
         "Superbook Kids Bible has 68 full-length, free episodes from the Superbook series, plus Bible games and trivia for children."),
        ("Can I watch the whole Bible in order in an app?",
         "Faithe says you can watch its Bible videos in chronological order, through the Old and New Testaments. Video Bible says it adds new videos regularly, but its description lists no full series."),
    ],
    "sources": src("us"),
}

PAGES = [EN]
