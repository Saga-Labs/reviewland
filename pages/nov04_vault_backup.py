"""Photo vault apps with a backup, so the photos survive a new iPhone. EN. Our app: Photo Vault (id1532670722), 4th of 6.
Checked 2026-11-04 (JST): iTunes lookup and US App Store pages. Criterion: the listing says where the vault can be backed
up or synced, and the app was updated in the last 12 months. Backup facts are only what each listing says; we did not
test a restore. Reserved in ios-playbook/references/temas-webs.md (c88c5f1)."""

DAY = "2026-11-04"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
NONE = "Data Not Collected"
HIDE = '<a href="/best-apps-to-hide-photos-iphone/">apps to hide photos</a>'
NODATA = '<a href="/best-photo-vault-apps-no-data-collection-iphone/">photo vaults that collect no data</a>'
CALC = '<a href="/calculator-vault-alternatives-iphone/">Calculator# alternatives</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, where, who, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, where, who, labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Private Photo Vault - Pic Safe", 417571834, "private-photo-vault", "Legendary Software Labs LLC", 4.82, 1018948, "26.0", "2 Nov 2026", label(TRACK, LINKED),
        "Premium from $6.99 to $39.99; Upgrade $39.99", "Cloud Vault: encrypted backup (paid)", "The company's cloud, locked with your own Cloud Vault password",
        "an automatic, encrypted backup from the best-known vault.",
        ["Its listing says Cloud Vault is an encrypted backup with a separate Cloud Vault password, and that its staff cannot view your photos.", "Space Saver keeps originals in the cloud; about 1 million ratings."],
        "its listing says the free version does not back up to Cloud Vault, so on the free version a lost phone means lost photos."),
    app("Secret Photo Vault: Keepsafe", 510873505, "keepsafe", "KeepSafe Software, Inc", 4.75, 385566, "13.35.0", "26 Oct 2026", label(TRACK, NOTLINKED),
        "Premium $4.99 to $35.99 (yearly $23.99, monthly $9.99)", "Private Cloud, up to 10,000 items; syncs to your other installs", "The company's cloud",
        "the same vault on several devices, synced automatically.",
        ["Its listing says Private Cloud stores up to 10,000 items and syncs to all your Keepsafe installations on any platform.", "Trash recovery for photos deleted by mistake."],
        "the cloud is Keepsafe's, and the 10,000-item limit is in the listing."),
    app("PV - Secret Photo Album", 867586326, "pv", "Haibin Jiao", 4.71, 30300, "7.7.9", "26 Oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Auto cloud backup 20 GB $12.99 or 100 GB $49.99 a year; Super Member 20 GB $29.99 or 100 GB $79.99 a year; Pro $17.99 a year", "PV cloud (paid), or Dropbox, Google Drive, Box or OneDrive with Pro", "The company's cloud, or a cloud service you choose",
        "choosing between its own cloud and Dropbox or Google Drive.",
        ["Its listing offers cloud sync for Super members and third-party cloud backup for Pro members, plus Wi-Fi transfer to a computer.", "Its listing warns that if you delete the app without a backup, the photos are gone."],
        "every backup option is paid, and the plans are many; its privacy label is the widest here."),
    app("Photo Vault: Hide Pics Video", 1532670722, "photo-vault", "Saga Ltd.", 4.17, 6, "1.3.1", "1 Nov 2026", NONE,
        "Premium $19.99 or $29.99 a year; lifetime $14.99 or $29.99", "Your own iCloud, end-to-end encrypted (Premium); or an encrypted backup file", "You: your own iCloud or a file you keep",
        "a backup only you can open, in your own iCloud, with no account.",
        ["Its listing says the optional iCloud copy is end-to-end encrypted and lives in your own iCloud; to move to a new iPhone you turn it on and restore.", "Or export the whole vault to one password-locked file in Files, on a computer or in iCloud Drive.", "The vault is left out of regular iCloud backups, per its listing; no account and no server."],
        "the iCloud copy needs Premium, and without it or an exported file there is no backup; only 6 ratings."),
    app("Converter: Hidden Photo Vault", 1536734125, "converter", "Dmitry Petrov", 4.86, 3657, "3.0.7", "2 Dec 2025", NONE,
        "One-time: Full Access $19.99 (offers at $9.99 and $14.99)", "Your own iCloud, encrypted", "You: your own iCloud",
        "your own iCloud with no subscription.",
        ["Its listing says files are encrypted and kept on the phone and in your own iCloud, opened only with your password.", "Paid once; the vault hides inside a currency converter."],
        "English only, needs iOS 18.2, and its last update was in December 2025."),
    app("Calculator# Hide Photos Videos", 1165276801, "calculator-sharp", "Salman Ashraf", 4.39, 28939, "3.4.13", "30 Oct 2026", label(TRACK, NOTLINKED),
        "Free with ads and limits; $4.99 a year", "iCloud, Dropbox, Google Drive or OneDrive", "A cloud service you choose",
        "backing up to the cloud you already use, for little money.",
        ["Its listing says you can back up locked data to iCloud, Dropbox, Google Drive or OneDrive.", "Also hides notes, passwords and contacts behind a calculator."],
        "the listing does not say whether the backup is encrypted, and the free version has ads."),
]

