"""Best AI photo enhancer apps for iPhone. EN. General topic, none of these apps is ours.
Checked 2026-11-02 (JST night): iTunes lookup and US App Store pages. Features from each listing; nothing installed or tested.
Excluded: Lensa (its listing is about editing and avatars, not enhancing)."""

DAY = "2026-11-02"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, langs, labels, price, does, best, facts, limits):
    return {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
            "row": [price, does, str(langs), labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}


APPS = [
    app("Remini - AI Photo Enhancer", 1470373330, "remini", "BENDING SPOONS OPERATIONS SPA", 4.61, 358448, "2.10.221", "10 Oct 2026", 17, label(TRACK, LINKED, NOTLINKED),
        "Lite weekly $4.99 to $7.99, Pro weekly $9.99, 1 month $9.99", "Old, blurry, scratched or low-resolution photos to HD",
        "faces in old or blurry photos, in one tap.",
        ["Its listing says it turns grainy, pixelated, damaged and low-resolution photos into clear HD, and repairs old or scratched ones.", "One of the most-rated enhancers on the App Store, about 358,000 ratings."],
        "the plans listed are weekly, and its privacy label includes Data Used to Track You."),
    app("Citrus 1 Tap Photo Enhancer AI", 1589210147, "citrus", "Wemagine.ai LLP", 4.77, 18953, "2.5.9", "17 Oct 2026", 1, label(TRACK, NOTLINKED),
        "Weekly $2.99 to $5.99, yearly $39.99 to $69.99; 3-day trial", "One-tap unblur, sharpen and denoise, kept natural",
        "a natural result with no sliders, and a free start.",
        ["Its listing says you can enhance photos for free, and Citrus Plus adds unlimited enhancements with no watermark or ads.", "Unblurs, sharpens, reduces noise and improves selfies while staying close to the original.", "A free web version is mentioned in the listing."],
        "English only, and the free tier has watermarks and ads, per the listing."),
    app("PhotoApp - AI Photo Enhancer", 1596089614, "photoapp", "SCALEUP YAZILIM HIZMETLERI ANONIM SIRKETI", 4.64, 86547, "2.9.0", "30 Oct 2026", 11, label(TRACK, NOTLINKED),
        "Weekly $4.99 to $9.99, yearly $34.99, lifetime $39.99", "Unblur, upscale, restore and colourise old photos",
        "colourising old black-and-white photos as well as sharpening them.",
        ["Unblur, restore, upscale to HD and colourise black-and-white photos, per its listing.", "Extras such as background removal and cartoon effects.", "A lifetime option at $39.99."],
        "most plans listed are weekly, and its privacy label includes Data Used to Track You."),
    app("Lightroom Photo Editor & Video", 878783582, "lightroom", "Adobe Inc.", 4.77, 339038, "11.6.21", "28 Oct 2026", 22, label(TRACK, LINKED),
        "Premium $1.99 to $9.99 a month or $19.99 to $49.99 a year; AI Photo Enhancer & Blur $49.99", "Full photo editor with one-tap Quick Actions",
        "people who also want to edit light and colour, not only sharpen.",
        ["Free photo and video editor, per its listing, with one-tap Quick Actions and Adaptive Presets to improve quality.", "The listing promises results that enhance the photo rather than change it.", "22 languages and Adobe cloud storage plans."],
        "it is an editor first, so restoring a damaged old photo takes more steps than in the one-tap apps."),
    app("Pixelup: AI Photo Enhancer App", 1589599169, "pixelup", "Codeway Dijital Hizmetler Anonim Sirketi", 4.42, 39289, "2.0.0", "4 Sep 2025", 1, label(TRACK, NOTLINKED),
        "Pro $2.99 to $29.99; lifetime $39.99", "Enhance, remove scratches, colourise and animate old photos",
        "scratched or torn prints, colourised and then animated.",
        ["Scratch removal for tears, marks and stains, then colourise and animate, per its listing.", "You can photograph an old print with the camera."],
        "its last update was in September 2025, over a year before we checked, and it is English only."),
]

PAGES = [{
    "group": "photo-enhancer", "lang": "en", "store": "us", "path": "best-ai-photo-enhancer-apps-iphone/", "ct": "rl-photo-enhancer",
    "category": "PhotoVideoApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best AI Photo Enhancer Apps for iPhone (2026)", "h1": "Best AI photo enhancer apps for iPhone",
    "description": "Five iPhone apps that sharpen blurry photos and restore old ones, compared by US price, privacy label, version and rating on the App Store on 2 November 2026.",
    "llms": "Five iPhone AI photo enhancers from the App Store: Remini, Citrus, PhotoApp, Lightroom, Pixelup. What each fixes, price, privacy label, rating. No quality test.",
    "answer": [
        "For faces in old or blurry photos, <strong>Remini</strong>, the most-rated enhancer here. For a natural one-tap fix you can start free, <strong>Citrus</strong>. To colourise black-and-white photos too, <strong>PhotoApp</strong>. To edit light and colour as well, <strong>Lightroom</strong>.",
        "Most of these sell weekly plans, so check the price before the trial ends. We did not test the results; take one blurry photo and try it in two apps.",
    ],
    "columns": ["App", "Price (US)", "What it fixes, per listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are those listed on each US App Store page on 2 November 2026; pages list only some purchases and often several prices for the same plan. All are free to download.",
    "apps": APPS,
    "who": ["<strong>Old or blurry faces:</strong> Remini.", "<strong>Natural result, free start:</strong> Citrus.", "<strong>Colourising old photos:</strong> PhotoApp.",
            "<strong>Editing beyond sharpening:</strong> Lightroom.", "<strong>Scratched prints:</strong> Pixelup."],
    "cases": ["A blurry photo from a party: Citrus or Remini.", "Grandparents' black-and-white print: photograph it, then PhotoApp or Pixelup to restore and colourise.", "A holiday photo that needs light and colour too: Lightroom."],
    "method": ["On 2 November 2026 we read each app's US App Store page and Apple's lookup data. What each app fixes comes from its listing; we did not enhance any photo or compare results.",
               "Lensa is not here because its listing is about editing and avatars rather than enhancing. Order follows how directly each listing describes enhancing photos, then the editor and the app that has not been updated in a year."],
    "faq": [
        ("What is the best free AI photo enhancer for iPhone?", "Citrus's listing says you can enhance photos for free, with ads and a watermark, and Lightroom is a free editor with paid Premium. The others offer trials or subscriptions."),
        ("Can an app fix an old damaged photo?", "Remini, PhotoApp and Pixelup say they restore old or damaged photos; Pixelup lists scratch removal, and PhotoApp and Pixelup colourise."),
        ("Do photo enhancer apps change faces?", "They can. Citrus and Lightroom say they keep results close to the original. Compare with the original before you share."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS],
}]
