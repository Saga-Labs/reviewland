"""Best image-to-video AI apps for iPhone. EN. Criterion: the App Store listing says it turns a photo or still image into video.
Checked 2026-11-23: Apple lookup (US) and the US App Store pages (version, rating, in-app purchases, privacy label). No quality test, nothing generated.
Dora: listing 1.4.12 says "Bring a photo to life as a short video"; plans from doravideo.com/pricing (web/lib/plans.ts, 23 Nov): Pro $6.99 a week (first week $4.99), $49.99 a year.
No coins, no cost per video, no waiting times for Dora (Marta's rules). Excluded: VideoGPT (listing is about text, not photos), resellers and apps with fewer than 10 ratings."""

DAY = "2026-11-23"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
TEXT = '<a href="/best-text-to-video-ai-apps-iphone/">text-to-video apps for iPhone</a>'
SOUND = '<a href="/best-ai-video-generator-apps-with-sound-iphone/">AI video apps with sound</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, how, langs, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, how, langs, labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 35406, "3.10.40", "23 Nov 2026", label(TRACK, LINKED),
        "Standard $10, Pro $37, Premier $92 a month; one week from $1.19; credits $5 to $100",
        "\"Turn static images into dynamic videos with a single click\"", "5",
        "turning a still image into video with a dedicated video model and a large rating base.",
        ["Its listing says you can turn text and images into videos and static images into dynamic videos in one click.", "Version 3.10.40 was released on 23 November 2026, and it has more than 35,000 ratings."],
        "only 5 languages, and its privacy label includes Data Used to Track You."),
    app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.5, 20985, "106.0.0", "20 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard $14.99 a month or $143.99 a year, Pro $35, Max $95 a month; credits $10 to $100",
        "\"Turn any photo into motion\"; \"Animation from a single still image\"", "1",
        "creators who want text, image and video-to-video tools in one app.",
        ["Its listing says \"Turn any photo into motion\" and names image to video next to text to video and video to video.", "It also makes images from a prompt or a reference photo, with consistent characters across shots."],
        "English only, and the cheapest monthly plan is the highest-priced entry point of the apps here."),
    app("Grok", 6670324846, "grok", "X Corp.", 4.87, 1632092, "1.4.66", "23 Nov 2026", label(TRACK, LINKED),
        "SuperGrok Lite $10, SuperGrok $30, Plus $100, Heavy $300 a month; extra credits $5 to $100",
        "\"Turn your photos into dynamic videos\" in Grok Imagine", "38",
        "animating a photo inside a chat app you may already have.",
        ["Its listing says Grok Imagine can create short videos with sound or turn your photos into dynamic videos.", "38 languages, and the most ratings of any app here."],
        "video is one feature of a chat app, and the listing gives no clip length."),
    app("DORA: AI Video Generator Maker", 6754180384, "dora", "Saga Ltd.", 4.33, 18, "1.4.12", "21 Nov 2026", NOTLINKED,
        "Pro $6.99 a week (first week $4.99) or $49.99 a year, per its site",
        "\"Bring a photo to life as a short video\"", "33",
        "a photo of a person, pet or product that you want animated, from a template or your own idea.",
        ["Its listing says to add a photo of yourself, a product or a pet and Dora animates it or places it in a new scene, from a template or your own prompt.", "It can also copy the moves of a dance video onto the person in your photo (Motion Control), per the listing.",
         "33 languages, and the only privacy label here that is only Data Not Linked to You. It has few ratings (18) so far."],
        "a young app with 18 ratings, and every video is paid."),
    app("Pollo AI: AI Video & Image", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.47, 13900, "4.4.1", "23 Nov 2026", label(TRACK, LINKED),
        "$5.99 a week, $99.99 a year; Lite $15 or Pro $29 a month; credits $6.99 to $164.99",
        "Lists \"Image to video\" among its tools, with many video models", "1",
        "trying several video models on the same photo in one app.",
        ["Its listing names models such as Seedance, Veo 3.1, Sora 2, Kling, Wan, Hailuo, Vidu, PixVerse, Luma and Pika.", "It adds ad, product-photo and design tools, so it reads as a marketing app more than a photo animator."],
        "English only, and the listing does not say what each model costs."),
    app("AI Picture To Video : StoryZ", 1370761595, "storyz", "Andor Communications Private Limited", 4.77, 11807, "1.5.8", "20 Nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Premium $9.99 to $69.99, weekly $4.99; credits $5.99",
        "\"Image to Video AI: upload a static image and enter a text prompt\"", "43",
        "photo-motion effects such as ripple and double exposure, plus plain image to video.",
        ["Its listing says to upload a static image and enter a text prompt for the AI to create motion.", "It also has Ripple and Motion tools that animate part of a still picture or blend it with an overlay video."],
        "an older, effect-heavy app, and its privacy label includes Data Used to Track You."),
]

