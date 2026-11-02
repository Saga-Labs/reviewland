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
DORA_APP = "https://apps.apple.com/us/app/id6754180384?pt=118348020&ct=rl-seedance-veo-kling"
DORA = f'<a href="{DORA_APP}">Dora</a>'


def model(name, anchor, dev, url, best, facts, limits, res, length, audio, price):
    return {"name": name, "anchor": anchor, "developer": dev, "url": url, "best_for": best, "facts": facts,
            "limits": limits, "row": [res, length, audio, price, dev]}


MODELS = [
    model("Seedance 2 Mini", "seedance-2-mini", "ByteDance (BytePlus ModelArk)", BP_MODELS,
          "the lowest price per second of the three, with sound, at 480p or 720p.",
          ["Output: 480p or 720p at 24 fps, 4 to 15 seconds per clip (BytePlus model list).",
           "API price: $3.5 per million tokens without input video. BytePlus's own example for a 5-second 16:9 clip works out to $0.04 per second at 480p and $0.08 per second at 720p (pricing page, last updated 23 October 2026).",
           "Tokens are counted from width × height × frame rate × seconds ÷ 1024, so a vertical or square clip costs about the same as a 16:9 one at the same resolution.",
           "Sound: BytePlus's Seedance 2.0 series tutorial covers generating video with audio for the series, including Mini, and quotes no separate audio price.",
           "Starts from text, a first frame, first and last frames, or reference images; video editing and extension are also listed."],
          "no 1080p or 4K: BytePlus lists both as not supported for Mini.",
          "480p, 720p", "4–15 s", "Yes, same price", "$0.04 (480p) · $0.08 (720p)"),
    model("Veo 3.1", "veo-3-1", "Google (Vertex AI)", VEO_DOC,
          "1080p and 4K, and the most options in Google's line-up, at the highest price of the three.",
          ["Output: 720p, 1080p or 4K at 24 fps, in 16:9 or 9:16; clips of 4, 6 or 8 seconds (Veo 3.1 model page).",
           "Price on Google's Vertex AI pricing page: $0.40 per second with audio and $0.20 without at 720p or 1080p; $0.60 and $0.40 at 4K. Google writes the unit as \"1 count\"; we read it as one second of video, which is how third-party guides quote it.",
           "Cheaper versions on the same page: Veo 3.1 Fast, $0.10 per second with audio at 720p and $0.12 at 1080p; Veo 3.1 Lite, $0.05 at 720p and $0.08 at 1080p with audio.",
           "Starts from text, an image, or first and last frames; it can extend videos and use reference images."],
          "Google says the Veo 3.1 previews in the Gemini API were shut down on 22 October 2026, and the model page lists a retirement date of \"November 17, 2026 or later\" on Vertex AI. The same page marks pay-as-you-go as not supported, with fixed quota and Provisioned Throughput instead. Prompts are listed in English only.",
          "720p, 1080p, 4K", "4, 6 or 8 s", "Optional, costs more", "$0.20–$0.40 (720p/1080p)"),
    model("Kling 2.6", "kling-2-6", "Kuaishou (Kling AI API)", KLING_DOC,
          "the cheapest 1080p of the three without sound, and 5- or 10-second clips.",
          ["Output: 720p or 1080p, in 16:9, 9:16 or 1:1; 5 or 10 seconds (Kling 2.6 text-to-video reference).",
           "Native audio is optional, and with audio only 1080p is supported.",
           "Price in units: 0.3 units per second at 720p and 0.5 at 1080p without audio; 1.0 unit per second with audio, 1.2 with a voice reference. Prepaid packages for this model start at $700 for 5,000 units ($0.14 each), so $0.042, $0.07 and $0.14 per second.",
           "Newer Kling models are listed on the same page: Kling 3.0 at 0.6 to 0.9 units per second at 720p, up to 3.0 at 4K, and Kling 4.0 at 1.0 unit per second at 720p from a separate package."],
          "the API needs a prepaid package that lasts 180 days, with no rollover, so a small test still means buying units first. Kling 2.6 tops out at 1080p and 10 seconds.",
          "720p, 1080p", "5 or 10 s", "Optional, 1080p only", "$0.042 (720p) · $0.07–$0.14 (1080p)"),
]

