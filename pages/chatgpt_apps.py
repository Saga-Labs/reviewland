"""Best ChatGPT apps (plugins) in 2026. EN + ES. Our app: Dora AI Video (Saga Labs), in the directory since 24 Oct 2026.

Checked 2026-10-24 (all sources listed in SRC):
- Each app's listing in the ChatGPT plugin directory (chatgpt.com/plugins), read from a
  logged-in ChatGPT Plus account; the directory shows what is available to that plan and region.
- OpenAI Help Center: "Plugins in ChatGPT" (20001256), "Connected apps in ChatGPT" (11487775),
  "Notion app and setup in ChatGPT" (12532955).
- Each company's own help page, pricing page or press release (see SRC).
- Dora: doravideo.com/llms.txt (live) and the Dora listing. No Dora prices on purpose: since
  23 Oct 2026 llms.txt says prices are only published at doravideo.com/pricing.
Not used because they could not be confirmed from a primary source that day: Apple Music
(listing has no description), Higgsfield prices (pricing page did not load), Consensus account
and price rules, Booking.com and Skyscanner account rules.
Apps are ordered by use, not by score; Dora goes after Runway and Higgsfield in "video".
"""

CHECKED = "2026-10-24"
D = "https://chatgpt.com/plugins/"
PLUGIN = {
    "canva": D + "plugin_connector_68df33b1a2d081918778431a9cfca8ba",
    "figma": D + "plugin_connector_68df038e0ba48191908c8434991bbac2",
    "adobe": D + "plugin_asdk_app_69312da8e4dc81919370cb86fd172b6c",
    "runway": D + "plugin_asdk_app_6a05e3b201788191be12b590b43e6ce3",
    "higgsfield": D + "plugin_asdk_app_6a3293e129088191abf0875820e839da",
    "dora": D + "plugin_asdk_app_6ac7e595853c8191baefac6a3a2b9c24",
    "booking": D + "plugin_asdk_app_69272cb413a081919685ec3c88d1744e",
    "skyscanner": D + "plugin_asdk_app_694546cd042881919bb746a8dc300f38",
    "tripadvisor": D + "plugin_asdk_app_69050bf6de9c8191b3968f2cc08d33d6",
    "spotify": D + "plugin_asdk_app_68de829bf7648191acd70a907364c67c",
    "notion": D + "plugin_asdk_app_69c18c28f1188191bf5b8445c4ab0a2e",
    "lovable": D + "plugin_asdk_app_693a0a79ffe48191901173077edcf914",
    "consensus": D + "plugin_asdk_app_6943e6f4a928819195962de16fb9ffe4",
}

SRC = [
    ("ChatGPT plugin directory", "https://chatgpt.com/plugins"),
    ("OpenAI Help Center: Plugins in ChatGPT", "https://help.openai.com/en/articles/20001256-plugins-in-chatgpt"),
    ("OpenAI Help Center: Connected apps in ChatGPT", "https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt"),
    ("OpenAI Help Center: Notion app and setup in ChatGPT", "https://help.openai.com/en/articles/12532955-notion-app-and-setup-in-chatgpt"),
    ("Canva Help: Connect ChatGPT to Canva", "https://www.canva.com/help/connect-chatgpt-to-canva/"),
    ("Figma Help: ChatGPT and Figma", "https://help.figma.com/hc/en-us/articles/35326636109975"),
    ("Adobe newsroom, 10 Dec 2025", "https://news.adobe.com/news/2025/12/adobe-photoshop-express-acrobat-chatgpt"),
    ("Runway pricing", "https://runway.com/pricing"),
    ("Dora llms.txt", "https://doravideo.com/llms.txt"),
    ("Tripadvisor in ChatGPT (FAQ)", "https://www.tripadvisor.com/ChatGPT"),
    ("Travolution: Skyscanner launches app in ChatGPT for UK and US, 27 Feb 2026", "https://www.travolution.com/news/travel-sectors/intermediaries/skyscanner-launches-app-in-chatgpt-for-uk-and-us/"),
    ("Spotify newsroom, 6 Oct 2025 (with later updates)", "https://newsroom.spotify.com/2025-10-06/spotify-personalized-prompts-chatgpt/"),
    ("Lovable docs: ChatGPT app", "https://docs.lovable.dev/tips-tricks/chatgpt-app"),
    ("Lovable pricing", "https://lovable.dev/pricing"),
] + [(f"Directory listing: {k}", v) for k, v in PLUGIN.items()]


def a(href, text):
    return f'<a href="{href}">{text}</a>'


