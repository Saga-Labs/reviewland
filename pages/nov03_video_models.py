"""Seedance 2 Mini vs Veo 3.1 vs Kling. EN. Specs only, each with its source, read 2 Nov 2026:
BytePlus ModelArk pricing (last updated 23 Oct 2026), model list and Seedance 2.0 tutorial; Google Cloud Veo 3.1 model page
and Vertex AI pricing; Gemini API video page; Kling API pricing and Kling 2.6 text-to-video reference; doravideo.com/models.
No video was generated, nothing was paid, and there is no quality test. Prices are list prices before any discount."""

DAY = "2026-11-02"
BP_PRICE = "https://docs.byteplus.com/en/docs/modelark/model-pricing"
BP_MODELS = "https://docs.byteplus.com/en/docs/modelark/model-list"
BP_TUTORIAL = "https://docs.byteplus.com/en/docs/modelark/seedance-2-0"
VEO_DOC = "https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate"
VEO_PRICE = "https://cloud.google.com/vertex-ai/generative-ai/pricing"
GEMINI_VIDEO = "https://ai.google.dev/gemini-api/docs/video"
KLING_PRICE = "https://kling.ai/document-api/pricing/base/video"
KLING_PACKS = "https://kling.ai/dev/pricing"
KLING_DOC = "https://kling.ai/document-api/api/video/2-6/text-to-video"
DORA_MODELS = "https://doravideo.com/models"
XAI_PRICE = "https://docs.x.ai/docs/pricing"
XAI_VIDEO = "https://docs.x.ai/docs/guides/video-generation"
XAI_MODEL = "https://docs.x.ai/docs/models/grok-imagine-video-1.5"
DAY2 = "2026-11-03"
DORA_APP = "https://apps.apple.com/us/app/id6754180384?pt=118348020&ct=rl-seedance-veo-kling"
DORA = f'<a href="{DORA_APP}">Dora</a>'


def model(name, anchor, dev, url, best, facts, limits, res, length, audio, price):
    return {"name": name, "anchor": anchor, "developer": dev, "url": url, "best_for": best, "facts": facts,
            "limits": limits, "row": [res, length, audio, price, dev]}


