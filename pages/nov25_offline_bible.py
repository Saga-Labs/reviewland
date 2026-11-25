"""Best Bible apps that work offline on iPhone. EN. Bible Videos (ours, on sale since 24 Nov 2026) is the last entry:
the list is ordered by rating and it has none yet.

Checked 2026-11-25 (UTC): iTunes search (US) for "bible offline", "offline bible free" and "audio bible", and iTunes
lookup (US) for the six apps (name, seller, price, rating, version, date, minimum iOS and description). What works
offline, the translations and the prices come only from each listing's own text.
"""

DAY = "2026-11-25"
AS_OF = "Nov 25, 2026"


def src(cc="us"):
    return [
        ("Bible, by Life.Church (App Store)", f"https://apps.apple.com/{cc}/app/id282935706"),
        ("Bible Offline - KJV Holy Bible (App Store)", f"https://apps.apple.com/{cc}/app/id1472850697"),
        ("Bible - Daily Bible Verse KJV (App Store)", f"https://apps.apple.com/{cc}/app/id1357464684"),
        ("Bible · Audio Study Offline (App Store)", f"https://apps.apple.com/{cc}/app/id1405764030"),
        ("KJV Bible Offline - Audio KJV (App Store)", f"https://apps.apple.com/{cc}/app/id1286409899"),
        ("Bible Videos: Audio & Prayer (App Store)", f"https://apps.apple.com/{cc}/app/id6833978906"),
    ]


