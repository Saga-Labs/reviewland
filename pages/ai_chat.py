"""Best AI chat apps for iPhone (free use, account, price). EN + ES. Our app: Brainy (id1667947372).

Checked 2026-10-11: iTunes lookup API and App Store web pages (US for EN,
Spain for ES). Brainy 1.3.5 facts from its repo (brainy-28 session, 11 Oct):
chat = DeepSeek V3.1 via OpenRouter, photos = Gemini 2.5 Flash Lite, 20 free
messages a day, Pro 500, images (Nano Banana) only with Pro, 3 a day.
Ask AI (formerly Fast AI, also ours, id1662608035) added 2026-10-23 from its
listing 1.4.4 (US and Spain): chat only, few free messages a day, Pro weekly or
yearly. Never list GPT/OpenAI as an Ask AI feature.
"""

CHECKED = "2026-10-11"


def src(cc):
    return [
        ("Brainy (App Store)", f"https://apps.apple.com/{cc}/app/id1667947372"),
        ("ChatGPT (App Store)", f"https://apps.apple.com/{cc}/app/id6448311069"),
        ("Google Gemini (App Store)", f"https://apps.apple.com/{cc}/app/id6477489729"),
        ("Claude by Anthropic (App Store)", f"https://apps.apple.com/{cc}/app/id6473753684"),
        ("Perplexity (App Store)", f"https://apps.apple.com/{cc}/app/id1668000334"),
        ("DeepSeek (App Store)", f"https://apps.apple.com/{cc}/app/id6737597349"),
        ("Ask AI (App Store)", f"https://apps.apple.com/{cc}/app/id1662608035"),
    ]


