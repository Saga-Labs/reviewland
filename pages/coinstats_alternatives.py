"""CoinStats / Delta alternatives for iPhone. EN. Our app: Crypton (id1143691286), live 2.0.4.

Checked 2026-10-16: iTunes lookup API + App Store web pages (US). Crypton facts
carried from reviewland's crypto-widgets page (2026-10-11) and the live 2.0.4 listing.
"""

CHECKED = "2026-10-16"


def src(cc):
    return [
        ("Crypton (App Store)", f"https://apps.apple.com/{cc}/app/id1143691286"),
        ("CoinStats (App Store)", f"https://apps.apple.com/{cc}/app/id1247849330"),
        ("Delta by eToro (App Store)", f"https://apps.apple.com/{cc}/app/id1288676542"),
        ("CoinGecko (App Store)", f"https://apps.apple.com/{cc}/app/id1390323960"),
        ("CoinMarketCap (App Store)", f"https://apps.apple.com/{cc}/app/id1282107098"),
    ]


EN = {
    "group": "coinstats-alternatives", "cover": "crypto-widgets", "lang": "en", "store": "us",
    "path": "coinstats-alternatives-iphone/",
    "ct": "rl-coinstats-alt",
    "category": "FinanceApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best CoinStats and Delta Alternatives for iPhone (2026)",
    "h1": "CoinStats and Delta alternatives for iPhone in 2026",
    "description": "Five crypto portfolio trackers for iPhone compared: CoinStats, Delta, CoinGecko, CoinMarketCap and Crypton. Prices, ratings and privacy labels.",
    "llms": "Compares CoinStats and Delta with three alternatives for iPhone (CoinGecko, CoinMarketCap, Crypton) by price, wallet and exchange sync, alerts, free-plan limits and App Store privacy label.",
    "disclosure": "Crypton is made by Saga Labs, the company behind Reviewland. It is one more option in this list, not placed first because it is ours, and it is much simpler than CoinStats or Delta. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "If you want a tracker that connects to your exchanges and wallets, CoinStats and Delta are the heavy options, and both have paid plans (CoinStats lists Premium subscriptions from $65.99 to $164.99; Delta's free plan tracks 10 assets). If you only want prices, news and a watchlist, CoinGecko and CoinMarketCap are free and far larger. If you just want a fast, free, ad-free list of the top coins with your holdings typed in, Crypton does that and nothing else.",
        "Crypton does not connect to wallets or exchanges and has no price alerts, so it is not a replacement for CoinStats or Delta for people who need automatic sync.",
    ],
    "columns": ["App", "Price (US)", "What it is best at", "Wallet / exchange sync", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "All five are free to download. Prices are the in-app purchases listed on the US App Store on 16 October 2026 (apps list several price points for the same plan). Ratings are the App Store average and number of ratings that day.",
    "apps": [
        {
            "name": "Crypto Tracker: Crypton", "id": 1143691286, "ours": True, "anchor": "crypton",
            "developer": "Saga Ltd.", "rating": (4.72, 184),
            "row": ["Free, no ads, no in-app purchases", "A fast, simple list of top coins with a manual portfolio", "No",
                    "Data Not Linked to You (diagnostics, usage data)", "2.0.8 (24 Oct 2026)", "4.7 (184 ratings)"],
            "best_for": "a free, ad-free look at the top coins and your holdings, once or twice a day.",
            "facts": [
                "Portfolio with the amounts you enter, their value and change per coin, and a price chart with 1D, 1W, 1M, 3M and 1Y views.",
                "Favourites and a watchlist; tracks 250+ coins according to the listing.",
                "Account optional (only to sync), no ads, nothing to buy.",
                "English only, iOS 18 or later, 29 MB.",
            ],
            "limits": "no wallet or exchange connection, no price alerts and no Apple Watch app (it has two free Home Screen widgets, Coin List and Portfolio, since version 2.0.6); prices are refreshed every few hours, so it is not for trading; and price charts load from Binance, which blocks US connections, so charts may fail in the US (found when we checked on 11 October). No profit and loss by purchase price.",
        },
        {
            "name": "CoinStats: Crypto Portfolio", "id": 1247849330, "anchor": "coinstats",
            "developer": "COINSTATSAPP LLC", "rating": (4.76, 85864),
            "row": ["Free; Premium listed from $65.99 to $164.99 a year or $15.99 to $19.99 a month; Pro from $39.99 a year", "Portfolio across 300+ wallets and exchanges, with P&L and AI insights", "Yes: 300+ wallets and exchanges, or paste a wallet address",
                    "Data Not Linked to You (contact info, diagnostics, identifiers, usage data)", "5.31.0 (3 Oct 2026)", "4.8 (85,864 ratings)"],
            "best_for": "people with several wallets and exchanges who want everything in one portfolio.",
            "facts": [
                "Connects 300+ wallets and exchanges (MetaMask, Phantom, Binance, Coinbase and others), or from a pasted wallet address.",
                "Realized and unrealized profit and loss, cost basis and tax-report export.",
                "Prices for 20,000+ coins, custom and automatic alerts, news from 140+ sources, and an AI assistant over your holdings.",
                "13 languages, iOS 15 or later, 197 MB.",
            ],
            "limits": "the best features are in paid plans with many price points, and it is a large app that asks to connect your accounts.",
        },
        {
            "name": "Delta by eToro", "id": 1288676542, "anchor": "delta",
            "developer": "Opus Labs CVBA", "rating": (4.71, 11362),
            "row": ["Free (up to 10 assets); PRO listed from $6.99 a month or $58.99 a year; PRO+ up to $107.99 a year", "Crypto, stocks, ETFs and forex in one portfolio", "Yes: 200+ exchanges, brokers and wallets",
                    "Data Not Linked to You (diagnostics, identifiers, search history, usage data, user content)", "2026.3.1 (24 Aug 2026)", "4.7 (11,362 ratings)"],
            "best_for": "tracking crypto and stocks together, with automatic syncing.",
            "facts": [
                "Syncs 200+ exchanges, brokers and wallets; tracks stocks, ETFs, forex, commodities and 10,000+ coins.",
                "Free plan: up to 10 assets, unlimited connections, price alerts and 3 AI uses a month.",
                "PRO raises it to 40 assets; PRO+ is unlimited, per the listing.",
                "18 languages, iOS 16.4 or later, 131 MB.",
            ],
            "limits": "the free plan stops at 10 assets, and its pricing has many tiers (PRO, PRO+).",
        },
        {
            "name": "CoinGecko: Crypto Tracker", "id": 1390323960, "anchor": "coingecko",
            "developer": "Gecko Labs Pte. Ltd.", "rating": (4.81, 27147),
            "row": ["Free; Premium $9.90 a month or $99.90 a year", "Market data on 10,000+ coins, NFTs and categories, plus a portfolio", "No (portfolio is entered manually)",
                    "Data Linked to You (contact info); other data not linked", "3.59.0 (12 Oct 2026)", "4.8 (27,147 ratings)"],
            "best_for": "researching coins and categories, with a free portfolio on the side.",
            "facts": [
                "Real-time data for 10,000+ cryptocurrencies, exchange volumes and 3,000+ NFT collections.",
                "Portfolio with profit and loss, price alerts, home screen widgets and a converter.",
                "English only, iOS 16 or later, 161 MB.",
            ],
            "limits": "it is built for market research more than for syncing your accounts; the portfolio is manual.",
        },
        {
            "name": "CoinMarketCap: Crypto Tracker", "id": 1282107098, "anchor": "coinmarketcap",
            "developer": "CoinMarketCap, LLC", "rating": (4.81, 172970),
            "row": ["Free; paid plans Essential from $11.99 a month up to Max at $119.99 a month", "Prices, watchlists, news and a real-time portfolio tracker", "Not stated",
                    "Data Linked to You (identifiers); other data not linked", "5.22.0 (25 Sep 2026)", "4.8 (172,970 ratings)"],
            "best_for": "the biggest price database and news in a free app.",
            "facts": [
                "Portfolio tracker in 90+ fiat currencies, personalised watchlists and price alerts.",
                "Crypto news and market trends in the same app.",
                "21 languages, iOS 15 or later, 224 MB.",
            ],
            "limits": "a large app with news and many extras; its paid plans list monthly prices that go up to $119.99.",
        },
    ],
    "who": [
        "<strong>You hold coins on several exchanges and wallets:</strong> CoinStats or Delta.",
        "<strong>You track stocks and crypto together:</strong> Delta.",
        "<strong>You research coins and want a free portfolio:</strong> CoinGecko or CoinMarketCap.",
        "<strong>You just want to glance at the top coins and your holdings, free and with no ads:</strong> Crypton.",
    ],
    "cases": [
        "Seeing the total value of wallets and exchanges in one place (CoinStats, Delta).",
        "Checking the price of a coin and why it moved (CoinGecko, CoinMarketCap).",
        "A quick morning glance at the top coins and your own holdings (Crypton).",
        "Exporting transactions for tax season (CoinStats lists tax reporting).",
    ],
    "method": [
        "On 16 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchases, version and release date, rating and number of ratings, languages, size, minimum iOS and the privacy label. Features are the ones each developer lists on its App Store page. Crypton's limits come from our own testing of version 2.0.4. We did not invent ratings or reviews, and none of this is financial advice.",
    ],
    "faq": [
        ("What is the best alternative to CoinStats on iPhone?",
         "Delta is the closest for syncing exchanges and wallets. CoinGecko and CoinMarketCap are free for prices and a manual portfolio, and Crypton is a simple free list."),
        ("Is there a free alternative to Delta?",
         "CoinGecko and CoinMarketCap are free to download with optional paid plans, and Crypton is free with no purchases. Delta itself has a free plan limited to 10 assets."),
        ("Which crypto tracker connects to exchanges and wallets?",
         "CoinStats lists 300+ wallets and exchanges and Delta lists 200+. Crypton does not connect to any."),
        ("Does Crypton have price alerts or widgets?",
         "Not in the current version (2.0.8). It has favourites, a watchlist and a manual portfolio with charts."),
        ("Is any of this financial advice?",
         "No. This page compares app features, prices and ratings as listed on the App Store."),
    ],
    "sources": src("us"),
}

PAGES = [EN]
