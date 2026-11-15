"""Best Pokemon card scanner apps for iPhone. EN. No app of ours is listed (it is not on sale yet).

Checked 2026-11-15 (JST): iTunes lookup (US) for the seven apps (name, price, rating, version) and the iTunes search
for "pokemon card scanner" (US, 25 results) to pick the other four. Features only from each listing's own text.
In-app purchase prices were not readable without a browser, so the page says "in-app purchases" and gives no price.
Complaint shares: 895 one- to three-star reviews of FoilSnap (283), HoloDex (284) and Collectr (328) from 7 stores
(us, ca, gb, de, au, fr, jp), downloaded 15 Nov 2026 and grouped by keyword (saga-growth data/mercado/tcg-2026-11-15).
For the other four apps we did not read reviews, and the page says so.
"""

DAY = "2026-11-15"
AS_OF = "Nov 15, 2026"


def src(cc="us"):
    return [
        ("Collectr - TCG Collector App (App Store)", f"https://apps.apple.com/{cc}/app/id1603892248"),
        ("Dex - for TCG Collectors (App Store)", f"https://apps.apple.com/{cc}/app/id1555489854"),
        ("TCG Card Scanner - FoilSnap (App Store)", f"https://apps.apple.com/{cc}/app/id6752642525"),
        ("HoloDex - TCG Scan & Collect (App Store)", f"https://apps.apple.com/{cc}/app/id6747442689"),
        ("Poké TCG Scanner Dragon Shield (App Store)", f"https://apps.apple.com/{cc}/app/id1199495742"),
        ("PriceCharting: TCG Collector (App Store)", f"https://apps.apple.com/{cc}/app/id6452190948"),
        ("Rare Candy: TCG Card Scanner (App Store)", f"https://apps.apple.com/{cc}/app/id1608616408"),
    ]


