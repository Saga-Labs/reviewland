"""PocketPal AI alternatives for iPhone. EN. Our app: Pinku (id6754878073), 4th of 6.
Checked 2026-11-03 (JST): iTunes lookup and US App Store pages. PocketPal AI (Gooya UG, id6502579498): v1.22.0
(1 Nov 2026), 4.0 from 167 ratings, free, Data Not Collected, PocketPal Plus listed at $3.99 to $44.99, English only.
Criterion: runs open AI models on the iPhone with no internet after the download, and updated in the last 60 days.
Not on reditor (it has Private LLM, Ollama, LM Studio and offline chat pages, not PocketPal), aisagalab or doravideo.com;
reserved in ios-playbook/references/temas-webs.md (16b6e48). Pinku facts from its US listing (1.4, 31 Oct 2026)."""

DAY = "2026-11-03"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
NONE = "Data Not Collected"
OPEN = '<a href="/best-apps-run-open-source-ai-models-iphone/">apps that run open-source AI models on iPhone</a>'
NOACCOUNT = '<a href="/best-ai-chat-apps-iphone-no-account/">AI chat apps with no account</a>'
REDITOR = '<a href="https://reditor.cloud/private-llm-alternatives-iphone/">Private LLM alternatives</a>'


def app(name, i, anchor, dev, r, n, ver, date, labels, price, models, own, ios, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, models, own, ios, labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Secret AI: Local AI Chat", 6744668980, "secret-ai", "Secret AI L.L.C.", 4.5, 86, "1.12.0", "16 Sep 2026", NONE,
        "Free; Plus $4.99, Pro $9.99; lifetime $59.99 or $119.99", "Qwen3.5 VL, Gemma 4, LFM2.5 VL, gpt-oss, Llama 4, Phi 4, Mistral and more", "Yes: GGUF, MLX and MNN from Hugging Face", "17.0",
        "the closest to PocketPal: your own model files from Hugging Face, plus characters, tools and MCP.",
        ["Its listing says it downloads models straight from Hugging Face and runs GGUF (llama.cpp), MLX and MNN files.", "Custom characters, tool calling, MCP servers and Skills; can also connect to your own Ollama or LLM server.", "No account, and its privacy label says Data Not Collected; 18 languages."],
        "the listing does not say which features need Plus or Pro."),
    app("Locally AI by LM Studio", 6741426692, "locally", "Element Labs Inc", 4.7, 1903, "1.66.0", "15 Oct 2026", NONE,
        "Free (no in-app purchases)", "Llama 3.2, Gemma 2 and 3, Qwen 3, DeepSeek and more", "No, a curated list", "18.1",
        "a free, polished app from the LM Studio team that just works.",
        ["Its listing says it runs on iPhone and iPad with Apple MLX, with no login and no data collection.", "Reads images as well as text; the most-rated app here."],
        "you cannot load your own model files as in PocketPal, and the listed families are not the newest."),
    app("Enclave - Local AI Assistant", 6476614556, "enclave", "Piotr Gorzelany", 4.69, 1116, "1.77.0", "1 Oct 2026", NOTLINKED,
        "Free; Pro $9.99", "\"Hundreds\": Llama, DeepSeek, Gemma, Qwen, Phi, Mistral, SmolLM", "Yes, from a large catalog", "27.0",
        "the most models from a menu, with voice chat and optional cloud models.",
        ["Its listing says you can try hundreds of open-source models and chat offline, with no account.", "Voice chat; Pro adds cloud models from Anthropic, OpenAI, Google and xAI without API keys."],
        "needs iOS 27, and cloud chats (Pro) leave the phone."),
    app("Private Offline AI Chat: Pinku", 6754878073, "pinku", "Saga Ltd.", 4.67, 12, "1.4", "31 Oct 2026", LINKED,
        "Free with Llama 3.2 1B; Pinku Pro yearly ($16.99) or one-time", "11 models: Qwen3, Llama 3.2, Gemma 3, 3n and 4, SmolLM3, LFM2.5", "No, a curated list", "18.6",
        "not having to choose a model file: it only lists models your iPhone can run.",
        ["Its listing says it lists only the models your device has enough memory for and checks memory before loading one, so the app does not crash.", "Since 1.4 it reads PDFs (even scanned), text and Markdown files, and with Gemma 4 E2B it can see photos, all on the device.", "No account; interface in 33 languages; also on Mac."],
        "11 models only (0.4 to 4.7 GB), all but Llama 3.2 1B need Pinku Pro, and its privacy label lists purchase data linked to you (for Pro), not chats."),
    app("Private LLM - Local AI Chat", 6448106860, "private-llm", "Numen Technologies Limited", 4.15, 741, "1.9.18", "28 Oct 2026", NONE,
        "$4.99 once", "Llama 3.1 and 3.2, Gemma 2 and 3, Phi-3, Mistral 7B, Qwen 2.5 and 3 and more", "No, a curated list", "17.0",
        "paying once, with Siri and Shortcuts.",
        ["Its listing says models use its own OmniQuant quantization, and it is a one-time purchase with no subscription.", "Also on iPad and Mac."],
        "paid upfront, English only, and the listed families are older than Gemma 4 or Qwen3.5."),
    app("Liquid Apollo", 6448019325, "apollo", "Liquid AI, Inc.", 4.51, 667, "2.3.0", "2 Nov 2026", NONE,
        "Free (no in-app purchases)", "Liquid AI's LFM models on the device; any model through OpenRouter or your own server", "Your own server (LM Studio, Ollama), not files", "18.0",
        "Liquid AI's small LFM3 models on the phone, and your own home server when you need a bigger one.",
        ["Its listing says it runs smaller models on the device with LEAP and LFM3 since 2.3 (2 November 2026).", "Connects to OpenRouter with your own key, or to LM Studio or Ollama on your computer."],
        "on-device models are only Liquid AI's own; OpenRouter chats leave the phone; English only."),
]

