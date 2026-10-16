"""Best simple to-do list apps for iPhone. EN + ES. Our app: 3 Tasks (id1553693943).

Checked 2026-10-11: iTunes lookup API and App Store web pages (US for EN,
Spain for ES). 3 Tasks 1.1.2 is free with no in-app purchases (Pro is not
released yet; when it ships, update price and features here).
"""

CHECKED = "2026-10-11"


def src(cc):
    return [
        ("3 Tasks (App Store)", f"https://apps.apple.com/{cc}/app/id1553693943"),
        ("Do! (App Store)", f"https://apps.apple.com/{cc}/app/id421819675"),
        ("MinimaList (App Store)", f"https://apps.apple.com/{cc}/app/id993066159"),
        ("Clear (App Store)", f"https://apps.apple.com/{cc}/app/id493136154"),
        ("Microsoft To Do (App Store)", f"https://apps.apple.com/{cc}/app/id1212616790"),
        ("Todoist (App Store)", f"https://apps.apple.com/{cc}/app/id572688855"),
    ]


EN = {
    "group": "simple-todo", "lang": "en", "store": "us",
    "path": "best-simple-to-do-list-apps-iphone/",
    "ct": "rl-simple-todo",
    "category": "ProductivityApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best simple to-do list apps for iPhone (2026): 6 options compared",
    "h1": "Best simple to-do list apps for iPhone in 2026",
    "description": "Six simple to-do list apps for iPhone compared: 3 Tasks, Do!, MinimaList, Clear, Microsoft To Do and Todoist. Prices, account needs and privacy labels checked on the App Store on 11 October 2026.",
    "llms": "Compares six simple to-do list apps for iPhone (3 Tasks, Do!, MinimaList, Clear, Microsoft To Do, Todoist) by price, whether they need an account, reminders and widgets, and privacy label.",
    "disclosure": "3 Tasks is made by Saga Labs, the company behind Reviewland. It is listed first because it is ours. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "The simplest to-do list on iPhone is one that limits you: 3 Tasks (ours) lets you write only three priorities a day and times each one, free, with no account and no in-app purchases. If you want a normal list that stays simple, Do! and MinimaList add reminders and widgets, and Microsoft To Do is completely free with sync through a Microsoft account.",
        "Todoist is the most complete of the six, but its Pro plan is a subscription ($6.99 a month or $59.99 a year in the US).",
    ],
    "columns": ["App", "Price (US)", "What makes it simple", "Account", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the US App Store in-app purchases on 11 October 2026; all six are free to download. Ratings are the App Store average and number of ratings that day.",
    "apps": [
        {
            "name": "3 Tasks - Daily", "id": 1553693943, "ours": True, "anchor": "3-tasks",
            "developer": "Saga Ltd.", "rating": (5.0, 5),
            "row": ["Free, no in-app purchases", "Only 3 tasks a day, one screen, a timer per task", "No account",
                    "Data Used to Track You; Data Not Linked to You", "1.1.2 (9 Oct 2026)", "5.0 (5 ratings)"],
            "best_for": "people who drown in long lists and want to pick the three things that matter today.",
            "facts": [
                "Write down three daily priorities; nothing else to configure.",
                "Start and pause each task, Pomodoro-style, and see the time spent on it.",
                "No ads and no account. The app uses Firebase Analytics to count how tasks and timers are used, which is why its privacy label lists tracking data.",
                "English only, iOS 18 or later, 7 MB, the smallest app here.",
            ],
            "limits": "no reminders, no recurring tasks, no widgets and no sync between devices: it is deliberately a one-day list of three. Only 5 ratings in the US so far.",
        },
        {
            "name": "Do! – Simple To Do List", "id": 421819675, "anchor": "do",
            "developer": "SIMPLERION", "rating": (4.73, 26187),
            "row": ["Free with ads; remove ads $20.00 once; tip $0.99", "Add a task, double-tap when done; groups and colours", "Not stated",
                    "Data Used to Track You; Data Linked to You; Data Not Linked to You", "7.7.2 (1 Oct 2026)", "4.7 (26,187 ratings)"],
            "best_for": "a paper-like daily list with reminders and repeating tasks.",
            "facts": [
                "Themes, fonts and pen-and-paper sounds.",
                "Groups for work, study and shopping; pinned tasks.",
                "Repeating tasks (daily to yearly) and reminders.",
                "5 languages, iOS 13 or later, 157 MB.",
            ],
            "limits": "shows ads unless you pay $20 once, and its privacy label includes data used to track you.",
        },
        {
            "name": "To Do List MinimaList & Widget", "id": 993066159, "anchor": "minimalist",
            "developer": "Inner Grow Limited", "rating": (4.77, 48222),
            "row": ["Lifetime from $5.99 (offers) to $9.99; family $14.99; or $2.99 a month", "Coloured lists, smart input that detects times", "Not stated",
                    "Data Not Linked to You", "2.27.3 (11 Oct 2026)", "4.8 (48,222 ratings)"],
            "best_for": "a minimal-looking list that still has widgets, shared lists and location reminders.",
            "facts": [
                "Home Screen and Lock Screen widgets.",
                "Time- and location-based reminders, sub-tasks and shared lists.",
                "Works with Siri; on iPhone, iPad and Mac according to the developer.",
                "10 languages, iOS 15 or later, 126 MB.",
            ],
            "limits": "several overlapping prices for the same lifetime upgrade, which makes it hard to know what you will pay.",
        },
        {
            "name": "Clear: To Dos & Reminders", "id": 493136154, "anchor": "clear",
            "developer": "Impending, Inc.", "rating": (4.6, 5144),
            "row": ["Clear Pro $3.99; legacy Pro $2.99 a month or $24.99 a year; sound packs", "Gesture-only lists, colour heatmap of priority", "Not stated",
                    "Data Used to Track You; Data Not Linked to You", "2.8.0 (30 Sep 2026)", "4.6 (5,144 ratings)"],
            "best_for": "people who like swiping lists with no buttons on screen.",
            "facts": [
                "Swipe to complete, pinch and drag to reorder; a heatmap shows priority.",
                "Daily kanban (Today, Tomorrow, Next Day), routines and reminders.",
                "2 languages, iOS 16 or later, 203 MB.",
            ],
            "limits": "gestures take a few minutes to learn, and its privacy label includes data used to track you.",
        },
        {
            "name": "Microsoft To Do", "id": 1212616790, "anchor": "microsoft-to-do",
            "developer": "Microsoft", "rating": (4.72, 268432),
            "row": ["Free, no in-app purchases", "My Day with suggested tasks", "Microsoft account for sync",
                    "Data Linked to You", "2.177 (6 Jul 2026)", "4.7 (268,432 ratings)"],
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
            "developer": "Doist", "rating": (4.8, 129694),
            "row": ["Pro $6.99 a month or $59.99 a year", "Natural-language quick add and voice capture", "Yes",
                    "Data Linked to You", "26.10.8 (8 Oct 2026)", "4.8 (129,694 ratings)"],
            "best_for": "people whose list is outgrowing a simple app and who want projects, dates and teams.",
            "facts": [
                "Quick Add understands dates in plain language; Ramble turns speech into tasks.",
                "Projects, calendar view and team workspaces.",
                "Works with Siri. 19 languages, iOS 17 or later, 384 MB.",
            ],
            "limits": "Pro is a subscription, and it is the least simple app in this list.",
        },
    ],
    "who": [
        "<strong>You keep writing lists you never finish:</strong> 3 Tasks (ours), three a day and nothing more.",
        "<strong>You want reminders and repeating tasks but a calm design:</strong> Do! or MinimaList.",
        "<strong>You want everything free and synced:</strong> Microsoft To Do.",
        "<strong>You like gestures and no buttons:</strong> Clear.",
        "<strong>You need projects, dates and shared work:</strong> Todoist.",
    ],
    "cases": [
        "Picking the three things that must happen today before opening email.",
        "A shopping or errands list that reminds you when you get to the shop (MinimaList).",
        "Work tasks that come from flagged Outlook emails (Microsoft To Do).",
        "Timing focused work blocks on each priority (3 Tasks).",
    ],
    "method": [
        "On 11 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchases, version and release date, rating and number of ratings, languages, size, minimum iOS and the privacy label. Features are the ones each developer lists on its App Store page. \"Not stated\" means the listing does not say whether an account is needed. We did not invent ratings or reviews.",
    ],
    "faq": [
        ("What is the simplest to-do list app for iPhone?",
         "3 Tasks only lets you write three tasks a day on one screen. Among classic list apps, Do! and Clear are the most minimal."),
        ("Is there a free to-do list app with no subscription?",
         "3 Tasks and Microsoft To Do are free with no in-app purchases. Do! is free with ads and a one-time $20 to remove them; MinimaList and Clear also offer one-time upgrades."),
        ("Which to-do app works without an account?",
         "3 Tasks needs no account. Microsoft To Do uses a Microsoft account to sync, and Todoist uses its own account."),
        ("Why limit yourself to three tasks a day?",
         "A short list forces you to choose what matters most, so the list gets finished instead of growing. That is the idea behind 3 Tasks."),
        ("Which simple to-do app has widgets?",
         "MinimaList has Home Screen and Lock Screen widgets. 3 Tasks does not have widgets."),
    ],
    "sources": src("us"),
}

