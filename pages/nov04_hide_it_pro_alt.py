"""Hide it Pro alternatives for iPhone. EN. Our app: Photo Vault (id1532670722), 4th of 6.
Checked 2026-11-04 (JST): iTunes lookup and US App Store pages. Hide it Pro (Anuj Tenani, id523488488): 6.3.0, last updated
11 Jan 2026, 4.7 from 24,796 ratings, English only, Data Not Linked to You; Cloud Storage $9.99, Password Reset $4.99;
disguise screen that looks like a crash, albums, USB export, cloud backup. Criterion: photo vault updated since August 2026.
Reserved in ios-playbook/references/temas-webs.md (d49b498)."""

DAY = "2026-11-04"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
NONE = "Data Not Collected"
CALC = '<a href="/calculator-vault-alternatives-iphone/">Calculator# alternatives</a>'
BACKUP = '<a href="/photo-vault-apps-with-backup-iphone/">photo vaults with a backup</a>'
HIDE = '<a href="/best-apps-to-hide-photos-iphone/">apps to hide photos</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, protects, langs, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, protects, langs, labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Safe Lock - Hidden Photo Vault", 1195429570, "safe-lock", "Katerina Akhlebinina", 4.81, 24931, "3.1", "17 Aug 2026", NONE,
        "Premium $4.99, $19.99 or $29.99", "Fake password with a fake gallery; break-in photos; lock by shaking or flipping", "13",
        "the closest to Hide it Pro in size and privacy, with more ways to fool a snooper.",
        ["Its listing says photos are saved only on the device, with a fake password that opens a fake gallery and break-in reports with photos.", "Custom app icon; export to iCloud, Dropbox, Google Drive or Box; Wi-Fi transfer."],
        "no automatic cloud copy: you export yourself."),
    app("Private Photo Vault - Pic Safe", 417571834, "private-photo-vault", "Legendary Software Labs LLC", 4.82, 1018948, "26.0", "2 Nov 2026", label(TRACK, LINKED),
        "Premium from $6.99 to $39.99; Upgrade $39.99", "Decoy password, face-down lock, break-in report with photo and GPS", "11",
        "the best-known vault, updated this week, with an encrypted cloud backup.",
        ["About 1 million ratings; updated on 2 November 2026.", "Encrypted Cloud Vault backup (paid) and a private browser, per its listing."],
        "its privacy label includes data used to track you, and the free version has no cloud backup."),
    app("Secret Photo Vault: Keepsafe", 510873505, "keepsafe", "KeepSafe Software, Inc", 4.75, 385566, "13.35.0", "26 Oct 2026", label(TRACK, NOTLINKED),
        "Premium $4.99 to $35.99 (yearly $23.99, monthly $9.99)", "PIN per album; Private Cloud up to 10,000 items", "16",
        "the same vault on several devices, synced automatically.",
        ["Its listing says Private Cloud stores up to 10,000 items and syncs to all your Keepsafe installs.", "Trash recovery for photos deleted by mistake; 16 languages."],
        "the cloud is Keepsafe's, and its label includes data used to track you."),
    app("Photo Vault: Hide Pics Video", 1532670722, "photo-vault", "Saga Ltd.", 4.17, 6, "1.3.1", "1 Nov 2026", NONE,
        "Premium $19.99 or $29.99 a year; lifetime $14.99 or $29.99", "Password per album; icon like Calculator, Notes or Weather; face-down exit", "19",
        "no account and nothing uploaded unless you choose, updated this month.",
        ["Its listing says each album can have its own password, the icon can look like Calculator, Notes or Weather, and flipping the phone jumps to another app.", "Optional end-to-end encrypted copy in your own iCloud; privacy label Data Not Collected."],
        "the free version is limited (Premium adds unlimited photos and the iCloud copy)."),
    app("PV - Secret Photo Album", 867586326, "pv", "Haibin Jiao", 4.71, 30300, "7.7.9", "26 Oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Pro $3.99 a month or $17.99 a year; lifetime $41.99; cloud backup from $12.99 a year", "Fake password; custom icon; face-down jump to another app", "12",
        "the most features for the money, with Wi-Fi transfer like Hide it Pro's USB export.",
        ["Its listing names a fake password, custom app icon, Emergency Switch, trash folder and Wi-Fi transfer to a computer.", "Free unlimited storage on the phone; ads until you pay."],
        "backups and the fake password are paid, and its privacy label is the widest here."),
    app("SPV - Secret Photo Vault", 1449239240, "spv", "MAPLE LABS COMPANY LIMITED", 4.59, 70064, "7.6.1", "30 Aug 2026", label(TRACK, NOTLINKED),
        "Premium $4.99 to $39.99", "PIN lock for photos, contacts, passwords and a private browser", "4",
        "keeping contacts and passwords in the same locked app.",
        ["Its listing says it stores photos, videos, passwords, contacts and browser data behind a PIN.", "About 70,000 ratings."],
        "no decoy or disguise named in the listing, and its label includes data used to track you."),
]