EN = {
    "group": "tcg-scanners", "lang": "en", "store": "us", "cover": None,
    "path": "best-pokemon-card-scanner-apps-iphone/",
    "ct": "rl-pokemon-card-scanner",
    "category": "UtilitiesApplication",
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Best Pokémon Card Scanner Apps for iPhone (2026)",
    "h1": "Best Pokémon card scanner apps for iPhone (2026)",
    "description": "Seven Pokémon card scanner apps for iPhone compared: games covered, free scans, price and rating, plus the complaint that repeats most in 895 low-star reviews. Checked on the App Store on 15 November 2026.",
    "llms": "Compares seven Pokémon and TCG card scanner apps for iPhone (Collectr, Dex, FoilSnap, HoloDex, Dragon Shield Poké TCG Scanner, PriceCharting, Rare Candy) by games covered, price, rating and what each listing says. Includes the most repeated complaints in 895 one- to three-star reviews of FoilSnap, HoloDex and Collectr: wrong or changing prices, early paywalls and scan limits, cards not recognised.",
    "answer": [
        "If you collect only Pokémon, Dex is the listing built around it, with prices from TCGplayer, Cardmarket, eBay and CardTrader shown free for everyone; if you collect several card games, Collectr (4.9) and HoloDex cover the most. PriceCharting is the one to open when you want past sales, not just a price. We checked seven apps on the App Store on Nov 15, 2026.",
        "Whatever you pick, expect two things. All seven are free to download, but in most of them scanning more cards, AI grading or full features sit behind in-app purchases. And in 895 one- to three-star reviews of FoilSnap, HoloDex and Collectr, the most repeated complaint (21%) is a wrong or changing price, so check any value you plan to act on against a second source.",
    ],
    "complaints": [
        {"id": "complaints", "h2": "What 895 low-star reviews complain about", "body": [
            "We read the 1-3 star reviews of the three apps with the most data: 283 for FoilSnap, 284 for HoloDex and 328 for Collectr, from seven App Store countries. Counts come from keyword matching, so one review can fall in more than one group and the shares are approximate.",
            "<strong>Wrong, outdated or changing prices: 21% of the 895.</strong> It is the top complaint for FoilSnap (28% of its low-star reviews) and Collectr (21%), and 15% for HoloDex. A FoilSnap reviewer wrote: &ldquo;Results were all different values ranging from cents to $25.&rdquo;",
            "<strong>Cards not recognised or identified wrongly: 12%.</strong> Mostly FoilSnap (23% of its low-star reviews): wrong set, rarity or edition.",
            "<strong>Paywall too early: 11.5%, and scan limits: 9.7%.</strong> HoloDex is the one where the paywall shows up most (19%); a reviewer wrote &ldquo;Immediate pay wall for core app functionality&rdquo;. For Collectr a reviewer wrote &ldquo;After you scan 35 cards they make you pay&rdquo;. The listings of HoloDex and Collectr both say unlimited scanning is an in-app purchase.",
            "<strong>Surprise charges and trouble cancelling: 8%.</strong> Highest for FoilSnap (15%). Before you start any trial, read the price on Apple's payment sheet, and know where to cancel: " + "<a href=\"https://support.apple.com/en-us/118428\">Apple: cancel a subscription</a>.",
        ]},
    ],
    "columns": ["App", "Games", "Price (US)", "Rating (US)", "Main complaint in low-star reviews"],
    "table_note": "Price and rating are from the US App Store as of Nov 15, 2026; rating counts are rounded. \"Free\" means free to download. Games come from each app's own description. The last column is the most common topic among 1-3 star reviews read on Nov 15, 2026; for the four apps marked \"not analysed\" we did not read reviews.",
    "apps": [
        {
            "name": "Collectr - TCG Collector App", "id": 1603892248, "anchor": "collectr",
            "developer": "Collectr Inc",
            "row": ["Pokémon, Magic, Yu-Gi-Oh!, One Piece, Lorcana and about 20 more, including Funko", "Free; in-app purchases", "4.9 (70K ratings)", "Wrong or changing prices (21%)"],
            "best_for": "collectors of several card games who think of their cards as a portfolio.",
            "facts": [
                "Values raw, graded and sealed products and tracks your collection as a portfolio, with biggest gains and losses and multi-currency support.",
                "The listing says unlimited card scanning, exclusive filters, data exports and custom backgrounds need an in-app purchase.",
                "Version 2.5.14 (4 Nov 2026), iOS 17.0 or later.",
            ],
            "limits": "in 328 low-star reviews, wrong or changing prices (21%) and missing card languages (13%) lead, then app crashes (11%) and scan limits (10%).",
        },
        {
            "name": "Dex - for TCG Collectors", "id": 1555489854, "anchor": "dex",
            "developer": "Dex",
            "row": ["Pokémon (English, Japanese and Simplified Chinese sets)", "Free; Dex+ subscription inside", "4.8 (15K ratings)", "Not analysed"],
            "best_for": "Pokémon-only collectors who want a binder-style collection and free prices.",
            "facts": [
                "Scans one card, or sweeps a whole binder page or stack in one shot.",
                "Shows prices from TCGplayer, Cardmarket, eBay and CardTrader, free for everyone, per the listing.",
                "Virtual binders, a Pokédex binder, folders, deck building and sharing your collection with a link.",
                "Version 28.0.0 (13 Nov 2026), iOS 16.6 or later.",
            ],
            "limits": "Pokémon only; the listing mentions a Dex+ subscription and does not say which features it unlocks.",
        },
        {
            "name": "TCG Card Scanner - FoilSnap", "id": 6752642525, "anchor": "foilsnap",
            "developer": "Next Vision Limited",
            "row": ["Magic, Pokémon, Yu-Gi-Oh!, MetaZoo and others", "Free; Premium subscription inside", "4.8 (15K ratings)", "Wrong or changing prices (28%)"],
            "best_for": "telling foil and non-foil copies apart and getting a pre-grade estimate.",
            "facts": [
                "The listing says it detects whether a card is foil and matches it to the right price tier.",
                "A grading assistant gives a pre-grade estimate before PSA or BGS, with a digital magnifying tool.",
                "Premium is described as limitless identifications, market insights and priority support.",
                "Version 2.2.0 (5 Nov 2026), iOS 16 or later.",
            ],
            "limits": "in 283 low-star reviews, wrong or changing prices (28%), cards not recognised (23%) and surprise charges or trouble cancelling (15%) lead.",
        },
        {
            "name": "HoloDex - TCG Scan & Collect", "id": 6747442689, "anchor": "holodex",
            "developer": "MAVELLI - FZCO",
            "row": ["Pokémon, One Piece, Lorcana, Yu-Gi-Oh!, Magic, Dragon Ball, Digimon and more (11 games listed)", "Free; in-app purchases", "4.8 (25K ratings)", "AI grading behind a paywall (21%) and early paywall (19%)"],
            "best_for": "the widest list of supported card games, with AI grading as an extra.",
            "facts": [
                "Scans cards, shows real-time prices, builds portfolios and wishlists and tracks profit and loss.",
                "AI grading looks at whitening, centering and surface wear before you grade or sell.",
                "The listing says in-app purchases unlock unlimited scans, exclusive filters and AI grading.",
                "Version 2.5.3 (11 Nov 2026), iOS 16.0 or later.",
            ],
            "limits": "in 284 low-star reviews, AI grading that costs money with no free try (21%), a paywall early on (19%), grades that did not match a real grading result (16%) and scan limits (12%).",
        },
        {
            "name": "Poké TCG Scanner Dragon Shield", "id": 1199495742, "anchor": "dragon-shield",
            "developer": "ARCANE TINMEN APS",
            "row": ["Pokémon (the listing also describes Magic scanning)", "Free", "4.6 (14K ratings)", "Not analysed"],
            "best_for": "scanning plus a deck builder and trade tool in one app.",
            "facts": [
                "Scans cards and shows daily prices from TCGPlayer and CardMarket.",
                "Custom folders with value over time, CSV or text export, a Pokémon deck builder and a tool that compares the value of a trade.",
                "Weekly collection emails and friends lists.",
                "Version 8.2.1 (5 Nov 2026), iOS 17.0 or later.",
            ],
            "limits": "parts of its listing talk about Magic cards, so check that a card you care about is covered before you scan a collection.",
        },
        {
            "name": "PriceCharting: TCG Collector", "id": 6452190948, "anchor": "pricecharting",
            "developer": "PriceCharting, LLC.",
            "row": ["Pokémon, Yu-Gi-Oh!, Magic, Lorcana, sports cards, video games, comics and more", "Free (the listing says completely free)", "4.8 (28K ratings)", "Not analysed"],
            "best_for": "checking what a card actually sold for, by condition.",
            "facts": [
                "Tracks sales from eBay, Heritage, PWCC and other auction sites and sorts them by condition.",
                "Search by photo or barcode to identify a card, plus a wishlist with alerts when something is listed below market value on eBay.",
                "Grading recommendations for ungraded cards that would gain the most value.",
                "Version 1.35.1 (12 Nov 2026), iOS 16.0 or later.",
            ],
            "limits": "it is a price guide for many kinds of collectibles, so it is less of a Pokémon-first binder than Dex.",
        },
        {
            "name": "Rare Candy: TCG Card Scanner", "id": 1608616408, "anchor": "rare-candy",
            "developer": "Rare Candy",
            "row": ["English and Japanese cards (scanning)", "Free; Instapacks and marketplace purchases are paid", "4.8 (12K ratings)", "Not analysed"],
            "best_for": "collectors who also want to open digital packs and buy from verified sellers.",
            "facts": [
                "Identifies raw and graded cards with the camera and adds them to digital binders and a wishlist.",
                "Shows market values and compares raw and graded prices to help you decide what to grade.",
                "Instapacks reveal real trading cards; a marketplace sells singles, sealed products and auctions.",
                "Version 3.5.1 (2 Nov 2026), iOS 17.0 or later.",
            ],
            "limits": "you need to create an account, and the app is partly a shop, so much of it is about buying cards.",
        },
    ],
    "who": [
        "<strong>You collect only Pokémon:</strong> Dex, or Dragon Shield if you also want a deck builder.",
        "<strong>You collect several card games:</strong> Collectr or HoloDex.",
        "<strong>You want to know what a card really sold for:</strong> PriceCharting, then compare with TCGplayer or Cardmarket.",
        "<strong>You want a pre-grade estimate before PSA or BGS:</strong> FoilSnap or HoloDex, and treat the grade as a guess.",
        "<strong>You also want to buy or open packs:</strong> Rare Candy.",
    ],
    "cases": [
        "Checking the price of a card at a trade night or a local game store (any of the seven).",
        "Cataloguing a childhood binder in an afternoon (Dex, Collectr, HoloDex).",
        "Deciding which cards are worth sending to PSA or BGS (FoilSnap, HoloDex, Rare Candy, PriceCharting).",
        "Keeping a multi-game collection as a portfolio (Collectr).",
    ],
    "method": [
        "On 15 November 2026 we searched the US App Store for \"pokemon card scanner\", took the 25 results, kept the apps whose own description says they scan cards, and looked up seven with Apple's lookup data for name, price, rating, version and description. We started from FoilSnap, Collectr and HoloDex, the three with the most reviews to read.",
        "Games and features come only from each app's own App Store description, not from our own scanning tests. In-app purchase prices were not readable without a browser, so we give none. Apps are ordered by how well their listing fits scanning Pokémon cards plus tracking, then by rating.",
        "For the complaint shares we downloaded the most recent 1-3 star reviews of FoilSnap, HoloDex and Collectr from seven App Store countries on 15 November 2026 (895 reviews) and grouped them by keyword; the shares are approximate and reviews are opinions. We did not read reviews of the other four apps.",
    ],
    "faq": [
        ("What is the best Pokémon card scanner app for iPhone?",
         "For Pokémon only, Dex is the listing built around it; for several card games, Collectr and HoloDex cover the most. All seven apps here are free to download, with in-app purchases in most."),
        ("Are Pokémon card scanner apps free?",
         "They are free to download, but the listings of HoloDex and Collectr say unlimited scanning is an in-app purchase, and FoilSnap's says Premium gives limitless identifications. PriceCharting's listing calls itself completely free."),
        ("Why does a card scanner show a different price each time?",
         "In reviews of FoilSnap, HoloDex and Collectr, a wrong or changing price is the top complaint (21% of 895). Compare any price you act on with TCGplayer and Cardmarket sales and with eBay sold listings."),
        ("Can an app grade my cards?",
         "FoilSnap and HoloDex describe AI grading or pre-grading. 16% of HoloDex's low-star reviews say a grade did not match a real result, so use it as a rough guide, not a grade."),
        ("How do I stop a card scanner subscription?",
         "On iPhone: Settings, tap your name, tap Subscriptions, tap the subscription, then Cancel Subscription. Apple explains it at support.apple.com/en-us/118428."),
    ],
    "sources": src("us"),
}

PAGES = [EN]
