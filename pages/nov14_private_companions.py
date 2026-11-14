"""Best Private AI Companion Apps for iPhone. EN. No app of ours is listed (Zib is not on sale yet).

Checked 2026-11-14 (JST): iTunes search (US) for "private ai companion", "offline ai companion", "ai friend to talk to",
"on-device ai chat private", plus name searches; iTunes lookup for the eight apps; US App Store page for privacy labels.
Title chosen from App Store search hints ("private ai companion", "ai friend to talk to") and Search Console
("private ai app iphone", "is nomi ai private").
Privacy claims come only from each listing's text and its App Store privacy label; otherwise "Not stated".
"""

DAY = "2026-11-14"
AS_OF = "Nov 14, 2026"
NS = "Not stated"


def src(cc="us"):
    return [
        ("Talking Friday: AI Voice Chat (App Store)", f"https://apps.apple.com/{cc}/app/id6786747271"),
        ("Najimi: Private AI Companion (App Store)", f"https://apps.apple.com/{cc}/app/id6767312661"),
        ("SOUL.AI - Offline AI Companion (App Store)", f"https://apps.apple.com/{cc}/app/id6476977857"),
        ("Nomi: AI Companion with a Soul (App Store)", f"https://apps.apple.com/{cc}/app/id6450270929"),
        ("Pi, your personal AI (App Store)", f"https://apps.apple.com/{cc}/app/id6445815935"),
        ("Replika - AI Companion Chat (App Store)", f"https://apps.apple.com/{cc}/app/id1158555867"),
        ("Tolan: Your Friendly Guide (App Store)", f"https://apps.apple.com/{cc}/app/id6477549878"),
        ("Character AI: Chat, Talk, Text (App Store)", f"https://apps.apple.com/{cc}/app/id1671705818"),
    ]


