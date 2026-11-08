"""Calculator# alternatives for iPhone. EN. Our app: Photo Vault (id1532670722), 4th of 6.
Checked 2026-11-03 (JST): iTunes lookup and US App Store pages. Calculator# Hide Photos Videos (Salman Ashraf, id1165276801):
3.4.13 (30 Oct 2026), 4.4 from 28,938 ratings, free with ads and limitations, $4.99 a year, label Data Used to Track You.
Criterion: a photo vault whose listing offers a way to hide or disguise the vault (another app's look, a decoy password,
a fake crash screen, a face-down exit) and updated in the last 12 months. Left out: Calculator Lock - Secure Vault (last
update 20 Dec 2024), Secret Photo Album ++ (2020). Keepsafe has its own page on reditor. Reserved in
ios-playbook/references/temas-webs.md (16b6e48). Photo Vault facts from its US listing (1.3.1, 1 Nov 2026)."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
NONE = "Data Not Collected"
HIDE = '<a href="/best-apps-to-hide-photos-iphone/">apps to hide photos</a>'
PPV = '<a href="/private-photo-vault-alternatives-iphone/">Private Photo Vault alternatives</a>'
NODATA = '<a href="/best-photo-vault-apps-no-data-collection-iphone/">photo vaults that collect no data</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, disguise, backup, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, disguise, backup, labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Converter: Hidden Photo Vault", 1536734125, "converter", "Dmitry Petrov", 4.86, 3657, "3.0.7", "2 Dec 2025", NONE,
        "One-time purchase: Full Access $19.99 (offers at $9.99 and $14.99)", "Looks like a currency converter", "Encrypted, in your own iCloud",
        "the closest idea to Calculator#: a vault hidden inside an ordinary-looking utility, paid once.",
        ["Its listing says the vault sits inside a currency converter, and files are encrypted and kept on the phone and in your own iCloud.", "Sold as a one-time purchase, \"without subscription\", and its privacy label says Data Not Collected."],
        "photos and documents only (no notes, passwords or browser like Calculator#), English only, needs iOS 18.2, and its last update was in December 2025."),
    app("Private Photo Vault - Pic Safe", 417571834, "private-photo-vault", "Legendary Software Labs LLC", 4.82, 1018919, "26.0", "2 Nov 2026", label(TRACK, LINKED),
        "Premium from $6.99 to $39.99; Upgrade $39.99", "Decoy password, face-down lock, break-in report with photo and GPS", "Encrypted Cloud Vault (paid)",
        "the best-known vault, with a decoy password and a report of who tried to get in.",
        ["About 1 million ratings, the most of any vault here, and updated on 2 November 2026.", "Its listing names a decoy password, a face-down lock, a break-in report with a photo and GPS, and a private browser."],
        "the free version does not back up to its Cloud Vault, per its listing, and its privacy label includes data used to track you."),
    app("PV - Secret Photo Album", 867586326, "pv", "Haibin Jiao", 4.71, 30298, "7.7.9", "26 Oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Pro $3.99 a month or $17.99 a year; lifetime $41.99; cloud backup from $12.99 a year", "Fake password, custom app icon, face-down jump to another app", "Paid cloud sync; third-party clouds with Pro",
        "the most features per dollar: fake password, custom icon and an emergency switch.",
        ["Its listing names a fake password, a custom app icon, and an Emergency Switch that jumps to another app when the phone faces down.", "Free unlimited storage on the phone, a trash folder and a photo editor; ads until you pay."],
        "the fake password needs a paid plan, per its listing, and the privacy label is the widest here."),
    app("Photo Vault: Hide Pics Video", 1532670722, "photo-vault", "Saga Ltd.", 4.17, 6, "1.3.1", "1 Nov 2026", NONE,
        "Premium $19.99 or $29.99 a year; lifetime $14.99 or $29.99", "Icon that looks like Calculator, Notes or Weather; face-down exit", "Optional encrypted copy in your own iCloud",
        "a calculator-looking icon with no account, no ads and nothing uploaded unless you choose.",
        ["Its listing says you can make the icon look like Calculator, Notes or Weather, and flipping the phone face down jumps to Safari, Calendar or Messages.", "A separate password for each album; no account and no server; privacy label Data Not Collected.", "Optional end-to-end encrypted copy in your own iCloud, or an encrypted backup file you keep."],
        "the icon looks like a calculator but the app does not work as one, and the free version is limited (Premium adds unlimited photos and the iCloud copy)."),
    app("Safe Lock - Hidden Photo Vault", 1195429570, "safe-lock", "Katerina Akhlebinina", 4.81, 24930, "3.1", "17 Aug 2026", NONE,
        "Premium $4.99, $19.99 or $29.99", "Fake password that opens a fake gallery; custom icon; shake or flip to lock", "Export to iCloud, Dropbox, Google Drive or Box",
        "a decoy gallery and a custom icon with a privacy label of Data Not Collected.",
        ["Its listing names a fake password that opens a fake gallery, a custom app icon, break-in reports with photos, and locking by shaking or flipping.", "Photos and videos are saved only on the device, per its listing; 13 languages."],
        "no automatic cloud copy: you export to a cloud service yourself."),
    app("Hide Photos Video -Hide it Pro", 523488488, "hide-it-pro", "Anuj Tenani", 4.65, 24796, "6.3.0", "11 Jan 2026", NOTLINKED,
        "Cloud Storage $9.99; Password Reset $4.99", "Disguise screen that looks as if the app crashed", "Paid cloud storage",
        "the same fake-crash trick as Calculator#'s Disguise Mode.",
        ["Its listing says a disguise screen makes the app look as if it crashed when someone opens it.", "Albums, USB export and an option to back up to cloud storage."],
        "English only, and its last update was in January 2026."),
]

PAGES = [{
    "group": "calculator-vault-alternatives", "lang": "en", "store": "us", "path": "calculator-vault-alternatives-iphone/", "ct": "rl-calculator-vault-alt",
    "category": "PhotographyApplication", "cover": "hide-photos", "hide_from_related": True,
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Calculator# Alternatives: Photo Vaults for iPhone (2026)", "h1": "Calculator# alternatives for iPhone",
    "description": "Six iPhone photo vaults that hide or disguise themselves like Calculator#: decoy passwords, fake icons, fake crash screens. US prices, privacy labels and ratings on 3 November 2026.",
    "llms": "Six alternatives to Calculator# Hide Photos Videos on iPhone, each with a way to hide or disguise the vault: Converter: Hidden Photo Vault, Private Photo Vault, PV - Secret Photo Album, Photo Vault: Hide Pics Video, Safe Lock, Hide it Pro. Price, disguise, backup, privacy label, version, rating on 3 November 2026.",
    "llms_note": "Photo Vault: Hide Pics Video, one of the six, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "Calculator# (by Salman Ashraf) looks like a calculator and hides photos, videos, notes and passwords behind it. It is free with ads and limits, and the full version is $4.99 a year; its privacy label includes data used to track you. For the same trick of a vault inside an ordinary-looking app, <strong>Converter: Hidden Photo Vault</strong> (a currency converter, paid once). For the best-known vault with a decoy password, <strong>Private Photo Vault</strong>. For a fake password and a custom icon at a low price, <strong>PV - Secret Photo Album</strong>. For a calculator-looking icon with no account and nothing uploaded, <strong>Photo Vault</strong>.",
        "If you only need photos out of your camera roll, iOS also has a locked Hidden album in Photos; see " + HIDE + ".",
    ],
    "columns": ["App", "Price (US)", "How it hides, per listing", "Backup", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "All six are free to download; prices are in-app purchases on each US App Store page on 3 November 2026 (pages list only some). For comparison, Calculator# 3.4.13 (30 October 2026): free with ads and limitations, Yearly Subscription $4.99 and Premium Features Pack $4.99; privacy label Data Used to Track You and Data Not Linked to You; rated 4.4 from 28,938 ratings.",
    "apps": APPS,
    "who": ["<strong>A vault inside a working-looking utility, paid once:</strong> Converter.", "<strong>Decoy password and break-in report:</strong> Private Photo Vault.", "<strong>Fake password and custom icon, cheapest yearly plan:</strong> PV - Secret Photo Album.",
            "<strong>Calculator-looking icon, no account, nothing uploaded:</strong> Photo Vault.", "<strong>A fake gallery behind a second password:</strong> Safe Lock.", "<strong>A fake crash screen:</strong> Hide it Pro."],
    "cases": ["Someone borrows your phone and asks you to open the app: a decoy password (Private Photo Vault, PV, Safe Lock) shows a different set of photos.",
              "You don't want a vault app on your home screen at all: Converter, or Photo Vault with the Calculator icon.",
              "You keep passwords and notes in Calculator# too: none of these six does all of it. Private Photo Vault adds a private browser and Safe Lock secret notes; for passwords, Apple's Passwords app."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data. An app is here only if its listing names a way to hide or disguise the vault and it was updated in the last 12 months. We did not test how well each disguise holds up.",
               "Order: first the apps whose disguise is closest to Calculator#'s, then the rest. Left out: Calculator Lock - Secure Vault (last update December 2024). See also " + PPV + " and " + NODATA + "."],
    "faq": [
        ("What is the best alternative to Calculator#?", "For the same idea of a vault hidden inside an ordinary-looking app, Converter: Hidden Photo Vault. For the biggest, best-known vault, Private Photo Vault. For a calculator-looking icon with no account, Photo Vault."),
        ("Is there a calculator vault app without ads?", "Photo Vault shows no ads and can use a Calculator icon, but it does not work as a calculator. Converter works the same way with a currency converter and is paid once. Calculator# is free with ads until you pay $4.99 a year."),
        ("Which photo vault has a fake password?", "Private Photo Vault (decoy password), PV - Secret Photo Album (fake password, paid plan) and Safe Lock (fake password that opens a fake gallery), per their listings."),
        ("Which of these collect no data?", "Converter, Photo Vault and Safe Lock show Data Not Collected on their App Store privacy labels on 3 November 2026."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("Calculator# Hide Photos Videos (App Store)", "https://apps.apple.com/us/app/id1165276801"),
        ("Apple: Hide photos and videos on iPhone", "https://support.apple.com/en-us/104987")],
}]