# ------------------------------------------------------------------ EN
EN_APPS = [
    {
        "name": "Canva", "anchor": "canva", "developer": "Canva Pty Ltd.", "url": PLUGIN["canva"],
        "row": ["Design", "Presentations, posters, social posts and other designs from a brief; image generation, background removal, resizing", "Canva account; Canva Free works", "Free with Canva Free; Brand Templates need a paid Canva plan, data autofill needs Canva Enterprise", "Business and Enterprise: the workspace admin must enable apps first", "Canva Pty Ltd."],
        "best_for": "turning a brief or notes into a deck, poster or social post you can keep editing in Canva.",
        "facts": [
            "The listing says it can create designs from a brief, outline or draft copy (presentation, doc, poster, flyer, social post, resume), generate images, remove backgrounds, resize a design for Facebook, Instagram and LinkedIn, and bulk-create designs from spreadsheet data with a brand template.",
            "Canva's help page says the plugin is available for all Canva accounts, including Canva Free and Canva Education.",
            "Canva's help page: some actions, such as Brand Templates, need a paid plan (Pro, Teams, Business, Nonprofit, Enterprise or Education); data autofill needs Canva Enterprise.",
        ],
        "limits": "on ChatGPT Business or Enterprise an admin has to enable apps first, and on a Canva team an admin may need to allow AI assistants to connect.",
    },
    {
        "name": "Figma", "anchor": "figma", "developer": "Figma, Inc.", "url": PLUGIN["figma"],
        "row": ["Design", "FigJam diagrams and Figma Slides decks from a chat; product screens sent to Figma as editable layers (listing)", "You may be asked to log in or sign up for Figma", "Any Figma plan; Slides is in beta with usage limits, largest allowance on full paid seats", "Not available in the EU (Figma Help)", "Figma, Inc."],
        "best_for": "flowcharts, diagrams and slide decks that land in Figma as editable files.",
        "facts": [
            "The listing says you can create and edit decks in Figma Slides, generate diagrams in FigJam, and send product screens to Figma as editable layers.",
            "Figma's help page: available on any Figma plan; the Figma Slides integration is in beta and may have usage limits; full seats on paid plans get the largest allowance.",
            "Figma's help page: files you have not claimed are visible to anyone with the link; sign in and add them to your drafts to keep them private.",
        ],
        "limits": "Figma's help page says it is not available in the EU and cannot create files for Figma's other products.",
    },
    {
        "name": "Adobe", "anchor": "adobe", "developer": "Adobe Inc.", "url": PLUGIN["adobe"],
        "row": ["Design, photos and PDF", "Photo edits, Express templates, PDF creation and editing, video resizing", "Not required: you can start as a guest; an Adobe account adds storage and saved work", "Adobe announced the apps as free to ChatGPT users (10 Dec 2025)", "Adobe: available worldwide on ChatGPT desktop, web and iOS at launch", "Adobe Inc."],
        "best_for": "quick photo edits, a flyer from a template, or merging and editing PDFs without opening another app.",
        "facts": [
            "The listing says Adobe was previously available as Photoshop and now brings Creative Cloud and Acrobat capabilities: editing photos, creating PDFs, designing social assets, resizing videos and starting from Express templates.",
            "The listing: you can get started as a guest and sign in with an Adobe account for more tools, Creative Cloud storage and saved work.",
            "Adobe's 10 December 2025 release says Photoshop, Adobe Express and Acrobat in ChatGPT are free to ChatGPT users globally, on desktop, web and iOS; Express also on Android.",
        ],
        "limits": "Adobe's release said Photoshop and Acrobat on Android were coming later; more advanced work still means opening the full Adobe apps.",
    },
    {
        "name": "Runway", "anchor": "runway", "developer": "Runway AI, Inc.", "url": PLUGIN["runway"],
        "row": ["Video, image and audio", "Generate and edit images, video and audio; animate a photo, upscale, voiceover, music", "Runway account", "Uses Runway credits: Free plan 125 one-time credits; Standard $15/month (625 credits)", "Not stated", "Runway AI, Inc."],
        "best_for": "people who already use Runway and want its video and editing tools inside a chat.",
        "facts": [
            "The listing says you generate and edit images, videos and audio using your Runway account: animate images into video, edit footage, expand to new aspect ratios, multi-shot story videos, remove backgrounds, upscale, convert to HDR, generate music, sound effects and voiceover, and check remaining credits and plan.",
            "Runway's pricing page: Free $0 with 125 credits once; Standard $15 a month ($12 billed yearly) with 625 credits a month; Pro $35 ($28) with 2,250; Max $95 ($76) with 9,500.",
        ],
        "limits": "every generation spends Runway credits from your own Runway plan; the free credits are given once, not every month.",
    },
    {
        "name": "Higgsfield", "anchor": "higgsfield", "developer": "Higgsfield AI, Inc.", "url": PLUGIN["higgsfield"],
        "row": ["Video and image", "Images, videos and product ads from text, a product photo or reference media; presets and motion transfer", "Higgsfield account", "Uses your Higgsfield plan (we could not confirm current prices)", "Not stated", "Higgsfield AI, Inc."],
        "best_for": "short product ads and effect-driven clips with ready-made presets.",
        "facts": [
            "The listing says you can generate images and videos from text or references, turn product photos into promotional visuals and short video ads (Marketing Studio), browse presets with commands such as /effects and /product, and transfer motion from a reference video (Genjutsu).",
            "The listing says: connect your Higgsfield account to get started.",
        ],
        "limits": "Higgsfield's pricing page did not load for us on 24 October 2026, so this page does not state its prices.",
    },
    {
        "name": "Dora AI Video", "anchor": "dora", "ours": True, "developer": "Saga Labs", "url": PLUGIN["dora"],
        "row": ["Video and image", "Short videos from a photo or an idea, images, the same character across clips, vertical, horizontal or square", "Dora account", "Dora Pro subscription, no free tier; prices only on doravideo.com/pricing", "Not stated", "Saga Labs"],
        "best_for": "turning a product photo or portrait into a short vertical clip for TikTok, Reels or Shorts.",
        "facts": [
            "The listing says Dora brings a photo to life as a short video, creates images from a description or a reference photo, keeps the same character across a series of clips, offers vertical, horizontal or square, and copies the moves of a dance video onto the person in your photo.",
            "The listing says images arrive in about a minute and videos in about two, and everything you make is also saved to your gallery at doravideo.com and in the Dora iPhone app.",
            "Per doravideo.com/llms.txt: one paid plan (Dora Pro) with a weekly credit allowance and unlimited Dora image generation; no free tier; top-up credits never expire; the same balance is shared across web, iOS and other AI clients.",
        ],
        "limits": "there is no free tier, and Dora does not publish or schedule posts to TikTok, Instagram or YouTube: you download the file and post it yourself. The listing says it does not create sexual content, content involving minors or graphic violence.",
    },
    {
        "name": "Booking.com", "anchor": "booking", "developer": "Booking.com B.V.", "url": PLUGIN["booking"],
        "row": ["Travel", "Search stays, attractions and rental cars", "Not stated", "Not stated; you book and pay on Booking.com", "Not stated", "Booking.com B.V."],
        "best_for": "browsing places to stay, attractions and car rental in a conversation before booking.",
        "facts": [
            "The listing says you can explore stays, attractions and rental cars, then tap \"View on Booking.com\" to book.",
        ],
        "limits": "the booking itself happens on Booking.com, not in ChatGPT.",
    },
    {
        "name": "Skyscanner", "anchor": "skyscanner", "developer": "Skyscanner Limited", "url": PLUGIN["skyscanner"],
        "row": ["Travel", "Compare flight fares from airlines and travel providers", "Not stated", "Not stated; you book with the airline or provider", "Launched in the UK and US (Travolution, Feb 2026)", "Skyscanner Limited"],
        "best_for": "comparing flight prices with plain-language requests and follow-ups on dates or airports.",
        "facts": [
            "The listing says Skyscanner scans airlines and travel providers to compare fares, and you book directly with the provider.",
            "Travolution reported on 27 February 2026 that the app launched in the UK and US.",
        ],
        "limits": "flights only in this listing, and booking happens on the provider's site.",
    },
    {
        "name": "Tripadvisor", "anchor": "tripadvisor", "developer": "Tripadvisor", "url": PLUGIN["tripadvisor"],
        "row": ["Travel", "Hotel search on a map with traveler reviews, photos and price offers", "No Tripadvisor account needed to browse", "Not stated; you book with a booking partner", "Logged-in users in the US on Free, Go, Plus and Pro (Tripadvisor FAQ)", "Tripadvisor"],
        "best_for": "choosing a hotel by neighborhood with reviews and prices from several booking sites side by side.",
        "facts": [
            "The listing describes a map-first view of top-rated hotels with traveler photos, recent reviews, amenities and price offers, and click-out to booking partners.",
            "Tripadvisor's FAQ: available to all logged-in ChatGPT users in the United States on Free, Go, Plus and Pro plans; no Tripadvisor account needed to browse; works on desktop, mobile web, tablet, iOS and Android.",
            "Tripadvisor says it works with 400+ booking sites and hotel partners.",
        ],
        "limits": "Tripadvisor says the app is only available to users in the United States for now (you can search hotels anywhere).",
    },
    {
        "name": "Spotify", "anchor": "spotify", "developer": "Spotify", "url": PLUGIN["spotify"],
        "row": ["Music", "Music, podcast and audiobook recommendations and playlists", "Spotify account (you connect it on first use)", "Works with Spotify Free; personalized playlists from detailed prompts need Premium", "Launched for ChatGPT Free, Plus and Pro in 145 countries; later UK, Switzerland and the EU (Spotify)", "Spotify"],
        "best_for": "getting a playlist for a run, study session or party from a description.",
        "facts": [
            "Spotify's newsroom (6 October 2025): Free users get picks from Spotify's existing playlists; Premium users get a new, personalized selection from more detailed prompts.",
            "Spotify's newsroom: launched in English in 145 countries for logged-in ChatGPT Free, Plus and Pro accounts; later updates add the UK, Switzerland and the EU, and French, Italian, German, Spanish and Portuguese.",
            "Spotify says it does not share its audio or video content with OpenAI for training.",
        ],
        "limits": "the most personalized playlists need Spotify Premium.",
    },
    {
        "name": "Notion", "anchor": "notion", "developer": "Notion", "url": PLUGIN["notion"],
        "row": ["Productivity", "Search your Notion pages and databases; create and update pages (listing)", "Notion account", "Not stated", "Depends on ChatGPT plan, workspace settings and Notion permissions (OpenAI Help)", "Notion"],
        "best_for": "asking questions about your team's Notion pages and saving chat results back as pages.",
        "facts": [
            "The listing says you can search your workspace, create and update pages, and save research, plans and notes as pages.",
            "OpenAI's help article: ChatGPT can only read pages your connected Notion account can already access; availability depends on your ChatGPT plan, workspace configuration and Notion permissions.",
        ],
        "limits": "an admin cannot give you access to pages your Notion account cannot see, and with several workspaces you must authorize the right one.",
    },
    {
        "name": "Lovable", "anchor": "lovable", "developer": "Lovable Labs", "url": PLUGIN["lovable"],
        "row": ["Code", "Builds full-stack web apps from a description, with a live preview", "Lovable account (you connect the app on first use)", "Lovable credits, charged only when it starts building; Free plan has 5 build credits a day (up to 30 a month)", "Not stated", "Lovable Labs"],
        "best_for": "going from an idea in a chat to a working first version of a web app or landing page.",
        "facts": [
            "The listing says Lovable writes TypeScript, Tailwind and shadcn/ui code, returns a live preview, and lets you refine the app with follow-up messages.",
            "Lovable's docs: you are not charged credits until you send the prompt to Lovable and it begins to build.",
            "Lovable's pricing page: the free plan includes 5 build credits a day, up to 30 a month.",
        ],
        "limits": "Lovable's docs say that for the initial release you need to open Lovable to keep editing the project.",
    },
    {
        "name": "Consensus", "anchor": "consensus", "developer": "Consensus", "url": PLUGIN["consensus"],
        "row": ["Research", "Search peer-reviewed research; paper details such as authors, journal, year, citations, abstract and DOI", "Not stated", "Not stated", "Not stated", "Consensus"],
        "best_for": "checking what published studies say on a question, with the papers listed.",
        "facts": [
            "The listing says you can search peer-reviewed research and review paper details such as authors, journal, year, citation count, abstract and DOI when available.",
        ],
        "limits": "we could not confirm from Consensus or OpenAI whether the ChatGPT app needs a Consensus account or a paid plan.",
    },
]

