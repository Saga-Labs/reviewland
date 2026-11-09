"""Binaural beats apps for iPhone. EN. Our app: Drop (id1462269642), 4th of 6.
Checked 2026-11-04 (JST): iTunes lookup and US App Store pages. Criterion: the listing offers binaural beats and the app
was updated since August 2026. Drop's binaural sounds come from its code (Drop/Meditation/Models/SoundCatalog.swift, 2.14):
Delta Dreamwaves plus Alpha (10 Hz), Theta (6 Hz) and Gamma (40 Hz) over soft brown noise, all Pro; its App Store
description does not name them. Live version 2.14.1 (4 Nov 2026). Reserved in ios-playbook/references/temas-webs.md (ab4429b)."""

DAY = "2026-11-04"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
NONE = "Data Not Collected"
CALM = '<a href="/calm-alternatives-iphone/">Calm alternatives</a>'
SLEEP = '<a href="/best-free-sleep-sound-apps-iphone/">free sleep sound apps</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, waves, langs, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, waves, langs, labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Moongate: Binaural Beats", 6471041035, "moongate", "Moongate Studios, Inc.", 4.67, 60954, "3.12.0", "3 Nov 2026", label(TRACK, LINKED),
        "Premium $9.99 a month, $39.99 or $47.99 a year; $69.99", "Delta, theta, alpha, beta and gamma (40 Hz); isochronic tones; Solfeggio; white, brown, green and pink noise", "1",
        "the most complete binaural app, with control over how strong each frequency is.",
        ["Its listing says every soundscape is checked by audio analysis, and you can adjust the intensity of the active frequencies.", "Backdrop mode plays under podcasts or audiobooks; timers, favorites and playlists; the most ratings here."],
        "English only, a subscription for the full library, and its privacy label includes data used to track you."),
    app("BrainWave: 40 Binaural Series", 307219387, "brainwave", "Banzai Labs Inc.", 4.87, 11224, "11.0.2", "20 Sep 2026", NONE,
        "$5.99 once; no in-app purchases", "Multi-stage programs (sleep, focus, memory, power nap and more) and 20 pure tones", "14",
        "paying once, with no subscription and no data collected.",
        ["Its listing names multi-stage programs for sleep, focus, memory, energy, power nap and anxiety, plus 20 pure binaural frequencies.", "Runs alongside Spotify or audiobooks; its notes say it has been sold for 18 years."],
        "you pay before you can try it, and the listing shows no update since September."),
    app("Anima: Binaural Beats", 6753141187, "anima", "Mega e Limited", 4.74, 5218, "2.7.1", "24 Sep 2026", label(TRACK, LINKED, NOTLINKED),
        "Premium $9.99 or $14.99 a month, $47.99 or $59.99 a year; lifetime $129", "Delta, theta, alpha, beta and gamma; isochronic tones; Solfeggio; white, pink and brown noise", "17",
        "the same kind of library as Moongate, in 17 languages.",
        ["Its listing says each soundscape states its target frequency, with adjustable intensity and background play.", "Sound therapy for tinnitus, per its listing."],
        "the priciest lifetime plan here, and its privacy label includes data used to track you."),
    app("Sleep Sounds & Focus: Drop", 1462269642, "drop", "Saga Ltd.", 4.42, 12, "2.14.1", "4 Nov 2026", label(LINKED, NOTLINKED),
        "Free (9 sounds); Drop Pro $4.99 a month, $14.99, lifetime $9.99 to $49.99", "Delta, alpha (10 Hz), theta (6 Hz) and gamma (40 Hz), over soft brown noise", "33",
        "a few binaural tracks inside a calm, ad-free sleep and breathing app, in 33 languages.",
        ["Version 2.14 added four binaural tracks: delta for sleep, alpha, theta and gamma at 40 Hz, each a tone per ear over soft brown noise.", "Also 56 nature and noise sounds, short guided breathing, a sleep timer up to 8 hours and no ads."],
        "only four binaural tracks, all with Drop Pro, no custom frequencies and no mixer; its App Store description does not list them yet."),
    app("Binaural Beats Generator +", 1206442552, "generator", "TMSOFT", 4.72, 1193, "5.2.1", "8 Oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Free; no in-app purchases listed", "Any beat from 1 to 50 Hz on a base tone from 20 to 1500 Hz", "1",
        "making your own beat: pick the exact frequency, for free.",
        ["Its listing says you choose a binaural beat from 1 to 50 Hz and a base frequency from 20 to 1500 Hz, and play to AirPlay devices.", "From TMSOFT, the makers of the White Noise app."],
        "just a tone generator: no music, nature sounds or programs, English only, and its label includes data used to track you."),
    app("Beatfulness", 1120843229, "beatfulness", "Benjamin Araque", 4.84, 4804, "8.836.14", "29 Oct 2026", NOTLINKED,
        "Pro $1.99 a month or $19.99 a year; lifetime $99.99", "A binaural beat per session, with sacred-geometry visuals", "1",
        "the cheapest subscription here, with sessions for sleep, study and meditation.",
        ["Its listing names sessions for deep sleep, study and work, focus, learning and memory, deep relaxation and a morning boost, plus advanced pure tones.", "Privacy label Data Not Linked to You."],
        "many sessions are spiritual (chakras, astral projection), English only, and its developer's notes say updates paused for a long time."),
]

