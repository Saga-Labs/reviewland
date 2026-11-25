"""Best Bible apps with videos for iPhone. EN. Bible Videos (ours, on sale since 24 Nov 2026) is the last entry: it has
no ratings yet and the list is ordered by rating. It sits at the end of "apps" so the translations (first five) still build.

Checked 2026-11-25 (UTC; first published 2026-11-17): iTunes lookup (US) for the six apps (name, seller, price, rating, version, date, minimum iOS
and description) and the iTunes search (US) for "bible videos", "bible stories videos" and "bible app for kids".
Features, limits and prices come only from each listing's own text. In-app purchase prices were not readable without a
browser, so the page gives none and says "subscription" only where the listing says it.
"""

FIRST = "2026-11-17"
DAY = "2026-11-25"
AS_OF = "Nov 25, 2026"


def src(cc="us"):
    return [
        ("Video Bible (App Store)", f"https://apps.apple.com/{cc}/app/id1660831327"),
        ("Faithe: Bible Videos & Stories (App Store)", f"https://apps.apple.com/{cc}/app/id6736618823"),
        ("Sacred Shorts: Bible Videos (App Store)", f"https://apps.apple.com/{cc}/app/id6759298323"),
        ("Bible - Audio & Video Bibles (App Store)", f"https://apps.apple.com/{cc}/app/id378075859"),
        ("Superbook Kids Bible (App Store)", f"https://apps.apple.com/{cc}/app/id606378030"),
        ("Bible Videos: Audio & Prayer (App Store)", f"https://apps.apple.com/{cc}/app/id6833978906"),
    ]


EN = {
    "group": "bible-video", "lang": "en", "store": "us", "cover": None,
    "path": "best-bible-apps-with-videos-iphone/",
    "ct": "rl-bible-video-apps",
    "category": "Reference",
    "published": FIRST, "updated": DAY, "checked": DAY,
    "title": "Best Bible Apps with Videos for iPhone (2026)",
    "h1": "Best Bible apps with videos for iPhone (2026)",
    "description": "Six Bible apps with videos compared for iPhone: what each video collection contains, what it costs to use fully, its rating and who it suits, including a free one for children. Checked on the App Store on 25 November 2026.",
    "llms": "Compares six Bible apps with videos for iPhone (Video Bible, Faithe, Sacred Shorts, Bible - Audio & Video Bibles, Superbook Kids Bible and Bible Videos: Audio & Prayer) by what each video collection contains, what its listing says about subscriptions, rating, version and who it suits. Checked on the App Store on Nov 25, 2026.",
    "answer": [
        "The best Bible app with videos depends on what you want to watch: Video Bible (4.9) pairs guided videos with study tools for each verse, Faithe and Sacred Shorts (4.8 each) are built around Bible videos and sell a subscription, and Superbook Kids Bible (4.8) is free and has 68 full-length episodes for children. Bible Videos: Audio & Prayer is new (24 Nov 2026, no ratings yet) and keeps daily prayer and the whole Bible free. We checked six apps on the App Store on Nov 25, 2026.",
        "Video Bible, Superbook Kids Bible and Bible - Audio & Video Bibles are free to download, and their descriptions name no subscription. Faithe, Sacred Shorts and Bible Videos: Audio & Prayer need a subscription for their premium content. Check the price on Apple's payment sheet before you buy.",
    ],
    "columns": ["App", "Works with", "Price (US)", "Rating (US)", "Best for"],
    "table_note": "Price and rating are from the US App Store as of Nov 25, 2026. \"Free\" means free to download. Works with and the price notes come from each app's own description. Ratings are rounded to one decimal.",
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
        {
            "name": "Bible Videos: Audio & Prayer", "id": 6833978906, "anchor": "bible-videos", "ours": True,
            "developer": "Saga Ltd.",
            "row": ["Short cinematic videos of Bible stories, audio readings and a daily prayer", "Free; Premium subscription", "No ratings yet", "A daily prayer and the Bible free, with story videos"],
            "best_for": "a daily verse and prayer at no cost, with short story videos and audio if you subscribe.",
            "facts": [
                "The listing describes Bible stories as short cinematic videos: Moses and the Red Sea, Jonah, Daniel in the lions' den, the wedding at Cana, the Nativity, and David and Goliath, with new chapters added as they are made.",
                "Per the listing, Daily Prayer (a verse, a short reflection and a prayer), the whole World English Bible, readable with no connection, and the widgets are free.",
                "Premium unlocks every video and every audio, including the spoken Daily Word, 8 guided meditations and Bible chapters read aloud, per the listing.",
                "Version 1.0 (24 Nov 2026), iOS 17.0 or later. There is an Android version on Google Play.",
            ],
            "limits": "it was released on 24 Nov 2026 and has no ratings yet; the listing names six stories so far, and the app, the videos and the Bible text are in English only.",
        },
    ],
    "who": [
        "<strong>You want a free Bible with videos for children:</strong> Superbook Kids Bible.",
        "<strong>You want a Bible you can read, hear and watch in your own language:</strong> Bible - Audio & Video Bibles.",
        "<strong>You want videos with a study tool for each verse:</strong> Video Bible.",
        "<strong>You want a daily Bible film with a subscription:</strong> Sacred Shorts or Faithe.",
        "<strong>You want a free daily prayer and Bible text, with story videos as an extra:</strong> Bible Videos: Audio &amp; Prayer.",
    ],
    "cases": [
        "A bedtime Bible story for a child, one episode at a time (Superbook Kids Bible).",
        "A short Bible film on your phone each morning (Sacred Shorts, Faithe).",
        "Reading one chapter with a video, verse meanings and a dictionary (Video Bible).",
        "Listening to the Bible in your language on the drive to work (Bible - Audio & Video Bibles).",
        "A verse and a prayer each morning from a Home Screen widget (Bible Videos: Audio & Prayer).",
    ],
    "method": [
        "On 17 November 2026 we searched the US App Store for \"bible videos\", \"bible stories videos\" and \"bible app for kids\", kept the apps whose own description says they show Bible videos, and looked up five with Apple's lookup data for name, seller, price, rating, version, date and description. On 25 November 2026 we looked all of them up again (ratings and versions had not changed) and added Bible Videos: Audio & Prayer, released the day before.",
        "We did not test the apps ourselves. Everything in the table comes from each listing; prices inside the app were not readable without a browser, so we give none. Apps are ordered by rating, highest first; the one with no ratings yet goes last.",
        "We do not list apps that were not on the App Store that day, and we do not compare features that a listing does not state.",
    ],
    "faq": [
        ("What is the best Bible app with videos?",
         "Video Bible (4.9) pairs guided videos with study tools for each verse. Faithe and Sacred Shorts (4.8 each) add Bible video series to a subscription. For children, Superbook Kids Bible (4.8) is free."),
        ("Are Bible video apps free?",
         "Video Bible, Superbook Kids Bible and Bible - Audio & Video Bibles are free to download, and their descriptions name no subscription. Faithe, Sacred Shorts and Bible Videos: Audio & Prayer need a subscription for premium content, and Sacred Shorts needs one for everything. Bible Videos keeps its daily prayer and the Bible text free."),
        ("Which Bible video app is good for kids?",
         "Superbook Kids Bible has 68 full-length, free episodes from the Superbook series, plus Bible games and trivia for children."),
        ("Can I watch the whole Bible in order in an app?",
         "Faithe says you can watch its Bible videos in chronological order, through the Old and New Testaments. Video Bible says it adds new videos regularly, but its description lists no full series."),
    ],
    "sources": src("us"),
}

PAGES = [EN]
