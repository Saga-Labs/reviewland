"""Best AI video generator apps with sound for iPhone. EN. Our app: Dora (id6754180384), 4th of 6.
Checked 2026-11-03 (JST): iTunes lookup and US App Store pages; Gemini from gemini.google/overview/video-generation (Gemini Omni,
native audio, 10 s, Google AI plan, 18+); Kling from klingai.com (Kling 4.0 "audio-visual"; the App Store listing does not mention sound).
Dora: listing 1.4.2 says "Videos with sound, on the models that support it"; default Seedance 2 Mini with sound, 31 coins for 8 s (doravideo.com/models).
Excluded: PixVerse Lite (seller AIVORA PTE. LTD.; could not confirm it is PixVerse's own app), Flashloop and VideoMax (resellers of the same models)."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
TEXT = '<a href="/best-text-to-video-ai-apps-iphone/">text-to-video apps for iPhone</a>'
MODELS = '<a href="/seedance-2-mini-vs-veo-3-1-vs-kling/">Seedance 2 Mini vs Veo 3.1 vs Kling</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, sound, length, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, sound, length, labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Grok", 6670324846, "grok", "X Corp.", 4.87, 1570441, "1.4.61", "1 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "SuperGrok Lite $10, SuperGrok $30, Plus $100, Heavy $300; extra credits $5 to $100",
        "\"Short videos with sound\", from text or a photo", "Short; length not stated",
        "a quick clip with sound inside a chat app you may already use.",
        ["Its listing says Grok Imagine creates short videos with sound and turns photos into videos.", "38 languages, and the most ratings of the video apps here after Gemini."],
        "video is one feature of a chat app, and the listing gives no length or cost per video."),
    app("Google Gemini", 6477489729, "gemini", "Google LLC", 4.73, 2394514, "1.2026.4262206", "29 Oct 2026", LINKED,
        "Google AI Plus $4.99, Pro $19.99, Ultra $199.99 a month", "Native audio with Gemini Omni, per Google's site", "Up to 10 s",
        "people who pay for a Google AI plan and want video with sound from text or up to five photos.",
        ["Its listing says Gemini Omni turns ideas into videos for Google AI Plus, Pro and Ultra users; Google's Gemini site lists native audio, 10-second videos and photo to video with up to five photos.", "Google's site says Gemini Omni replaced Veo in the Gemini app, and that you edit the video by asking in the chat.", "70 languages, and the only privacy label here without Data Used to Track You."],
        "video needs a paid Google AI plan, and Google's site says it is for users 18 and over."),
    app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 32838, "3.9.32", "2 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $10, Pro $37, Premier $92 a month; one week from $1.19; credits $1.49 to $50",
        "Kling 4.0 with sound, per Kling's site; the listing does not say", "Up to 15 s, extendable",
        "sharp clips when you want the model chosen for you, with sound on the newest model.",
        ["Kling's website presents Kling 4.0 as an audio-visual model that makes picture and sound together.", "The app makes video from text or photos; check in the model picker that the model you choose has sound."],
        "its App Store listing does not mention sound, and it is in 5 languages."),
    app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16, "1.4.2", "26 Oct 2026", label(TRACK, NOTLINKED),
        "Pro weekly $4.99 or $6.99, Pro yearly $119.99; coins $4.99 (300) to $224.99 (25,000)",
        "\"Videos with sound, on the models that support it\"", "8 s with sound for 31 coins on the default model",
        "one short clip with sound, with the coin cost shown before you tap.",
        ["Its listing says videos come with sound on the models that support it. Dora's site says the default model, Seedance 2 Mini, includes sound: 31 coins for 8 seconds, about $0.52 at the 300-coin pack price.",
         "In version 1.4.2 that default is still named \"SeeDance 1.5 Pro\" in the picker; Dora's site says those requests now run on Seedance 2 Mini.",
         "Text or a photo to video, vertical 9:16, no watermark, per its listing."],
        "short clips only, and no free video.", True),
    app("invideo: AI Video Editor", 6471394316, "invideo", "Invideo Inc", 4.55, 28028, "4.5.63", "27 Oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Plus $24 to $30, Max $72, Generative $143.99; add-on packs $12 to $60",
        "Generates voice, sound and music with 200+ AI models", "Whole edited videos",
        "a full video with voice-over, music and sound effects mixed on a timeline.",
        ["Its listing says it generates images, video, voice, sound and music with more than 200 AI models.", "A timeline editor where you balance dialogue, music and sound effects, with agents that help build the edit."],
        "English only, and the plans cost more than the single-clip apps."),
    app("Pollo AI: AI Video & Image", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.47, 13581, "4.3.1", "30 Oct 2026", label(TRACK, LINKED),
        "$5.99 a week, $99.99 a year; Lite $15 or Pro $29 a month; credits $6.99 to $164.99",
        "Multi-scene videos \"with cinematic motion and audio\"", "Depends on the model",
        "choosing among many video models, some with native audio, in one app.",
        ["Its listing names models such as Seedance, Veo 3.1, Kling, Hailuo, Vidu and PixVerse, and says you can pick one for native audio.", "Text, photo, reference and video to video, plus AI avatars and voices."],
        "English only, and the listing does not say which models have sound or what each costs."),
]

PAGES = [{
    "group": "video-sound", "lang": "en", "store": "us", "path": "best-ai-video-generator-apps-with-sound-iphone/", "ct": "rl-video-sound",
    "category": "PhotoVideoApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best AI Video Generator Apps With Sound for iPhone (2026)", "h1": "Best AI video generator apps with sound for iPhone",
    "description": "Six iPhone apps that make AI video with sound, not silent clips, compared by US price, clip length, privacy label and rating on 3 November 2026.",
    "llms": "Six iPhone AI video apps that generate video with sound: Grok, Google Gemini, Kling AI, Dora, invideo, Pollo AI. Where the sound claim comes from, price, length, privacy label, rating. No quality test.",
    "answer": [
        "Many AI videos still come out silent. These six iPhone apps say they make video with sound. For a quick clip in a chat app, <strong>Grok</strong>. If you pay for a Google AI plan, <strong>Gemini</strong> (Gemini Omni, up to 10 seconds with native audio). For a short clip with sound at a known price (about $0.52 for 8 seconds on its default model, Seedance 2 Mini), <strong>Dora</strong>. For a whole video with voice-over and music, <strong>invideo</strong>.",
        "Sound often depends on the model you pick, and some listings do not mention it at all, so check the model before you generate. Kling AI's website says Kling 4.0 makes sound; its App Store listing does not.",
    ],
    "columns": ["App", "Price (US)", "Sound, and where it is stated", "Clip length", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases on each US App Store page on 3 November 2026; pages list only some. All are free to download. Sound is quoted from the App Store listing unless the column names the maker's website.",
    "apps": APPS,
    "who": ["<strong>A clip with sound from a chat:</strong> Grok.", "<strong>You pay for Google AI:</strong> Gemini.", "<strong>Sharp clips on the newest model:</strong> Kling AI.",
            "<strong>The coin cost shown before each clip:</strong> Dora.", "<strong>Voice-over, music and editing:</strong> invideo.", "<strong>Trying many models:</strong> Pollo AI."],
    "cases": ["A pet video where you hear the dog bark: Dora, Grok or Gemini, and describe the sound in the prompt.", "A talking scene with dialogue: Gemini or Kling's newest model; write the line in quotes.", "A 30-second ad with voice-over and music: invideo."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data, and for Gemini and Kling the maker's own website, because their listings do not say whether videos have sound. We generated nothing and did not compare the sound.",
               "PixVerse Lite is not here because we could not confirm it is PixVerse's own app, and apps that only resell the same models are left out. Order: first the apps whose listing or site says plainly that video has sound, then the editor and the many-model app. For the models themselves, see " + MODELS + "; for video from text alone, see " + TEXT + "."],
    "faq": [
        ("Which AI video app makes video with sound on iPhone?", "Grok and Dora say so in their App Store listings, invideo generates voice, sound and music, and Pollo AI lists models with native audio. Gemini and Kling say so on their websites."),
        ("Is there a free AI video generator with sound?", "None of these listings promises free videos with sound. Gemini needs a Google AI plan for video, and the others sell subscriptions or credits."),
        ("How do I get sound in an AI video?", "Pick a model with audio, then describe the sound in the prompt, for example \"soft rain and a dog barking\", and put spoken lines in quotes."),
        ("How long are AI videos with sound?", "Gemini Omni makes up to 10 seconds, Dora's default model 8 seconds, and Kling up to 15 seconds per clip. Grok's listing only says short."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("Gemini Omni (Google)", "https://gemini.google/overview/video-generation/"), ("Kling AI", "https://klingai.com/global/"), ("Dora: models and coins", "https://doravideo.com/models")],
}]
