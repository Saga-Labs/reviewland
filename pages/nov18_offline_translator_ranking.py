"""Best offline translator apps for iPhone. EN. No app of ours is listed.

Checked 2026-11-18 (UTC): iTunes lookup (US) for the five apps (name, seller, price, rating, version, release date and
description). Features, limits and prices come only from each listing's own text. Microsoft Translator and Translate Now
were checked too and left out: their listings do not describe offline translation as a free feature. In-app purchase
prices were not readable without a browser, so the page gives none.
"""

DAY = "2026-11-18"
AS_OF = "Nov 18, 2026"


def src(cc="us"):
    return [
        ("OT Pro: Offline Translator (App Store)", f"https://apps.apple.com/{cc}/app/id6756822236"),
        ("iTranslate Translator (App Store)", f"https://apps.apple.com/{cc}/app/id288113403"),
        ("Google Translate (App Store)", f"https://apps.apple.com/{cc}/app/id414706506"),
        ("Translator Offline (App Store)", f"https://apps.apple.com/{cc}/app/id6443437243"),
        ("Translate, by Apple (App Store)", f"https://apps.apple.com/{cc}/app/id1514844618"),
    ]


EN = {
    "group": "offline-translators", "lang": "en", "store": "us", "cover": None,
    "path": "best-offline-translator-apps-iphone/",
    "ct": "rl-offline-translator-apps",
    "category": "Travel",
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Best Offline Translator Apps for iPhone (2026)",
    "h1": "Best offline translator apps for iPhone (2026)",
    "description": "Five translator apps for iPhone that say they work without internet, compared by what the offline mode covers, whether it costs extra, rating, version and who it suits. Checked on the App Store on 18 November 2026.",
    "llms": "Compares five iPhone translator apps that describe offline use (OT Pro: Offline Translator, iTranslate, Google Translate, Translator Offline and Apple's Translate) by what their offline mode covers, whether the listing says it needs a subscription, rating, version and who it suits. Checked on the App Store on Nov 18, 2026.",
    "answer": [
        "The best offline translator app depends on what you need offline: OT Pro: Offline Translator (4.8) covers text, voice and photos without internet, iTranslate (4.7) has an offline mode that needs downloaded language packs, and Google Translate (4.3) translates with no internet connection. We checked five apps on the App Store on Nov 18, 2026.",
        "All five are free to download. Translator Offline (3.9) says its offline mode needs a subscription, and iTranslate lists subscription terms with a free trial. Apple's Translate (2.4) offers an on-device mode for downloaded languages. Check the price on Apple's payment sheet before you buy.",
    ],
    "columns": ["App", "Works offline for", "Price (US)", "Rating (US)", "Best for"],
    "table_note": "Price and rating are from the US App Store as of Nov 18, 2026. \"Free\" means free to download. The offline notes come from each app's own description. Ratings are rounded to one decimal.",
    "apps": [
        {
            "name": "OT Pro: Offline Translator", "id": 6756822236, "anchor": "ot-pro",
            "developer": "Diego Martinez White",
            "row": ["Text, voice and photo translation with no internet", "Free to download; the listing names no subscription", "4.8", "Text, voice and photos in 50+ languages"],
            "best_for": "travel where you need text, speech and photo translation with no data at all.",
            "facts": [
                "The listing says it translates text without an internet connection, supports 50+ languages and works offline for voice and photo translation.",
                "It says it uses no roaming and no data, per the listing.",
                "The rating is based on fewer than 100 ratings, so it is a small sample.",
                "Version 1.0.1 (19 Mar 2026).",
            ],
            "limits": "the listing does not say which languages work offline or how many; check the language list in the App Store before you travel.",
        },
        {
            "name": "iTranslate Translator", "id": 288113403, "anchor": "itranslate",
            "developer": "Mosaic S.r.l.",
            "row": ["Text and voice translation, with an offline mode", "Free to download; subscription terms with a free trial", "4.7", "Text, voice, camera and phrasebook"],
            "best_for": "a traveller who wants a full translator with phrasebooks and an offline mode for downloaded languages.",
            "facts": [
                "The listing names an offline translation mode and says you need to download language packs to use it.",
                "It also lists text translation in over 100 languages, a phrasebook, a camera lens for menus and signs, and voice-to-voice conversations.",
                "The listing includes auto-renewable subscription terms with a free trial. It does not say which features need the subscription.",
                "Version 17.4.77 (12 Nov 2026).",
            ],
            "limits": "the listing does not say which features the subscription covers, so check the Apple payment sheet before you use offline mode.",
        },
        {
            "name": "Google Translate", "id": 414706506, "anchor": "google-translate",
            "developer": "Google LLC",
            "row": ["Text, speech and camera translation; offline translation", "Free to download; the listing names no subscription", "4.3", "Up to 249 languages, with support varying by language"],
            "best_for": "a wide choice of languages, with offline translation for the ones that support it.",
            "facts": [
                "The listing says it translates with no internet connection, under \"Offline\".",
                "It says feature support varies by language, and it lists instant camera translation, dictation, conversations and a phrasebook.",
                "The listing gives a permissions notice for the microphone, camera and photos.",
                "Version 10.47.381 (16 Nov 2026).",
            ],
            "limits": "the listing does not say which languages work offline, only that support varies by language.",
        },
        {
            "name": "Translator Offline", "id": 6443437243, "anchor": "translator-offline",
            "developer": "Evgeniy Labunchak",
            "row": ["Voice and text translation after you download a language", "Free to download; offline mode needs a subscription", "3.9", "30+ languages, voice first"],
            "best_for": "voice translation when you have a language downloaded and are willing to pay for offline mode.",
            "facts": [
                "The listing says you download a language once and then use it offline.",
                "It says some features need an active subscription, and it names offline mode, voice translation and PDF export of the history.",
                "It supports speech recognition in over 30 languages, according to the listing.",
                "The rating is based on fewer than 100 ratings. Version 2.9 (29 Sep 2026).",
            ],
            "limits": "the listing names offline mode as a subscription feature; check the App Store price before you rely on it while travelling.",
        },
        {
            "name": "Translate", "id": 1514844618, "anchor": "apple-translate",
            "developer": "Apple Inc.",
            "row": ["Apple's translator with an on-device mode", "Free to download; the listing names no subscription", "2.4", "On-device mode for downloaded languages"],
            "best_for": "people who already use Apple's own tools and want translations kept on the phone.",
            "facts": [
                "The listing says it has an on-device mode for a fully offline experience in Translate and for downloaded languages.",
                "It says the on-device mode keeps your translations private, per the listing.",
                "The rating is low (2.4), so read the recent reviews before you rely on it.",
                "Version 8.9 (19 Oct 2026).",
            ],
            "limits": "the listing ties the on-device mode to downloaded languages, and it does not list which languages those are.",
        },
    ],
    "who": [
        "<strong>You want offline text, voice and photo translation with no subscription:</strong> OT Pro: Offline Translator.",
        "<strong>You want a full translator with phrasebooks and an offline mode you can pay for:</strong> iTranslate Translator.",
        "<strong>You want the widest choice of languages, with offline use for some of them:</strong> Google Translate.",
        "<strong>You want Apple's own translator and on-device mode:</strong> Translate.",
    ],
    "cases": [
        "A flight with no Wi-Fi and a menu to read in a foreign language (OT Pro: Offline Translator, Google Translate).",
        "A phrase book and camera translation for signs on a trip (iTranslate Translator).",
        "Voice translation on a train in a country where you have no data (Translator Offline, with the subscription).",
        "Translations you keep on your phone with Apple's own app (Translate).",
    ],
    "method": [
        "On 18 November 2026 we looked up on the US App Store the apps named \"Offline Translator\", \"Google Translate\", \"iTranslate\", \"Microsoft Translator\", \"Translate Now\" and \"Translator Offline\", kept the five whose own description says they translate without internet or name an offline mode, and read each one's name, seller, price, rating, version, date and description from Apple's lookup data.",
        "We did not test the apps ourselves. Everything in the table comes from each listing. We do not give in-app prices, because they were not readable without a browser. Apps are ordered by rating, highest first.",
        "Microsoft Translator (4.8) and Translate Now (4.7) are not in the table. Their listings do not describe offline translation as a free feature.",
    ],
    "faq": [
        ("What is the best offline translator app for iPhone?",
         "OT Pro: Offline Translator (4.8) translates text, voice and photos without internet, according to its listing. iTranslate (4.7) has an offline mode that needs downloaded language packs."),
        ("Do offline translator apps cost money?",
         "Most of the five are free to download. Translator Offline says its offline mode needs a subscription, and iTranslate lists subscription terms with a free trial. Check the Apple payment sheet before you buy."),
        ("Does Google Translate work offline?",
         "Google Translate's listing says it translates with no internet connection under \"Offline\", and that feature support varies by language."),
        ("Is Apple's Translate app offline?",
         "Apple's Translate has an on-device mode, which its listing says gives a fully offline experience for downloaded languages. Its rating on the App Store is 2.4, so read the recent reviews first."),
    ],
    "sources": src("us"),
}

PAGES = [EN]
