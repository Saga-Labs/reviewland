"""DeepSeek alternatives for iPhone. EN. Our app: Ask AI (id1662608035), 5th of 7.
Checked 2026-11-03 (JST): iTunes lookup and US App Store pages; DeepSeek privacy policy (last updated 10 Feb 2026) says it stores
collected information on servers in the People's Republic of China (cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html).
Ask AI: listing 1.4.5; DeepSeek is one of its models. Never list GPT/OpenAI as an Ask AI feature."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
POLICY = "https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html"
CHAT = '<a href="/best-ai-chat-apps-iphone-no-account/">AI chat apps for iPhone</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, langs, labels, price, free, better, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, free, better, str(langs), labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("ChatGPT", 6448311069, "chatgpt", "OpenAI OpCo, LLC", 4.82, 11857165, "1.2026.293", "27 Oct 2026", 60, LINKED,
        "Go $8, Plus $19.99 a month; Pro $100 to $200; credits from $4", "Free tier", "Voice, image generation, photo questions",
        "the most complete all-round replacement, with voice and images.",
        ["Free, with history synced across devices, per its listing.", "Advanced Voice Mode, photo upload and an image generator."],
        "its privacy label says data is linked to you, and the bigger plans are expensive."),
    app("Claude by Anthropic", 6473753684, "claude", "Anthropic PBC", 4.72, 293374, "1.261030.19", "1 Nov 2026", 32, LINKED,
        "Pro $20 a month or $214.99 a year; Max $124.99 a month", "Free to try", "Long writing, research and code",
        "careful reasoning, long documents and code, which is what many people use DeepSeek for.",
        ["Writes, researches and codes, refining tone and structure with you, per its listing.", "Reviews and writes code at production level, its listing says."],
        "its listing does not mention making images, and its privacy label says data is linked to you."),
    app("Google Gemini", 6477489729, "gemini", "Google LLC", 4.73, 2394514, "1.2026.4262206", "29 Oct 2026", 70, LINKED,
        "Google AI Plus $4.99, Pro $19.99, Ultra $199.99 a month", "Free tier", "Google apps, Live camera, video",
        "people who live in Google apps and want a cheap paid tier.",
        ["Gemini 3.8 Flash and Gemini Omni, Gemini Live with camera and screen sharing, and a daily brief, per its listing.", "70 languages, about as many as DeepSeek's 71."],
        "its privacy label says data is linked to you, and video needs a paid plan."),
    app("Perplexity: AI Agent & Search", 1668000334, "perplexity", "Perplexity AI Inc.", 4.82, 521591, "26.43.0", "31 Oct 2026", 67, LINKED,
        "Pro $20 a month; Max $200; credits from $5", "Free app", "Answers with sources",
        "questions where you want to see the source of each answer.",
        ["Answers with sources and citations, Pro Search and Deep Research, per its listing.", "Uses top models from several companies, its listing says."],
        "it is built for search more than for long chats or writing."),
    app("All AI Models in One: Ask AI", 1662608035, "ask-ai", "Saga Ltd.", 5.0, 3, "1.4.5", "2 Nov 2026", 5, label(TRACK, LINKED, NOTLINKED),
        "Pro $49.99 a year (3-day trial); the page also lists older plans from $7.99 a week", "A few messages a day", "Several companies' models in one chat",
        "keeping DeepSeek's model next to others, such as Gemini, Claude, Grok and Perplexity Sonar, and switching in the same chat.",
        ["Pick a model, ask, and switch whenever you like in the same conversation, per its listing; DeepSeek is one of the models it names.", "Reads photos you attach and reads answers aloud; Pro adds every model, web search and a higher limit."],
        "chat only: no images, videos or files, and its privacy label includes Data Used to Track You."),
    app("Vibe by Mistral (ex-Le Chat)", 6740410176, "vibe", "MISTRAL AI", 4.76, 1346, "2.16.0", "23 Oct 2026", 10, label(LINKED, NOTLINKED),
        "Vibe Pro $14.99 a month or $149.99 a year", "Free for quick answers", "Agent for email, calendar and research",
        "a European company's assistant that also works across your email and calendar.",
        ["Formerly Le Chat. Free for quick answers and simple everyday tasks, Pro for complex work, per its listing.", "Catches up across email, chat and calendar, and runs deep research with sources."],
        "10 languages, and its listing is about work tasks more than chat."),
    app("Kimi - Your Personal AI Agent", 6474233312, "kimi", "Beijing Moonshot Technology Co., Ltd", 4.73, 5365, "3.1.7", "30 Oct 2026", 16, label(TRACK, NOTLINKED),
        "Plans from $19 to $199 on the page", "Free to download; plans listed", "Agents, coding, 3D models and games",
        "another Chinese model with agents that build things, not only chat.",
        ["Kimi K3.1 Pro, a 3D game and model maker, and an agent swarm of up to 300 agents, per its listing."],
        "it is also from a company in China, and its privacy label includes Data Used to Track You."),
]

PAGES = [{
    "group": "deepseek-alternatives", "lang": "en", "store": "us", "path": "deepseek-alternatives-iphone/", "ct": "rl-deepseek-alt", "hide_from_related": True,
    "category": "ProductivityApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best DeepSeek Alternatives for iPhone (2026)", "h1": "DeepSeek alternatives for iPhone",
    "description": "Seven alternatives to the DeepSeek app on iPhone, compared by US price, free use, privacy label and rating on 3 November 2026: ChatGPT, Claude, Gemini, Perplexity and more.",
    "llms": "Seven DeepSeek alternatives for iPhone: ChatGPT, Claude, Gemini, Perplexity, Ask AI, Vibe by Mistral, Kimi. Price, free use, privacy label, rating. DeepSeek's policy says it stores data in China.",
    "answer": [
        "DeepSeek's app is free with no in-app purchases, but its privacy policy says it stores what it collects on servers in China, and its App Store rating is 3.9. For an all-round replacement with voice and images, <strong>ChatGPT</strong>. For reasoning, long texts and code, <strong>Claude</strong>. For answers with sources, <strong>Perplexity</strong>. To keep DeepSeek's model next to others in one chat, <strong>Ask AI</strong>.",
        "All have a free way to start and sell subscriptions. If you leave DeepSeek over where your data goes, read each app's privacy label: every one here lists data linked to you or used to track you.",
    ],
    "columns": ["App", "Price (US)", "Free", "What it adds, per listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are those listed on each US App Store page on 3 November 2026; pages list only some purchases. For comparison, DeepSeek 2.7.2 (2 November 2026) is free with no in-app purchases, 71 languages, privacy label Data Linked to You, rated 3.9.",
    "apps": APPS,
    "who": ["<strong>One app for everything:</strong> ChatGPT.", "<strong>Reasoning, writing and code:</strong> Claude.", "<strong>Google apps and a cheap plan:</strong> Gemini.",
            "<strong>Answers with sources:</strong> Perplexity.", "<strong>DeepSeek's model plus others:</strong> Ask AI.", "<strong>A European company:</strong> Vibe by Mistral.", "<strong>Agents that build things:</strong> Kimi."],
    "cases": ["Math or code you used DeepSeek's reasoning for: Claude or ChatGPT, or the same question to several models in Ask AI.", "News and current facts: Perplexity, which shows its sources.", "Voice conversations: ChatGPT or Gemini Live."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data, and DeepSeek's privacy policy (last updated 10 February 2026) for where it stores data. Features come from each listing; we did not test the answers.",
               "Order: first the general assistants with the most complete free tier, then the apps for one job. For more chat apps, including ones you can use without an account, see " + CHAT + "."],
    "faq": [
        ("Why do people look for DeepSeek alternatives?", "Often for privacy: DeepSeek's policy says it stores the information it collects on servers in the People's Republic of China. Others want voice, images or sources, which its listing does not describe."),
        ("What is the best free DeepSeek alternative?", "ChatGPT and Gemini have free tiers, Perplexity is a free app, and Vibe by Mistral is free for quick answers. Ask AI gives a few free messages a day."),
        ("Can I still use DeepSeek's model in another app?", "Yes. Ask AI lists DeepSeek among its models, next to Gemini, Claude, Grok and Perplexity Sonar, in one chat."),
        ("Is Kimi like DeepSeek?", "Kimi is also from a company in China, Beijing Moonshot Technology. Its listing focuses on agents, coding and 3D creation."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("DeepSeek (App Store)", "https://apps.apple.com/us/app/id6737597349"), ("DeepSeek privacy policy", POLICY)],
}]
