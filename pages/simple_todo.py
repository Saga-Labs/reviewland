"""Best simple to-do list apps for iPhone. EN + ES. Our app: 3 Tasks (id1553693943).

Checked 2026-10-11: iTunes lookup API and App Store web pages (US for EN,
Spain for ES). 3 Tasks 1.1.2 is free with no in-app purchases (Pro is not
released yet; when it ships, update price and features here).
"""

CHECKED = "2026-10-11"


def src(cc, extra=False):
    base = [
        ("3 Tasks (App Store)", f"https://apps.apple.com/{cc}/app/id1553693943"),
        ("Do! (App Store)", f"https://apps.apple.com/{cc}/app/id421819675"),
        ("MinimaList (App Store)", f"https://apps.apple.com/{cc}/app/id993066159"),
        ("Clear (App Store)", f"https://apps.apple.com/{cc}/app/id493136154"),
        ("Microsoft To Do (App Store)", f"https://apps.apple.com/{cc}/app/id1212616790"),
        ("Todoist (App Store)", f"https://apps.apple.com/{cc}/app/id572688855"),
    ]
    if extra:
        base += [("TickTick (App Store)", f"https://apps.apple.com/{cc}/app/id626144601"),
                 ("Things 3 (App Store)", f"https://apps.apple.com/{cc}/app/id904237743")]
    return base