EN = {
    "group": "bible-offline", "lang": "en", "store": "us", "cover": None,
    "path": "best-offline-bible-apps-iphone/",
    "ct": "rl-offline-bible",
    "category": "Reference",
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Best Bible Apps That Work Offline on iPhone (2026)",
    "h1": "Best Bible apps that work offline on iPhone (2026)",
    "description": "Six Bible apps for iPhone that you can read without internet, compared: what works offline in each, which translations, what the subscription removes or adds, and the rating. Checked on the App Store on 25 November 2026.",
    "llms": "Compares six iPhone Bible apps you can read without internet (Bible by Life.Church, Bible Offline - KJV Holy Bible, Bible - Daily Bible Verse KJV, Bible · Audio Study Offline, KJV Bible Offline - Audio KJV and Bible Videos: Audio & Prayer) by what works offline, translations, what the subscription is for, rating and version. Checked on the App Store on Nov 25, 2026.",
    "answer": [
        "Every app here says in its App Store listing that you can read the Bible without internet. The Bible app by Life.Church (4.9) is free and lets you download select versions; its audio Bibles need a connection. Bible - Daily Bible Verse KJV (4.9) is the only listing here that says audio also works offline. Bible Offline - KJV Holy Bible (4.9) and KJV Bible Offline - Audio KJV (4.8) carry the King James Version, and Bible · Audio Study Offline (4.8) lists the KJV, NIV, ESV and NKJV. We checked six apps on Nov 25, 2026.",
        "All six are free to download. In four of them the subscription removes ads; in Bible Videos: Audio & Prayer, which is new and has no ratings yet, the whole World English Bible is free offline and the subscription is for videos and audio.",
    ],
    "columns": ["App", "What works offline", "Price (US)", "Rating (US)", "Best for"],
    "table_note": "Price and rating are from the US App Store as of Nov 25, 2026. \"Free\" means free to download. What works offline and what the subscription does come from each app's own description. Ratings are rounded to one decimal.",
    "apps": [
        {
            "name": "Bible", "id": 282935706, "anchor": "bible-youversion",
            "developer": "Life.Church",
            "row": ["Bible versions you download first (select versions); audio needs a connection", "Free", "4.9", "Many versions and languages, free"],
            "best_for": "choosing your own translation and language and paying nothing.",
            "facts": [
                "The listing says you can access everything when connected, or download specific versions to use offline (available for select versions).",
                "It lists 3,500+ Bible versions in 2,300+ languages, including the NIV, NASB, ESV, NKJV, NLT and KJV.",
                "Audio Bibles are available for select versions and are not downloadable, per the listing.",
                "The listing calls it the free YouVersion Bible App and names no subscription. Version 11.36.1 (20 Nov 2026), iOS 18.0 or later.",
            ],
            "limits": "you have to download a version before you lose signal, not every version can be downloaded, and audio does not play offline.",
        },
        {
            "name": "Bible Offline - KJV Holy Bible", "id": 1472850697, "anchor": "bible-offline-kjv",
            "developer": "PANDAS OF CARIBBEAN LIMITED",
            "row": ["Reading and studying King James Version verses", "Free with ads; monthly subscription removes them", "4.9", "A light KJV for daily reading"],
            "best_for": "a King James Bible that opens without internet, with reading plans and night mode.",
            "facts": [
                "The listing says: read and study Bible verses without internet access, and calls the app a fast, light, free offline Bible.",
                "It lists King James Version audio and Bible plan audio; the listing does not say that the audio works offline.",
                "Night mode is listed for reading at night.",
                "A monthly subscription gives the ad-free version, per the listing. Version 3.3.0 (21 Nov 2026), iOS 15.0 or later.",
            ],
            "limits": "one translation (the KJV), and it shows ads unless you subscribe.",
        },
        {
            "name": "Bible - Daily Bible Verse KJV", "id": 1357464684, "anchor": "daily-bible-verse-kjv",
            "developer": "OZION TECH PTE. LTD.",
            "row": ["The King James Version and audio Bibles", "Free with ads; $4.99 a month removes them", "4.9", "Listening to the KJV without internet"],
            "best_for": "reading and listening to the King James Version where there is no signal.",
            "facts": [
                "The listing says: study the KJV Bible offline and listen to audio Bibles offline.",
                "It sends a daily Bible verse and lets you search the text by keyword, per the listing.",
                "The listing says morning and evening audio devotionals, Bible quizzes and audio of the whole book are free.",
                "A monthly subscription of $4.99 removes ads, per the listing. Version 4.7.0 (18 Nov 2026), iOS 15.0 or later.",
            ],
            "limits": "one translation (the KJV), and it shows ads unless you subscribe.",
        },
        {
            "name": "Bible · Audio Study Offline", "id": 1405764030, "anchor": "bible-audio-study-offline",
            "developer": "BUCKET LIST LABS S.L.",
            "row": ["Reading the Bible", "Free with ads; Premium subscription for unlimited Bibles and no ads", "4.8", "Several well-known translations in one app"],
            "best_for": "comparing the KJV, NIV, ESV and NKJV, with podcasts when you are online.",
            "facts": [
                "The listing says you can stay connected to Scripture without an internet connection and read offline anytime.",
                "It names the King James Version, New International Version, English Standard Version and New King James Version.",
                "It lists an audio Bible, daily devotionals and Christian podcasts; the listing does not say that the audio works offline.",
                "A premium subscription gives unlimited Bibles and no ads, per the listing. Version 3.1.10 (10 Aug 2026), iOS 17.0 or later.",
            ],
            "limits": "the listing ties unlimited Bibles to the subscription, so check which translations are free before you rely on it.",
        },
        {
            "name": "KJV Bible Offline - Audio KJV", "id": 1286409899, "anchor": "kjv-bible-offline-audio",
            "developer": "Watchdis Group B.V",
            "row": ["The King James Version text; audio needs internet", "Free with ads; monthly subscription removes them", "4.8", "The KJV text with highlights"],
            "best_for": "the King James text offline, with a daily verse and highlights.",
            "facts": [
                "The listing says the Bible can be used without internet, and that media and audio require internet.",
                "It offers a daily Bible verse, a daily devotion and a daily chapter reading, per the listing.",
                "You can highlight verses, per the listing.",
                "A monthly premium subscription removes ads, per the listing. Version 90.1 (7 Nov 2026), iOS 15.0 or later.",
            ],
            "limits": "one translation (the KJV), audio only with a connection, and ads unless you subscribe.",
        },
        {
            "name": "Bible Videos: Audio & Prayer", "id": 6833978906, "anchor": "bible-videos", "ours": True,
            "developer": "Saga Ltd.",
            "row": ["The whole World English Bible", "Free Bible and daily prayer; Premium subscription for videos and audio", "No ratings yet", "A modern-English Bible offline, free"],
            "best_for": "a free Bible in modern English that needs no connection, with a daily prayer.",
            "facts": [
                "The listing says the whole World English Bible is in the app, with no connection needed; you can turn pages or scroll, jump from the index, save verses and share them as images.",
                "Daily Prayer (a verse, a short reflection and a prayer), the whole Bible and the widgets are free, per the listing.",
                "Premium unlocks the story videos and the audio, including the spoken Daily Word and Bible chapters read aloud, per the listing.",
                "Version 1.0 (24 Nov 2026), iOS 17.0 or later. There is an Android version on Google Play.",
            ],
            "limits": "it was released on 24 Nov 2026 and has no ratings yet; it has one translation (the World English Bible), in English only, and its listing does not say that videos or audio work offline.",
        },
    ],
    "who": [
        "<strong>You want your own translation and language, free:</strong> Bible, by Life.Church (download the version first).",
        "<strong>You want to listen without internet:</strong> Bible - Daily Bible Verse KJV.",
        "<strong>You want the King James Version offline:</strong> Bible Offline - KJV Holy Bible or KJV Bible Offline - Audio KJV.",
        "<strong>You want the NIV, ESV or NKJV next to the KJV:</strong> Bible · Audio Study Offline.",
        "<strong>You want a modern-English Bible offline with a daily prayer:</strong> Bible Videos: Audio &amp; Prayer.",
    ],
    "cases": [
        "Reading on a flight or on the subway, with the phone in airplane mode (any of the six).",
        "A mission trip or a camp with no signal, where you also want audio (Bible - Daily Bible Verse KJV).",
        "Following the reading in church without using mobile data (Bible, by Life.Church, with the version downloaded).",
        "A verse and a prayer each morning before you go online (Bible Videos: Audio & Prayer).",
    ],
    "method": [
        "On 25 November 2026 we searched the US App Store for \"bible offline\", \"offline bible free\" and \"audio bible\", kept apps whose own description says the Bible can be read without internet, and looked up six with Apple's lookup data for name, seller, price, rating, version, date and description.",
        "We did not test the apps ourselves, and we did not put any phone in airplane mode: what works offline is what each listing says. Prices are given only where a listing states them. Apps are ordered by rating, highest first, and by number of ratings when the rounded rating is the same; the one with no ratings yet goes last.",
        "We do not list apps that were not on the App Store that day, and we do not compare features that a listing does not state.",
    ],
    "faq": [
        ("Which Bible app works without internet?",
         "All six on this page say so in their listings. The Bible app by Life.Church lets you download select versions; Bible Offline - KJV Holy Bible, Bible - Daily Bible Verse KJV and KJV Bible Offline - Audio KJV carry the King James Version; Bible · Audio Study Offline lists several translations; Bible Videos: Audio & Prayer includes the whole World English Bible."),
        ("Is there a free offline Bible app for iPhone?",
         "Yes. All six are free to download. The Bible app by Life.Church names no subscription. In Bible Offline - KJV Holy Bible, Bible - Daily Bible Verse KJV, KJV Bible Offline - Audio KJV and Bible · Audio Study Offline the subscription removes ads. In Bible Videos: Audio & Prayer the Bible text is free and the subscription is for videos and audio."),
        ("Can I listen to the Bible offline?",
         "Bible - Daily Bible Verse KJV is the only listing here that says you can listen to audio Bibles offline. The Bible app by Life.Church says its audio Bibles are not downloadable, and KJV Bible Offline - Audio KJV says audio requires internet."),
        ("Does the YouVersion Bible app work offline?",
         "Yes, for the versions you download first. Its listing says you can download specific versions to use offline, available for select versions, and that audio Bibles are not downloadable."),
    ],
    "sources": src("us"),
}

PAGES = [EN]
