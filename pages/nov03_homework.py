"""Best AI homework helper apps for iPhone. EN. Our app: Ask AI (id1662608035), placed 5th of 7: it is a general chat, not built for homework.
Checked 2026-11-03 (JST): iTunes lookup and US App Store pages. Features from each listing; nothing installed or tested.
Ask AI: listing 1.4.5 (2 Nov). Sells the yearly plan ($49.99, 3-day trial) since 23 Oct; older plans still show on the page.
Never list GPT/OpenAI as an Ask AI feature. Excluded: "Socratic AI" (BEFUN AI TECH, not Google's old Socratic), apps with under 1,000 ratings."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
CHAT = '<a href="/best-ai-chat-apps-iphone-no-account/">AI chat apps for iPhone</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, langs, labels, price, free, subjects, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, free, subjects, str(langs), labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Photomath", 919087726, "photomath", "Google LLC", 4.77, 733190, "8.47.0", "31 Aug 2026", 32, NOTLINKED,
        "Photomath Plus $5.99 to $9.99 on the page", "Step-by-step explanations at no charge", "Math only",
        "math homework you want to understand step by step, for free.",
        ["Scan a math problem and get the steps, with several methods, word-problem help and interactive graphs, per its listing.", "Basic step-by-step explanations are free; Plus adds animated tutorials and textbook solutions.", "The only app here whose privacy label is only Data Not Linked to You, and 32 languages."],
        "math only, and its last update was on 31 August 2026."),
    app("Gauth: AI Study Companion", 1542571008, "gauth", "GAUTHTECH PTE. LTD.", 4.83, 1541316, "2.11.0", "23 Oct 2026", 13, label(TRACK, LINKED),
        "Gauth Plus $11.99 a month, $31.99 a quarter or $99.99 a year (3-day trial)", "Free to download; Plus unlocks unlimited explanations", "Math, biology, physics, chemistry and more",
        "every science subject, with a voice tutor when you are stuck.",
        ["Step-by-step explanations across subjects, an AI Live Tutor by voice with a whiteboard, and human experts 24/7, per its listing.", "Quizzes, flashcards, a writing assistant and a study timer.", "The most ratings of any homework app here, about 1.5 million."],
        "the full explanations need Plus, and its privacy label includes Data Used to Track You."),
    app("Brainly: Your Personal Tutor", 745089947, "brainly", "Brainly sp. z o o", 4.72, 284276, "4.234.0", "2 Nov 2026", 10, label(TRACK, LINKED, NOTLINKED),
        "Plus $9.99 a month or $39.99 a year; Tutor $29.99 a month or $95.99 a year", "Free with limited features", "Math, science, history, English; K-12",
        "parents who want real human tutors as well as AI.",
        ["Its listing is written for parents: one-on-one help from human tutors and AI in math, reading, science and more, from kindergarten to grade 12.", "Scan a math problem for a step-by-step walkthrough.", "Brainly Tutor adds the live human tutors."],
        "the live tutors are in the $29.99-a-month plan, and the page lists Plus at several prices, from $2 a month."),
    app("Answer.AI - Your AI tutor", 6446047896, "answer-ai", "ANSWER AI LAB INC", 4.69, 166298, "2.11.3", "8 Sep 2026", 9, label(TRACK, LINKED, NOTLINKED),
        "Pro $2.99 a week, $9.99 a month, $71.90 or $99.99 a year", "Free to download; you sign up to chat", "School subjects, AP study plans",
        "high-school students who also want help with AP plans and college applications.",
        ["Step-by-step explanations, study tools and study groups, per its listing; Pro adds voice chat, AP study plans and scholarship advice.", "Says it was founded by educators."],
        "you need an account to chat, it needs iOS 18, and the free tier has ads, per its listing."),
    app("All AI Models in One: Ask AI", 1662608035, "ask-ai", "Saga Ltd.", 5.0, 3, "1.4.5", "2 Nov 2026", 5, label(TRACK, LINKED, NOTLINKED),
        "Pro $49.99 a year (3-day trial); the page also lists older plans from $7.99 a week", "A few messages a day", "Any subject, as a chat",
        "checking an answer with a second AI model, or homework that is not math.",
        ["Attach a photo of the question and ask about it, then switch to another model in the same chat to compare, per its listing; models come from several companies, such as Gemini, Claude, Grok, DeepSeek and Perplexity Sonar.",
         "Writes, rewrites, summarizes and translates, and reads any answer aloud. Pro adds every model, web search and a much higher limit."],
        "it is a general chat, not a homework solver: no math steps built for school, no textbook solutions, and it does not read files."),
    app("Solvely - AI Study Tools", 6446930976, "solvely", "Aignite Inc.", 4.77, 42344, "5.6.4", "23 Oct 2026", 14, label(TRACK, LINKED, NOTLINKED),
        "$6.99 a week, $12.99 a month, $38.99 for 6 months, $46.99 a year", "Free to download; Unlimited listed", "Math, sciences, humanities, SAT, ACT, AP",
        "turning lecture notes, PDFs and videos into quizzes as well as solving problems.",
        ["Each answer is checked by several AI models, per its listing, and you can photograph a textbook, worksheet or whiteboard.", "An AI note taker turns YouTube videos, PDFs, slides and recordings into notes, quizzes and flashcards."],
        "the in-depth explanations are in Unlimited, and the page also sells gems and vouchers."),
    app("Quizard AI: Homework Helper", 1667996582, "quizard", "Quizard AI, Inc.", 4.73, 59031, "1.20", "20 Oct 2026", 1, label(TRACK, NOTLINKED),
        "Unlimited answers $6.99 or $9.99 a week; Pro $17.99 to $19.99 a month, $29.99 to $79.99 a year", "Free to download; unlimited answers paid", "Quiz questions and math",
        "multiple-choice and short-answer questions before a quiz.",
        ["Snap a photo of a question, including math, and get the answer with an explanation, per its listing."],
        "English only, and the page lists many prices for the same plans."),
]

PAGES = [{
    "group": "homework-helpers", "lang": "en", "store": "us", "path": "best-ai-homework-helper-apps-iphone/", "ct": "rl-homework",
    "category": "EducationalApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best AI Homework Helper Apps for iPhone (2026)", "h1": "Best AI homework helper apps for iPhone",
    "description": "Seven iPhone apps that explain homework from a photo, compared by US price, what is free, subjects, privacy label and rating on the App Store on 3 November 2026.",
    "llms": "Seven AI homework helper apps for iPhone: Photomath, Gauth, Brainly, Answer.AI, Ask AI, Solvely, Quizard. Price, free tier, subjects, privacy label, rating. No accuracy test.",
    "answer": [
        "For math, <strong>Photomath</strong>: its step-by-step explanations are free and its privacy label is the lightest here. For every science subject with a voice tutor, <strong>Gauth</strong>. For real human tutors, <strong>Brainly</strong>. For homework that is not math, or to check an answer with a second AI model, a general chat such as <strong>Ask AI</strong>.",
        "All seven are free to download; the full explanations are usually paid, and several plans are weekly. Use the steps to learn the method, and check what your school allows.",
    ],
    "columns": ["App", "Price (US)", "Free", "Subjects", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are those listed on each US App Store page on 3 November 2026; pages list only some purchases and often several prices for the same plan.",
    "apps": APPS,
    "who": ["<strong>Math, free steps:</strong> Photomath.", "<strong>All sciences, voice tutor:</strong> Gauth.", "<strong>A parent who wants human tutors:</strong> Brainly.",
            "<strong>AP and college prep:</strong> Answer.AI.", "<strong>Essays, languages, history, or a second opinion:</strong> Ask AI.", "<strong>Notes and quizzes from lectures:</strong> Solvely.", "<strong>Multiple-choice practice:</strong> Quizard."],
    "cases": ["An algebra worksheet: Photomath for the steps, free.", "A chemistry question you do not understand: Gauth or Solvely, then ask why each step works.", "An answer that looks wrong: ask the same question to a second model in Ask AI, or check it in Photomath."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data. Subjects, free use and features come from each listing; we did not install the apps or test how often they are right.",
               "Order: first the apps built for homework whose listing says clearly what is free, then the general chat and the study and quiz tools. \"Socratic AI\" on the App Store is not Google's old Socratic app, so it is not here. For general chat apps, see " + CHAT + "."],
    "faq": [
        ("What is the best free homework helper app for iPhone?", "For math, Photomath: its listing says basic step-by-step explanations are free. Brainly is free with limited features, and Ask AI gives a few messages a day. The others are free to download and sell subscriptions."),
        ("Which app solves homework from a photo?", "All seven accept a photo of the question, per their listings. Photomath is for math only; Gauth, Brainly, Solvely and Quizard cover several subjects, and Ask AI answers questions about any photo you attach."),
        ("Is there a homework app with real tutors?", "Brainly Tutor ($29.99 a month) adds live human tutors, and Gauth lists human experts 24/7 next to its AI."),
        ("Are AI homework answers always right?", "No. Check the steps, not only the answer. Solvely says it cross-checks answers with several models; in Ask AI you can ask a second model yourself."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS],
}]