PAGES = [{
    "group": "binaural-beats", "lang": "en", "store": "us", "path": "best-binaural-beats-apps-iphone/", "ct": "rl-binaural",
    "category": "HealthApplication", "cover": "sleep-sounds", "hide_from_related": True,
    "published": DAY, "updated": "2026-11-09", "checked": DAY,
    "title": "Best Binaural Beats Apps for iPhone (2026)", "h1": "Binaural beats apps for iPhone",
    "description": "Six iPhone apps with binaural beats for sleep and focus: delta, theta, alpha and gamma. US prices, languages, privacy labels and ratings on 4 November 2026.",
    "llms": "Six binaural beats apps for iPhone: Moongate, BrainWave, Anima, Drop, Binaural Beats Generator +, Beatfulness. Price, which frequencies each offers, languages, privacy label, version and rating on 4 November 2026.",
    "llms_note": "Drop, one of the six, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "Binaural beats play a slightly different tone in each ear, so they need headphones. For the biggest library with control over each frequency, <strong>Moongate</strong>. To pay once with no data collected, <strong>BrainWave</strong> ($5.99). For a Moongate-style library in 17 languages, <strong>Anima</strong>. For a few binaural tracks inside a simple sleep and breathing app with no ads, <strong>Drop</strong>. To set the exact frequency yourself for free, <strong>Binaural Beats Generator +</strong>.",
        "We list what each app offers, not whether binaural beats work: the health claims on these pages are each developer's own.",
    ],
    "columns": ["App", "Price (US)", "Binaural beats, per listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the US App Store on 4 November 2026; BrainWave costs $5.99 to download and the rest are free with in-app purchases (pages list only some). Drop's binaural tracks are from the app itself (version 2.14), because its listing does not name them. Privacy labels rechecked on 9 November 2026.",
    "apps": APPS,
    "who": ["<strong>Biggest library, adjustable intensity:</strong> Moongate.", "<strong>Pay once, no data collected:</strong> BrainWave.", "<strong>In your language:</strong> Anima (17) or Drop (33).",
            "<strong>A few tracks in a simple sleep app:</strong> Drop.", "<strong>Your own frequency, free:</strong> Binaural Beats Generator +.", "<strong>Cheapest subscription:</strong> Beatfulness."],
    "cases": ["Falling asleep: delta or theta tracks with a sleep timer (Moongate, Anima, Drop).",
              "Studying or working: gamma at 40 Hz or beta; Moongate, BrainWave and Anima play under other apps.",
              "Only want rain or white noise, not beats: see " + SLEEP + "."],
    "method": ["On 4 November 2026 we read each app's US App Store page and Apple's lookup data, and for Drop the app's own sound list. An app is here only if it offers binaural beats and was updated since August 2026. We did not measure the frequencies or test any effect.",
               "Order: first the full binaural libraries, then the simpler apps. See also " + CALM + "."],
    "faq": [
        ("What is the best binaural beats app for iPhone?", "Moongate has the biggest library and lets you adjust each frequency. BrainWave is $5.99 once with no data collected. Binaural Beats Generator + is free if you only want a tone."),
        ("Do I need headphones for binaural beats?", "Yes. Each ear gets a slightly different tone, so the listings of these apps say to use headphones or earbuds."),
        ("Is there a free binaural beats app?", "Binaural Beats Generator + lists no purchases. Moongate, Anima, Drop and Beatfulness are free to download with paid plans; Drop's binaural tracks need Drop Pro."),
        ("Which frequency is for sleep and which for focus?", "The apps use delta (below 4 Hz) and theta for sleep, alpha for calm, and beta and gamma (40 Hz) for focus, per their listings."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS],
}]
