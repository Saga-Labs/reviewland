"""Best apps to run open-source AI models on iPhone (2026). EN only.

Checked 2026-10-20: iTunes lookup API (US) for version, date, price, rating,
minimum iOS and size; App Store web pages for in-app purchases and privacy
labels (19-20 Oct); each app's App Store description for the model families it
lists. Pinku (ours) is listed as one more option, not first and without the
"Our app" tag, per Marta (20 Oct 2026); the transparency note is in "method".
Ranked by model choice and freshness for this question.
"""

CHECKED = "2026-10-20"
AISAGALAB = "https://aisagalab.com/blog/best-open-weight-ai-models.html"
REDITOR = "https://reditor.cloud/ollama-alternatives-mac-iphone/"

EN = {
    "group": "local-models", "cover": "ai-chat", "lang": "en", "store": "us",
    "path": "best-apps-run-open-source-ai-models-iphone/",
    "ct": "rl-local-models",
    "category": "ProductivityApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best apps to run open-source AI models on iPhone (2026): 5 compared",
    "h1": "Best apps to run open-source AI models on iPhone in 2026",
    "description": "Five iPhone apps that download open models (Gemma, Qwen, Llama, DeepSeek and more) and run them offline, compared by which models they can load, requirements, price and privacy label: PocketPal AI, Locally AI, Enclave, Pinku and Private LLM. Checked on the App Store on 20 October 2026.",
    "llms": "Compares five iPhone apps that run open-weight AI models on the device (PocketPal AI, Locally AI, Enclave, Pinku, Private LLM) by the model families each one can load, minimum iOS, price, privacy label and version date. Notes that none of their App Store descriptions lists Gemma 4 or Qwen3.5 yet.",
    "disclosure": "Pinku is made by Saga Labs, the company behind Reviewland. It is ranked on the same criteria as the others.",
    "llms_note": "Pinku, one of the five, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "To run an open model such as Gemma, Qwen or Llama on an iPhone, you need an app that downloads the model once and then answers on the phone with no server. For the widest choice, PocketPal AI loads any GGUF model from Hugging Face and its code is public. For a free, simple app with a curated list, Locally AI. On iOS 27, Enclave offers the most models in an app with optional cloud models. Pinku and Private LLM have shorter curated lists.",
        "On 20 October 2026, none of these five App Store descriptions lists the newest families, Gemma 4 or Qwen3.5. PocketPal can load them anyway if you pick a GGUF file that fits your phone's memory. Phone-sized models (about 0.4 to 5 GB) are much weaker than ChatGPT or Claude; see <a href=\"" + AISAGALAB + "\">the guide to open-weight models</a> for what each family is good at.",
    ],
    "columns": ["App", "Models it can load", "Price (US)", "Min iOS", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Model families are the ones each App Store description lists on 20 October 2026. Prices are the US App Store; all except Private LLM are free to download. Ratings are the App Store average and number of ratings that day.",
    "apps": [
        {
            "name": "PocketPal AI", "id": 6502579498, "anchor": "pocketpal", "developer": "Gooya UG", "rating": (4.07, 163),
            "row": ["Any GGUF model from Hugging Face", "Free; optional character presets from $0.99", "15.1", "Data Not Collected", "v1.19.1 (8 Oct 2026)", "4.1 (163 ratings)"],
            "best_for": "choosing any open model yourself, including new ones the day a GGUF build appears.",
            "facts": [
                "Searches and downloads GGUF models straight from Hugging Face.",
                "Open source on GitHub; also on Android.",
                "The lowest requirement here: iOS 15.1. 88 MB before models.",
            ],
            "limits": "you pick the model and its size, so it is easy to download one your iPhone cannot run well; English interface only.",
        },
        {
            "name": "Locally AI by LM Studio", "id": 6741426692, "anchor": "locally", "developer": "Element Labs", "rating": (4.71, 1804),
            "row": ["Llama 3.2, Gemma 2 and 3, Qwen 3, DeepSeek and more", "Free", "18.1", "Data Not Collected", "1.66.0 (15 Oct 2026)", "4.7 (1,804 ratings)"],
            "best_for": "a free, polished app from the LM Studio team, with image understanding.",
            "facts": [
                "Runs models with Apple's MLX; no login.",
                "Also on Mac (macOS 26 or later).",
                "Updated on 15 October 2026, the most ratings of the five.",
            ],
            "limits": "a curated list rather than any model; not sold in the Russian or Chinese App Stores.",
        },
        {
            "name": "Enclave - Local AI Assistant", "id": 6476614556, "anchor": "enclave", "developer": "Piotr Gorzelany", "rating": (4.7, 1101),
            "row": ["\"Hundreds\": Llama, DeepSeek, Gemma, Qwen, Phi, Mistral, SmolLM", "Free; Pro $9.99", "27.0", "Data Not Linked to You", "1.77.0 (1 Oct 2026)", "4.7 (1,101 ratings)"],
            "best_for": "the most features: documents, voice chat, custom assistants, and cloud models if you want them.",
            "facts": [
                "Attach PDFs, text files, images and code to a chat, processed on the device.",
                "Voice chat with on-device speech recognition.",
                "Pro adds cloud models from several providers.",
            ],
            "limits": "needs iOS 27 (iPhone 11 or later on the newest iOS); its label declares analytics and identifiers, not linked to you; cloud chats leave the device.",
        },
        {
            "name": "Pinku: Private Offline AI Chat", "id": 6754878073, "anchor": "pinku", "developer": "Saga Ltd.", "rating": (4.67, 12),
            "row": ["Gemma 3 and 3n, Llama 3.2, Qwen3, DeepSeek-R1 Distill, SmolLM3, LFM2 (12 models)", "Free; Pinku Pro in-app purchase", "18.6, Metal 3 (iPhone 12+)", "Purchase history and an anonymous user ID (for Pro); chats stay on the device", "1.0.9 (16 Oct 2026)", "4.7 (12 ratings)"],
            "best_for": "a short, tested list where the app hides models your iPhone cannot run.",
            "facts": [
                "Checks free memory before loading a model; no account.",
                "Interface in 8 languages, including Russian and Chinese; downloads from ModelScope where Hugging Face is blocked.",
                "Also on Mac with Apple silicon.",
            ],
            "limits": "12 curated models only (0.4 to 4.7 GB); larger models need Pinku Pro; no image or document input; few ratings.",
        },
        {
            "name": "Private LLM - Local AI Chat", "id": 6448106860, "anchor": "privatellm", "developer": "Numen Technologies", "rating": (4.15, 736),
            "row": ["Qwen 2.5 and 3, Llama 3.1 and 3.2, Gemma 2 and 3, Phi 4, Mistral 7B, DeepSeek R1 Distill, Yi", "$4.99 once", "17.0 (A12 or later)", "Data Not Collected", "1.9.16 (14 Sep 2026)", "4.2 (736 ratings)"],
            "best_for": "paying once, with Siri and Shortcuts, on older iPhones such as the iPhone 11.",
            "facts": [
                "Its own quantisation (OmniQuant) for each model.",
                "Family Sharing; also on Mac (macOS 14).",
                "Qwen 2.5 Coder models up to 14B.",
            ],
            "limits": "the listed families are older than the others; paid upfront; the largest app here (1.36 GB before models).",
        },
    ],
    "who": [
        "You want to try any new model the week it comes out: PocketPal AI.",
        "You want something free that just works: Locally AI.",
        "You are on iOS 27 and want documents and voice: Enclave.",
        "You want the app to choose safe sizes for your iPhone, or a Russian or Chinese interface: Pinku.",
        "You have an iPhone 11 or SE and prefer to pay once: Private LLM.",
    ],
    "cases": [
        "Chat on a plane or with no signal.",
        "Ask questions you would not send to a cloud service.",
        "Try the open models compared in <a href=\"" + AISAGALAB + "\">the guide to open-weight models</a> before running bigger ones on a computer.",
        "Use AI where ChatGPT is not offered: PocketPal, Pinku, Private LLM and Enclave are sold in Russia; PocketPal, Pinku and Private LLM in mainland China.",
    ],
    "method": [
        "We read each app's App Store page in the US on 20 October 2026: description, version, price, in-app purchases, privacy label and ratings. Model families are copied from the descriptions; we did not count models inside each app.",
        "Order: how many open models each app can load and how current its list is, then requirements and price. On a computer the equivalent tools are Ollama, LM Studio, llama.cpp and Jan; see <a href=\"" + REDITOR + "\">Ollama alternatives for Mac and iPhone</a>.",
        "Transparency: Pinku is made by Saga Labs, which runs Reviewland. It is ranked on the same criteria as the others.",
    ],
    "faq": [
        ("Can I run Gemma or Qwen on my iPhone?", "Yes. Apps such as PocketPal AI, Locally AI, Enclave, Pinku and Private LLM download an open model once and run it on the phone. Phone-sized versions (up to about 4B parameters) are the realistic choice."),
        ("Which app can run any Hugging Face model on iPhone?", "PocketPal AI loads any GGUF model from Hugging Face. The others offer curated lists."),
        ("Do these apps work offline?", "Yes, after the first model download. Enclave also has optional cloud models in Pro; those need the internet."),
        ("Is there an app that runs Gemma 4 on iPhone?", "On 20 October 2026 none of these five App Store descriptions lists Gemma 4. PocketPal can load a Gemma 4 GGUF file if one fits your phone's memory."),
    ],
    "sources": [
        ("PocketPal AI (App Store)", "https://apps.apple.com/us/app/id6502579498"),
        ("Locally AI (App Store)", "https://apps.apple.com/us/app/id6741426692"),
        ("Enclave (App Store)", "https://apps.apple.com/us/app/id6476614556"),
        ("Pinku (App Store)", "https://apps.apple.com/us/app/id6754878073"),
        ("Private LLM (App Store)", "https://apps.apple.com/us/app/id6448106860"),
        ("PocketPal AI source code", "https://github.com/a-ghorbani/pocketpal-ai"),
        ("Guide to open-weight models (aisagalab.com)", AISAGALAB),
    ],
}

PAGES = [EN]