EN = {
    "group": "chatgpt-apps", "cover": "ai-chat", "lang": "en", "store": "us",
    "path": "best-chatgpt-apps-plugins/", "ct": "rl-chatgpt-apps",
    "category": "ProductivityApplication", "os": "ChatGPT (web, desktop, iOS, Android)",
    "checked_label": "Data checked in the ChatGPT plugin directory and each company's docs on",
    "link_label": "Listing in the ChatGPT plugin directory",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best ChatGPT apps (plugins) in 2026, by use: design, video, travel, music, code",
    "h1": "Best ChatGPT apps (plugins) in 2026",
    "description": "13 apps from the ChatGPT plugin directory grouped by use: Canva, Figma, Adobe, Runway, Booking.com, Tripadvisor, Spotify, Notion, Lovable and more. Account, cost and availability checked.",
    "llms": "13 apps from the ChatGPT plugin directory grouped by use (design, video, travel, music, productivity, code, research), with what each does, which account it needs, whether it costs extra, where it is available and who makes it, each with its source.",
    "disclosure": "Dora AI Video is made by Saga Labs, the company behind Reviewland.",
    "answer": [
        "There is no single best ChatGPT app: each one connects ChatGPT to one service. For design, Canva, Figma and Adobe are in the directory; for video, Runway, Higgsfield and Dora; for travel, Booking.com, Skyscanner and Tripadvisor; for music, Spotify; for work, Notion; for building web apps, Lovable; for research papers, Consensus.",
        "Most of them work with your account at that company and its own plan. Adobe announced its apps as free to ChatGPT users, Canva works with Canva Free, and Tripadvisor needs no account to browse. Video generators (Runway, Higgsfield, Dora) spend credits from their own paid plans.",
        "Apps now live in ChatGPT's plugin directory (Plugins in the sidebar). OpenAI says the directory is visible on every ChatGPT plan, but whether you can install or use a given plugin depends on your plan, workspace, role, region and the plugin itself.",
    ],
    "columns": ["App", "Use", "What it does in ChatGPT", "Account needed", "Extra cost", "Plans and regions", "Made by"],
    "table_note": "Grouped by use, not ranked by quality. \"Not stated\" means neither the directory listing nor the company's own pages said so on 24 October 2026. Listings were read from a ChatGPT Plus account; the directory only shows plugins available to your plan and region.",
    "apps": EN_APPS,
    "who": [
        "<strong>You make slides, posters or social posts:</strong> Canva; Figma for diagrams and Figma Slides; Adobe for photo edits and PDFs.",
        "<strong>You want video from a prompt or a photo:</strong> Runway or Higgsfield if you already pay for them; Dora for short vertical clips from a photo.",
        "<strong>You are planning a trip:</strong> Skyscanner for flights, Booking.com for stays, attractions and cars, Tripadvisor for hotels with reviews (US only).",
        "<strong>You want music:</strong> Spotify (Premium for fully personalized playlists).",
        "<strong>You work in Notion, or want to build a web app:</strong> Notion; Lovable.",
        "<strong>You need studies, not opinions:</strong> Consensus.",
    ],
    "cases": [
        "Turning meeting notes into a pitch deck (Canva, Figma Slides).",
        "Merging and editing PDFs or a quick photo fix without opening another app (Adobe).",
        "A product photo turned into a short ad clip (Runway, Higgsfield, Dora).",
        "Comparing flights and hotels for one trip in one chat (Skyscanner, Booking.com, Tripadvisor).",
        "A first version of a landing page or internal tool (Lovable).",
    ],
    "method": [
        "On 24 October 2026 we opened each app's listing in the ChatGPT plugin directory (chatgpt.com/plugins) from a ChatGPT Plus account, and read OpenAI's help articles on plugins and connected apps. For account rules, extra cost and availability we used only each company's own help page, pricing page or press release, plus one trade report for Skyscanner's launch markets. If neither said something, the table says \"Not stated\". We did not test every app, and we left out apps whose listing or rules we could not confirm (for example Apple Music, whose listing had no description that day).",
        "Dora is ours; its data comes from its directory listing and doravideo.com/llms.txt, which publishes no prices (they are only on doravideo.com/pricing).",
    ],
    "faq": [
        ("What are ChatGPT apps or plugins?",
         "They connect ChatGPT to another service, such as Canva, Spotify or Booking.com, so you can use it from a chat. They are listed in ChatGPT's plugin directory, under Plugins in the sidebar on web, desktop and mobile; OpenAI notes that very old versions of the iOS or Android app may still show Apps instead of Plugins."),
        ("Do ChatGPT apps cost extra?",
         "It depends on the app. Adobe announced its apps as free to ChatGPT users, Canva works with a free Canva account and Tripadvisor needs no account to browse. Others use your plan with that company: Runway and Lovable spend their own credits, Spotify needs Premium for its most personalized playlists, and Dora needs a Dora Pro subscription."),
        ("Do ChatGPT apps work on the free ChatGPT plan?",
         "Some do. Tripadvisor says it works for logged-in US users on Free, Go, Plus and Pro, and Spotify launched for Free, Plus and Pro. OpenAI says the directory is visible on every plan, but installing or using each plugin depends on your plan, workspace, role and region."),
        ("Which ChatGPT apps can make videos?",
         "In the directory on 24 October 2026: Runway, Higgsfield and Dora AI Video, among others. Each uses its own account and credits; Adobe can also resize videos."),
        ("Are ChatGPT apps available in Europe?",
         "Not all of them. Figma says its integration is not available in the EU and Tripadvisor's app is US-only for now, while Spotify says it added the UK, Switzerland and the EU after launch. Check each listing from your own account."),
    ],
    "sources": SRC,
}

