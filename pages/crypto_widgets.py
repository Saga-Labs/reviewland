"""Best crypto price tracker apps with widgets for iPhone. EN + ES. Our app: Crypton (id1143691286).

Checked 2026-10-11: iTunes lookup API and App Store web pages (US for EN,
Spain for ES). Crypton 2.0.4 facts from its repo (cryptonapp-bf session,
11 Oct): prices from a JSON refreshed every 3 to 7 hours (not real time),
top 249 coins, NO widgets and NO Apple Watch app in the 2.0.4 build (extensions
not embedded since Jan 2025, commit 5f35a07), no price alerts, charts from api.binance.com (fail in the US, HTTP 451), optional
account, no ads, no purchases. Update when 2.0.5 ships.
"""

CHECKED = "2026-10-11"


def src(cc):
    return [
        ("Crypton (App Store)", f"https://apps.apple.com/{cc}/app/id1143691286"),
        ("CoinGecko (App Store)", f"https://apps.apple.com/{cc}/app/id1390323960"),
        ("CoinMarketCap (App Store)", f"https://apps.apple.com/{cc}/app/id1282107098"),
        ("Crypto Pro (App Store)", f"https://apps.apple.com/{cc}/app/id980888073"),
        ("CoinStats (App Store)", f"https://apps.apple.com/{cc}/app/id1247849330"),
        ("HODL (App Store)", f"https://apps.apple.com/{cc}/app/id1253668876"),
    ]