EN = {
    "group": "ai-chat", "lang": "en", "store": "us",
    "path": "best-ai-chat-apps-iphone-no-account/",
    "ct": "rl-ai-chat",
    "category": "ProductivityApplication",
    "published": CHECKED, "updated": "2026-10-23", "checked": CHECKED,
    "title": "Best AI chat apps for iPhone users without an account (2026)",
    "h1": "Best AI chat apps for iPhone without an account in 2026",
    "description": "Seven AI chat apps for iPhone compared by account, free use, price and privacy: Brainy, ChatGPT, Gemini, Claude, Perplexity, DeepSeek and Ask AI.",
    "llms": "Compares seven AI chat apps for iPhone (Brainy, ChatGPT, Gemini, Claude, Perplexity, DeepSeek, Ask AI) by account requirement, free use, subscription price and App Store privacy label. Says which model Brainy really uses.",
    "disclosure": "Brainy is made by Saga Labs, the company behind Reviewland. It is one more option in this list, not placed first because it is ours. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages. Ask AI is also ours (added on 23 October 2026, from its App Store listing).",
    "answer": [
        "To chat with an AI on iPhone without creating an account, Brainy opens straight into the chat with 20 free messages a day; it answers with DeepSeek V3.1 and reads photos with Gemini 2.5 Flash Lite. The big assistants, ChatGPT, Gemini, Claude and Perplexity, are free to start too, but their App Store listings describe history synced across your devices, which means signing in.",
        "If you want the most capable models, the official apps are better than ours: ChatGPT, Claude, Gemini and Perplexity give you their newest models, with paid plans from $8 (ChatGPT Go) to $20 a month.",
    ],
    "columns": ["App", "Price (US)", "Free use", "Account", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the US App Store in-app purchases on 11 October 2026 (Ask AI: 23 October 2026); all seven are free to download. \"Account\" is what the App Store listing says; where it does not say, we write so. Ratings are the App Store average and number of ratings that day.",
    "apps": [
        {
            "name": "Brainy AI Helper Chat & Create", "id": 1667947372, "ours": True, "anchor": "brainy",
            "developer": "Saga Ltd.",
            "row": ["Pro $6.99 a week (3-day trial) or $89.99 a year; discounted yearly $79.99", "20 messages a day", "None (anonymous sign-in you never see)",
                    "Data Used to Track You; Data Not Linked to You", "1.3.5 (29 Aug 2026)", "4.7 (3 ratings)"],
            "best_for": "quick questions, homework and rewriting text without signing up for anything.",
            "facts": [
                "Chat runs on DeepSeek V3.1; photos you send are read by Gemini 2.5 Flash Lite.",
                "Camera scanner reads text from a page and sends it to the chat; a Solve math shortcut for equations.",
                "Pro raises the limit to 500 messages a day and adds image generation with Google's Nano Banana (3 images a day).",
                "English only, iOS 18 or later, 25 MB.",
            ],
            "limits": "its App Store listing still says it uses Gemini, Claude and Grok for chat; today the chat model is DeepSeek V3.1, and the listing will be corrected with the next version. The Terms and Privacy links inside the app point to an old domain we no longer control, also fixed in that version. Only 3 ratings in the US.",
        },
        {
            "name": "ChatGPT", "id": 6448311069, "anchor": "chatgpt",
            "developer": "OpenAI", "rating": (4.83, 11178273),
            "row": ["Go $8, Plus $19.99 a month; Pro $100 to $500; credits from $4", "Free tier", "Listing says history syncs across devices",
                    "Data Linked to You", "1.2026.272 (6 Oct 2026)", "4.8 (11,178,273 ratings)"],
            "best_for": "the most complete assistant: voice, images and OpenAI's newest models.",
            "facts": [
                "Image generation and editing from a description.",
                "Advanced Voice Mode for real-time spoken conversation.",
                "60 languages, iOS 18 or later, 271 MB.",
            ],
            "limits": "its privacy label says data is linked to you, and the best models need a paid plan.",
        },
        {
            "name": "Google Gemini", "id": 6477489729, "anchor": "gemini",
            "developer": "Google", "rating": (4.72, 2330532),
            "row": ["Google AI Plus $4.99, Pro $19.99, Ultra $199.99", "Free tier", "Not stated in the listing",
                    "Data Linked to You", "1.2026.3970207 (7 Oct 2026)", "4.7 (2,330,532 ratings)"],
            "best_for": "people who live in Google apps; paid plans include Google storage.",
            "facts": [
                "Reads documents, spreadsheets, photos and videos you upload.",
                "Video generation with Gemini Omni on paid plans.",
                "70 languages, iOS 17.4 or later, 391 MB.",
            ],
            "limits": "its privacy label says data is linked to you, and video and the newest models need a paid plan.",
        },
        {
            "name": "Claude by Anthropic", "id": 6473753684, "anchor": "claude",
            "developer": "Anthropic", "rating": (4.72, 277404),
            "row": ["Pro $20 a month or $214.99 a year; Max $124.99 or $249.99 a month", "Free to try", "Not stated in the listing",
                    "Data Linked to You", "1.261009.20 (10 Oct 2026)", "4.7 (277,404 ratings)"],
            "best_for": "writing, coding and long documents.",
            "facts": [
                "Voice conversations and dictation in several languages.",
                "Research and data analysis features.",
                "32 languages, iOS 18 or later, 203 MB. Rated 17+.",
            ],
            "limits": "the free tier is limited and the paid plans are among the most expensive here.",
        },
        {
            "name": "Perplexity - AI Search & Chat", "id": 1668000334, "anchor": "perplexity",
            "developer": "Perplexity AI", "rating": (4.82, 513889),
            "row": ["Pro $20 a month or $200 a year; Max $200; credits from $5", "Free app", "Listing says it syncs across devices",
                    "Data Linked to You", "26.40.0 (8 Oct 2026)", "4.8 (513,889 ratings)"],
            "best_for": "answers with sources from the web.",
            "facts": [
                "Pro Search and Deep Research for longer questions.",
                "Uses top models from OpenAI, Anthropic, Meta and others, according to the listing.",
                "67 languages, iOS 18 or later, 178 MB.",
            ],
            "limits": "it is a search engine first, less suited to long creative chats, and its privacy label says data is linked to you.",
        },
        {
            "name": "DeepSeek - AI Assistant", "id": 6737597349, "anchor": "deepseek",
            "developer": "Hangzhou DeepSeek", "rating": (3.88, 12204),
            "row": ["Free, no in-app purchases", "Free", "Not stated in the listing",
                    "Data Linked to You", "2.6.2 (8 Oct 2026)", "3.9 (12,204 ratings)"],
            "best_for": "free use of DeepSeek's own newest model, the family Brainy also uses.",
            "facts": [
                "DeepSeek's official assistant, free with no in-app purchases.",
                "71 languages, iOS 15 or later, 80 MB.",
            ],
            "limits": "the lowest rating in this list (3.9), and its privacy label says data is linked to you.",
        },
        {
            "name": "All AI Models in One: Ask AI", "id": 1662608035, "ours": True, "anchor": "ask-ai",
            "developer": "Saga Ltd.", "rating": (5.0, 3),
            "row": ["Pro $7.99 a week or $69.99 a year (discounted yearly from $39.99)", "A few messages a day", "Not stated in the listing",
                    "Data Used to Track You; Data Linked to You", "1.4.4 (22 Oct 2026)", "5.0 (3 ratings)"],
            "best_for": "trying models from several companies (such as Gemini, Claude, Grok, DeepSeek and Perplexity Sonar) in one chat.",
            "facts": [
                "Switch model in the middle of a chat and keep the same conversation.",
                "Writes, rewrites, summarizes and translates; reads answers aloud; automatic chat titles.",
                "Pro unlocks every model, web search and a much higher daily limit.",
                "5 languages, iOS 18.6 or later, 36 MB.",
            ],
            "limits": "chat only: no images, videos or files. Its description still uses its old name, Fast AI. Only 3 ratings in the US, and its privacy label lists usage data used to track you.",
        },
    ],
    "who": [
        "<strong>You do not want to sign up for anything:</strong> Brainy.",
        "<strong>You want the strongest models and voice:</strong> ChatGPT or Claude.",
        "<strong>You want answers with web sources:</strong> Perplexity.",
        "<strong>You use Google apps every day:</strong> Gemini.",
        "<strong>You want something completely free:</strong> DeepSeek, or Brainy's 20 messages a day.",
        "<strong>You want to switch between models from several companies:</strong> Ask AI, chat only.",
    ],
    "cases": [
        "Asking a quick question on a borrowed or work phone where you do not want to log in.",
        "Scanning a page of homework and asking for an explanation (Brainy's scanner).",
        "Researching a topic with sources you can check (Perplexity).",
        "Long writing or coding sessions (Claude, ChatGPT).",
    ],
    "method": [
        "On 11 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchases, version and release date, rating and number of ratings, languages, size, minimum iOS and the privacy label. Features and account notes come from each listing. For Brainy, which is ours, we also checked the app's code: which models it calls and its daily limits. We did not invent ratings or reviews.",
    ],
    "faq": [
        ("Can I use an AI chatbot on iPhone without an account?",
         "Yes. Brainy opens without any sign-up and gives 20 free messages a day. The App Store listings of ChatGPT and Perplexity describe history synced across devices; the others do not say."),
        ("Which AI model does Brainy use?",
         "On 11 October 2026 Brainy's chat uses DeepSeek V3.1 and reads photos with Gemini 2.5 Flash Lite. Its App Store listing still names Gemini, Claude and Grok; that will be corrected with the next version."),
        ("Which AI chat app is free?",
         "DeepSeek is free with no in-app purchases. ChatGPT, Gemini, Claude and Perplexity have free tiers, and Brainy gives 20 messages a day for free."),
        ("Which AI chat app is best for privacy?",
         "None of the seven has the label Data Not Collected. Brainy needs no account. If privacy is the priority, an offline app that runs the model on the phone is a better fit."),
        ("Is Ask AI (formerly Fast AI) in this list?",
         "Yes, since 23 October 2026. It is also ours: a chat-only app with models from several companies, such as Gemini, Claude, Grok, DeepSeek and Perplexity Sonar, and a few free messages a day."),
    ],
    "sources": src("us"),
}

ES = {
    "group": "ai-chat", "lang": "es", "store": "es",
    "path": "es/mejores-apps-chat-ia-sin-cuenta-iphone/",
    "ct": "rl-ai-chat-es",
    "category": "ProductivityApplication",
    "published": CHECKED, "updated": "2026-10-23", "checked": CHECKED,
    "title": "Mejores apps de chat con IA para usar en iPhone sin cuenta (2026)",
    "h1": "Mejores apps de chat con IA para iPhone sin cuenta en 2026",
    "description": "Siete apps de chat con IA para iPhone comparadas por cuenta, uso gratis, precio y privacidad: Brainy, ChatGPT, Gemini, Claude, Perplexity, DeepSeek y Ask AI.",
    "llms": "Compara siete apps de chat con IA para iPhone (Brainy, ChatGPT, Gemini, Claude, Perplexity, DeepSeek, Ask AI) por cuenta, uso gratis, precio en euros y etiqueta de privacidad. Dice qué modelo usa de verdad Brainy.",
    "disclosure": "Brainy es de Saga Labs, la empresa que hace Reviewland. Es una opción más de la lista, no va primera por ser nuestra. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store. Ask AI también es nuestra (añadida el 23 de octubre de 2026, con los datos de su ficha del App Store).",
    "answer": [
        "Para chatear con una IA en el iPhone sin crear cuenta, Brainy entra directamente al chat con 20 mensajes gratis al día; responde con DeepSeek V3.1 y lee fotos con Gemini 2.5 Flash Lite. Los grandes asistentes, ChatGPT, Gemini, Claude y Perplexity, también se pueden empezar gratis, pero sus fichas hablan de historial sincronizado entre dispositivos, es decir, de iniciar sesión.",
        "Si quieres los modelos más potentes, las apps oficiales son mejores que la nuestra: ChatGPT, Claude, Gemini y Perplexity dan sus modelos más nuevos, con planes desde 7,99 € (ChatGPT Go) hasta unos 23 € al mes.",
    ],
    "columns": ["App", "Precio (España)", "Uso gratis", "Cuenta", "Etiqueta de privacidad", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Precios: compras dentro de la app del App Store de España el 11 de octubre de 2026 (Ask AI: 23 de octubre de 2026); las siete se descargan gratis. «Cuenta» es lo que dice la ficha; si no lo dice, lo ponemos. Valoración: media y número de valoraciones en España ese día.",
    "apps": [
        {
            "name": "Brainy AI Helper Chat & Create", "id": 1667947372, "ours": True, "anchor": "brainy",
            "developer": "Saga Ltd.",
            "row": ["Pro 7,99 € a la semana o 99,99 € al año; anual con descuento 89,99 €", "20 mensajes al día", "Ninguna (acceso anónimo que no ves)",
                    "Datos utilizados para rastrearte; datos no vinculados a ti", "1.3.5 (29 ago 2026)", "5,0 (1 valoración)"],
            "best_for": "preguntas rápidas, deberes y reescribir textos sin registrarte en nada.",
            "facts": [
                "El chat funciona con DeepSeek V3.1; las fotos que mandas las lee Gemini 2.5 Flash Lite.",
                "Escáner con la cámara que lee el texto de una página y lo pasa al chat; atajo «Solve math» para ecuaciones.",
                "Pro sube el límite a 500 mensajes al día y añade imágenes con Nano Banana de Google (3 al día).",
                "La app está solo en inglés. iOS 18 o posterior, 25 MB.",
            ],
            "limits": "su ficha del App Store aún dice que usa Gemini, Claude y Grok para el chat; hoy el modelo del chat es DeepSeek V3.1, y la ficha se corrige con la próxima versión. Los enlaces de Términos y Privacidad dentro de la app llevan a un dominio antiguo que ya no es nuestro, también arreglado en esa versión. La app está en inglés.",
        },
        {
            "name": "ChatGPT", "id": 6448311069, "anchor": "chatgpt",
            "developer": "OpenAI", "rating": (4.78, 908827),
            "row": ["Go 7,99 €, Plus 22,99 € al mes; Pro desde 102,99 €", "Plan gratis", "La ficha dice que el historial se sincroniza entre dispositivos",
                    "Datos vinculados a ti", "1.2026.272 (6 oct 2026)", "4,8 (908.827 valoraciones)"],
            "best_for": "el asistente más completo: voz, imágenes y los modelos más nuevos de OpenAI.",
            "facts": [
                "Crea y edita imágenes a partir de una descripción.",
                "Modo de voz avanzado para hablar en tiempo real.",
                "60 idiomas, iOS 18 o posterior, 271 MB.",
            ],
            "limits": "su etiqueta dice que los datos se vinculan a ti, y los mejores modelos piden plan de pago.",
        },
        {
            "name": "Google Gemini", "id": 6477489729, "anchor": "gemini",
            "developer": "Google", "rating": (4.68, 207849),
            "row": ["Google AI Plus 4,99 €, Pro 21,99 €", "Plan gratis", "La ficha no lo indica",
                    "Datos vinculados a ti", "1.2026.3970207 (7 oct 2026)", "4,7 (207.849 valoraciones)"],
            "best_for": "quien vive en las apps de Google; los planes de pago incluyen almacenamiento.",
            "facts": [
                "Lee documentos, hojas de cálculo, fotos y vídeos que subes.",
                "Vídeo con Gemini Omni en los planes de pago.",
                "70 idiomas, iOS 17.4 o posterior, 391 MB.",
            ],
            "limits": "su etiqueta dice que los datos se vinculan a ti, y el vídeo y los modelos más nuevos piden plan de pago.",
        },
        {
            "name": "Claude by Anthropic", "id": 6473753684, "anchor": "claude",
            "developer": "Anthropic", "rating": (4.67, 14676),
            "row": ["Pro 22 € al mes o 249,99 € al año; Max 149,99 € o 299,99 € al mes", "Se puede probar gratis", "La ficha no lo indica",
                    "Datos vinculados a ti", "1.261009.20 (10 oct 2026)", "4,7 (14.676 valoraciones)"],
            "best_for": "escribir, programar y trabajar con documentos largos.",
            "facts": [
                "Conversación por voz y dictado en varios idiomas.",
                "Funciones de investigación y análisis de datos.",
                "32 idiomas, iOS 18 o posterior, 203 MB.",
            ],
            "limits": "el plan gratis es limitado y los de pago están entre los más caros de la lista.",
        },
        {
            "name": "Perplexity - Búsqueda con IA", "id": 1668000334, "anchor": "perplexity",
            "developer": "Perplexity AI", "rating": (4.75, 44269),
            "row": ["Pro 22 € al mes o 229 € al año; créditos desde 6 €", "App gratis", "La ficha dice que se sincroniza entre dispositivos",
                    "Datos vinculados a ti", "26.40.0 (8 oct 2026)", "4,8 (44.269 valoraciones)"],
            "best_for": "respuestas con fuentes de la web.",
            "facts": [
                "Pro Search y Deep Research para preguntas más largas.",
                "Usa modelos de OpenAI, Anthropic, Meta y otros, según la ficha.",
                "67 idiomas, iOS 18 o posterior, 178 MB.",
            ],
            "limits": "es ante todo un buscador, menos pensado para charlas creativas largas, y su etiqueta dice que los datos se vinculan a ti.",
        },
        {
            "name": "DeepSeek - Asistente de AI", "id": 6737597349, "anchor": "deepseek",
            "developer": "Hangzhou DeepSeek", "rating": (3.7, 733),
            "row": ["Gratis, sin compras dentro", "Gratis", "La ficha no lo indica",
                    "Datos vinculados a ti", "2.6.2 (8 oct 2026)", "3,7 (733 valoraciones)"],
            "best_for": "usar gratis el modelo más nuevo de DeepSeek, la familia que también usa Brainy.",
            "facts": [
                "El asistente oficial de DeepSeek, gratis y sin compras dentro.",
                "71 idiomas, iOS 15 o posterior, 80 MB.",
            ],
            "limits": "la peor valoración de la lista (3,7), y su etiqueta dice que los datos se vinculan a ti.",
        },
        {
            "name": "Todos los modelos IA: Ask AI", "id": 1662608035, "ours": True, "anchor": "ask-ai",
            "developer": "Saga Ltd.", "rating": (5.0, 1),
            "row": ["Pro 8,99 € a la semana o 79,99 € al año (anual con descuento desde 44,99 €)", "Unos mensajes al día", "La ficha no lo indica",
                    "Datos usados para rastrearte; datos vinculados a ti", "1.4.4 (22 oct 2026)", "5,0 (1 valoración)"],
            "best_for": "probar modelos de varias empresas (como Gemini, Claude, Grok, DeepSeek y Perplexity Sonar) en un mismo chat.",
            "facts": [
                "Cambias de modelo en mitad del chat y sigues en la misma conversación.",
                "Escribe, reescribe, resume y traduce; lee las respuestas en voz alta; pone título a los chats.",
                "Pro desbloquea todos los modelos, la búsqueda web y un límite diario mucho más alto.",
                "5 idiomas, iOS 18.6 o posterior, 36 MB.",
            ],
            "limits": "solo chat: sin imágenes, vídeos ni archivos. Su descripción aún usa su nombre anterior, Fast AI. Solo 1 valoración en España, y su etiqueta de privacidad incluye datos de uso para rastrearte.",
        },
    ],
    "who": [
        "<strong>No quieres registrarte en nada:</strong> Brainy.",
        "<strong>Quieres los modelos más potentes y la voz:</strong> ChatGPT o Claude.",
        "<strong>Quieres respuestas con fuentes:</strong> Perplexity.",
        "<strong>Usas las apps de Google cada día:</strong> Gemini.",
        "<strong>Quieres algo totalmente gratis:</strong> DeepSeek, o los 20 mensajes al día de Brainy.",
        "<strong>Quieres cambiar entre modelos de varias empresas:</strong> Ask AI, solo chat.",
    ],
    "cases": [
        "Hacer una pregunta rápida en un móvil prestado o del trabajo donde no quieres iniciar sesión.",
        "Escanear una hoja de deberes y pedir que te la expliquen (escáner de Brainy).",
        "Investigar un tema con fuentes que puedas comprobar (Perplexity).",
        "Sesiones largas de escritura o programación (Claude, ChatGPT).",
    ],
    "method": [
        "El 11 de octubre de 2026 abrimos la ficha de cada app en el App Store de España y los datos de Apple: compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño, iOS mínimo y etiqueta de privacidad. Las funciones y lo de la cuenta salen de cada ficha. En Brainy, que es nuestra, miramos además el código: qué modelos usa y sus límites diarios. No inventamos valoraciones ni reseñas.",
    ],
    "faq": [
        ("¿Se puede usar un chat de IA en el iPhone sin cuenta?",
         "Sí. Brainy se abre sin registro y da 20 mensajes gratis al día. Las fichas de ChatGPT y Perplexity hablan de historial sincronizado entre dispositivos; las demás no lo dicen."),
        ("¿Qué modelo de IA usa Brainy?",
         "El 11 de octubre de 2026 el chat de Brainy usa DeepSeek V3.1 y lee las fotos con Gemini 2.5 Flash Lite. Su ficha aún nombra Gemini, Claude y Grok; se corrige con la próxima versión."),
        ("¿Qué app de chat con IA es gratis?",
         "DeepSeek es gratis y sin compras dentro. ChatGPT, Gemini, Claude y Perplexity tienen plan gratis, y Brainy da 20 mensajes al día gratis."),
        ("¿Qué app de chat con IA es mejor para la privacidad?",
         "Ninguna de las siete tiene la etiqueta «No se recopilan datos». Brainy no pide cuenta. Si la privacidad es lo primero, encaja mejor una app que ejecute el modelo en el propio móvil, sin conexión."),
        ("¿Está Ask AI (antes Fast AI) en la lista?",
         "Sí, desde el 23 de octubre de 2026. También es nuestra: solo chat, con modelos de varias empresas, como Gemini, Claude, Grok, DeepSeek y Perplexity Sonar, y unos mensajes gratis al día."),
    ],
    "sources": src("es"),
}

PAGES = [EN, ES]
