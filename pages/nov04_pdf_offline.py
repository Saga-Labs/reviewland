"""Chat with a PDF offline on iPhone (AI that reads documents on the device). EN. Our app: Pinku (id6754878073), 4th of 6.
Checked 2026-11-04 (JST): iTunes lookup and US App Store pages. Criterion: the listing or its latest release notes say the
app reads PDFs or documents with models that run on the device, and it was updated in the last 60 days. Pinku's PDF
reading comes from its 1.4 release notes (31 Oct 2026); Reins' on-device models from its 2.3.3 notes. Left out:
ChatPDF (uploads the PDF; last update May 2025) and Maple Chat (encrypted cloud, not on the device). Reserved in
ios-playbook/references/temas-webs.md (224cc43)."""

DAY = "2026-11-04"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
NONE = "Data Not Collected"
POCKET = '<a href="/pocketpal-ai-alternatives-iphone/">PocketPal AI alternatives</a>'
OPEN = '<a href="/best-apps-run-open-source-ai-models-iphone/">apps that run open-source AI models on iPhone</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, files, ios, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, files, ios, labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Enclave - Local AI Assistant", 6476614556, "enclave", "Piotr Gorzelany", 4.69, 1117, "1.77.0", "1 Oct 2026", NOTLINKED,
        "Free; Pro $9.99", "PDFs, text files, images and source code", "27.0",
        "the most polished app for documents, if your iPhone runs iOS 27.",
        ["Its listing says you attach PDFs, text files, images and code, and get answers, summaries and key points, all processed on the device.", "Voice chat; hundreds of open models; the most ratings here."],
        "needs iOS 27, and its Pro cloud models send chats off the phone (you choose)."),
    app("Noema: Local AI & Offline LLM", 6751169935, "noema", "Alexandru Stamate", 4.61, 36, "4.2", "20 Oct 2026", NONE,
        "Free (no in-app purchases)", "PDFs, EPUBs and textbooks, indexed for search", "18.0",
        "long PDFs and books: answers grounded in indexed passages, for free.",
        ["Its listing says you import PDFs, EPUBs and textbooks and get answers grounded in indexed passages, offline.", "Also on iPad, Mac and Apple Vision; downloads models that fit your device."],
        "no voice or image input is named in the listing."),
    app("KernelAI - Offline AI Chat", 6757350731, "kernelai", "Anes Khadiri", 4.58, 43, "2.2.0", "15 Oct 2026", label(LINKED, NOTLINKED),
        "Free; optional tips $1.99 to $6.99", "PDF, DOCX, CSV, Markdown and text; photos and screenshots", "16.4",
        "the widest list of file types, including Word files, on older iOS.",
        ["Its listing says you ask questions about PDFs, DOCX, CSV, Markdown and text files, with on-device search and summaries.", "Checks model compatibility before you download, so you pick one that fits your iPhone or iPad."],
        "its privacy label includes data linked to you."),
    app("Private Offline AI Chat: Pinku", 6754878073, "pinku", "Saga Ltd.", 4.67, 12, "1.4", "31 Oct 2026", LINKED,
        "Free with Llama 3.2 1B; Pinku Pro $16.99 a year or one-time", "PDFs (even scanned), text and Markdown; photos with Gemma 4 E2B", "18.6",
        "reading a PDF, even a scanned one, with no setup: it only shows models your iPhone can run.",
        ["Its 1.4 release notes say it reads PDFs (even scanned ones), text and Markdown files, and with Gemma 4 E2B it can see photos; everything stays on the device.", "No account; interface in 33 languages; also on Mac."],
        "photo reading needs Gemma 4 E2B, a Pro model; only 11 curated models; its privacy label lists purchase data linked to you, not chats."),
    app("Off Grid AI - Private Local AI", 6759299882, "off-grid", "Wednesday Solutions, Inc", 3.42, 40, "0.0.120", "3 Nov 2026", NONE,
        "Free (no in-app purchases)", "Documents in Projects; receipts through the camera; voice notes", "17.0",
        "asking across several work documents at once, grouped in a Project.",
        ["Its listing says you put documents in a Project and ask about them, point the camera at a receipt, or talk instead of typing.", "No account; chats, files and photos stay on the phone."],
        "a version below 1.0 with a 3.4 rating, English only, and the listing does not name the file types."),
    app("Reins: for Ollama & LM Studio", 6739738501, "reins", "Ibrahim Cetin", 4.56, 317, "2.3.3", "21 Oct 2026", NONE,
        "Free; $6.99 a month, $39.99 a year or $99.99 lifetime", "Images, PDFs, CSVs and text files", "17.0",
        "using the same app with your home Ollama or LM Studio server for bigger documents.",
        ["Its listing says you attach images, PDFs, CSVs and text files; its 2.3.3 notes add on-device models with all of Reins' features.", "Also connects to Ollama, LM Studio or any OpenAI-compatible server."],
        "made first as a client for a home server, English only, and the listing does not say which features need a plan."),
]