PAGES = [{
    "group": "video-models", "lang": "en", "store": "us", "path": "seedance-2-mini-vs-veo-3-1-vs-kling/", "ct": "rl-seedance-veo-kling",
    "category": "MultimediaApplication", "os": "Web API", "link_label": "Official documentation", "kicker": "3 models · Specs", "count_word": "models",
    "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Seedance 2 Mini vs Veo 3.1 vs Kling: Specs and Price", "h1": "Seedance 2 Mini vs Veo 3.1 vs Kling 2.6",
    "description": "Resolution, clip length, audio and API price per second for Seedance 2 Mini, Veo 3.1 and Kling 2.6, from each official page on 2 November 2026.",
    "llms": "Spec sheet comparison of three AI video models from official pages: Seedance 2 Mini (BytePlus), Veo 3.1 (Google Vertex AI) and Kling 2.6 (Kling API). Resolution, length, audio, price per second. No quality test.",
    "answer": [
        "From the official pages on 2 November 2026: <strong>Seedance 2 Mini</strong> is the cheapest per second ($0.04 at 480p, $0.08 at 720p, sound included) and the longest, up to 15 seconds, but stops at 720p. <strong>Veo 3.1</strong> is the only one with 4K and costs the most, $0.40 per second with audio at 720p or 1080p. <strong>Kling 2.6</strong> gives 1080p for $0.07 per second without sound, or $0.14 with it, in 5- or 10-second clips.",
        "<strong>This page compares spec sheets, not results.</strong> We generated nothing and did not judge quality. Every number links to the page it came from, and prices are list prices for each official API. Veo 3.1's previews in the Gemini API closed on 22 October 2026, so check that it is still offered where you plan to use it.",
    ],
    "columns": ["Model", "Resolution", "Clip length", "Audio", "API list price per second (USD)", "Maker (API)"],
    "table_note": "Read on 2 November 2026. Seedance: BytePlus example for 16:9 without input video. Veo 3.1: without and with audio. Kling: at $0.14 per unit, the smallest prepaid package for these models.",
    "apps": MODELS,
    "who": [
        "<strong>The lowest cost per second, with sound:</strong> Seedance 2 Mini.",
        "<strong>4K, or Google's cloud:</strong> Veo 3.1, or Veo 3.1 Fast or Lite to pay less.",
        "<strong>1080p without sound for little money:</strong> Kling 2.6.",
        "<strong>Clips longer than 10 seconds:</strong> Seedance 2 Mini, up to 15 seconds.",
        "<strong>All three without an API account:</strong> the " + DORA + " app and doravideo.com list all three models (more below).",
    ],
    "cases": [
        "An 8-second clip with sound: $0.64 on Seedance 2 Mini at 720p and $3.20 on Veo 3.1 at 720p or 1080p. Kling 2.6 has no 8-second option and only adds sound at 1080p: $0.70 for 5 seconds, $1.40 for 10.",
        "A 4K product shot: of these three, only Veo 3.1 lists 4K.",
        "A silent 1080p loop for a website: Kling 2.6 at $0.07 per second, or Veo 3.1 without audio at $0.20.",
    ],
    "method": [
        "On 2 November 2026 we read, for each model, the maker's official API documentation and pricing page, linked under Sources. Per-second prices for Seedance come from BytePlus's own worked examples; for Kling we multiplied the units per second by the unit price of the smallest package that covers these models. Resellers charge different prices, which we did not compare.",
        "We did not generate a video, pay for anything or test quality, speed or how well each follows a prompt.",
        "<strong>Where to use them without an API:</strong> " + DORA + " (iPhone app and doravideo.com) lists all three on its models page, priced in credits: Seedance 2 Mini 16 credits for 4 seconds at 480p, 31 for 8 seconds, 66 for 8 seconds at 720p; Veo 3.1 60 credits per 8-second clip; Kling 2.6 55 credits for 5 seconds, 110 with audio. That page also says that in Dora, Veo 3.1 has no audio and no 1080p, and Kling 2.6 only animates a photo (it cannot start from text). Dora has no free tier.",
    ],
    "faq": [
        ("Which is cheapest: Seedance 2 Mini, Veo 3.1 or Kling?", "On their official APIs, Seedance 2 Mini at $0.04 per second at 480p. With sound at 720p, Seedance 2 Mini ($0.08) is far below Veo 3.1 ($0.40). Without sound at 1080p, Kling 2.6 ($0.07) is below Veo 3.1 ($0.20), and Seedance 2 Mini has no 1080p."),
        ("Which one makes 1080p or 4K?", "Veo 3.1 lists 720p, 1080p and 4K. Kling 2.6 lists 720p and 1080p. Seedance 2 Mini lists 480p and 720p only."),
        ("Do they generate sound?", "All three can. Veo 3.1 and Kling 2.6 make it optional and charge more for it; Kling 2.6 only does it at 1080p. BytePlus quotes a single price for Seedance 2 Mini."),
        ("How long can a clip be?", "Seedance 2 Mini 4 to 15 seconds, Veo 3.1 4, 6 or 8 seconds, Kling 2.6 5 or 10 seconds, per their API documentation."),
        ("Which one looks best?", "We do not know, because we did not test them. Run the same short prompt on each at the same resolution before you commit."),
    ],
    "sources": [
        ("BytePlus ModelArk pricing", BP_PRICE), ("BytePlus ModelArk model list", BP_MODELS), ("BytePlus Seedance 2.0 series tutorial", BP_TUTORIAL),
        ("Google Cloud: Veo 3.1 model page", VEO_DOC), ("Google Cloud: Vertex AI pricing (Veo)", VEO_PRICE), ("Gemini API: video generation", GEMINI_VIDEO),
        ("Kling API: video pricing", KLING_PRICE), ("Kling API: packages", KLING_PACKS), ("Kling API: Kling 2.6 text to video", KLING_DOC),
        ("Dora: models and credits", DORA_MODELS), ("Dora on the App Store", "https://apps.apple.com/us/app/id6754180384"),
    ],
}]
