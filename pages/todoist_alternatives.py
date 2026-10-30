"""Todoist alternatives for iPhone. EN. Our app: 3 Tasks (id1553693943), "3 Tasks: To Do List & Focus".

Checked 2026-10-16: iTunes lookup API + App Store web pages (US). 3 Tasks 1.2.0
(13 Oct): free; widget, repeat daily, Pro one-time purchase with history/streak/CSV/themes.
"""

CHECKED = "2026-10-16"


def src(cc):
    return [
        ("3 Tasks (App Store)", f"https://apps.apple.com/{cc}/app/id1553693943"),
        ("Todoist (App Store)", f"https://apps.apple.com/{cc}/app/id572688855"),
        ("TickTick (App Store)", f"https://apps.apple.com/{cc}/app/id626144601"),
        ("Things 3 (App Store)", f"https://apps.apple.com/{cc}/app/id904237743"),
        ("Microsoft To Do (App Store)", f"https://apps.apple.com/{cc}/app/id1212616790"),
        ("Structured (App Store)", f"https://apps.apple.com/{cc}/app/id1499198946"),
    ]


EN = {
    "group": "todoist-alternatives", "cover": "simple-todo", "lang": "en", "store": "us",
    "path": "todoist-alternatives-iphone/",
    "ct": "rl-todoist-alt",
    "category": "ProductivityApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best Todoist Alternatives for iPhone (2026)",
    "h1": "Todoist alternatives for iPhone in 2026",
    "description": "Five alternatives to Todoist on iPhone compared: TickTick, Things 3, Microsoft To Do, Structured and 3 Tasks. Prices, ratings and privacy labels.",
    "llms": "Compares Todoist with five alternatives for iPhone (TickTick, Things 3, Microsoft To Do, Structured, 3 Tasks) by price, account needs, key features and App Store privacy label.",
    "disclosure": "3 Tasks is made by Saga Labs, the company behind Reviewland. It is one more option in this list, not placed first because it is ours, and it is a deliberately tiny app, not a full Todoist replacement. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "If you want a full Todoist replacement, TickTick is the closest (free plan, Premium $4.99 a month or $49.99 a year, with habits, a calendar and a Pomodoro timer), Things 3 is the polished one-time purchase ($9.99, no subscription) and Microsoft To Do is free. If Todoist feels like too much, 3 Tasks does the opposite: three tasks a day, a timer on each, free.",
        "Todoist Pro costs $6.99 a month or $59.99 a year in the US; the free plan is still a normal Todoist account.",
    ],
    "columns": ["App", "Price (US)", "What it is best at", "Account", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the US App Store prices and in-app purchases on 16 October 2026 (an app can list several price points for the same plan). Ratings are the App Store average and number of ratings that day. \"Not stated\" means the listing does not say whether an account is needed.",
    "apps": [
        {
            "name": "3 Tasks: To Do List & Focus", "id": 1553693943, "ours": True, "anchor": "3-tasks",
            "developer": "Saga Ltd.", "rating": (5.0, 5),
            "row": ["Free; 3 Tasks Pro is a one-time purchase (listed at $4.99 and $9.99)", "Only three priorities a day, with a timer on each", "No account",
                    "Data Not Linked to You (usage data)", "1.4.3 (26 Oct 2026)", "5.0 (5 ratings)"],
            "best_for": "people who find a full task manager overwhelming and want to pick the three things that matter today.",
            "facts": [
                "Three daily priorities on one screen; a start/pause timer on every task, Pomodoro-style, that keeps counting with the screen locked.",
                "Repeat Daily for tasks you do every day, a home screen widget and dark mode, all free.",
                "Pro (one-time, no subscription): history of finished days, streaks, CSV export and four colour themes.",
                "No ads and no account. 33 languages, iOS 18 or later, 21 MB.",
            ],
            "limits": "no projects, no due dates, no reminders, no sharing and no sync between devices: it is a one-day list of three. Only 5 ratings so far.",
        },
        {
            "name": "Todoist: To Do List & Calendar", "id": 572688855, "anchor": "todoist",
            "developer": "Todoist Inc.", "rating": (4.8, 129814),
            "row": ["Free plan; Pro $6.99 a month or $59.99 a year", "Projects, natural-language dates, calendar and teams", "Yes",
                    "Data Linked to You (contact info, identifiers, usage data, user content, diagnostics)", "26.10.12 (12 Oct 2026)", "4.8 (129,814 ratings)"],
            "best_for": "the reference point: projects, recurring dates and shared work across many platforms.",
            "facts": [
                "Quick Add understands dates in plain language.",
                "Projects, calendar view and team workspaces.",
                "19 languages, iOS 17 or later, 385 MB.",
            ],
            "limits": "Pro is a subscription, and it is the least simple app in this list.",
        },
        {
            "name": "TickTick: To-Do List & Calendar", "id": 626144601, "anchor": "ticktick",
            "developer": "Appest Limited", "rating": (4.86, 46382),
            "row": ["Free; Premium $4.99 a month or $49.99 a year", "Tasks, calendar views, habits, Pomodoro timer", "Yes (cloud sync)",
                    "Data Linked to You (contact info, identifiers, user content, diagnostics); some data not linked", "8.2.22 (12 Oct 2026)", "4.9 (46,382 ratings)"],
            "best_for": "the closest feature-for-feature alternative at a lower subscription price.",
            "facts": [
                "Recurring tasks, multiple reminders, calendar views, tags, checklists and shared lists.",
                "Pomo timer and habit tracking built in; Siri support.",
                "Premium raises the limits (299 lists, 999 tasks per list and up to 5 reminders per task, per the listing).",
                "40 languages, iOS 15.5 or later, 329 MB.",
            ],
            "limits": "it is just as full-featured as Todoist, so it does not solve the problem of a list that is too big. Some features need Premium.",
        },
        {
            "name": "Things 3", "id": 904237743, "anchor": "things-3",
            "developer": "Cultured Code GmbH & Co. KG", "rating": (4.82, 28010),
            "row": ["$9.99 once for iPhone, no subscription", "Projects, areas, Today and Upcoming views with calendar events", "Not stated",
                    "Data Linked to You (user content); diagnostics not linked", "3.24.2 (22 Sep 2026)", "4.8 (28,010 ratings)"],
            "best_for": "people who prefer paying once for a polished, well-designed task manager.",
            "facts": [
                "To-dos with notes, tags and deadlines; Projects and Areas for different parts of life.",
                "Reminders, repeating to-dos and calendar integration.",
                "9 languages, iOS 16.4 or later, 124 MB.",
            ],
            "limits": "the iPhone app is a paid download up front, with no free version to try.",
        },
        {
            "name": "Microsoft To Do", "id": 1212616790, "anchor": "microsoft-to-do",
            "developer": "Microsoft Corporation", "rating": (4.72, 268633),
            "row": ["Free, no in-app purchases", "My Day plan and lists synced with Microsoft 365", "Microsoft account",
                    "Data Linked to You (contact info, location, identifiers, usage data and more)", "2.177 (6 Jul 2026)", "4.7 (268,633 ratings)"],
            "best_for": "a completely free list that works with Outlook and Microsoft 365.",
            "facts": [
                "My Day and suggestions to plan the day from all your lists.",
                "Shared lists for personal accounts; flagged Outlook emails can become tasks.",
                "34 languages, iOS 17.6 or later, 168 MB.",
            ],
            "limits": "needs a Microsoft account, and the privacy label lists the most data types of the apps here.",
        },
        {
            "name": "Structured: Daily Planner Todo", "id": 1499198946, "anchor": "structured",
            "developer": "unorderly GmbH", "rating": (4.79, 167579),
            "row": ["Free; Pro monthly (listed $2.99 to $7.99), yearly (listed $9.99 to $34.99) or lifetime $99.99", "A visual timeline of your day with tasks and calendar events", "Not stated",
                    "Data Linked to You (contact info, user content); other data not linked", "4.6.4 (29 Sep 2026)", "4.8 (167,579 ratings)"],
            "best_for": "people who think in time blocks rather than lists, including those who want a visual daily routine.",
            "facts": [
                "Drag-and-drop day timeline, an inbox, sub-tasks with notes and a Pomodoro focus timer, free.",
                "Syncs across iPhone, iPad, Apple Watch and Mac per its listing; widgets and Live Activities.",
                "Pro adds calendar and Reminders connection, recurring tasks and routines, and AI day planning.",
                "28 languages, iOS 18 or later, 291 MB.",
            ],
            "limits": "recurring tasks and calendar connection are Pro features, and Pro lists many price points including a $99.99 lifetime option.",
        },
    ],
    "who": [
        "<strong>You want the same features for less per month:</strong> TickTick.",
        "<strong>You want to pay once and never subscribe:</strong> Things 3.",
        "<strong>You want everything free and you use Outlook:</strong> Microsoft To Do.",
        "<strong>Your day is a schedule of time blocks:</strong> Structured.",
        "<strong>Your lists keep growing and you never finish them:</strong> 3 Tasks, three a day and nothing more.",
    ],
    "cases": [
        "Moving from a project-heavy Todoist setup to something with a one-time price (Things 3).",
        "A team or family sharing lists (Todoist, TickTick, Microsoft To Do).",
        "Picking the three things that must happen today before opening email (3 Tasks).",
        "Timing focused work blocks per task (TickTick's Pomodoro timer or 3 Tasks' per-task timer).",
    ],
    "method": [
        "On 16 October 2026 we opened each app's US App Store page and Apple's lookup data: price and in-app purchases, version and release date, rating and number of ratings, languages, size, minimum iOS and the privacy label. Features are the ones each developer lists on its App Store page. We did not invent ratings or reviews. iPhone's built-in Reminders app is also free and needs no extra download, but it has no App Store page to compare.",
    ],
    "faq": [
        ("What is the best free alternative to Todoist?",
         "Microsoft To Do is free with no in-app purchases. TickTick has a free plan with a capped Premium upgrade, and 3 Tasks is free if you want a much simpler list."),
        ("Is there a Todoist alternative with a one-time price?",
         "Things 3 costs $9.99 once on iPhone, with no subscription. 3 Tasks is free, with an optional one-time Pro purchase for history, streaks, CSV export and colour themes."),
        ("Which Todoist alternative is the most similar?",
         "TickTick: recurring tasks, reminders, calendar views, tags and shared lists, with a Premium subscription of $4.99 a month or $49.99 a year."),
        ("Is 3 Tasks a replacement for Todoist?",
         "No. 3 Tasks only holds three tasks per day, with a timer on each. It has no projects, reminders, due dates, sharing or sync. It suits people who want fewer tasks, not more."),
        ("Do these apps need an account?",
         "Todoist, TickTick and Microsoft To Do need one to sync. 3 Tasks needs no account."),
    ],
    "sources": src("us"),
}

from pages.store_1016 import refresh

refresh(EN, "us")

PAGES = [EN]
