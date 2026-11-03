"""Crypto portfolio trackers you fill in by hand, without connecting a wallet or exchange. EN. Our app: Crypton
(id1143691286), live 2.0.8, 4th of 5. Checked 2026-11-03 (JST): iTunes lookup and US App Store pages.
Criterion: the listing says you can add holdings by hand (or that no account or exchange hookup is needed), and the
app was updated in 2026. Left out: CoinCap (last update 13 Oct 2021), CoinMarketCap (its listing says to sign up to
make a portfolio), CoinStats, Delta and CoinTracker (built around syncing; they are on /coinstats-alternatives-iphone/).
Crypton facts from its live 2.0.8 listing only (no wallet by address, no Pro, no alerts until 2.1.1 is live).
Reserved in ios-playbook/references/temas-webs.md (7788d66); replaces the Delta alternatives idea."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
FREE = '<a href="/best-free-crypto-portfolio-tracker-apps-iphone/">free crypto portfolio trackers</a>'
SYNC = '<a href="/coinstats-alternatives-iphone/">CoinStats and Delta alternatives</a>'
WIDGETS = '<a href="/best-crypto-price-widget-apps-iphone/">crypto widget apps</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, labels, price, account, sync, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, account, sync, labels, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Crypto Pro - Live Coin Tracker", 980888073, "crypto-pro", "Crypto Inc.", 4.72, 46616, "10.0.0", "28 Oct 2026", NOTLINKED,
        "Free, no ads; Premium $7.99 to $47.99 (automatic sync, candlestick charts)", "Data kept on the device; optional iCloud sync", "Optional, Premium: wallet addresses or exchange API keys",
        "the most complete tracker that still keeps your data on your own devices.",
        ["Its listing says personal data is stored on your device, not on its servers, with no user monitoring or analytics; optional iCloud backup and sync.", "Also on iPad, Mac and Apple Watch, with widgets and price notifications.", "Tracks precious metals and fiat currencies as well as crypto."],
        "automatic import from addresses and exchanges is a Premium feature, and the listing does not say what else the free version limits."),
    app("BitWorth - Crypto Tracker", 1239107714, "bitworth", "Andy Feng", 4.75, 1658, "3.02.09", "13 Oct 2026", NOTLINKED,
        "Free (no in-app purchases)", "\"No account. No sign-up.\"", "No: \"no exchange hookups\"",
        "one number, what your crypto is worth now, with nothing to sign up for.",
        ["Its listing says you open the app, add the coins you hold and see their value in your currency; everything stays on the device unless you back it up.", "Built by one developer; has a live global chat and news feed if you want them."],
        "needs iOS 26, English only, and it is deliberately simple: no P&L by buy price is mentioned in the listing."),
    app("CoinGecko: Crypto Tracker", 1390323960, "coingecko", "Gecko Labs Pte. Ltd.", 4.81, 27215, "3.60.0", "27 Oct 2026", label(LINKED, NOTLINKED),
        "Free; Premium $9.90 a month or $99.90 a year", "Not stated in the listing", "No: you build the portfolio from your transactions",
        "a manual portfolio next to the biggest free price and research database.",
        ["Its listing says you build your own portfolio and track real-time profit and loss based on your transactions.", "Over 10,000 coins, NFT floor prices, categories, price alerts and widgets."],
        "a big research app more than a portfolio tool, English only, and its privacy label includes data linked to you."),
    app("Crypto Tracker: Crypton", 1143691286, "crypton", "Saga Ltd.", 4.72, 185, "2.0.8", "24 Oct 2026", NOTLINKED,
        "Free, no ads, no in-app purchases", "Optional, only to sync the portfolio", "No: you type the amount you hold",
        "a free, ad-free portfolio you fill in yourself, with P&L and a Home Screen widget.",
        ["Its listing says you add how much of each coin you hold and, if you want, your average buy price to see profit and loss per coin.", "Top 250 coins by market cap, and search finds any other coin listed on CoinGecko.", "Free Home Screen widgets for prices and for your portfolio; light (29 MB) and runs on older iPhones, per its listing."],
        "no wallet or exchange import at all, no price alerts and no Apple Watch app in 2.0.8; English only."),
    app("Crypto Tracker by BitScreener", 1240849311, "bitscreener", "BITSCREENER PTE. LTD.", 4.74, 20152, "4.6.7", "29 May 2026", label(TRACK, LINKED, NOTLINKED),
        "Free; $4.99 or $41.99, lifetime $9.99", "Not stated in the listing", "Optional: exchange API or CSV; manual mode",
        "a manual portfolio with trader tools: screener, technical charts and many alert types.",
        ["Its listing says the portfolio supports a manual adding mode, API integration from exchanges and CSV import and export.", "Five kinds of alerts, a screener with 100+ criteria and charts with 100+ indicators."],
        "its privacy label includes data used to track you, and its last update was in May 2026."),
]

PAGES = [{
    "group": "crypto-no-connect", "lang": "en", "store": "us", "path": "crypto-portfolio-tracker-without-connecting-wallet-iphone/", "ct": "rl-crypto-no-connect",
    "category": "FinanceApplication", "cover": "crypto-widgets", "hide_from_related": True,
    "published": DAY, "updated": DAY, "checked": DAY,
    "title": "Crypto Portfolio Trackers Without Connecting a Wallet (2026)", "h1": "Track your crypto portfolio on iPhone without connecting a wallet or exchange",
    "description": "Five iPhone apps where you type in what you hold: no wallet, exchange or API key to connect, and in some no account. US prices, privacy labels and ratings on 3 November 2026.",
    "llms": "Five iPhone crypto portfolio trackers you fill in by hand, without connecting a wallet or exchange: Crypto Pro, BitWorth, CoinGecko, Crypton, BitScreener. Price, account, optional sync, privacy label, version and rating on 3 November 2026.",
    "llms_note": "Crypton, one of the five, is made by Saga Labs, which runs Reviewland.",
    "answer": [
        "You don't need to connect a wallet, an exchange or an API key to follow what your crypto is worth: these apps let you type in the coins and amounts you hold and price them live. For the most complete app that keeps your data on your devices, <strong>Crypto Pro</strong>. For no account at all and one clear number, <strong>BitWorth</strong>. For a manual portfolio inside a big research app, <strong>CoinGecko</strong>. For a free, ad-free portfolio with profit and loss and a widget, <strong>Crypton</strong>.",
        "A wallet address is public, but pasting it into an app links your holdings to that app; an exchange API key gives an app access to your account. Typing amounts by hand shares neither. The trade-off: you update the amounts yourself after each buy or sale.",
    ],
    "columns": ["App", "Price (US)", "Account", "Wallet or exchange sync", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "All five are free to download; prices are in-app purchases on each US App Store page on 3 November 2026. \"Not stated\" means the listing does not say whether you need an account.",
    "apps": APPS,
    "who": ["<strong>Everything on your own devices, with iPad, Mac and Watch:</strong> Crypto Pro.", "<strong>No account, just the total:</strong> BitWorth.", "<strong>A portfolio next to research and alerts:</strong> CoinGecko.",
            "<strong>Free, no ads, P&L by buy price and a widget:</strong> Crypton.", "<strong>Manual portfolio plus trader tools:</strong> BitScreener."],
    "cases": ["You hold coins on a hardware wallet and don't want to paste its address anywhere: type the amounts into any of the five.",
              "You want the total on your Home Screen: Crypto Pro, CoinGecko, Crypton and BitScreener list widgets; see " + WIDGETS + ".",
              "You hold coins on several exchanges and want them to update by themselves: that needs syncing; see " + SYNC + "."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data. An app is here only if its listing says you can add holdings by hand or needs no exchange hookup, and it was updated in 2026. We did not test accuracy of prices.",
               "Order: first the apps that say most clearly that your data stays with you, then the rest. Left out: CoinCap (last update October 2021) and CoinMarketCap (its listing says to sign up to make a portfolio). See also " + FREE + ". None of this is financial advice."],
    "faq": [
        ("Can I track crypto without connecting my wallet?", "Yes. Crypto Pro, BitWorth, CoinGecko, Crypton and BitScreener let you add the coins and amounts by hand, and they price them live."),
        ("Which crypto tracker needs no account?", "BitWorth says no account and no sign-up. Crypton's account is optional, only to sync the portfolio. Crypto Pro keeps data on the device with optional iCloud sync. CoinMarketCap's listing asks you to sign up to make a portfolio."),
        ("Is it safe to paste my wallet address into a tracker?", "An address only lets an app read public balances, not move coins, but it links that wallet to you in the app. Never type a seed phrase or private key into a tracker."),
        ("Which of these collect the least data?", "Crypto Pro, BitWorth and Crypton show only Data Not Linked to You on their App Store privacy labels on 3 November 2026."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [
        ("CoinMarketCap (App Store)", "https://apps.apple.com/us/app/id1282107098"), ("CoinCap (App Store)", "https://apps.apple.com/us/app/id1074052280")],
}]