ES = {
    "group": "simple-todo", "lang": "es", "store": "es",
    "path": "es/mejores-apps-de-tareas-sencillas-iphone/",
    "ct": "rl-simple-todo-es",
    "category": "ProductivityApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Mejores apps de listas de tareas sencillas para iPhone (2026): 6 comparadas",
    "h1": "Mejores apps de listas de tareas sencillas para iPhone en 2026",
    "description": "Seis apps de tareas sencillas para iPhone comparadas: 3 Tasks, Do!, MinimaList, Clear, Microsoft To Do y Todoist. Precios, cuenta y privacidad comprobados en el App Store de España el 11 de octubre de 2026.",
    "llms": "Compara seis apps de listas de tareas sencillas para iPhone (3 Tasks, Do!, MinimaList, Clear, Microsoft To Do, Todoist) por precio en euros, si piden cuenta, recordatorios y widgets, y privacidad.",
    "disclosure": "3 Tasks (en España, «3 Tareas - Diario») es de Saga Labs, la empresa que hace Reviewland. Va primera porque es nuestra. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store.",
    "answer": [
        "La lista de tareas más sencilla del iPhone es la que te limita: 3 Tasks (nuestra) solo te deja apuntar tres prioridades al día y cronometra cada una, gratis, sin cuenta y sin compras dentro. Si quieres una lista normal que siga siendo sencilla, Do! y MinimaList añaden recordatorios y widgets, y Microsoft To Do es totalmente gratis y sincroniza con una cuenta de Microsoft.",
        "Todoist es la más completa de las seis, pero su plan Pro es una suscripción (6,99 € al mes o 59,99 € al año en España).",
    ],
    "columns": ["App", "Precio (España)", "Qué la hace sencilla", "Cuenta", "Etiqueta de privacidad", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Precios: compras dentro de la app del App Store de España el 11 de octubre de 2026; las seis se descargan gratis. Valoración: media y número de valoraciones en España ese día.",
    "apps": [
        {
            "name": "3 Tasks (3 Tareas - Diario)", "id": 1553693943, "ours": True, "anchor": "3-tasks",
            "developer": "Saga Ltd.", "rating": (5.0, 2),
            "row": ["Gratis, sin compras dentro", "Solo 3 tareas al día, una pantalla, un cronómetro por tarea", "Sin cuenta",
                    "Datos utilizados para rastrearte; datos no vinculados a ti", "1.1.2 (9 oct 2026)", "5,0 (2 valoraciones)"],
            "best_for": "quien se ahoga en listas largas y quiere elegir las tres cosas que importan hoy.",
            "facts": [
                "Apuntas tres prioridades del día y nada más que configurar.",
                "Empiezas y pausas cada tarea, al estilo Pomodoro, y ves el tiempo que llevas.",
                "Sin anuncios y sin cuenta. Usa Firebase Analytics para contar cómo se usan las tareas y los cronómetros; por eso su etiqueta de privacidad habla de rastreo.",
                "La app está solo en inglés. iOS 18 o posterior, 7 MB, la más ligera de la lista.",
            ],
            "limits": "no tiene recordatorios, tareas repetidas, widgets ni sincronización: a propósito es una lista de tres para un día. La app está en inglés y en España tiene solo 2 valoraciones.",
        },
        {
            "name": "Do! – Simple To Do List", "id": 421819675, "anchor": "do",
            "developer": "SIMPLERION", "rating": (4.61, 234),
            "row": ["Gratis con anuncios; quitar anuncios 22,00 € una vez; propina 0,99 €", "Añades una tarea y la marcas con doble toque; grupos y colores", "No lo indica",
                    "Datos utilizados para rastrearte; datos vinculados a ti; datos no vinculados a ti", "7.7.2 (1 oct 2026)", "4,6 (234 valoraciones)"],
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
                    "Datos no vinculados a ti", "2.27.3 (11 oct 2026)", "4,7 (1.025 valoraciones)"],
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
                    "Datos utilizados para rastrearte; datos no vinculados a ti", "2.8.0 (30 sep 2026)", "4,6 (131 valoraciones)"],
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
                    "Datos vinculados a ti", "2.177 (6 jul 2026)", "4,7 (21.250 valoraciones)"],
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
                    "Datos vinculados a ti", "26.10.8 (8 oct 2026)", "4,7 (7.585 valoraciones)"],
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
        "<strong>Siempre escribes listas que no terminas:</strong> 3 Tasks (nuestra), tres al día y nada más.",
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
        "El 11 de octubre de 2026 abrimos la ficha de cada app en el App Store de España y los datos de Apple: compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño, iOS mínimo y etiqueta de privacidad. Las funciones son las que cada desarrollador pone en su ficha. «No lo indica» quiere decir que la ficha no dice si hace falta cuenta. No inventamos valoraciones ni reseñas.",
    ],
    "faq": [
        ("¿Cuál es la app de tareas más sencilla para iPhone?",
         "3 Tasks solo deja apuntar tres tareas al día en una pantalla. Entre las listas clásicas, Do! y Clear son las más mínimas."),
        ("¿Hay alguna app de tareas gratis y sin suscripción?",
         "3 Tasks y Microsoft To Do son gratis y sin compras dentro. Do! es gratis con anuncios y un pago único de 22 € para quitarlos; MinimaList también tiene pago único."),
        ("¿Qué app de tareas funciona sin cuenta?",
         "3 Tasks no pide cuenta. Microsoft To Do usa una cuenta de Microsoft para sincronizar y Todoist usa su propia cuenta."),
        ("¿Por qué limitarse a tres tareas al día?",
         "Una lista corta te obliga a elegir lo que más importa, así que se termina en vez de crecer. Esa es la idea de 3 Tasks."),
        ("¿Qué app de tareas sencilla tiene widgets?",
         "MinimaList tiene widgets en la pantalla de inicio y en la bloqueada. 3 Tasks no tiene widgets."),
    ],
    "sources": src("es"),
}

PAGES = [EN, ES]


from pages.store_1016 import refresh_ours
for _p in PAGES:
    refresh_ours(_p, _p["store"], 3, 4, 5)