PAGES = [{
    "group": "pocketpal-alternatives", "lang": "en", "store": "us", "path": "pocketpal-ai-alternatives-iphone/", "ct": "rl-pocketpal-alt",
    "category": "UtilitiesApplication", "cover": "ai-chat", "hide_from_related": True,
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Best PocketPal AI Alternatives for iPhone: Offline AI (2026)", "h1": "PocketPal AI alternatives for iPhone",
    "description": "Six iPhone apps that run AI models on the phone with no internet, like PocketPal AI. Models, own files, price, iOS version and privacy label on 3 November 2026.",
    "llms": "Six alternatives to PocketPal AI for running AI models offline on iPhone: Secret AI, Locally AI, Enclave, Pinku, Private LLM, Liquid Apollo. Models, whether you can load your own model files, price, minimum iOS, privacy label, version and rating on 3 November 2026.",
    "llms_note": "Pinku, one of the six, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "PocketPal AI runs open AI models on your iPhone with no internet, and you pick any GGUF file from Hugging Face. It is free and collects no data, but it is in English only, rated 4.0, and you must choose a model size your phone can handle. For the same freedom to load your own files, <strong>Secret AI</strong>. For a free app that just works, <strong>Locally AI</strong>. For the most models from a menu, on iOS 27, <strong>Enclave</strong>. For an app that only shows models your iPhone can run, <strong>Pinku</strong>. To pay once, <strong>Private LLM</strong>.",
        "All six work offline after the model download. Phone-sized models are much weaker than ChatGPT or Claude; see " + OPEN + " for what each model family is good at.",
    ],
    "columns": ["App", "Price (US)", "Models, per listing", "Load your own model files", "Min iOS", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the US App Store on 3 November 2026; all except Private LLM are free to download. For comparison, PocketPal AI v1.22.0 (1 November 2026): free, PocketPal Plus listed from $3.99 to $44.99 and character packs from $0.99, any GGUF model from Hugging Face, iOS 15.1, Data Not Collected, rated 4.0.",
    "apps": APPS,
    "who": ["<strong>Your own model files, like PocketPal:</strong> Secret AI.", "<strong>Free and simple:</strong> Locally AI.", "<strong>The biggest menu of models, on iOS 27:</strong> Enclave.",
            "<strong>No model sizes to work out, and PDFs and photos on the device:</strong> Pinku.", "<strong>Pay once, use Siri:</strong> Private LLM.", "<strong>Small models on the phone and a bigger one at home:</strong> Liquid Apollo."],
    "cases": ["Chat on a plane or with no signal: all six, after you download a model on Wi-Fi.",
              "Ask about a private PDF without uploading it: Pinku and Enclave read documents on the device, per their listings.",
              "Try a model released this week: Secret AI (Hugging Face files) or PocketPal itself; the curated apps add new models later."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data. An app is here only if its listing says it runs models on the device without internet and it was updated in the last 60 days. Model lists are copied from the descriptions; we did not test speed or quality.",
               "Order: first the apps closest to PocketPal (your own model files), then the curated ones. See also " + REDITOR + " and " + NOACCOUNT + "."],
    "faq": [
        ("What is the best alternative to PocketPal AI?", "To keep loading your own GGUF files from Hugging Face, Secret AI. For a free app with a curated list, Locally AI. For an app that hides models your iPhone cannot run, Pinku."),
        ("Is PocketPal AI free?", "Yes, it is free to download and run models; its US page also lists a PocketPal Plus purchase from $3.99 to $44.99 and character packs from $0.99 on 3 November 2026."),
        ("Which offline AI apps collect no data?", "Secret AI, Locally AI, Private LLM and Liquid Apollo show Data Not Collected on their App Store privacy labels, like PocketPal. Enclave shows Data Not Linked to You; Pinku shows Data Linked to You, for purchases."),
        ("Which ones work on an older iPhone?", "PocketPal needs iOS 15.1. Of the six, Secret AI and Private LLM need iOS 17; Enclave needs iOS 27. Small models (under 1 GB) are the realistic choice on older phones."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("PocketPal AI (App Store)", "https://apps.apple.com/us/app/id6502579498")],
}]