EN = {
    "group": "simple-todo", "lang": "en", "store": "us",
    "path": "best-simple-to-do-list-apps-iphone/",
    "ct": "rl-simple-todo",
    "category": "ProductivityApplication",
    "published": "2026-10-11", "updated": "2026-11-10", "checked": "2026-11-10",
    "title": "Best Free To-Do List App for iPhone: No Paywall, No Lost Tasks (2026)",
    "h1": "Best Free To-Do List App for iPhone: No Paywall, No Lost Tasks (2026)",
    "description": "The best free to-do list apps for iPhone, and the fix for what 1-2 star reviews complain about most: crashes, tasks that vanish, reminders that never fire, paywalls. Checked 10 November 2026.",
    "llms": "Answers the most common 1-2 star complaints about to-do apps (crashes, lost tasks, reminders, paywalls, widgets) and compares eight to-do list apps for iPhone (Things 3, TickTick, 3 Tasks, Do!, MinimaList, Clear, Microsoft To Do, Todoist) by price, whether they need an account, reminders and widgets, and privacy label.",
    "answer": [
        "The best free to-do list app for iPhone is Microsoft To Do: free, no in-app purchases, and it syncs through a Microsoft account. If you are searching because your current app crashes, loses tasks or put its features behind a subscription, pick a simpler app that keeps the list on your phone: 3 Tasks (free, no account, three tasks a day) or Things 3 ($9.99 once). If reminders are what fail, check iOS first: Settings > Notifications, then your Focus settings.",
        "Below are the five complaints that repeat most in 1-2 star reviews of eight to-do apps, each with its fix. Todoist is the most complete app of the eight, but its Pro plan is a subscription ($6.99 a month or $59.99 a year in the US, checked 10 November 2026).",
    ],
    "cta": {
        "line": "3 Tasks is free, needs no account and keeps its list on your phone, so there is no sync to break and no subscription to cancel (its Pro is an optional one-time purchase). It has no reminders; for a free list that syncs, Microsoft To Do needs no purchase.",
        "buttons": [("Download 3 Tasks (free)", 1553693943), ("Download Microsoft To Do (free)", 1212616790)],
    },
    "complaints": [
        {"id": "crashes", "h2": "\"Crashes every time I open it\": 158 of 775 low reviews", "body": [
            "We read 775 one- and two-star US App Store reviews of the eight apps below (taken from the latest 500 reviews of each). 158 of them are about crashes, freezing or an app that stopped working after an update. Typical wording: \"crashes every time I open it\" (Do!, 1 star) and \"always crashes without an error message\" (Microsoft To Do, 1 star).",
            "The fix: update the app and iOS first. Then, before deleting anything, make sure the list is somewhere else (open it on another device or on the web). If it still crashes, use Settings > General > iPhone Storage > the app > Offload App, which removes the app but keeps its data, and reinstall. If it keeps happening, the cause is usually size: an app with fewer parts has fewer things to break, which is why 3 Tasks (one screen, no account) and Things 3 (one purchase, no ads) suit people who left a bigger app because of crashes.",
        ]},
        {"id": "lost-tasks", "h2": "\"Lost all my tasks\" and \"doesn't sync\": 130 reviews", "body": [
            "The second-biggest group is tasks that disappear or lists that do not match between devices (130 reviews; Clear 58, Microsoft To Do 37). In the words of reviewers: \"My set of 15 plus reminders disappeared twice\" (MinimaList, 1 star) and \"Not syncing across devices is crazy\" (Clear, 1 star).",
            "The fix: sign in with the same account on every device, check in Settings > your name > iCloud that the app is allowed to use iCloud if it uses it, and do not reinstall before you have seen the list on a second device. If you only need today's list, you do not need sync at all: 3 Tasks is a one-day list of three, so nothing important lives in it for long. For a list you keep for years, use an app with its own cloud account (Things 3, Todoist, TickTick, Microsoft To Do) and look at the list on the web once to confirm it is saved.",
        ]},
        {"id": "reminders", "h2": "\"Reminders don't go off\": 75 reviews", "body": [
            "75 reviews say reminders or notifications never arrive, arrive on the wrong day or cannot be deleted (Todoist 22, Things 3 16, Clear 14). Example: \"Reoccurring reminders show up on the wrong days and can't be deleted\" (Do!, 2 stars).",
            "The fix is often in iOS, not the app. Check Settings > Notifications > the app (Allow Notifications on, Time Sensitive on), Settings > Notifications > Scheduled Summary (it can hold alerts until the evening) and Settings > Focus (each Focus has an allowed-apps list). If a repeating reminder is wrong, delete the whole series and create it again. For reminders you cannot miss, Apple's own Reminders app is a good second layer.",
        ]},
        {"id": "paywall", "h2": "\"Now it wants a subscription\": 66 reviews", "body": [
            "66 reviews are about paywalls and subscriptions, most about features that used to be free (Todoist 21, Clear 18, MinimaList 13). Example: \"Needlessly added subscriptions as a means to nickel and dime functionality like widgets\" (Clear, 1 star).",
            "The fix: pick an app whose free version is complete. On 10 November 2026 Microsoft To Do lists no in-app purchases, 3 Tasks is free with an optional one-time Pro ($4.99 or $9.99), and Things 3 costs $9.99 once. If you already pay and want to stop, cancel in Settings > your name > Subscriptions.",
        ]},
        {"id": "widget", "h2": "\"The widget is blank or won't update\": 51 reviews", "body": [
            "51 reviews are about widgets that show nothing or do not update (Microsoft To Do 20, Do! 9, Things 3 7). Example: \"The widget would not update the list\" (Do!, 1 star).",
            "The fix: remove the widget and add it again, open the app once after each update, and keep Background App Refresh on for it (Settings > General > Background App Refresh). For a widget that has little to refresh, 3 Tasks has a free Home Screen widget that shows the day's three.",
        ]},
    ],
    "columns": ["App", "Price (US)", "What makes it simple", "Account", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices (download and in-app purchases), version, date and rating are from the US App Store on 10 November 2026. Seven of the eight are free to download; Things 3 is a paid app.",
    "apps": [
        {
            "name": "3 Tasks a Day: To Do List", "id": 1553693943, "ours": True, "anchor": "3-tasks",
            "developer": "Saga Ltd.", "rating": (5.0, 6),
            "row": ["Free; 3 Tasks Pro is a one-time purchase (listed at $4.99 and $9.99)", "Only 3 tasks a day, one screen, a timer per task", "No account",
                    "Data Used to Track You; Data Not Linked to You", "1.4.6 (5 Nov 2026)", "5.0"],
            "best_for": "people who drown in long lists and want to pick the three things that matter today.",
            "facts": [
                "Write down three daily priorities; nothing else to configure.",
                "Start and pause each task, Pomodoro-style, and see the time spent on it.",
                "No ads and no account. The app uses Firebase Analytics to count how tasks and timers are used, which is why its privacy label lists tracking data.",
                "33 languages, iOS 18 or later, 24 MB.",
            ],
            "limits": "no reminders and no sync between devices: it is deliberately a one-day list of three (it does have Repeat Daily and a Home Screen widget, free).",
        },
        {
            "name": "Do! – Simple To Do List", "id": 421819675, "anchor": "do",
            "developer": "SIMPLERION", "rating": (4.73, 26203),
            "row": ["Free with ads; remove ads $20.00 once; tip $0.99", "Add a task, double-tap when done; groups and colours", "Not stated",
                    "Data Used to Track You; Data Linked to You; Data Not Linked to You", "7.9.0 (22 Oct 2026)", "4.7"],
            "best_for": "a paper-like daily list with reminders and repeating tasks.",
            "facts": [
                "Themes, fonts and pen-and-paper sounds.",
                "Groups for work, study and shopping; pinned tasks.",
                "Repeating tasks (daily to yearly) and reminders.",
                "5 languages, iOS 15 or later, 159 MB.",
            ],
            "limits": "shows ads unless you pay $20 once, and its privacy label includes data used to track you.",
        },
        {
            "name": "To Do List MinimaList & Widget", "id": 993066159, "anchor": "minimalist",
            "developer": "Inner Grow Limited", "rating": (4.77, 49032),
            "row": ["Lifetime from $5.99 (offers) to $9.99; family $14.99; or $2.99 a month", "Coloured lists, smart input that detects times", "Not stated",
                    "Data Not Linked to You", "2.27.9 (30 Oct 2026)", "4.8"],
            "best_for": "a minimal-looking list that still has widgets, shared lists and location reminders.",
            "facts": [
                "Home Screen and Lock Screen widgets.",
                "Time- and location-based reminders, sub-tasks and shared lists.",
                "Works with Siri; on iPhone, iPad and Mac according to the developer.",
                "10 languages, iOS 15 or later, 130 MB.",
            ],
            "limits": "several overlapping prices for the same lifetime upgrade, which makes it hard to know what you will pay.",
        },
        {
            "name": "Clear: To Dos & Reminders", "id": 493136154, "anchor": "clear",
            "developer": "Impending, Inc.", "rating": (4.6, 5240),
            "row": ["Clear Pro $3.99 or $29.99 a year; legacy Pro $2.99 a month or $24.99 a year; sound packs", "Gesture-only lists, colour heatmap of priority", "Not stated",
                    "Data Used to Track You; Data Not Linked to You", "2.8.8 (9 Nov 2026)", "4.6"],
            "best_for": "people who like swiping lists with no buttons on screen.",
            "facts": [
                "Swipe to complete, pinch and drag to reorder; a heatmap shows priority.",
                "Daily kanban (Today, Tomorrow, Next Day), routines and reminders.",
                "2 languages, iOS 16 or later, 206 MB.",
            ],
            "limits": "gestures take a few minutes to learn, and its privacy label includes data used to track you.",
        },
        {
            "name": "Microsoft To Do", "id": 1212616790, "anchor": "microsoft-to-do",
            "developer": "Microsoft", "rating": (4.72, 269935),
            "row": ["Free, no in-app purchases", "My Day with suggested tasks", "Microsoft account for sync",
                    "Data Linked to You", "2.177 (6 Jul 2026)", "4.7"],
            "best_for": "a free list that syncs everywhere, especially if you use Outlook or Microsoft 365.",
            "facts": [
                "My Day and Suggestions help plan the day from all your lists.",
                "Syncs with Microsoft 365; flagged Outlook emails can become tasks.",
                "Shared lists for personal accounts.",
                "34 languages, iOS 17.6 or later, 167 MB.",
            ],
            "limits": "it is a full task manager with lists, steps and suggestions, so it can grow into the long lists a simple app avoids.",
        },
        {
            "name": "Todoist: To Do List & Calendar", "id": 572688855, "anchor": "todoist",
            "developer": "Doist", "rating": (4.8, 130607),
            "row": ["Pro $6.99 a month or $59.99 a year", "Natural-language quick add and voice capture", "Yes",
                    "Data Linked to You", "26.11.5 (9 Nov 2026)", "4.8"],
            "best_for": "people whose list is outgrowing a simple app and who want projects, dates and teams.",
            "facts": [
                "Quick Add understands dates in plain language; Ramble turns speech into tasks.",
                "Projects, calendar view and team workspaces.",
                "Works with Siri. 19 languages, iOS 17 or later, 394 MB.",
            ],
            "limits": "Pro is a subscription, and it is a full project manager rather than a simple list.",
        },
        {
            "name": "TickTick:To-Do List & Calendar", "id": 626144601, "anchor": "ticktick",
            "developer": "Appest Limited", "rating": (4.86, 46891),
            "row": ["Free to download; Premium $4.99 a month or $49.99 a year", "Calendar views, four priority levels, reminders, Pomo timer", "Not stated",
                    "Data Linked to You; Data Not Linked to You", "8.3.00 (9 Nov 2026)", "4.9"],
            "best_for": "a free list that also has calendar views, habits and shared lists.",
            "facts": [
                "Sync across devices, multiple reminders and flexible calendar views.",
                "Recurring tasks, checklists, tags and four priority levels.",
                "Share task lists, add tasks by email, Siri and voice entry with AI.",
                "Pomo timer and habit goals; 41 languages, iOS 15.5 or later, 329 MB.",
            ],
            "limits": "its page says it is always free, but Premium raises the limits (for example 299 lists and 5 reminders per task), and it is far from the simplest app here.",
        },
        {
            "name": "Things 3", "id": 904237743, "anchor": "things-3",
            "developer": "Cultured Code GmbH & Co. KG", "rating": (4.82, 28083),
            "row": ["$9.99 once to download", "To-dos, projects and areas; Today and Upcoming lists", "Not stated",
                    "Data Linked to You; Data Not Linked to You", "3.25.2 (2 Nov 2026)", "4.8"],
            "best_for": "people who want a polished planner with projects and areas and are happy to pay once.",
            "facts": [
                "Projects, areas, headings, tags and deadlines.",
                "Today and Upcoming lists that show to-dos and calendar events; a This Evening section.",
                "Reminders and repeaters. 9 languages, iOS 16.4 or later, 126 MB.",
            ],
            "limits": "it costs $9.99 up front, and it is a full planner, not a simple list.",
        },
    ],
    "who": [
        "<strong>You keep writing lists you never finish:</strong> 3 Tasks, three a day and nothing more.",
        "<strong>You want reminders and repeating tasks but a calm design:</strong> Do! or MinimaList.",
        "<strong>You want everything free and synced:</strong> Microsoft To Do.",
        "<strong>You like gestures and no buttons:</strong> Clear.",
        "<strong>Your app crashed, lost tasks or went behind a paywall:</strong> see the five fixes above, then 3 Tasks, Microsoft To Do or Things 3.",
        "<strong>You need projects, dates and shared work:</strong> Todoist or TickTick.",
        "<strong>You want a polished planner and prefer paying once:</strong> Things 3.",
    ],
    "cases": [
        "Picking the three things that must happen today before opening email.",
        "A shopping or errands list that reminds you when you get to the shop (MinimaList).",
        "Work tasks that come from flagged Outlook emails (Microsoft To Do).",
        "Timing focused work blocks on each priority (3 Tasks).",
    ],
    "method": [
        "On 10 November 2026 we rechecked each app's US App Store page and Apple's lookup data: download and in-app purchase prices, version and release date, rating, size, minimum iOS and the privacy label. The first six were first checked on 11 October 2026 and no price had changed; TickTick and Things 3 were added on 9 November. Features are the ones each developer lists on its App Store page. \"Not stated\" means the listing does not say whether an account is needed. We did not invent ratings or reviews.",
        "Complaint counts: on 10 November 2026 we downloaded the latest 500 US App Store reviews of each app (3,502 in all) and read the 775 with one or two stars. Each review was counted once per complaint by matching its words (for example crash, freez, sync, disappear, reminder, subscri, widget); a review can count in more than one group. Counts show how often a complaint comes up in the sample, not how often an app fails.",
    ],
    "faq": [
        ("What is the best to-do list app for iPhone?",
         "Things 3 for a polished paid planner ($9.99 once), Microsoft To Do for a free list that syncs, TickTick or Todoist for calendar views and shared lists, and 3 Tasks for the simplest list. Prices and versions checked on 10 November 2026."),
        ("What is the best free to-do list app for iPhone?",
         "Microsoft To Do is free with no in-app purchases. TickTick, Todoist and 3 Tasks are free to download with optional paid upgrades; Do! is free with ads."),
        ("What is the best iPhone todo list app if I only want a few tasks?",
         "3 Tasks, which lets you write three tasks a day on one screen. Among classic list apps, Do! and Clear are the most minimal."),
        ("Is there a free to-do list app with no subscription?",
         "Microsoft To Do is free with no in-app purchases, and 3 Tasks is free with an optional one-time Pro (no subscription). Do! is free with ads and a one-time $20 to remove them; MinimaList and Clear also offer one-time upgrades."),
        ("Which to-do app works without an account?",
         "3 Tasks needs no account. Microsoft To Do uses a Microsoft account to sync, and Todoist uses its own account. TickTick and Things 3 do not say on their App Store pages."),
        ("Why do to-do apps lose my tasks?",
         "Most reports come after an update, a reinstall or a new phone, when the list lived only on one device or the sign-in differed. Sign in with the same account everywhere and check the list on a second device before you reinstall."),
        ("Why aren't my to-do list reminders going off on iPhone?",
         "Check Settings > Notifications for the app (Allow Notifications and Time Sensitive), the Scheduled Summary setting and the allowed apps of each Focus. If a repeating reminder is wrong, delete the series and create it again."),
        ("Why limit yourself to three tasks a day?",
         "A short list forces you to choose what matters most, so the list gets finished instead of growing. That is the idea behind 3 Tasks."),
        ("Which simple to-do app has widgets?",
         "MinimaList has Home Screen and Lock Screen widgets. 3 Tasks has a free Home Screen widget."),
    ],
    "sources": src("us", True),
}

ES = {
    "group": "simple-todo", "lang": "es", "store": "es",
    "path": "es/mejores-apps-de-tareas-sencillas-iphone/",
    "ct": "rl-simple-todo-es",
    "category": "ProductivityApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Mejores apps de tareas sencillas para iPhone (2026)",
    "h1": "Mejores apps de listas de tareas sencillas para iPhone en 2026",
    "description": "Seis apps de tareas sencillas para iPhone comparadas: 3 Tasks, Do!, MinimaList, Clear, Microsoft To Do y Todoist. Precio, cuenta y privacidad.",
    "llms": "Compara seis apps de listas de tareas sencillas para iPhone (3 Tasks, Do!, MinimaList, Clear, Microsoft To Do, Todoist) por precio en euros, si piden cuenta, recordatorios y widgets, y privacidad.",
    "answer": [
        "La lista de tareas más sencilla del iPhone es la que te limita: 3 Tasks solo te deja apuntar tres prioridades al día y cronometra cada una, gratis, sin cuenta y sin suscripción (el Pro opcional es un pago único). Si quieres una lista normal que siga siendo sencilla, Do! y MinimaList añaden recordatorios y widgets, y Microsoft To Do es totalmente gratis y sincroniza con una cuenta de Microsoft.",
        "Todoist es la más completa de las seis, pero su plan Pro es una suscripción (6,99 € al mes o 59,99 € al año en España).",
    ],
    "columns": ["App", "Precio (España)", "Qué la hace sencilla", "Cuenta", "Etiqueta de privacidad", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Precios: compras dentro de la app del App Store de España el 11 de octubre de 2026; las seis se descargan gratis. Valoración: media en España ese día.",
    "apps": [
        {
            "name": "Lista de Tareas: 3 Tasks", "id": 1553693943, "ours": True, "anchor": "3-tasks",
            "developer": "Saga Ltd.", "rating": (5.0, 2),
            "row": ["Gratis; 3 Tasks Pro es una compra única (listada a 5,99 € y 9,99 €)", "Solo 3 tareas al día, una pantalla, un cronómetro por tarea", "Sin cuenta",
                    "Datos utilizados para rastrearte; datos no vinculados a ti", "1.4.3 (26 oct 2026)", "5,0"],
            "best_for": "quien se ahoga en listas largas y quiere elegir las tres cosas que importan hoy.",
            "facts": [
                "Apuntas tres prioridades del día y nada más que configurar.",
                "Empiezas y pausas cada tarea, al estilo Pomodoro, y ves el tiempo que llevas.",
                "Sin anuncios y sin cuenta. Usa Firebase Analytics para contar cómo se usan las tareas y los cronómetros; por eso su etiqueta de privacidad habla de rastreo.",
                "33 idiomas, español incluido. iOS 18 o posterior, 21 MB.",
            ],
            "limits": "no tiene recordatorios ni sincronización: a propósito es una lista de tres para un día (sí tiene «Repetir a diario» y un widget gratis).",
        },
        {
            "name": "Do! – Simple To Do List", "id": 421819675, "anchor": "do",
            "developer": "SIMPLERION", "rating": (4.61, 234),
            "row": ["Gratis con anuncios; quitar anuncios 22,00 € una vez; propina 0,99 €", "Añades una tarea y la marcas con doble toque; grupos y colores", "No lo indica",
                    "Datos utilizados para rastrearte; datos vinculados a ti; datos no vinculados a ti", "7.7.2 (1 oct 2026)", "4,6"],
            "best_for": "una lista diaria con aire de papel, con recordatorios y tareas repetidas.",
            "facts": [
                "Temas, tipos de letra y sonidos de lápiz y papel.",
                "Grupos para trabajo, estudio y compra; tareas fijadas arriba.",
                "Tareas que se repiten (de diarias a anuales) y recordatorios.",
                "5 idiomas, iOS 13 o posterior, 157 MB.",
            ],
            "limits": "lleva anuncios si no pagas 22 € una vez, la app no está en español y su etiqueta incluye datos para rastrearte.",
        },
        {
            "name": "To do list - MinimaList", "id": 993066159, "anchor": "minimalist",
            "developer": "Inner Grow Limited", "rating": (4.72, 1025),
            "row": ["De por vida desde 6,99 € (ofertas) a 9,99 €; familiar 17,99 €; o 2,99 € al mes", "Listas de colores y escritura que detecta horas", "No lo indica",
                    "Datos no vinculados a ti", "2.27.3 (11 oct 2026)", "4,7"],
            "best_for": "una lista de aspecto mínimo que aun así tiene widgets, listas compartidas y avisos por ubicación.",
            "facts": [
                "Widgets en la pantalla de inicio y en la pantalla bloqueada.",
                "Recordatorios por hora y por lugar, subtareas y listas compartidas.",
                "Funciona con Siri; en iPhone, iPad y Mac según el desarrollador.",
                "10 idiomas, iOS 15 o posterior, 126 MB.",
            ],
            "limits": "tiene varios precios distintos para la misma mejora de por vida, y cuesta saber cuánto vas a pagar.",
        },
        {
            "name": "Clear: To Dos & Reminders", "id": 493136154, "anchor": "clear",
            "developer": "Impending, Inc.", "rating": (4.6, 131),
            "row": ["Pro antiguo 2,99 € al mes; packs de sonidos", "Listas solo con gestos y mapa de calor por prioridad", "No lo indica",
                    "Datos utilizados para rastrearte; datos no vinculados a ti", "2.8.0 (30 sep 2026)", "4,6"],
            "best_for": "quien prefiere deslizar listas sin botones en pantalla.",
            "facts": [
                "Deslizas para completar y pellizcas o arrastras para ordenar; los colores marcan la prioridad.",
                "Kanban diario (Hoy, Mañana, Pasado), rutinas y recordatorios.",
                "2 idiomas, iOS 16 o posterior, 203 MB.",
            ],
            "limits": "los gestos tardan unos minutos en aprenderse, la app no está en español y su etiqueta incluye datos para rastrearte.",
        },
        {
            "name": "Microsoft To Do", "id": 1212616790, "anchor": "microsoft-to-do",
            "developer": "Microsoft", "rating": (4.65, 21250),
            "row": ["Gratis, sin compras dentro", "Mi día con tareas sugeridas", "Cuenta de Microsoft para sincronizar",
                    "Datos vinculados a ti", "2.177 (6 jul 2026)", "4,7"],
            "best_for": "una lista gratis que se sincroniza en todas partes, sobre todo si usas Outlook o Microsoft 365.",
            "facts": [
                "Mi día y Sugerencias ayudan a planear el día con tus listas.",
                "Se sincroniza con Microsoft 365; los correos marcados en Outlook pueden pasar a tareas.",
                "Listas compartidas en cuentas personales.",
                "34 idiomas, iOS 17.6 o posterior, 167 MB.",
            ],
            "limits": "es un gestor de tareas completo, con listas, pasos y sugerencias, así que puede acabar en las listas largas que una app sencilla evita.",
        },
        {
            "name": "Todoist: To do list–Calendario", "id": 572688855, "anchor": "todoist",
            "developer": "Doist", "rating": (4.71, 7585),
            "row": ["Pro 6,99 € al mes o 59,99 € al año", "Escritura en lenguaje natural y captura por voz", "Sí",
                    "Datos vinculados a ti", "26.10.8 (8 oct 2026)", "4,7"],
            "best_for": "quien ya necesita más que una app sencilla: proyectos, fechas y equipos.",
            "facts": [
                "Quick Add entiende fechas escritas con normalidad; Ramble convierte lo que dices en tareas.",
                "Proyectos, vista de calendario y espacios de equipo.",
                "Funciona con Siri. 19 idiomas, iOS 17 o posterior, 384 MB.",
            ],
            "limits": "Pro es una suscripción y es la menos sencilla de la lista.",
        },
    ],
    "who": [
        "<strong>Siempre escribes listas que no terminas:</strong> 3 Tasks, tres al día y nada más.",
        "<strong>Quieres recordatorios y tareas repetidas con un diseño tranquilo:</strong> Do! o MinimaList.",
        "<strong>Quieres todo gratis y sincronizado:</strong> Microsoft To Do.",
        "<strong>Te gustan los gestos sin botones:</strong> Clear.",
        "<strong>Necesitas proyectos, fechas y trabajo compartido:</strong> Todoist.",
    ],
    "cases": [
        "Elegir las tres cosas que tienen que salir hoy antes de abrir el correo.",
        "Una lista de la compra o de recados que te avisa al llegar a la tienda (MinimaList).",
        "Tareas de trabajo que salen de correos marcados en Outlook (Microsoft To Do).",
        "Cronometrar bloques de trabajo concentrado en cada prioridad (3 Tasks).",
    ],
    "method": [
        "El 11 de octubre de 2026 abrimos la ficha de cada app en el App Store de España y los datos de Apple: compras dentro de la app, versión y fecha, valoración, idiomas, tamaño, iOS mínimo y etiqueta de privacidad. Las funciones son las que cada desarrollador pone en su ficha. «No lo indica» quiere decir que la ficha no dice si hace falta cuenta. No inventamos valoraciones ni reseñas.",
    ],
    "faq": [
        ("¿Cuál es la app de tareas más sencilla para iPhone?",
         "3 Tasks solo deja apuntar tres tareas al día en una pantalla. Entre las listas clásicas, Do! y Clear son las más mínimas."),
        ("¿Hay alguna app de tareas gratis y sin suscripción?",
         "Microsoft To Do es gratis y sin compras dentro, y 3 Tasks es gratis con un Pro opcional de pago único (sin suscripción). Do! es gratis con anuncios y un pago único de 22 € para quitarlos; MinimaList también tiene pago único."),
        ("¿Qué app de tareas funciona sin cuenta?",
         "3 Tasks no pide cuenta. Microsoft To Do usa una cuenta de Microsoft para sincronizar y Todoist usa su propia cuenta."),
        ("¿Por qué limitarse a tres tareas al día?",
         "Una lista corta te obliga a elegir lo que más importa, así que se termina en vez de crecer. Esa es la idea de 3 Tasks."),
        ("¿Qué app de tareas sencilla tiene widgets?",
         "MinimaList tiene widgets en la pantalla de inicio y en la bloqueada. 3 Tasks tiene un widget gratis en la pantalla de inicio."),
    ],
    "sources": src("es"),
}

PAGES = [EN, ES]


from pages.store_1016 import refresh_ours
for _p in PAGES:
    refresh_ours(_p, _p["store"], 3, 4, 5)