EN = {
    "group": "crypto-widgets", "lang": "en", "store": "us",
    "path": "best-crypto-price-widget-apps-iphone/",
    "ct": "rl-crypto-widgets",
    "category": "FinanceApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best crypto price tracker apps for iPhone (2026): widgets, alerts and ads compared",
    "h1": "Best crypto price tracker apps for iPhone in 2026: widgets, alerts and ads",
    "description": "Six crypto price apps for iPhone compared by widgets, price alerts, how fresh the prices are, price and privacy: Crypton, CoinGecko, CoinMarketCap, Crypto Pro, CoinStats and HODL. Checked on the App Store on 11 October 2026.",
    "llms": "Compares six crypto price tracker apps for iPhone (Crypton, CoinGecko, CoinMarketCap, Crypto Pro, CoinStats, HODL) by widgets, price alerts, real-time data, price and privacy label. States that Crypton has no widgets, no alerts and delayed prices.",
    "disclosure": "Crypton is made by Saga Labs, the company behind Reviewland. It is listed first because it is ours. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages. None of these apps is financial advice.",
    "answer": [
        "For a simple look at crypto prices and your portfolio with no ads and nothing to pay, Crypton (ours) is free, but today it has no widgets, no price alerts, and its prices are refreshed every few hours, not in real time. If you want prices on your Home Screen, alerts or live data, CoinGecko, CoinStats and Crypto Pro list widgets, and CoinGecko, CoinMarketCap, CoinStats and HODL list price alerts.",
        "Crypto Pro is the most complete for Apple devices (widgets, Mac menu bar, Apple Watch complications) and its privacy label is Data Not Linked to You.",
    ],
    "columns": ["App", "Price (US)", "Widgets", "Price alerts", "Prices", "App Store privacy label", "Rating (US)"],
    "table_note": "Prices are the US App Store in-app purchases on 11 October 2026; all six are free to download. Widgets, alerts and real-time data are as each developer describes them on its App Store page (for Crypton, as the app works today). Ratings are the App Store average and number of ratings that day.",
    "apps": [
        {
            "name": "Crypton: Crypto Tracker", "id": 1143691286, "ours": True, "anchor": "crypton",
            "developer": "Saga Ltd.", "rating": (4.72, 183),
            "row": ["Free, no ads, no in-app purchases", "No", "No",
                    "Top 249 coins, refreshed every 3 to 7 hours", "Data Used to Track You; Data Not Linked to You", "4.7 (183 ratings)"],
            "best_for": "a free, ad-free look at the top coins and your holdings, once or twice a day.",
            "facts": [
                "Portfolio with amounts, value, a 1D to 1Y portfolio chart and the change per coin.",
                "Favourites and watchlist; account optional (only to sync), no ads, nothing to buy.",
                "Version 2.0.4 (9 Oct 2026), iOS 18 or later, 18 MB, English only.",
            ],
            "limits": "no widgets and no Apple Watch app in the current version; no price alerts; prices are refreshed every 3 to 7 hours, so it is not for trading; only the top 249 coins; and price charts load from Binance, which blocks the US, so charts fail there. No profit and loss by purchase price yet.",
        },
        {
            "name": "CoinGecko: Crypto Tracker", "id": 1390323960, "anchor": "coingecko",
            "developer": "Gecko Labs", "rating": (4.81, 27127),
            "row": ["Premium $9.90 a month or $99.90 a year", "Prices and portfolio", "Yes, plus large-move alerts",
                    "Real time, 10,000+ coins", "Data Linked to You; Data Not Linked to You", "4.8 (27,127 ratings)"],
            "best_for": "the widest coin coverage with alerts, news and NFT floor prices.",
            "facts": [
                "Portfolio with real-time profit and loss, synced between web and app; several portfolios.",
                "Categories such as memecoins, AI coins and Layer 2, plus 3,000+ NFT collections.",
                "News from CryptoPanic and 10+ outlets. Version 3.58.0 (28 Sep 2026), English only, 160 MB.",
            ],
            "limits": "Premium is a subscription, and the app is in English only.",
        },
        {
            "name": "CoinMarketCap: Crypto Tracker", "id": 1282107098, "anchor": "coinmarketcap",
            "developer": "CoinMarketCap", "rating": (4.81, 172929),
            "row": ["Essential $11.99 a month or $109.99 a year; Plus and Max up to $229.99", "Not mentioned in the listing", "Yes",
                    "Real time", "Data Used to Track You; Data Linked to You; Data Not Linked to You", "4.8 (172,929 ratings)"],
            "best_for": "market-wide stats, exchange data and news from the best-known price site.",
            "facts": [
                "Price alerts on coins or on your portfolio.",
                "Watchlists, incognito mode without logging in that saves data on the device.",
                "Version 5.22.0 (25 Sep 2026), 21 languages, 223 MB.",
            ],
            "limits": "the most expensive subscriptions here, and its privacy label includes data used to track you.",
        },
        {
            "name": "Crypto Pro - Live Coin Tracker", "id": 980888073, "anchor": "crypto-pro",
            "developer": "Crypto Inc.", "rating": (4.72, 46611),
            "row": ["Premium $7.99, $31.99 or $47.99", "Prices, charts, news and portfolio; Mac menu bar", "Breaking-news alerts",
                    "Real time from Coinbase, Binance, Kraken and others", "Data Not Linked to You", "4.7 (46,611 ratings)"],
            "best_for": "people with iPhone, iPad, Mac and Apple Watch who want everything in sync.",
            "facts": [
                "Imports holdings from wallet addresses or exchange API keys; profit and loss.",
                "Apple Watch complications; optional iCloud sync; no ads.",
                "Version 9.3.0 (12 Sep 2026), 66 languages, 103 MB.",
            ],
            "limits": "its listing mentions news alerts but does not describe price-target alerts.",
        },
        {
            "name": "CoinStats: Crypto Portfolio", "id": 1247849330, "anchor": "coinstats",
            "developer": "CoinStats", "rating": (4.76, 85820),
            "row": ["Pro $4.99 a month or $39.99 a year; Premium up to $164.99 a year", "Home and Lock Screen; Apple Watch", "Yes, price, volume and market cap",
                    "Real time, 20,000+ coins", "Data Not Linked to You", "4.8 (85,820 ratings)"],
            "best_for": "tracking holdings across 300+ wallets and exchanges, including DeFi.",
            "facts": [
                "Connects MetaMask, Phantom, Binance, Coinbase and more; realised and unrealised profit and loss.",
                "Tax export of every trade, news from 140+ sources, AI questions about your portfolio.",
                "Version 5.31.0 (3 Oct 2026), 13 languages, 196 MB.",
            ],
            "limits": "many overlapping plans, and the full features need Premium.",
        },
        {
            "name": "HODL Real-Time Crypto Tracker", "id": 1253668876, "anchor": "hodl",
            "developer": "HODL Media", "rating": (4.83, 35390),
            "row": ["Basic $4.99; Premium $6.99 to $83.99", "Not mentioned in the listing", "Yes, targets, percentages and smart brackets",
                    "Real time from 240+ exchanges", "Data Used to Track You; Data Linked to You; Data Not Linked to You", "4.8 (35,390 ratings)"],
            "best_for": "traders who want many alerts and a watchlist of crypto and stocks.",
            "facts": [
                "Unlimited watchlist and price alerts with Premium; smart alert brackets.",
                "Portfolio that can sync with ERC20 wallets; screener of top gainers and losers.",
                "Version 9.36 (26 Apr 2026), English only, 66 MB.",
            ],
            "limits": "last updated in April 2026, and its privacy label includes data used to track you.",
        },
    ],
    "who": [
        "<strong>You want a free tracker with no ads and do not trade:</strong> Crypton (ours).",
        "<strong>You need price alerts:</strong> CoinGecko, CoinMarketCap, CoinStats or HODL.",
        "<strong>You use a Mac and an Apple Watch too:</strong> Crypto Pro.",
        "<strong>You hold coins in many wallets and exchanges:</strong> CoinStats.",
        "<strong>You track small or new coins:</strong> CoinGecko (10,000+) or CoinStats (20,000+).",
    ],
    "cases": [
        "Seeing Bitcoin and Ethereum on the Home Screen without opening an app (CoinGecko, CoinStats, Crypto Pro).",
        "Checking the value of a long-term portfolio once or twice a day (Crypton is enough).",
        "Getting a notification when a coin hits a price (any app with alerts, not Crypton).",
        "Importing holdings from wallets and exchanges for taxes (CoinStats).",
    ],
    "method": [
        "On 11 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchases, version and release date, rating and number of ratings, languages, size and the privacy label. Widgets, alerts and data sources are as each developer describes them. For Crypton, which is ours, we also checked how version 2.0.4 works: where its prices come from and how often they are refreshed. We did not invent ratings or reviews.",
    ],
    "faq": [
        ("Which crypto app has the best iPhone widget?",
         "CoinStats, CoinGecko and Crypto Pro list Home Screen widgets; CoinStats also has Lock Screen widgets, and Crypto Pro has a Mac menu bar widget. Crypton has no widgets in its current version."),
        ("Does Crypton have price alerts?",
         "No. On 11 October 2026 Crypton has no price alerts or notifications, and no widgets either."),
        ("Are Crypton's prices real time?",
         "No. In version 2.0.4 prices are refreshed every 3 to 7 hours. For live prices use CoinGecko, CoinMarketCap, CoinStats, Crypto Pro or HODL."),
        ("Is there a free crypto tracker without ads?",
         "Crypton is free with no ads and no in-app purchases. The others are free to download with paid plans."),
        ("Do I need an account?",
         "Not for Crypton (account only to sync). CoinMarketCap lists an incognito mode without logging in."),
    ],
    "sources": src("us"),
}

