"""Poe alternatives for iPhone. EN. Our app: Ask AI (id1662608035), 4th of 5. Criterion: the listing says you can use AI models from several companies in one app.
Checked 2026-11-03 (JST): iTunes lookup and US App Store pages. Excluded: Genie (listing does not name its models), Chat AI by Niyaz Vakhpiev (same), You.com (enterprise).
aisagalab.com has a multi-model list; this page is only about leaving Poe. Never list GPT/OpenAI as an Ask AI feature."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
DEEPSEEK = '<a href="/deepseek-alternatives-iphone/">DeepSeek alternatives</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, langs, labels, price, models, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, models, str(langs), labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Perplexity: AI Agent & Search", 1668000334, "perplexity", "Perplexity AI Inc.", 4.82, 521591, "26.43.0", "31 Oct 2026", 67, LINKED,
        "Free app; Pro $20 a month; Max $200; credits from $5", "Top models from OpenAI, Anthropic, Meta and more",
        "answers with sources, using several companies' models behind one search box.",
        ["Free, with answers backed by sources and citations, per its listing.", "Pro Search and Deep Research; uses top models from several companies.", "The most ratings here, about 520,000."],
        "it is built around search, so you do not compare models side by side as in Poe."),
    app("ChatOn AI - Chat Bot Assistant", 1661308505, "chaton", "AIBY Incorporated", 4.7, 287958, "1.100", "30 Oct 2026", 19, label(TRACK, LINKED, NOTLINKED),
        "Premium $6.99 to $7.99 a week, $39.99 a year; PRO+ $59.99 a year", "GPT-5, Gemini 3.5, Claude Sonnet 5 and Sonar, per its listing",
        "writing, images and math help, with ready prompts, from several models.",
        ["Its listing names GPT-5, Gemini 3.5, Claude Sonnet 5 and Sonar.", "Over 100 ready-made prompts, image creation and photo-to-text."],
        "mostly weekly plans, and its privacy label includes Data Used to Track You."),
    app("Monica AI: Ultimate AI Assist", 6450770590, "monica", "BUTTERFLY EFFECT PTE. LTD.", 4.72, 6865, "5.14.0", "21 Jul 2026", 22, NOTLINKED,
        "Pro $4.99 a week, $9.99 a month or $99 a year; Unlimited $24.99 a month", "GPT-5.4, Claude 4.6, Gemini 3.1 Pro, Nano Banana 2 and more",
        "the longest model list, plus images and video, closest to Poe's mix.",
        ["Its listing names GPT-5.4 Pro, Claude 4.6 Sonnet and Opus, Gemini 3.1 Pro and image models such as Nano Banana 2.", "Voice mode, writing, translation and an image and video studio.", "Its privacy label is only Data Not Linked to You."],
        "its last update was on 21 July 2026, and the bigger plans cost $199 a year."),
    app("All AI Models in One: Ask AI", 1662608035, "ask-ai", "Saga Ltd.", 5.0, 3, "1.4.5", "2 Nov 2026", 5, label(TRACK, LINKED, NOTLINKED),
        "Pro $49.99 a year (3-day trial); the page also lists older plans from $7.99 a week", "Gemini, Claude, Grok, DeepSeek, Perplexity Sonar and more",
        "switching model in the middle of a conversation, as you would between Poe bots.",
        ["Pick a model, ask, and switch whenever you like in the same chat, per its listing.", "Reads photos you attach and reads answers aloud; Pro adds every model, web search and a higher limit; a few free messages a day."],
        "chat only: no images, videos, files or custom bots, and its privacy label includes Data Used to Track You."),
    app("OpenCat - AI Chat, Agent, MCP", 6445999201, "opencat", "Early Moon, LLC", 4.64, 852, "26.10.2", "15 Oct 2026", 11, NOTLINKED,
        "OpenCat Pro $9.99; Cloud AI $3.99 or $24.99; tokens $5.99", "Your own API keys, OpenCat Cloud, local models, Apple Intelligence",
        "people who already pay for API keys and want one app for all of them, on iPhone, iPad and Mac.",
        ["Its listing says you can use your own API key, its Cloud subscription, local open-source models or Apple Intelligence.", "Supports MCP and tool calls; chats are stored locally and synced through iCloud.", "An AI keyboard and system-wide translation with Pro."],
        "bringing your own keys takes setup, and it has under 1,000 ratings."),
]

PAGES = [{
    "group": "poe-alternatives", "lang": "en", "store": "us", "path": "poe-alternatives-iphone/", "ct": "rl-poe-alt", "hide_from_related": True,
    "category": "ProductivityApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best Poe Alternatives for iPhone (2026)", "h1": "Poe alternatives for iPhone",
    "description": "Five iPhone apps that, like Poe, give you AI models from several companies in one place, compared by US price, models, privacy label and rating on 3 November 2026.",
    "llms": "Five Poe alternatives for iPhone, all with models from several companies: Perplexity, ChatOn, Monica, Ask AI, OpenCat. Price, models named in the listing, privacy label, rating.",
    "answer": [
        "Poe puts many companies' models in one app, from $4.99 a month (Basic) to $19.99 (Plus). These five do the same in their own way. For answers with sources, <strong>Perplexity</strong>, which is free. For the longest model list plus images and video, <strong>Monica</strong>. To switch model in the middle of a chat, <strong>Ask AI</strong>. To use your own API keys, <strong>OpenCat</strong>.",
        "Poe's App Store listing still names older models such as o3, GPT-4.5 and Claude 3.7 Sonnet. Check which models each app lists today, and whether you want custom bots, which only Poe offers here.",
    ],
    "columns": ["App", "Price (US)", "Models, per listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are those listed on each US App Store page on 3 November 2026; pages list only some purchases. For comparison, Poe 6.1.0 (5 October 2026): Basic $4.99 a month or $49.99 a year, $19.99 a month or $199.99 a year, privacy label Data Linked to You, rated 4.7 from 53,842 ratings.",
    "apps": APPS,
    "who": ["<strong>Answers with sources:</strong> Perplexity.", "<strong>Ready prompts for writing:</strong> ChatOn.", "<strong>The most models, plus images:</strong> Monica.",
            "<strong>Switching model mid-chat:</strong> Ask AI.", "<strong>Your own API keys:</strong> OpenCat."],
    "cases": ["Comparing two answers to the same question: Ask AI, switching model in the chat, or Monica.", "Research with links you can check: Perplexity.", "Using a Claude or Gemini key you already pay for: OpenCat."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data. An app is here only if its listing says it gives access to models from several companies; Genie and Chat AI are left out because their listings do not name their models. We did not test the answers.",
               "Order: first the apps with the most users and the clearest free option, then the ones for one way of working. See also " + DEEPSEEK + "."],
    "faq": [
        ("What is the best free alternative to Poe?", "Perplexity is a free app that uses several companies' models. Ask AI gives a few free messages a day, and OpenCat works with your own API keys."),
        ("Which app lets me compare AI models like Poe?", "Ask AI lets you switch model in the same conversation, per its listing; Monica lists the most models in one app."),
        ("Is there a Poe alternative with custom bots?", "None of these five listings describes building custom bots the way Poe does."),
        ("Which is the most private?", "Monica and OpenCat have privacy labels with only Data Not Linked to You, and OpenCat stores chats on the device and in your iCloud, per its listing."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [("Poe (App Store)", "https://apps.apple.com/us/app/id1640745955")],
}]