# ------------------------------------------------------------------ ES
ES_ROWS = {
    "canva": (["Diseño", "Presentaciones, carteles, posts y otros diseños a partir de un briefing; generar imágenes, quitar fondos, cambiar tamaño", "Cuenta de Canva; sirve Canva Free", "Gratis con Canva Free; las plantillas de marca piden un plan de pago y el autorrelleno de datos, Canva Enterprise", "Business y Enterprise: el administrador debe activar las apps", "Canva Pty Ltd."],
              "convertir un briefing o unas notas en una presentación, un cartel o un post que sigues editando en Canva.",
              ["La ficha dice que crea diseños a partir de un briefing, un esquema o un borrador (presentación, documento, cartel, flyer, post, currículum), genera imágenes, quita fondos, adapta un diseño a Facebook, Instagram y LinkedIn y crea diseños en lote desde una hoja de cálculo con una plantilla de marca.",
               "La ayuda de Canva dice que funciona con todas las cuentas de Canva, también Canva Free y Canva Education.",
               "La ayuda de Canva: algunas acciones, como las plantillas de marca, piden un plan de pago (Pro, Teams, Business, Nonprofit, Enterprise o Education); el autorrelleno de datos pide Canva Enterprise."],
              "en ChatGPT Business o Enterprise un administrador tiene que activar las apps, y en un equipo de Canva puede que tenga que permitir que se conecten asistentes de IA."),
    "figma": (["Diseño", "Diagramas de FigJam y presentaciones de Figma Slides desde el chat; pantallas enviadas a Figma como capas editables (ficha)", "Puede pedirte entrar o crear cuenta de Figma", "Cualquier plan de Figma; Slides está en beta con límites de uso, más uso en asientos completos de pago", "No disponible en la UE (ayuda de Figma)", "Figma, Inc."],
              "diagramas de flujo y presentaciones que acaban en Figma como archivos editables.",
              ["La ficha dice que crea y edita presentaciones en Figma Slides, genera diagramas en FigJam y manda pantallas a Figma como capas editables.",
               "La ayuda de Figma: disponible en cualquier plan; la integración con Figma Slides está en beta y puede tener límites de uso; los asientos completos de pago tienen el mayor margen.",
               "La ayuda de Figma: los archivos que no reclamas los ve cualquiera con el enlace; entra y añádelos a tus borradores para que sean privados."],
              "la ayuda de Figma dice que no está disponible en la UE y que no crea archivos de los demás productos de Figma."),
    "adobe": (["Diseño, fotos y PDF", "Retoque de fotos, plantillas de Express, crear y editar PDF, cambiar el tamaño de vídeos", "No hace falta: puedes empezar como invitado; con cuenta de Adobe tienes almacenamiento y trabajo guardado", "Adobe las anunció gratis para los usuarios de ChatGPT (10 dic 2025)", "Adobe: en todo el mundo en ChatGPT escritorio, web e iOS al lanzarse", "Adobe Inc."],
              "retocar una foto, sacar un flyer de una plantilla o unir y editar PDF sin abrir otra app.",
              ["La ficha dice que antes se llamaba Photoshop y que ahora trae funciones de Creative Cloud y Acrobat: editar fotos, crear PDF, diseñar piezas para redes, cambiar el tamaño de vídeos y partir de plantillas de Express.",
               "La ficha: puedes empezar como invitado y entrar con tu cuenta de Adobe para tener más herramientas, almacenamiento en Creative Cloud y trabajo guardado.",
               "La nota de prensa de Adobe del 10 de diciembre de 2025 dice que Photoshop, Adobe Express y Acrobat en ChatGPT son gratis para los usuarios de ChatGPT de todo el mundo, en escritorio, web e iOS; Express también en Android."],
              "según la nota de Adobe, Photoshop y Acrobat para Android llegarían más tarde; para trabajos avanzados hay que abrir las apps completas de Adobe."),
    "runway": (["Vídeo, imagen y audio", "Generar y editar imágenes, vídeo y audio; animar una foto, mejorar resolución, voz en off, música", "Cuenta de Runway", "Gasta créditos de Runway: plan Free con 125 créditos una vez; Standard 15 $/mes (625 créditos)", "No consta", "Runway AI, Inc."],
               "quien ya usa Runway y quiere sus herramientas de vídeo dentro de un chat.",
               ["La ficha dice que generas y editas imágenes, vídeos y audio con tu cuenta de Runway: animar imágenes, editar metraje, ampliar a otros formatos, vídeos de varias tomas, quitar fondos, mejorar resolución, pasar a HDR, generar música, efectos y voz, y consultar créditos y plan.",
                "Página de precios de Runway: Free 0 $ con 125 créditos una sola vez; Standard 15 $ al mes (12 $ pagando al año) con 625 créditos al mes; Pro 35 $ (28 $) con 2.250; Max 95 $ (76 $) con 9.500."],
               "cada generación gasta créditos de tu plan de Runway; los créditos gratis se dan una vez, no cada mes."),
    "higgsfield": (["Vídeo e imagen", "Imágenes, vídeos y anuncios de producto desde texto, una foto de producto o referencias; presets y transferencia de movimiento", "Cuenta de Higgsfield", "Usa tu plan de Higgsfield (no pudimos confirmar los precios actuales)", "No consta", "Higgsfield AI, Inc."],
                   "anuncios cortos de producto y clips con efectos a partir de presets.",
                   ["La ficha dice que genera imágenes y vídeos desde texto o referencias, convierte fotos de producto en piezas promocionales y anuncios cortos (Marketing Studio), tiene presets con comandos como /effects y /product y transfiere el movimiento de un vídeo de referencia (Genjutsu).",
                    "La ficha dice: conecta tu cuenta de Higgsfield para empezar."],
                   "la página de precios de Higgsfield no nos cargó el 24 de octubre de 2026, así que aquí no ponemos sus precios."),
    "dora": (["Vídeo e imagen", "Vídeos cortos desde una foto o una idea, imágenes, el mismo personaje en varios clips, vertical, horizontal o cuadrado", "Cuenta de Dora", "Suscripción Dora Pro, sin plan gratis; precios solo en doravideo.com/pricing", "No consta", "Saga Labs"],
             "convertir una foto de producto o un retrato en un clip vertical corto para TikTok, Reels o Shorts.",
             ["La ficha dice que Dora da vida a una foto como vídeo corto, crea imágenes desde una descripción o una foto de referencia, mantiene el mismo personaje en una serie de clips, permite vertical, horizontal o cuadrado y copia los pasos de un vídeo de baile a la persona de tu foto.",
              "La ficha dice que las imágenes llegan en un minuto más o menos y los vídeos en unos dos, y que todo se guarda también en tu galería de doravideo.com y en la app de Dora para iPhone.",
              "Según doravideo.com/llms.txt: un solo plan de pago (Dora Pro) con créditos cada semana e imágenes de Dora ilimitadas; no hay plan gratis; los créditos extra no caducan; el mismo saldo vale en la web, en iOS y en otros clientes de IA."],
             "no hay plan gratis, y Dora no publica ni programa en TikTok, Instagram o YouTube: descargas el archivo y lo subes tú. La ficha dice que no crea contenido sexual, con menores ni violencia explícita."),
    "booking": (["Viajes", "Buscar alojamientos, actividades y coches de alquiler", "No consta", "No consta; reservas y pagas en Booking.com", "No consta", "Booking.com B.V."],
                "mirar alojamientos, actividades y coches de alquiler en una conversación antes de reservar.",
                ["La ficha dice que puedes explorar alojamientos, actividades y coches de alquiler y pulsar \"View on Booking.com\" para reservar."],
                "la reserva se hace en Booking.com, no en ChatGPT."),
    "skyscanner": (["Viajes", "Comparar precios de vuelos de aerolíneas y agencias", "No consta", "No consta; reservas con la aerolínea o la agencia", "Se lanzó en Reino Unido y EE. UU. (Travolution, feb 2026)", "Skyscanner Limited"],
                   "comparar precios de vuelos pidiéndolo con tus palabras y cambiando fechas o aeropuertos sobre la marcha.",
                   ["La ficha dice que Skyscanner busca en aerolíneas y agencias para comparar tarifas y que reservas directamente con el proveedor.",
                    "Travolution publicó el 27 de febrero de 2026 que la app se lanzó en Reino Unido y Estados Unidos."],
                   "en esta ficha solo hay vuelos, y la reserva se hace en la web del proveedor."),
    "tripadvisor": (["Viajes", "Buscar hoteles en un mapa con opiniones, fotos y ofertas de precio", "Sin cuenta de Tripadvisor para mirar", "No consta; reservas con una web de reservas", "Usuarios con sesión en EE. UU. con Free, Go, Plus y Pro (FAQ de Tripadvisor)", "Tripadvisor"],
                    "elegir hotel por barrio con opiniones y precios de varias webs de reserva a la vez.",
                    ["La ficha describe una vista de mapa con hoteles bien valorados, fotos de viajeros, opiniones recientes, servicios y ofertas de precio, y salida a las webs de reserva.",
                     "FAQ de Tripadvisor: disponible para todos los usuarios de ChatGPT con sesión iniciada en Estados Unidos con los planes Free, Go, Plus y Pro; no hace falta cuenta de Tripadvisor para mirar; funciona en escritorio, web móvil, tableta, iOS y Android.",
                     "Tripadvisor dice que trabaja con más de 400 webs de reserva y hoteles."],
                    "Tripadvisor dice que de momento solo está disponible para usuarios de Estados Unidos (se pueden buscar hoteles de todo el mundo)."),
    "spotify": (["Música", "Recomendaciones y listas de música, pódcasts y audiolibros", "Cuenta de Spotify (la conectas la primera vez)", "Funciona con Spotify Free; las listas personalizadas a partir de peticiones detalladas piden Premium", "Se lanzó para ChatGPT Free, Plus y Pro en 145 países; después Reino Unido, Suiza y la UE (Spotify)", "Spotify"],
                "sacar una lista para correr, estudiar o una fiesta a partir de una descripción.",
                ["Nota de Spotify (6 de octubre de 2025): los usuarios Free reciben listas que ya existen en Spotify; los Premium, una selección nueva y personalizada a partir de peticiones más detalladas.",
                 "Nota de Spotify: se lanzó en inglés en 145 países para cuentas de ChatGPT Free, Plus y Pro; actualizaciones posteriores añaden Reino Unido, Suiza y la UE, y francés, italiano, alemán, español y portugués.",
                 "Spotify dice que no comparte su contenido de audio o vídeo con OpenAI para entrenar."],
                "las listas más personalizadas piden Spotify Premium."),
    "notion": (["Productividad", "Buscar en tus páginas y bases de datos de Notion; crear y actualizar páginas (ficha)", "Cuenta de Notion", "No consta", "Depende del plan de ChatGPT, del espacio de trabajo y de los permisos de Notion (ayuda de OpenAI)", "Notion"],
               "preguntar por las páginas de Notion de tu equipo y guardar lo que sale del chat como páginas.",
               ["La ficha dice que puedes buscar en tu espacio de trabajo, crear y actualizar páginas y guardar investigaciones, planes y notas como páginas.",
                "Ayuda de OpenAI: ChatGPT solo lee las páginas a las que ya tiene acceso tu cuenta de Notion conectada; la disponibilidad depende de tu plan de ChatGPT, del espacio de trabajo y de los permisos de Notion."],
               "un administrador no puede darte acceso a páginas que tu cuenta de Notion no ve, y si tienes varios espacios de trabajo tienes que autorizar el correcto."),
    "lovable": (["Código", "Construye aplicaciones web completas a partir de una descripción, con vista previa en vivo", "Cuenta de Lovable (conectas la app la primera vez)", "Créditos de Lovable, solo cuando empieza a construir; el plan gratis da 5 créditos al día (hasta 30 al mes)", "No consta", "Lovable Labs"],
                "pasar de una idea en el chat a una primera versión de una web o una landing que funciona.",
                ["La ficha dice que Lovable escribe código TypeScript, Tailwind y shadcn/ui, devuelve una vista previa en vivo y deja afinar la app con más mensajes.",
                 "Documentación de Lovable: no se cobran créditos hasta que mandas la petición a Lovable y empieza a construir.",
                 "Página de precios de Lovable: el plan gratis da 5 créditos de construcción al día, hasta 30 al mes."],
                "la documentación de Lovable dice que, en esta primera versión, para seguir editando el proyecto hay que abrir Lovable."),
    "consensus": (["Investigación", "Buscar estudios revisados por pares; datos del artículo como autores, revista, año, citas, resumen y DOI", "No consta", "No consta", "No consta", "Consensus"],
                  "ver qué dicen los estudios publicados sobre una pregunta, con los artículos a la vista.",
                  ["La ficha dice que busca investigación revisada por pares y muestra datos de cada artículo como autores, revista, año, número de citas, resumen y DOI cuando los hay."],
                  "no pudimos confirmar ni con Consensus ni con OpenAI si la app de ChatGPT pide cuenta de Consensus o un plan de pago."),
}