PAGES = [{
    "group": "pdf-offline", "lang": "en", "store": "us", "path": "chat-with-pdf-offline-iphone/", "ct": "rl-pdf-offline",
    "category": "UtilitiesApplication", "cover": "ai-chat", "hide_from_related": True,
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Chat With a PDF Offline on iPhone: 6 Private AI Apps (2026)", "h1": "Ask AI about a PDF on iPhone without uploading it",
    "description": "Six iPhone apps whose AI reads your PDF on the phone, with no upload and no internet: Enclave, Noema, KernelAI, Pinku, Off Grid AI, Reins. Checked 4 November 2026.",
    "llms": "Six iPhone apps that read PDFs and documents with AI models running on the device, without uploading them: Enclave, Noema, KernelAI, Pinku, Off Grid AI, Reins. File types, price, minimum iOS, privacy label, version and rating on 4 November 2026.",
    "llms_note": "Pinku, one of the six, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "Most \"chat with PDF\" apps upload your file to a server. These six run the AI model on the iPhone, so a contract, a medical report or a bank letter stays on the phone and works in airplane mode. For the most polished app on iOS 27, <strong>Enclave</strong>. For long PDFs and books, free, <strong>Noema</strong>. For Word and CSV files too, <strong>KernelAI</strong>. For a scanned PDF with no setup, <strong>Pinku</strong>.",
        "Phone-sized models are small: they summarize and find passages well, but they are weaker than ChatGPT or Claude at long reasoning. See " + OPEN + " for what each model family is good at.",
    ],
    "columns": ["App", "Price (US)", "Files, per listing", "Min iOS", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the US App Store on 4 November 2026; all six are free to download. You need Wi-Fi once to download a model; after that, documents are read on the device, per each listing.",
    "apps": APPS,
    "who": ["<strong>Polished, with voice, on iOS 27:</strong> Enclave.", "<strong>Long PDFs and ebooks, free:</strong> Noema.", "<strong>Word, CSV and Markdown too:</strong> KernelAI.",
            "<strong>A scanned PDF, no setup:</strong> Pinku.", "<strong>Several documents in one project:</strong> Off Grid AI.", "<strong>Your home server for bigger models:</strong> Reins."],
    "cases": ["Summarize a contract or a lease before you sign it, without sending it anywhere.",
              "Find what a medical report or a bank letter says about one thing.",
              "Study a textbook chapter on a plane: Noema indexes PDFs and EPUBs."],
    "method": ["On 4 November 2026 we read each app's US App Store page, its latest release notes and Apple's lookup data. An app is here only if its listing or notes say it reads PDFs or documents with on-device models, and it was updated in the last 60 days. We did not test answers.",
               "Left out: ChatPDF (uploads the file, last update May 2025) and Maple Chat (end-to-end encrypted, but the AI runs in the cloud). See also " + POCKET + "."],
    "faq": [
        ("Can I chat with a PDF on iPhone without uploading it?", "Yes. Enclave, Noema, KernelAI, Pinku, Off Grid AI and Reins read documents with an AI model that runs on the iPhone, per their listings, so the file does not leave the phone."),
        ("Does it work without internet?", "Yes, after you download a model once on Wi-Fi."),
        ("Can it read a scanned PDF?", "Pinku's 1.4 release notes say it reads scanned PDFs. The other listings do not say."),
        ("Which is free?", "Noema and Off Grid AI list no purchases; KernelAI only tips. Enclave, Pinku and Reins are free to download with paid options."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("ChatPDF (App Store)", "https://apps.apple.com/us/app/id6742454061"), ("Maple Chat (App Store)", "https://apps.apple.com/us/app/id6743764835")],
}]