MODELS = [
    model("Seedance 2 Mini", "seedance-2-mini", "ByteDance (BytePlus ModelArk)", BP_MODELS,
          "a low price per second with sound included, up to 15 seconds at 480p or 720p.",
          ["Output: 480p or 720p at 24 fps, 4 to 15 seconds per clip (BytePlus model list).",
           "API price: $3.5 per million tokens without input video. BytePlus's own example for a 5-second 16:9 clip works out to $0.04 per second at 480p and $0.08 per second at 720p (pricing page, last updated 23 October 2026).",
           "Tokens are counted from width × height × frame rate × seconds ÷ 1024, so a vertical or square clip costs about the same as a 16:9 one at the same resolution.",
           "Sound: BytePlus's Seedance 2.0 series tutorial covers generating video with audio for the series, including Mini, and quotes no separate audio price.",
           "Starts from text, a first frame, first and last frames, or reference images; video editing and extension are also listed."],
          "no 1080p or 4K: BytePlus lists both as not supported for Mini.",
          "480p, 720p", "4–15 s", "Yes, same price", "$0.04 (480p) · $0.08 (720p)"),
    model("Veo 3.1", "veo-3-1", "Google (Vertex AI)", VEO_DOC,
          "1080p and 4K, and the most options in Google's line-up, at the highest price of the four.",
          ["Output: 720p, 1080p or 4K at 24 fps, in 16:9 or 9:16; clips of 4, 6 or 8 seconds (Veo 3.1 model page).",
           "Price on Google's Vertex AI pricing page: $0.40 per second with audio and $0.20 without at 720p or 1080p; $0.60 and $0.40 at 4K. Google writes the unit as \"1 count\"; we read it as one second of video, which is how third-party guides quote it.",
           "Cheaper versions on the same page: Veo 3.1 Fast, $0.10 per second with audio at 720p and $0.12 at 1080p; Veo 3.1 Lite, $0.05 at 720p and $0.08 at 1080p with audio.",
           "Starts from text, an image, or first and last frames; it can extend videos and use reference images."],
          "Google says the Veo 3.1 previews in the Gemini API were shut down on 22 October 2026, and the model page lists a retirement date of \"November 17, 2026 or later\" on Vertex AI. The same page marks pay-as-you-go as not supported, with fixed quota and Provisioned Throughput instead. Prompts are listed in English only.",
          "720p, 1080p, 4K", "4, 6 or 8 s", "Optional, costs more", "$0.20–$0.40 (720p/1080p)"),
    model("Kling 2.6", "kling-2-6", "Kuaishou (Kling AI API)", KLING_DOC,
          "the cheapest 1080p of the four without sound, and 5- or 10-second clips.",
          ["Output: 720p or 1080p, in 16:9, 9:16 or 1:1; 5 or 10 seconds (Kling 2.6 text-to-video reference).",
           "Native audio is optional, and with audio only 1080p is supported.",
           "Price in units: 0.3 units per second at 720p and 0.5 at 1080p without audio; 1.0 unit per second with audio, 1.2 with a voice reference. Prepaid packages for this model start at $700 for 5,000 units ($0.14 each), so $0.042, $0.07 and $0.14 per second.",
           "Newer Kling models are listed on the same page: Kling 3.0 at 0.6 to 0.9 units per second at 720p, up to 3.0 at 4K, and Kling 4.0 at 1.0 unit per second at 720p from a separate package."],
          "the API needs a prepaid package that lasts 180 days, with no rollover, so a small test still means buying units first. Kling 2.6 tops out at 1080p and 10 seconds.",
          "720p, 1080p", "5 or 10 s", "Optional, 1080p only", "$0.042 (720p) · $0.07–$0.14 (1080p)"),
    model("Grok Imagine Video 1.5", "grok-imagine", "xAI (xAI API)", XAI_MODEL,
          "1080p up to 15 seconds with lip-synced speech, and a Lite version that is the cheapest per second here.",
          ["Output: 480p, 720p or 1080p, from text or an image, with a configurable duration of up to 15 seconds (xAI video generation guide, read 3 November 2026).",
           "Price on xAI's pricing page: $0.08 per second at 480p, $0.14 at 720p and $0.25 at 1080p, plus $0.01 per input image.",
           "Grok Imagine Video 1.5 Lite: $0.02 per second at 480p, $0.03 at 720p and $0.14 at 1080p, also up to 1080p and 15 seconds.",
           "xAI lists lip-synced speech for both, up to 14 reference images and 3 voice references for 1.5, and video editing on the older grok-imagine-video model."],
          "xAI describes the audio as lip-synced speech; its pages do not say whether music or sound effects are included or priced separately.",
          "480p, 720p, 1080p", "Up to 15 s", "Lip-synced speech", "$0.08–$0.25 (Lite $0.02–$0.14)"),
]