PAGES = [{
    "group": "vault-backup", "lang": "en", "store": "us", "path": "photo-vault-apps-with-backup-iphone/", "ct": "rl-vault-backup",
    "category": "PhotographyApplication", "cover": "hide-photos", "hide_from_related": True,
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Photo Vault Apps With Backup for a New iPhone (2026)", "h1": "Photo vault apps with a backup, so you don't lose them on a new iPhone",
    "description": "Where six iPhone photo vaults back up your hidden photos: the company's cloud, your own iCloud or Dropbox. Prices and privacy labels on 4 November 2026.",
    "llms": "Six iPhone photo vault apps compared by where the backup goes and who can open it: Private Photo Vault (Cloud Vault), Keepsafe (Private Cloud), PV (own cloud or Dropbox/Google Drive), Photo Vault (your own iCloud, end-to-end encrypted, or a file), Converter (your own iCloud), Calculator# (iCloud, Dropbox, Google Drive, OneDrive). Prices, privacy label, version and rating on 4 November 2026.",
    "llms_note": "Photo Vault: Hide Pics Video, one of the six, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "A photo vault keeps its photos inside the app, so if the app has no backup, deleting it or losing the phone can lose them. Before you switch iPhones, check where your vault backs up. For an automatic backup in the company's cloud, <strong>Private Photo Vault</strong> (Cloud Vault, paid) or <strong>Keepsafe</strong> (Private Cloud). For Dropbox or Google Drive, <strong>PV</strong> or <strong>Calculator#</strong>. For a backup in your own iCloud that only you can open, <strong>Photo Vault</strong> or <strong>Converter</strong>.",
        "In almost all of them the backup is a paid feature. Turn it on, or export the vault, before you reset or trade in the old phone.",
    ],
    "columns": ["App", "Price (US)", "Where the backup goes, per listing", "Who holds it", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "All six are free to download; prices are in-app purchases on each US App Store page on 4 November 2026 (pages list only some). Backup details are what each listing says; we did not test a restore.",
    "apps": APPS,
    "who": ["<strong>Automatic backup, best-known app:</strong> Private Photo Vault.", "<strong>The same vault on several devices:</strong> Keepsafe.", "<strong>Dropbox or Google Drive:</strong> PV or Calculator#.",
            "<strong>Your own iCloud, no account, only you can open it:</strong> Photo Vault.", "<strong>Your own iCloud, paid once:</strong> Converter."],
    "cases": ["You are getting a new iPhone next week: turn on the backup or export the vault on the old phone first, then restore on the new one.",
              "You don't want your private photos on a company's server: Photo Vault or Converter keep the copy in your own iCloud.",
              "You only need photos out of your camera roll: iOS's locked Hidden album syncs with iCloud Photos; see " + HIDE + "."],
    "method": ["On 4 November 2026 we read each app's US App Store page and Apple's lookup data. An app is here only if its listing says where the vault is backed up or synced, and it was updated in the last 12 months. We did not test a backup or a restore.",
               "Order: first the backups that run by themselves, then the ones you control. See also " + NODATA + " and " + CALC + "."],
    "faq": [
        ("Do photo vault apps back up to iCloud?", "Some do. Photo Vault and Converter keep an encrypted copy in your own iCloud, and Calculator# can back up to iCloud, Dropbox, Google Drive or OneDrive. Private Photo Vault and Keepsafe use their own cloud."),
        ("Will I lose my vault photos when I get a new iPhone?", "You can, if the vault has no backup. Turn on the app's backup or export the vault before you reset the old phone, then restore on the new one."),
        ("Is the backup free?", "Mostly not. Private Photo Vault's listing says the free version does not back up; PV's backups are paid plans; Photo Vault's iCloud copy needs Premium; Converter is a one-time purchase."),
        ("Which vault backup can only I open?", "Photo Vault's iCloud copy is end-to-end encrypted in your own iCloud, and Converter's files are encrypted in your iCloud, per their listings. Private Photo Vault's Cloud Vault uses a separate password."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("Apple: Hide photos and videos on iPhone", "https://support.apple.com/en-us/104987")],
}]