PAGES = [{
    "group": "image-to-video", "lang": "en", "store": "us", "path": "best-image-to-video-ai-apps-iphone/", "ct": "rl-image-to-video",
    "category": "PhotoVideoApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best Image to Video AI Apps for iPhone (2026)", "h1": "Best image to video AI apps for iPhone",
    "description": "Six iPhone apps that turn a photo into an AI video, compared by US price, languages, privacy label and rating on 23 November 2026.",
    "llms": "Six iPhone apps that turn a photo into AI video: Kling AI, Runway, Grok, Dora, Pollo AI, StoryZ. Price, languages, privacy label, rating, where the photo claim comes from. No quality test.",
    "answer": [
        "Six iPhone apps say they turn a still photo into a video: Kling AI, Runway, Grok, Dora, Pollo AI and StoryZ. For a dedicated image-to-video app with a big rating base, <strong>Kling AI</strong> (4.67 from 35,406 ratings). To animate a photo inside a chat app, <strong>Grok</strong>. To try many models on one photo, <strong>Pollo AI</strong>. For a photo of a person, pet or product from a template, <strong>Dora</strong>.",
        "Every app here sells video through in-app subscriptions or credits, so compare the price you will pay each month, not only the download. Prices below are the US App Store lists of 23 November 2026.",
    ],
    "columns": ["App", "Price (US)", "Photo to video, where it is stated", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases on each US App Store page on 23 November 2026; pages list only some. Dora's prices come from its own site. The photo-to-video claim is quoted from the App Store listing.",
    "apps": APPS,
    "who": ["<strong>A dedicated app with a big rating base:</strong> Kling AI.", "<strong>Text, image and video-to-video tools:</strong> Runway.", "<strong>Photo to video inside a chat app:</strong> Grok.",
            "<strong>A photo of a person, pet or product, from a template:</strong> Dora.", "<strong>Many models on one photo:</strong> Pollo AI.", "<strong>Ripple and photo-motion effects:</strong> StoryZ."],
    "cases": ["A portrait you want to move: Kling AI, Runway or Dora; describe the motion in the prompt, for example a slow smile and a head turn.", "A pet photo: Dora (template or your own idea) or Grok.", "A product photo for a short ad: Pollo AI or Runway."],
    "method": ["On 23 November 2026 we read each app's US App Store page and Apple's lookup data: version, rating, in-app purchases and privacy label, and checked that the listing says photos or still images become video. We generated nothing and did not compare the quality of the videos.",
               "Left out: VideoGPT, whose listing is about text; apps that resell the same models; apps with fewer than 10 ratings. Order: first the apps whose listing says plainly that a photo becomes a video, then the broader ones. For video from words alone, see " + TEXT + "; for clips with audio, " + SOUND + "."],
    "faq": [
        ("What is the best image to video AI app for iPhone?", "It depends on what you animate. Kling AI has the most ratings among the dedicated video apps (4.67 from 35,406), Grok animates photos inside a chat app, Pollo AI offers many models, and Dora starts from a photo of a person, pet or product."),
        ("How much do image to video apps cost?", "All six sell video through in-app purchases. On 23 November 2026 the cheapest listed entry points were Kling's one-week plan from $1.19, Pollo AI's $5.99 a week, StoryZ's $4.99 a week and Dora's $6.99 a week. Monthly plans run from $10 to $95 in the other apps."),
        ("Can I animate a photo of a person or a pet?", "Kling AI, Runway, Grok, Pollo AI and StoryZ say they turn photos into video; Dora's listing names a photo of yourself, a product or a pet. Check the app's rules on faces before you upload someone else's photo."),
        ("How do I get a good image to video result?", "Start from a sharp photo with the subject clear, then describe one simple motion in the prompt, such as a slow zoom or a smile, instead of a whole scene."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [("Dora: plans", "https://doravideo.com/pricing")],
}]