ES = {
    "group": "crypto-widgets", "lang": "es", "store": "es",
    "path": "es/mejores-apps-precios-cripto-widgets-iphone/",
    "ct": "rl-crypto-widgets-es",
    "category": "FinanceApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Mejores apps de precios de cripto para iPhone (2026): widgets, alertas y anuncios",
    "h1": "Mejores apps de precios de cripto para iPhone en 2026: widgets, alertas y anuncios",
    "description": "Seis apps de precios de cripto para iPhone comparadas por widgets, alertas, si los precios van al momento, precio y privacidad: Crypton, CoinGecko, CoinMarketCap, Crypto Pro, CoinStats y HODL. Comprobado en el App Store de España el 11 de octubre de 2026.",
    "llms": "Compara seis apps de precios de cripto para iPhone (Crypton, CoinGecko, CoinMarketCap, Crypto Pro, CoinStats, HODL) por widgets, alertas, datos en tiempo real, precio en euros y privacidad. Dice que Crypton no tiene widgets ni alertas y que sus precios llevan horas de retraso.",
    "disclosure": "Crypton es de Saga Labs, la empresa que hace Reviewland. Va primera porque es nuestra. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store. Nada de esto es asesoramiento financiero.",
    "answer": [
        "Para mirar precios de cripto y tu cartera sin anuncios y sin pagar nada, Crypton (nuestra) es gratis, pero hoy no tiene widgets ni alertas de precio, y sus precios se actualizan cada pocas horas, no al momento. Si quieres precios en la pantalla de inicio, alertas o datos en tiempo real, CoinGecko, CoinStats y Crypto Pro tienen widgets según su ficha, y CoinGecko, CoinMarketCap, CoinStats y HODL tienen alertas.",
        "Crypto Pro es la más completa para dispositivos Apple (widgets, barra de menús del Mac y complicaciones del Apple Watch), y su etiqueta de privacidad es «Datos no vinculados a ti».",
    ],
    "columns": ["App", "Precio (España)", "Widgets", "Alertas de precio", "Precios", "Etiqueta de privacidad", "Valoración (España)"],
    "table_note": "Precios: compras dentro de la app del App Store de España el 11 de octubre de 2026; las seis se descargan gratis. Widgets, alertas y datos en tiempo real según la ficha de cada desarrollador (en Crypton, según cómo funciona hoy). Valoración: media y número de valoraciones en España ese día.",
    "apps": [
        {
            "name": "Crypton: Precios Cripto", "id": 1143691286, "ours": True, "anchor": "crypton",
            "developer": "Saga Ltd.", "rating": (4.6, 35),
            "row": ["Gratis, sin anuncios ni compras dentro", "No", "No",
                    "Las 249 primeras monedas, cada 3 a 7 horas", "Datos utilizados para rastrearte; datos no vinculados a ti", "4,6 (35 valoraciones)"],
            "best_for": "ver gratis y sin anuncios las monedas principales y tu cartera una o dos veces al día.",
            "facts": [
                "Cartera con cantidades, valor, gráfico de 1 día a 1 año y cambio por moneda.",
                "Favoritas y lista de seguimiento; cuenta opcional (solo para sincronizar), sin anuncios y sin nada que comprar.",
                "Versión 2.0.4 (9 oct 2026), iOS 18 o posterior, 18 MB. La app está solo en inglés.",
            ],
            "limits": "la versión actual no tiene widgets ni app para Apple Watch; no tiene alertas de precio; los precios se actualizan cada 3 a 7 horas, así que no sirve para hacer trading; solo cubre las 249 primeras monedas; y los gráficos se cargan de Binance, que bloquea EE. UU. (allí fallan). Aún no calcula ganancias y pérdidas por precio de compra.",
        },
        {
            "name": "CoinGecko: Crypto Tracker, NFT", "id": 1390323960, "anchor": "coingecko",
            "developer": "Gecko Labs", "rating": (4.76, 1771),
            "row": ["Premium 9,90 € al mes o 99,90 € al año", "Precios y cartera", "Sí, y avisos de grandes movimientos",
                    "Tiempo real, más de 10.000 monedas", "Datos vinculados a ti; datos no vinculados a ti", "4,8 (1.771 valoraciones)"],
            "best_for": "la mayor cobertura de monedas con alertas, noticias y precios de NFT.",
            "facts": [
                "Cartera con ganancias y pérdidas en tiempo real, sincronizada entre web y app; varias carteras.",
                "Categorías como memecoins, monedas de IA y Layer 2, y más de 3.000 colecciones NFT.",
                "Noticias de CryptoPanic y más de 10 medios. Versión 3.58.0 (28 sep 2026), solo en inglés, 160 MB.",
            ],
            "limits": "Premium es una suscripción y la app está solo en inglés.",
        },
        {
            "name": "CoinMarketCap: Crypto Tracker", "id": 1282107098, "anchor": "coinmarketcap",
            "developer": "CoinMarketCap", "rating": (4.77, 13648),
            "row": ["Essential 12,99 € al mes o 119,99 € al año; Plus y Max hasta 249,99 €", "La ficha no los menciona", "Sí",
                    "Tiempo real", "Datos utilizados para rastrearte; datos vinculados a ti; datos no vinculados a ti", "4,8 (13.648 valoraciones)"],
            "best_for": "datos de todo el mercado, de exchanges y noticias de la web de precios más conocida.",
            "facts": [
                "Alertas de precio por moneda o por cartera.",
                "Listas de seguimiento y modo incógnito sin iniciar sesión que guarda los datos en el móvil.",
                "Versión 5.22.0 (25 sep 2026), 21 idiomas, español incluido, 223 MB.",
            ],
            "limits": "las suscripciones más caras de la lista, y su etiqueta incluye datos para rastrearte.",
        },
        {
            "name": "Crypto Pro - Criptomonedas", "id": 980888073, "anchor": "crypto-pro",
            "developer": "Crypto Inc.", "rating": (4.65, 929),
            "row": ["Premium 7,99 €, 31,99 € o 47,99 €", "Precios, gráficos, noticias y cartera; barra de menús del Mac", "Avisos de noticias",
                    "Tiempo real de Coinbase, Binance, Kraken y otros", "Datos no vinculados a ti", "4,7 (929 valoraciones)"],
            "best_for": "quien tiene iPhone, iPad, Mac y Apple Watch y lo quiere todo sincronizado.",
            "facts": [
                "Importa saldos con direcciones de cartera o claves de API de exchanges; ganancias y pérdidas.",
                "Complicaciones para Apple Watch; sincronización opcional con iCloud; sin anuncios.",
                "Versión 9.3.0 (12 sep 2026), 66 idiomas, 103 MB.",
            ],
            "limits": "su ficha menciona avisos de noticias, pero no describe alertas por precio objetivo.",
        },
        {
            "name": "Crypto Tracker - Coin Stats", "id": 1247849330, "anchor": "coinstats",
            "developer": "CoinStats", "rating": (4.67, 1465),
            "row": ["Pro 4,99 € al mes o 41,99 € al año; Premium hasta 184,99 € al año", "Pantalla de inicio y bloqueada; Apple Watch", "Sí: precio, volumen y capitalización",
                    "Tiempo real, más de 20.000 monedas", "Datos no vinculados a ti", "4,7 (1.465 valoraciones)"],
            "best_for": "seguir saldos en más de 300 carteras y exchanges, también DeFi.",
            "facts": [
                "Conecta MetaMask, Phantom, Binance, Coinbase y más; ganancias y pérdidas realizadas y no realizadas.",
                "Exportación para impuestos, noticias de más de 140 fuentes y preguntas a una IA sobre tu cartera.",
                "Versión 5.31.0 (3 oct 2026), 13 idiomas, 196 MB.",
            ],
            "limits": "muchos planes que se solapan, y lo completo pide Premium.",
        },
        {
            "name": "HODL: Cripto en tiempo real", "id": 1253668876, "anchor": "hodl",
            "developer": "HODL Media", "rating": (4.74, 323),
            "row": ["Basic 5,99 €; Premium de 6,99 € a 83,99 €", "La ficha no los menciona", "Sí: objetivos, porcentajes y rangos automáticos",
                    "Tiempo real de más de 240 exchanges", "Datos utilizados para rastrearte; datos vinculados a ti; datos no vinculados a ti", "4,7 (323 valoraciones)"],
            "best_for": "quien hace trading y quiere muchas alertas y una lista de cripto y acciones.",
            "facts": [
                "Lista de seguimiento y alertas ilimitadas con Premium; rangos de alerta automáticos.",
                "Cartera que se sincroniza con carteras ERC20; buscador de las que más suben y bajan.",
                "Versión 9.36 (26 abr 2026), solo en inglés, 66 MB.",
            ],
            "limits": "la última actualización es de abril de 2026, y su etiqueta incluye datos para rastrearte.",
        },
    ],
    "who": [
        "<strong>Quieres algo gratis y sin anuncios y no haces trading:</strong> Crypton (nuestra).",
        "<strong>Necesitas alertas de precio:</strong> CoinGecko, CoinMarketCap, CoinStats o HODL.",
        "<strong>También usas Mac y Apple Watch:</strong> Crypto Pro.",
        "<strong>Tienes monedas en muchas carteras y exchanges:</strong> CoinStats.",
        "<strong>Sigues monedas pequeñas o nuevas:</strong> CoinGecko (más de 10.000) o CoinStats (más de 20.000).",
    ],
    "cases": [
        "Ver Bitcoin y Ethereum en la pantalla de inicio sin abrir ninguna app (CoinGecko, CoinStats, Crypto Pro).",
        "Mirar el valor de una cartera a largo plazo una o dos veces al día (con Crypton basta).",
        "Recibir un aviso cuando una moneda llega a un precio (cualquiera con alertas, no Crypton).",
        "Importar saldos de carteras y exchanges para la declaración (CoinStats).",
    ],
    "method": [
        "El 11 de octubre de 2026 abrimos la ficha de cada app en el App Store de España y los datos de Apple: compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño y etiqueta de privacidad. Widgets, alertas y fuentes de datos según lo que dice cada desarrollador. En Crypton, que es nuestra, miramos además cómo funciona la versión 2.0.4: de dónde salen los precios y cada cuánto se actualizan. No inventamos valoraciones ni reseñas.",
    ],
    "faq": [
        ("¿Qué app de cripto tiene el mejor widget para iPhone?",
         "CoinStats, CoinGecko y Crypto Pro tienen widgets en la pantalla de inicio según su ficha; CoinStats también en la pantalla bloqueada, y Crypto Pro en la barra de menús del Mac. Crypton no tiene widgets en su versión actual."),
        ("¿Crypton tiene alertas de precio?",
         "No. El 11 de octubre de 2026 Crypton no tiene alertas de precio ni notificaciones, y tampoco widgets."),
        ("¿Los precios de Crypton van al momento?",
         "No. En la versión 2.0.4 los precios se actualizan cada 3 a 7 horas. Para precios al momento, CoinGecko, CoinMarketCap, CoinStats, Crypto Pro o HODL."),
        ("¿Hay alguna app de precios de cripto gratis y sin anuncios?",
         "Crypton es gratis, sin anuncios y sin compras dentro. Las demás se descargan gratis y tienen planes de pago."),
        ("¿Hace falta cuenta?",
         "En Crypton no (solo para sincronizar). La ficha de CoinMarketCap describe un modo incógnito sin iniciar sesión."),
    ],
    "sources": src("es"),
}

PAGES = [EN, ES]


from pages.store_1016 import refresh_ours
for _p in PAGES:
    refresh_ours(_p, _p["store"], 4, None, 5)
