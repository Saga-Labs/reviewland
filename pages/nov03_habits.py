"""Best habit tracker apps for iPhone. EN. General topic, none of these apps is ours.
Checked 2026-11-02 (JST night): iTunes lookup and US App Store pages. Features from each listing; nothing installed or tested."""

DAY = "2026-11-02"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, langs, labels, price, free, best, facts, limits):
    return {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
            "row": [price, free, str(langs), labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}


APPS = [
    app("Streaks", 963034692, "streaks", "Crunchy Bagel Pty Ltd", 4.81, 27354, "11.5.3", "1 Nov 2026", 28, NOTLINKED,
        "$5.99 once; no in-app purchases listed", "Paid app; everything included",
        "paying once and keeping habits on every Apple device.",
        ["Up to 24 habits, each daily, on set days, a few times a week or every few days, per its listing.", "Completes some habits on its own from Apple Health and Screen Time, and has interactive widgets and a full Apple Watch app.", "No account: habits stay on the device and sync through your own iCloud. Apple Design Award winner."],
        "it costs $5.99 before you can try it, and it caps you at 24 habits."),
    app("Habit Tracker - HabitKit", 6443918070, "habitkit", "Sebastian Roehl", 4.84, 2528, "1.19.0", "27 Oct 2026", 17, label(LINKED, NOTLINKED),
        "Pro $1.99 a month, $11.99 a year or $29.99 lifetime (prices vary on the page)", "Up to 4 habits free",
        "seeing your streak as a grid of coloured tiles, with no account.",
        ["Free with up to four habits, including streaks, calendar, notes, reminders and backups, per its listing.", "No account; data stays on the device and it works offline.", "Pro adds unlimited habits, charts, widgets and up to three reminders per habit."],
        "widgets and charts need Pro, and the page lists several Pro prices from $0.99 to $59.99."),
    app("Habit Tracker", 1438388363, "habit-tracker", "Inner Grow Limited", 4.79, 148466, "2.15.10", "30 Oct 2026", 11, NOTLINKED,
        "Premium $4.99 a month or $7.99 a year; lifetime $19.99", "Free to download; premium listed",
        "a free start with Apple Health tracking and habits you share with others.",
        ["Syncs water, steps, sleep, exercise and calories with Apple Health, per its listing.", "Build habits or quit them, with goals in units such as minutes or glasses, not just checkmarks.", "Group habits and a focus timer with natural sounds. The most ratings of the dedicated trackers here."],
        "the listing does not say what is free and what needs premium."),
    app("Habitify: Habit Tracker", 1111447047, "habitify", "Unstatic Ltd Co", 4.59, 7161, "51.1.0", "27 Oct 2026", 40, NOTLINKED,
        "Pro $8.99 a month, $49.99 a year, $119.99 lifetime; family plans", "Free tier; Plus and Pro unlock more",
        "logging habits from an AI assistant or Siri, across iPhone, Mac and Watch.",
        ["Its listing says you can log habits and ask for your stats by chatting with an AI assistant, through its API, MCP, App Intents and Siri.", "Syncs across iPhone, iPad, Mac and Apple Watch, in 40 languages.", "Habitify Plus unlocks unlimited habits and smart reminders; Pro has a 7-day free trial."],
        "the free tier has a habit limit, and Pro costs $49.99 a year."),
    app("Atoms - from Atomic Habits", 6474421906, "atoms", "Atomic Development Inc.", 4.83, 10769, "3.5.0", "16 Feb 2026", 1, label(LINKED, NOTLINKED),
        "Atoms Pro $4.99 a month or $39.99 a year", "Free to download; Pro listed",
        "readers of Atomic Habits who want short lessons next to the tracker.",
        ["The official app of James Clear's book, per its listing, with bite-sized lessons on the book's ideas.", "Five minutes a day is its suggested routine, and it has an Apple Watch app."],
        "English only, and its last update was in February 2026."),
    app("Finch: Self-Care Pet", 1528595748, "finch", "Finch Care Public Benefit Corporation", 4.95, 770720, "3.73.233", "29 Oct 2026", 1, label(LINKED, NOTLINKED),
        "Finch Plus from $5.99 to $69.99 on the page; Guardian Program $7.99", "Free to download; Finch Plus listed",
        "small self-care habits when a plain checklist does not keep you going.",
        ["You grow a pet by doing quick self-care exercises, per its listing.", "The highest rating here, 4.95 from about 770,000 ratings."],
        "it is a self-care app more than a habit tracker, and it is English only."),
    app("Productive - Habit Tracker", 983826477, "productive", "Mosaic S.r.l.", 4.6, 91062, "3.26.39", "19 Mar 2026", 19, label(TRACK, LINKED, NOTLINKED),
        "Premium $10.99 a month; yearly from $19.99 to $79.99 on the page", "Free to download; premium listed",
        "guided programs and challenges with other users.",
        ["Habits you can pause or stop, notes, programs with daily tips, and challenges, per its listing."],
        "the only app here whose privacy label includes Data Used to Track You, and the yearly price varies a lot on the page."),
]

PAGES = [{
    "group": "habit-trackers", "lang": "en", "store": "us", "path": "best-habit-tracker-apps-iphone/", "ct": "rl-habit-trackers",
    "category": "HealthApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best Habit Tracker Apps for iPhone (2026)", "h1": "Best habit tracker apps for iPhone",
    "description": "Seven habit trackers for iPhone compared by US price, what is free, privacy label, version and rating on the App Store on 2 November 2026: Streaks, HabitKit, Habitify and more.",
    "llms": "Seven iPhone habit trackers compared from the App Store: Streaks, HabitKit, Habit Tracker, Habitify, Atoms, Finch, Productive. Price, free tier, privacy label, rating.",
    "answer": [
        "To pay once and be done, <strong>Streaks</strong> ($5.99, no subscription, synced through your own iCloud). To start free with no account, <strong>HabitKit</strong>, free for up to four habits. For Apple Health and habits shared with friends, <strong>Habit Tracker</strong> by Inner Grow. To log habits from Siri or an AI assistant, <strong>Habitify</strong>.",
        "Readers of Atomic Habits have <strong>Atoms</strong>, and <strong>Finch</strong> turns self-care into looking after a pet. All except Streaks are free to download and sell a subscription; only Productive's privacy label says it may track you.",
    ],
    "columns": ["App", "Price (US)", "Free", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are those listed on each US App Store page on 2 November 2026; pages list only some purchases, and some show several prices for the same plan. Ratings are that day's App Store average and count.",
    "apps": APPS,
    "who": ["<strong>Pay once, all Apple devices:</strong> Streaks.", "<strong>Free and no account:</strong> HabitKit.", "<strong>Apple Health and group habits:</strong> Habit Tracker.",
            "<strong>Siri or an AI assistant:</strong> Habitify.", "<strong>Learning the method:</strong> Atoms.", "<strong>Gentle self-care:</strong> Finch.", "<strong>Programs and challenges:</strong> Productive."],
    "cases": ["Drinking more water: Habit Tracker or Streaks read it from Apple Health.", "Quitting a bad habit: Streaks and Habit Tracker both list negative habits.", "Three habits and no subscription: HabitKit's free tier or Streaks."],
    "method": ["On 2 November 2026 we read each app's US App Store page and Apple's lookup data. Features, free limits and sync come from each listing; we did not install or test the apps.",
               "Order: first the apps whose listing is clearest about what you get and what it costs, then the ones built around lessons, a pet or programs. It is not a quality score."],
    "faq": [
        ("What is the best free habit tracker for iPhone?", "HabitKit is free for up to four habits with no account, per its listing. Habit Tracker and Habitify are free to download with paid tiers; their listings do not give the free limit in numbers."),
        ("Is there a habit tracker without a subscription?", "Streaks costs $5.99 once and lists no in-app purchases. HabitKit and Habitify also sell lifetime options."),
        ("Which habit tracker works with Apple Health?", "Streaks and Habit Tracker say they read Apple Health; Streaks also uses Screen Time."),
        ("Which ones work on Apple Watch?", "Streaks, Habitify and Atoms list an Apple Watch app."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS],
}]