EN = {
    "group": "private-ai-companions", "lang": "en", "store": "us", "cover": None,
    "path": "best-private-ai-companion-apps-iphone/",
    "ct": "rl-private-ai-companions",
    "category": "LifestyleApplication",
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Best Private AI Companion Apps for iPhone (2026)",
    "h1": "Best private AI companion apps for iPhone (2026)",
    "description": "Eight AI companion and AI friend apps for iPhone compared on privacy: on-device or cloud, works offline, account, price and App Store privacy label. Checked on 14 November 2026.",
    "llms": "Compares eight AI companion apps for iPhone (Talking Friday, Najimi, SOUL.AI, Nomi, Pi, Replika, Tolan, Character AI) by whether chats stay on the phone, offline use, account, price, rating and App Store privacy label. States what each listing says and what it does not.",
    "answer": [
        "If you want an AI companion whose chats stay on your phone, only three of the eight apps we checked say so in their App Store listing: Talking Friday, Najimi and SOUL.AI run the AI on the iPhone and say it works offline, and all three carry the label \"Data Not Collected\". The five bigger apps (Nomi, Pi, Replika, Tolan, Character AI) have far more ratings but their labels list data collected and linked to you, and none claims to run on the device.",
        "The trade-off is size: the on-device apps have 0 to 11 ratings, so their quality is unproven, and a privacy label is the developer's own statement. We checked on Nov 14, 2026 and wrote \"Not stated\" wherever a listing is silent.",
    ],
    "complaints": [
        {"id": "how-to-tell", "h2": "How to tell if an AI companion is private", "body": [
            "<strong>1. Does the listing say the AI runs on the device?</strong> \"Private\" in the name is not a claim. Look for words like on-device, local or \"works in airplane mode\". Najimi's and Talking Friday's listings say this; Nomi's, Pi's, Replika's and Tolan's do not.",
            "<strong>2. Read the App Store privacy label.</strong> On the app's page, scroll to App Privacy. \"Data Not Collected\" is the strongest label. \"Data Linked to You\" means the developer can tie the data to your identity; \"Data Used to Track You\" means it may be shared for tracking across other companies' apps and sites.",
            "<strong>3. Do the airplane-mode test.</strong> Start a chat, turn on airplane mode and send another message. If it still answers, the model is on your phone. If it fails, your messages go to a server.",
            "<strong>4. Check for an account.</strong> An account ties chats to an email or login. Talking Friday and SOUL.AI say no account is needed; for the others we write \"Not stated\".",
            "<strong>5. Read the privacy policy for chat storage.</strong> The label does not say how long chats are kept or whether they train models. A label is also self-reported by the developer and Apple does not audit each answer in advance.",
        ]},
    ],
    "columns": ["App", "Runs on the iPhone", "Works offline", "Account required", "Price (US)", "Rating (US)"],
    "table_note": "Price and rating are from the US App Store as of Nov 14, 2026. Other columns are what each app's own listing says; \"Not claimed\" means the listing does not say the AI runs on the device, and \"Not stated\" means it does not say. A rating with very few votes tells you little.",
    "apps": [
        {
            "name": "Talking Friday: AI Voice Chat", "id": 6786747271, "anchor": "talking-friday",
            "developer": "Chirag Jain",
            "row": ["Yes, per the listing (speech-to-speech on the Neural Engine)", "Yes", "No", "Free; no in-app purchases, per the listing", "No ratings yet"],
            "best_for": "private voice conversations that never leave the phone.",
            "facts": [
                "The listing says the whole speech-to-speech loop runs on the iPhone's Neural Engine, with no servers, no account and no internet required.",
                "App Store privacy label: Data Not Collected.",
                "You talk and it answers out loud; it is not a character or romance app, but a voice chat you can use for thinking out loud or practicing conversations.",
                "Version 1.0, iOS 18.0 or later, listing updated 14 Jul 2026.",
            ],
            "limits": "no ratings yet, so there is no public evidence of how good the conversations are; voice only, and it needs iOS 18.",
        },
        {
            "name": "Najimi: Private AI Companion", "id": 6767312661, "anchor": "najimi",
            "developer": "ShugoAI LLC",
            "row": ["Yes, per the listing (local AI and voice models bundled)", "Yes, per the listing (\"can run offline\")", NS, "Free", "4.0 (2 ratings)"],
            "best_for": "a customisable avatar companion that runs locally.",
            "facts": [
                "The listing says it bundles a local language model and voice model for on-device chat, so the download is larger than usual.",
                "You can change personality, appearance, voice and background, import your own VRM character and chat with documents.",
                "App Store privacy label: Data Not Collected.",
                "Version 1.1, iOS 18.6 or later, updated 6 Aug 2026.",
            ],
            "limits": "only 2 ratings; large download; the listing does not say whether an account is needed.",
        },
        {
            "name": "SOUL.AI - Offline AI Companion", "id": 6476977857, "anchor": "soul-ai",
            "developer": "Neuro.AI LTD",
            "row": ["Yes, per the listing", "Yes", "No", "Free", "2.5 (11 ratings)"],
            "best_for": "a plain offline chat model on a recent iPhone.",
            "facts": [
                "The listing says the model is inside the app, runs entirely on the device and sends no chats to the cloud; no account.",
                "App Store privacy label: Data Not Collected.",
                "It recommends iPhone 15 Pro or newer; older devices can be slow or crash, and devices below the iPhone 12 are not supported.",
                "Version 1.7.3, updated 10 Jul 2026.",
            ],
            "limits": "a 2.5 rating from 11 people, and it is a general assistant more than a personality-driven companion.",
        },
        {
            "name": "Nomi: AI Companion with a Soul", "id": 6450270929, "anchor": "nomi",
            "developer": "AI GLIMPSE INC",
            "row": ["Not claimed", NS, NS, "Free", "4.6 (3,029 ratings)"],
            "best_for": "long-term memory and relationship-style roleplay, if you accept a cloud service.",
            "facts": [
                "The listing stresses short and long-term memory, group chats, selfies and art generation, and does not say the AI runs on the device.",
                "App Store privacy label: Data Linked to You (purchases, contact info, user content, identifiers, usage data, diagnostics). It does not list tracking.",
                "Version 1.12.1, iOS 15.0 or later, updated 31 Mar 2026.",
            ],
            "limits": "user content is on the label as linked to you, so assume chats are stored by the company; read its privacy policy for retention. This answers the common question \"is Nomi AI private\": its label says data is linked to you and its listing makes no on-device claim.",
        },
        {
            "name": "Pi, your personal AI", "id": 6445815935, "anchor": "pi",
            "developer": "Inflection AI, Inc.",
            "row": ["Not claimed", NS, NS, "Free", "4.4 (2,555 ratings)"],
            "best_for": "a calm talk-it-out assistant with voice mode.",
            "facts": [
                "The listing describes talking things through, voice mode and getting things done; it does not say where the AI runs.",
                "App Store privacy label: Data Linked to You (identifiers, usage data, diagnostics), for analytics, personalisation and app functionality. No tracking listed.",
                "Version 26.1109.0 (13 Nov 2026), iOS 16 or later.",
            ],
            "limits": "no on-device or offline claim; the label has no user-content category, but the label does not tell you how chats are stored.",
        },
        {
            "name": "Replika - AI Companion Chat", "id": 1158555867, "anchor": "replika",
            "developer": "Luka, Inc.",
            "row": ["Not claimed", NS, NS, "Free", "4.4 (227,667 ratings)"],
            "best_for": "a long-running companion with calls and proactive check-ins.",
            "facts": [
                "The listing describes text, voice and video calls, internet access, app integrations and image generation, and says it remembers your people and plans.",
                "App Store privacy label: Data Used to Track You (identifiers, usage data); Data Linked to You (location, contact info, identifiers, usage data); and some diagnostics not linked to you.",
                "Version 12.5.2 (5 Nov 2026), iOS 17.0 or later.",
            ],
            "limits": "its label includes tracking data and location, and the listing describes features that need the internet.",
        },
        {
            "name": "Tolan: Your Friendly Guide", "id": 6477549878, "anchor": "tolan",
            "developer": "AQP, Inc.",
            "row": ["Not claimed", NS, NS, "Free", "4.8 (190,859 ratings)"],
            "best_for": "a friendly alien-style companion you can talk to about anything.",
            "facts": [
                "The listing is short: talk about interests, feelings and thoughts, share photos and design a planet together. It says nothing about where the AI runs.",
                "App Store privacy label: Data Used to Track You (purchases, location, contact info, identifiers, usage data, other data); Data Linked to You (including user content); and more not linked to you.",
                "Version 26.46.1 (11 Nov 2026), iOS 18.0 or later.",
            ],
            "limits": "the label lists tracking and location, and user content as linked to you; the listing gives no privacy claims.",
        },
        {
            "name": "Character AI: Chat, Talk, Text", "id": 1671705818, "anchor": "character-ai",
            "developer": "Character Technologies, Inc.",
            "row": ["Not claimed", NS, NS, "Free", "4.3 (561,523 ratings)"],
            "best_for": "millions of user-made characters, if privacy is not your first concern.",
            "facts": [
                "The listing describes chatting and calling a huge library of user-created characters, plus creating your own and sharing them with the community.",
                "App Store privacy label: Data Used to Track You (location, contact info, identifiers, usage data); Data Linked to You (purchases, financial info, location, contact info, user content, search history, identifiers, usage data, diagnostics).",
                "Version 1.17.4 (2 Oct 2026), iOS 15.1 or later.",
            ],
            "limits": "the longest data list of the eight, including financial info, user content and search history linked to you, and a community-and-sharing design.",
        },
    ],
    "who": [
        "<strong>You want chats that never leave the phone:</strong> Talking Friday (voice), Najimi (avatar) or SOUL.AI (plain chat).",
        "<strong>You want proven quality and accept a cloud service:</strong> Nomi, Pi, Replika or Tolan, with the label limits above.",
        "<strong>You want the least data collected among the big apps:</strong> Nomi and Pi list no tracking; Replika, Tolan and Character AI do.",
        "<strong>You want to use it on a plane or with no signal:</strong> Talking Friday, Najimi or SOUL.AI.",
    ],
    "cases": [
        "Venting or thinking out loud at night without an account (Talking Friday, SOUL.AI).",
        "A character you can customise that runs locally (Najimi).",
        "Long conversations with memory, accepting a cloud service (Nomi, Replika, Pi).",
        "Chatting with many user-made characters (Character AI).",
    ],
    "method": [
        "On 14 November 2026 we searched the US App Store for \"private ai companion\", \"offline ai companion\", \"ai friend to talk to\" and \"on-device ai chat private\", looked up the eight apps with Apple's lookup data for name, price, rating and description, and read each app's App Store page for its privacy label.",
        "We ordered the apps by how much each listing and label supports a private chat, then by rating. The on-device apps rank first on privacy, but their ratings are too few to judge quality, so read this as privacy first, not best companion.",
        "Features and privacy statements come only from the listings and labels, not from our own tests; we did not run network captures. We left out other apps that appeared in searches (Kindroid, Solace, Red Angel and others) to keep the list to eight; Solace's listing, for example, mentions account deletion and does not say chats stay on the device. Cora did not appear in the US App Store search.",
    ],
    "faq": [
        ("Is Nomi AI private?",
         "Its listing does not say the AI runs on your phone, and its App Store privacy label lists data linked to you, including user content, but no tracking. Read its privacy policy for how long chats are kept."),
        ("Can an AI companion work offline?",
         "Yes, if the model is on the phone. Talking Friday, Najimi and SOUL.AI say theirs works offline. Apps that do not say this, such as Nomi, Pi, Replika, Tolan and Character AI, are not described as offline in their listings."),
        ("What is the most private AI friend app for iPhone?",
         "Of the eight we checked, the ones with on-device claims and the label Data Not Collected: Talking Friday, Najimi and SOUL.AI. They have very few ratings, so test them yourself in airplane mode."),
        ("What does the App Store privacy label tell me?",
         "It is the developer's own list of data collected, split into used to track you, linked to you and not linked to you. It does not say how long chats are stored."),
    ],
    "sources": src("us"),
}

PAGES = [EN]

# PENDIENTE: añadir Zib (id 6833833745) en su puesto cuando el lookup la devuelva