def es_app(en_app):
    row, best, facts, limits = ES_ROWS[en_app["anchor"]]
    out = {k: v for k, v in en_app.items() if k not in ("row", "facts", "best_for", "limits")}
    out.update(row=row, best_for=best, facts=facts, limits=limits)
    return out


ES = dict(EN, **{
    "lang": "es", "store": "es",
    "path": "es/mejores-apps-de-chatgpt-plugins/", "ct": "rl-chatgpt-apps-es",
    "checked_label": "Datos comprobados en el directorio de plugins de ChatGPT y en la documentación de cada empresa el",
    "link_label": "Ficha en el directorio de plugins de ChatGPT",
    "title": "Mejores apps de ChatGPT (plugins) en 2026, por uso: diseño, vídeo, viajes, música, código",
    "h1": "Mejores apps de ChatGPT (plugins) en 2026",
    "description": "13 apps del directorio de plugins de ChatGPT agrupadas por uso: Canva, Figma, Adobe, Runway, Booking.com, Tripadvisor, Spotify, Notion, Lovable y más. Cuenta, coste y disponibilidad comprobados.",
    "llms": "13 apps del directorio de plugins de ChatGPT agrupadas por uso (diseño, vídeo, viajes, música, productividad, código, investigación): qué hace cada una, qué cuenta pide, si cobra aparte, dónde está disponible y quién la hace, con la fuente de cada dato.",
    "disclosure": "Dora AI Video es de Saga Labs, la empresa que hace Reviewland.",
    "answer": [
        "No hay una única mejor app de ChatGPT: cada una conecta ChatGPT con un servicio. Para diseño están Canva, Figma y Adobe; para vídeo, Runway, Higgsfield y Dora; para viajes, Booking.com, Skyscanner y Tripadvisor; para música, Spotify; para trabajo, Notion; para hacer webs, Lovable; para estudios científicos, Consensus.",
        "La mayoría funciona con tu cuenta en esa empresa y su propio plan. Adobe anunció sus apps gratis para los usuarios de ChatGPT, Canva funciona con Canva Free y Tripadvisor no pide cuenta para mirar. Los generadores de vídeo (Runway, Higgsfield, Dora) gastan créditos de sus propios planes de pago.",
        "Las apps están ahora en el directorio de plugins de ChatGPT (Plugins, en la barra lateral). OpenAI dice que el directorio se ve en todos los planes, pero que poder instalar o usar cada plugin depende del plan, del espacio de trabajo, del rol, de la región y del propio plugin.",
    ],
    "columns": ["App", "Uso", "Qué hace en ChatGPT", "Cuenta necesaria", "Coste aparte", "Planes y regiones", "Quién la hace"],
    "table_note": "Agrupadas por uso, no ordenadas por calidad. \"No consta\" quiere decir que ni la ficha del directorio ni las páginas de la empresa lo decían el 24 de octubre de 2026. Las fichas se leyeron desde una cuenta de ChatGPT Plus; el directorio solo enseña los plugins disponibles para tu plan y tu región.",
    "apps": [es_app(x) for x in EN_APPS],
    "who": [
        "<strong>Haces presentaciones, carteles o posts:</strong> Canva; Figma para diagramas y Figma Slides; Adobe para retocar fotos y PDF.",
        "<strong>Quieres vídeo a partir de un texto o una foto:</strong> Runway o Higgsfield si ya los pagas; Dora para clips verticales cortos desde una foto.",
        "<strong>Estás preparando un viaje:</strong> Skyscanner para vuelos, Booking.com para alojamiento, actividades y coches, Tripadvisor para hoteles con opiniones (solo EE. UU.).",
        "<strong>Quieres música:</strong> Spotify (Premium para listas del todo personalizadas).",
        "<strong>Trabajas en Notion o quieres hacer una web:</strong> Notion; Lovable.",
        "<strong>Necesitas estudios, no opiniones:</strong> Consensus.",
    ],
    "cases": [
        "Convertir las notas de una reunión en una presentación (Canva, Figma Slides).",
        "Unir y editar PDF o retocar una foto sin abrir otra app (Adobe).",
        "Una foto de producto convertida en un anuncio corto (Runway, Higgsfield, Dora).",
        "Comparar vuelos y hoteles de un viaje en el mismo chat (Skyscanner, Booking.com, Tripadvisor).",
        "Una primera versión de una landing o una herramienta interna (Lovable).",
    ],
    "method": [
        "El 24 de octubre de 2026 abrimos la ficha de cada app en el directorio de plugins de ChatGPT (chatgpt.com/plugins) desde una cuenta de ChatGPT Plus y leímos los artículos de ayuda de OpenAI sobre plugins y apps conectadas. Para la cuenta, el coste aparte y la disponibilidad solo usamos la página de ayuda, la de precios o la nota de prensa de cada empresa, más una noticia del sector para los países de lanzamiento de Skyscanner. Si ninguna lo decía, la tabla pone \"No consta\". No probamos todas las apps y dejamos fuera las que no pudimos confirmar (por ejemplo Apple Music, cuya ficha no tenía descripción ese día).",
        "Dora es nuestra; sus datos salen de su ficha en el directorio y de doravideo.com/llms.txt, que no publica precios (solo están en doravideo.com/pricing).",
    ],
    "faq": [
        ("¿Qué son las apps o plugins de ChatGPT?",
         "Conectan ChatGPT con otro servicio, como Canva, Spotify o Booking.com, para usarlo desde el chat. Están en el directorio de plugins de ChatGPT, en Plugins de la barra lateral en la web, el escritorio y el móvil; OpenAI avisa de que versiones muy antiguas de la app de iOS o Android pueden seguir mostrando Apps en vez de Plugins."),
        ("¿Las apps de ChatGPT cuestan dinero aparte?",
         "Depende de la app. Adobe anunció sus apps gratis para los usuarios de ChatGPT, Canva funciona con una cuenta gratis de Canva y Tripadvisor no pide cuenta para mirar. Otras usan tu plan en esa empresa: Runway y Lovable gastan sus propios créditos, Spotify pide Premium para las listas más personalizadas y Dora pide la suscripción Dora Pro."),
        ("¿Funcionan las apps con el plan gratis de ChatGPT?",
         "Algunas sí. Tripadvisor dice que funciona para usuarios con sesión en EE. UU. con Free, Go, Plus y Pro, y Spotify se lanzó para Free, Plus y Pro. OpenAI dice que el directorio se ve en todos los planes, pero que instalar o usar cada plugin depende del plan, del espacio de trabajo, del rol y de la región."),
        ("¿Qué apps de ChatGPT hacen vídeos?",
         "En el directorio, el 24 de octubre de 2026, entre otras: Runway, Higgsfield y Dora AI Video. Cada una usa su propia cuenta y sus créditos; Adobe también cambia el tamaño de vídeos."),
        ("¿Están disponibles en España y en Europa?",
         "No todas. Figma dice que su integración no está disponible en la UE y la de Tripadvisor de momento es solo para EE. UU., mientras que Spotify dice que añadió Reino Unido, Suiza y la UE después del lanzamiento. Mira cada ficha desde tu propia cuenta."),
    ],
    "sources": [(l.replace("Directory listing", "Ficha en el directorio"), u) for l, u in SRC],
})

PAGES = [EN, ES]
