"""Private Photo Vault alternatives for iPhone. EN. Our app: Photo Vault (id1532670722), "Photo Vault: Hide Pics Video".

Checked 2026-10-16: iTunes lookup API + App Store web pages (US). Photo Vault 1.2.8 facts
from its live listing and the reviewland hide-photos page (2026-10-11).
"""

CHECKED = "2026-10-16"


def src(cc):
    return [
        ("Photo Vault: Hide Pics Video (App Store)", f"https://apps.apple.com/{cc}/app/id1532670722"),
        ("Private Photo Vault - Pic Safe (App Store)", f"https://apps.apple.com/{cc}/app/id417571834"),
        ("Keepsafe (App Store)", f"https://apps.apple.com/{cc}/app/id510873505"),
        ("PV - Secret Photo Album (App Store)", f"https://apps.apple.com/{cc}/app/id867586326"),
        ("Secret Photo Album - SA (App Store)", f"https://apps.apple.com/{cc}/app/id1174964304"),
        ("Apple Support: hide photos on iPhone", "https://support.apple.com/en-us/104987"),
    ]


EN = {
    "group": "photo-vault-alternatives", "cover": "hide-photos", "lang": "en", "store": "us",
    "path": "private-photo-vault-alternatives-iphone/",
    "ct": "rl-vault-alt",
    "category": "PhotographyApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best Private Photo Vault alternatives for iPhone (2026)",
    "h1": "Private Photo Vault alternatives for iPhone in 2026",
    "description": "Five alternatives to Private Photo Vault on iPhone: Keepsafe, PV Secret Photo Album, Secret Photo Album SA and Photo Vault. Prices and privacy checked.",
    "llms": "Compares Private Photo Vault - Pic Safe with four alternatives for iPhone (Keepsafe, PV - Secret Photo Album, Secret Photo Album - SA, Photo Vault: Hide Pics Video) by price, cloud backup, decoy or break-in features and App Store privacy label.",
    "disclosure": "Photo Vault: Hide Pics Video is made by Saga Labs, the company behind Reviewland. It is one more option in this list, not placed first because it is ours. Note that it is a different app from \"Private Photo Vault - Pic Safe\", which is not ours. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "Private Photo Vault - Pic Safe is the biggest vault app on the App Store (about 1 million ratings, 4.8 stars). If you want an alternative, Keepsafe is the closest big one with an optional private cloud, PV - Secret Photo Album has the most features and the cheapest subscription, and Photo Vault: Hide Pics Video needs no account and keeps everything on the phone unless you turn on its optional encrypted iCloud copy.",
        "iOS already has a free Hidden album in Photos; for casual privacy that may be enough. Apple's own guide is linked in the sources.",
    ],
    "columns": ["App", "Price (US)", "Cloud backup", "Privacy features", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "All five are free to download. Prices are the in-app purchases listed on the US App Store on 16 October 2026 (apps list several price points for the same plan). Ratings are the App Store average and number of ratings that day.",
    "apps": [
        {
            "name": "Photo Vault: Hide Pics Video", "id": 1532670722, "ours": True, "anchor": "photo-vault",
            "developer": "Saga Ltd.", "rating": (4.17, 6),
            "row": ["Free to download; Premium yearly (listed $19.99 and $29.99) or lifetime (listed $14.99, $29.99 and $59.99)", "Optional: an end-to-end encrypted copy in your own iCloud, off by default; no account; or one encrypted file you export yourself", "Face ID, per-album passwords, decoy code (Premium), disguised icon, face-down exit, private camera",
                    "Data Not Collected", "1.3.0 (26 Oct 2026)", "4.2 (6 ratings)"],
            "best_for": "people who want photos only on their iPhone, with no account and nothing uploaded.",
            "facts": [
                "Opens with Face ID, Touch ID or a passcode, and each album can have its own password.",
                "Disguised icon (Calculator, Notes or Weather) and a face-down exit that jumps to Safari, Calendar or Messages.",
                "Private Camera takes photos straight into the vault, so they never reach the camera roll.",
                "Left out of iCloud backups; to move to a new iPhone you export one password-locked file and restore it. Works offline.",
                "19 languages, iOS 17 or later, 20 MB.",
            ],
            "limits": "without the optional iCloud copy there is no automatic backup: if you delete the app without exporting the vault, it is gone. The free version is limited (it held a single item when we checked on 11 October), so in practice it is a paid app. Only 6 ratings so far, and a much younger app than the others here.",
        },
        {
            "name": "Private Photo Vault - Pic Safe", "id": 417571834, "anchor": "private-photo-vault",
            "developer": "Legendary Software Labs LLC", "rating": (4.82, 1017221),
            "row": ["Free; Premium listed at $6.99, $12.99, $35.99 and $39.99", "Optional encrypted Cloud Vault", "PIN or pattern lock, per-album passwords, break-in report with photo and GPS, decoy password, face-down lock",
                    "Data Linked to You (diagnostics, identifiers, purchases, usage data, user content)", "25.8 (17 Sep 2026)", "4.8 (1,017,221 ratings)"],
            "best_for": "the best-known vault, with a long feature list including a private browser.",
            "facts": [
                "Break-in report with photo and GPS, decoy password and face-down lock, per its listing.",
                "Private web browser that can download photos into the app; import and export, wireless photo transfer.",
                "Optional encrypted cloud backup (\"Cloud Vault\"); the listing says its employees cannot view your photos.",
                "11 languages, iOS 15 or later, 172 MB.",
            ],
            "limits": "its privacy label lists several kinds of data linked to you, and several features need Premium.",
        },
        {
            "name": "Secret Photo Vault: Keepsafe", "id": 510873505, "anchor": "keepsafe",
            "developer": "KeepSafe Software, Inc", "rating": (4.75, 384414),
            "row": ["Free; Premium listed from $4.99 to $35.99 (yearly $23.99, monthly $9.99)", "Optional Private Cloud (Premium)", "PIN, Touch ID, album lock with separate PINs, Safe Send",
                    "Data Not Linked to You (usage data)", "13.34.0 (12 Oct 2026)", "4.8 (384,414 ratings)"],
            "best_for": "an easy vault with optional cloud sync across devices.",
            "facts": [
                "PIN and fingerprint lock; Album Lock gives each album its own PIN on Premium.",
                "Private Cloud stores up to 10,000 items and syncs across devices (Premium); Safe Send shares pictures for a limited time.",
                "Integrated camera and trash recovery.",
                "16 languages, iOS 17 or later, 210 MB.",
            ],
            "limits": "cloud backup and per-album locks need Premium, and your photos go to its cloud if you switch the cloud on.",
        },
        {
            "name": "PV - Secret Photo Album", "id": 867586326, "anchor": "pv-secret-photo-album",
            "developer": "Haibin Jiao", "rating": (4.71, 30267),
            "row": ["Free (with ads); Pro $3.99 a month or $17.99 a year, lifetime $41.99; cloud plans $12.99 to $79.99 a year", "Optional cloud backup plans", "Face ID, fake password, emergency switch when face down, customizable app icon",
                    "Data Linked to You (contact info, identifiers); other data not linked", "7.5.18 (8 Aug 2026)", "4.7 (30,267 ratings)"],
            "best_for": "the longest feature list at the lowest subscription prices.",
            "facts": [
                "Free unlimited storage, per its listing, with password and Face ID protection, fake password and a customizable icon.",
                "Tags, notes and search, a photo editor, audio support and Nearby Drop between phones.",
                "Wi-Fi transfer to a PC and third-party cloud backup are Pro features; ads are removed with a purchase.",
                "12 languages, iOS 15 or later, 157 MB.",
            ],
            "limits": "free version shows ads, and the privacy label includes contact info and identifiers linked to you.",
        },
        {
            "name": "Secret Photo Album - SA", "id": 1174964304, "anchor": "secret-photo-album-sa",
            "developer": "BP Mobile LLC", "rating": (4.59, 38913),
            "row": ["Free; Premium listed from $1.99 to $51.99 across plans", "Secure cloud backup (unlimited cloud storage on Premium)", "PIN, Touch ID and Face ID, decoy PIN, break-in alerts with intruder photos, separate PIN per album",
                    "Data Linked to You (diagnostics, identifiers, location, purchases, usage data, user content and more)", "2.18 (6 Oct 2026)", "4.6 (38,913 ratings)"],
            "best_for": "a simple vault if you are comfortable with a long list of data types on its privacy label.",
            "facts": [
                "Encrypted, PIN-protected vault with a decoy PIN, break-in alerts with photos of the intruder and a separate PIN for selected albums.",
                "Private browser with an ad blocker and a built-in camera; unlimited cloud storage is a Premium feature. A separate Secret Calculator Photo Vault purchase is listed at $9.99.",
                "12 languages, iOS 15 or later, 80 MB, the smallest of the competitors.",
            ],
            "limits": "it has the longest privacy label of the five, including location, and its Premium lists many different prices.",
        },
    ],
    "who": [
        "<strong>You want nothing uploaded and no account:</strong> Photo Vault: Hide Pics Video.",
        "<strong>You want the best-known app and a break-in report:</strong> Private Photo Vault - Pic Safe.",
        "<strong>You want your photos synced to a private cloud:</strong> Keepsafe or Private Photo Vault.",
        "<strong>You want the most features for the lowest price:</strong> PV - Secret Photo Album.",
        "<strong>You only need to hide a few photos from casual snooping:</strong> iOS's own Hidden album, which needs no app.",
    ],
    "cases": [
        "Keeping private photos out of the shared camera roll and out of iCloud (an app with no account and cloud only if you opt in, such as ours).",
        "Backing up a vault so a lost phone does not lose photos (Keepsafe or Private Photo Vault cloud).",
        "Handing your phone to someone without them seeing the app (disguised icons and face-down exit).",
        "Moving to a new iPhone: with ours you export and restore a file yourself; cloud-backed apps restore from their cloud.",
    ],
    "method": [
        "On 16 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchases, version and release date, rating and number of ratings, languages, size, minimum iOS and the privacy label. Features are the ones each developer lists on its App Store page; we did not verify their encryption. We did not invent ratings or reviews.",
    ],
    "faq": [
        ("What is the best alternative to Private Photo Vault?",
         "Keepsafe is the closest large alternative, with an optional private cloud. PV - Secret Photo Album has the most features for the lowest subscription price. Photo Vault: Hide Pics Video is the option with no account, and its iCloud copy is optional and off by default."),
        ("Is Photo Vault: Hide Pics Video the same as Private Photo Vault?",
         "No. They are different apps by different developers. Photo Vault: Hide Pics Video is by Saga Ltd.; Private Photo Vault - Pic Safe is by Legendary Software Labs."),
        ("Which photo vault does not use the cloud?",
         "Photo Vault: Hide Pics Video keeps everything on the iPhone, with no account and no sync, and its privacy label says Data Not Collected. Cloud backup is optional in Private Photo Vault, Keepsafe and PV."),
        ("Do I need a vault app at all?",
         "Not always. iPhone has a Hidden album in Photos that you can lock with Face ID or a passcode on recent iOS versions; an app adds separate albums, disguised icons and other features. See Apple's guide in the sources."),
        ("Can I move my vault to a new iPhone?",
         "With Photo Vault: Hide Pics Video you export one password-locked file and restore it on the new phone, because the vault is left out of iCloud backups. Cloud-based vaults restore from their own cloud."),
    ],
    "sources": src("us"),
}

from pages.store_1016 import refresh

refresh(EN, "us")

PAGES = [EN]