PAGES = [{
    "group": "hide-it-pro-alternatives", "lang": "en", "store": "us", "path": "hide-it-pro-alternatives-iphone/", "ct": "rl-hide-it-pro-alt",
    "category": "PhotographyApplication", "cover": "hide-photos", "hide_from_related": True,
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Best Hide it Pro Alternatives for iPhone (2026)", "h1": "Hide it Pro alternatives for iPhone",
    "description": "Hide it Pro has not been updated on iPhone since January 2026. Six photo vaults updated since August, with prices, privacy labels and ratings on 4 November 2026.",
    "llms": "Six alternatives to Hide it Pro on iPhone (last update 11 January 2026): Safe Lock, Private Photo Vault, Keepsafe, Photo Vault, PV - Secret Photo Album, SPV. Price, how each protects the vault, languages, privacy label, version and rating on 4 November 2026.",
    "llms_note": "Photo Vault: Hide Pics Video, one of the six, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "Hide it Pro hides photos behind a lock screen and can look as if it crashed, but its iPhone app was last updated on 11 January 2026 and is in English only. All six here were updated since August 2026. For the closest match with no data collected and a fake gallery, <strong>Safe Lock</strong>. For the best-known vault with an encrypted backup, <strong>Private Photo Vault</strong>. For a vault synced across devices, <strong>Keepsafe</strong>. For no account and a backup only in your own iCloud, <strong>Photo Vault</strong>.",
        "Before you switch, export your photos from Hide it Pro (its listing names USB export and unhide to the gallery), then import them into the new vault.",
    ],
    "columns": ["App", "Price (US)", "How it protects, per listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "All six are free to download; prices are in-app purchases on each US App Store page on 4 November 2026 (pages list only some). For comparison, Hide it Pro 6.3.0 (11 January 2026): Cloud Storage $9.99 and Password Reset $4.99; English only; Data Not Linked to You; rated 4.7 from 24,796 ratings.",
    "apps": APPS,
    "who": ["<strong>Closest match, no data collected:</strong> Safe Lock.", "<strong>Best-known, encrypted backup:</strong> Private Photo Vault.", "<strong>Synced across devices:</strong> Keepsafe.",
            "<strong>No account, backup in your own iCloud:</strong> Photo Vault.", "<strong>Most features, Wi-Fi transfer:</strong> PV.", "<strong>Contacts and passwords too:</strong> SPV."],
    "cases": ["Moving your albums out of Hide it Pro: unhide them to the gallery, import them into the new vault, then delete them from Photos and from Recently Deleted.",
              "Someone asks to open the app: a fake password (Safe Lock, PV) or decoy password (Private Photo Vault) shows other photos.",
              "You also want the vault to survive a new iPhone: see " + BACKUP + "."],
    "method": ["On 4 November 2026 we read each app's US App Store page and Apple's lookup data. An app is here only if it is a photo vault updated since August 2026. We did not test how each lock holds up.",
               "Order: first the app closest to Hide it Pro, then by how widely used. See also " + CALC + " and " + HIDE + "."],
    "faq": [
        ("Is Hide it Pro still updated on iPhone?", "Its App Store page shows version 6.3.0 from 11 January 2026 and nothing newer on 4 November 2026. The app is still on sale."),
        ("What is the best alternative to Hide it Pro?", "Safe Lock is the closest, with no data collected and a fake gallery. Private Photo Vault is the best known. Photo Vault needs no account and keeps the backup in your own iCloud."),
        ("Which alternative has a fake password?", "Safe Lock (opens a fake gallery), PV (paid) and Private Photo Vault (decoy password), per their listings."),
        ("How do I move my photos out of Hide it Pro?", "Its listing names unhide to the phone gallery and USB export. Unhide them, import them into the new vault, then delete them from Photos and Recently Deleted."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("Hide it Pro (App Store)", "https://apps.apple.com/us/app/id523488488")],
}]