PAGES = [{
    "group": "video-models", "lang": "en", "store": "us", "path": "seedance-2-mini-vs-veo-3-1-vs-kling/", "ct": "rl-seedance-veo-kling",
    "category": "MultimediaApplication", "os": "Web API", "link_label": "Official documentation", "kicker": "4 models · Specs", "count_word": "models",
    "published": DAY, "updated": DAY2, "checked": DAY2, "cover": None,
    "title": "Seedance 2 Mini vs Kling vs Veo vs Grok Imagine (2026)", "h1": "Seedance 2 Mini vs Kling 2.6 vs Veo 3.1 vs Grok Imagine",
    "description": "Resolution, clip length, audio and API price per second for Seedance 2 Mini, Kling 2.6, Veo 3.1 and Grok Imagine, from each official page, and iPhone apps that use them.",
    "llms": "Spec sheet comparison of four AI video models from official pages: Seedance 2 Mini (BytePlus), Veo 3.1 (Google Vertex AI), Kling 2.6 (Kling API) and Grok Imagine Video 1.5 (xAI). Resolution, length, audio, price per second, and iPhone apps that offer each. No quality test.",
    "answer": [
        "From the official pages on 2 and 3 November 2026: <strong>Seedance 2 Mini</strong> costs $0.04 per second at 480p and $0.08 at 720p with sound included, up to 15 seconds, but stops at 720p. <strong>Veo 3.1</strong> is the only one with 4K and costs the most, $0.40 per second with audio at 720p or 1080p. <strong>Kling 2.6</strong> gives 1080p for $0.07 per second without sound, or $0.14 with it, in 5- or 10-second clips. <strong>Grok Imagine Video 1.5</strong> reaches 1080p and 15 seconds with lip-synced speech for $0.25 per second, and its Lite version is the cheapest per second here, from $0.02 at 480p.",
        "<strong>This page compares spec sheets, not results.</strong> We generated nothing and did not judge quality. Every number links to the page it came from, and prices are list prices for each official API. Veo 3.1's previews in the Gemini API closed on 22 October 2026, so check that it is still offered where you plan to use it.",
    ],
    "columns": ["Model", "Resolution", "Clip length", "Audio", "API list price per second (USD)", "Maker (API)"],
    "table_note": "Read on 2 November 2026 (Grok Imagine on 3 November). Seedance: BytePlus example for 16:9 without input video. Veo 3.1: without and with audio. Kling: at $0.14 per unit, the smallest prepaid package for these models.",
    "apps": MODELS,
    "who": [
        "<strong>The lowest cost per second:</strong> Grok Imagine Video 1.5 Lite ($0.02 at 480p), then Seedance 2 Mini ($0.04, sound included).",
        "<strong>4K, or Google's cloud:</strong> Veo 3.1, or Veo 3.1 Fast or Lite to pay less.",
        "<strong>1080p without sound for little money:</strong> Kling 2.6.",
        "<strong>Clips longer than 10 seconds:</strong> Seedance 2 Mini or Grok Imagine, up to 15 seconds.",
        "<strong>Talking characters at 1080p:</strong> Grok Imagine, with lip-synced speech; Lite for less.",
        "<strong>Seedance 2 Mini or Kling 2.6 without an API account:</strong> the " + DORA + " app and doravideo.com list both (more below).",
    ],
    "cases": [
        "An 8-second clip with sound: $0.64 on Seedance 2 Mini at 720p and $3.20 on Veo 3.1 at 720p or 1080p. Kling 2.6 has no 8-second option and only adds sound at 1080p: $0.70 for 5 seconds, $1.40 for 10.",
        "A 4K product shot: of these four, only Veo 3.1 lists 4K.",
        "A silent 1080p loop for a website: Kling 2.6 at $0.07 per second, or Veo 3.1 without audio at $0.20.",
        "An 8-second talking clip at 720p: $1.12 on Grok Imagine Video 1.5, $0.24 on its Lite version, $0.64 on Seedance 2 Mini with sound.",
    ],
    "method": [
        "On 2 November 2026 (Grok Imagine on 3 November) we read, for each model, the maker's official API documentation and pricing page, linked under Sources. Per-second prices for Seedance come from BytePlus's own worked examples; for Kling we multiplied the units per second by the unit price of the smallest package that covers these models. Resellers charge different prices, which we did not compare.",
        "We did not generate a video, pay for anything or test quality, speed or how well each follows a prompt.",
        "<strong>Where to use them on iPhone, without an API account</strong> (from each app's US App Store listing and, for Dora, its models page, on 3 November 2026): " + DORA + " lists Seedance 2 Mini (16 credits for 4 seconds at 480p, 31 for 8 seconds, 66 for 8 seconds at 720p), Kling 2.6 (photo to video only, 55 credits for 5 seconds, 110 with audio) and Grok (480p, 6 seconds, 10 credits), but not Veo. The <a href=\"https://apps.apple.com/us/app/id6738049229\">Kling AI</a> app runs Kuaishou's own Kling models. The <a href=\"https://apps.apple.com/us/app/id6670324846\">Grok</a> app has Grok Imagine. <a href=\"https://apps.apple.com/us/app/id6740024098\">Pollo AI</a> names Seedance, Veo 3.1 and Kling among its models. <a href=\"https://apps.apple.com/us/app/id1665024375\">Runway</a> names Seedance 2.5 and Kling 3 Pro, other versions than the ones above. Google's site says Gemini Omni replaced Veo in the Gemini app. Prices inside apps are in their own credits and differ from the API prices in the table.",
    ],
    "faq": [
        ("Which is cheapest: Seedance 2 Mini, Kling, Veo or Grok Imagine?", "On their official APIs, Grok Imagine Video 1.5 Lite at $0.02 per second at 480p, then Seedance 2 Mini at $0.04. With sound at 720p, Seedance 2 Mini ($0.08) is far below Veo 3.1 ($0.40). Without sound at 1080p, Kling 2.6 ($0.07) is below Veo 3.1 ($0.20), and Seedance 2 Mini has no 1080p."),
        ("Which one makes 1080p or 4K?", "Veo 3.1 lists 720p, 1080p and 4K. Kling 2.6 lists 720p and 1080p, and Grok Imagine 480p to 1080p. Seedance 2 Mini lists 480p and 720p only."),
        ("Do they generate sound?", "All four list audio. Veo 3.1 and Kling 2.6 make it optional and charge more for it; Kling 2.6 only does it at 1080p. BytePlus quotes a single price for Seedance 2 Mini, and xAI lists lip-synced speech for Grok Imagine."),
        ("How long can a clip be?", "Seedance 2 Mini 4 to 15 seconds, Grok Imagine up to 15 seconds, Veo 3.1 4, 6 or 8 seconds, Kling 2.6 5 or 10 seconds, per their API documentation."),
        ("Which iPhone apps can use these models?", "Dora lists Seedance 2 Mini, Kling 2.6 and Grok; the Kling AI app has Kling; the Grok app has Grok Imagine; Pollo AI names Seedance, Veo 3.1 and Kling. See How we checked for the details."),
        ("Which one looks best?", "We do not know, because we did not test them. Run the same short prompt on each at the same resolution before you commit."),
    ],
    "sources": [
        ("BytePlus ModelArk pricing", BP_PRICE), ("BytePlus ModelArk model list", BP_MODELS), ("BytePlus Seedance 2.0 series tutorial", BP_TUTORIAL),
        ("Google Cloud: Veo 3.1 model page", VEO_DOC), ("Google Cloud: Vertex AI pricing (Veo)", VEO_PRICE), ("Gemini API: video generation", GEMINI_VIDEO),
        ("Kling API: video pricing", KLING_PRICE), ("Kling API: packages", KLING_PACKS), ("Kling API: Kling 2.6 text to video", KLING_DOC),
        ("xAI: pricing", XAI_PRICE), ("xAI: video generation guide", XAI_VIDEO), ("xAI: Grok Imagine Video 1.5", XAI_MODEL),
        ("Dora: models and credits", DORA_MODELS), ("Kling AI (App Store)", "https://apps.apple.com/us/app/id6738049229"), ("Grok (App Store)", "https://apps.apple.com/us/app/id6670324846"),
        ("Pollo AI (App Store)", "https://apps.apple.com/us/app/id6740024098"), ("Runway (App Store)", "https://apps.apple.com/us/app/id1665024375"), ("Gemini Omni (Google)", "https://gemini.google/overview/video-generation/"), ("Dora on the App Store", "https://apps.apple.com/us/app/id6754180384"),
    ],
}]
