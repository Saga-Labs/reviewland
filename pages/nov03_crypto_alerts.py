"""Best crypto price alert apps for iPhone. EN. General topic. Criterion: the listing advertises price alerts.
Checked 2026-11-02 (JST night): iTunes lookup and US App Store pages. Crypton is not here: its listing does not mention alerts.
Nothing installed or tested; free limits only where the listing states them."""

DAY = "2026-11-02"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
NONE = "Data Not Collected"


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, langs, labels, price, alerts, best, facts, limits):
    return {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
            "row": [price, alerts, str(langs), labels, f"{ver} ({date})", f"{round(r, 1)}"]}


APPS = [
    app("CoinGecko: Crypto Tracker", 1390323960, "coingecko", "Gecko Labs Pte. Ltd.", 4.81, 27209, "3.60.0", "27 Oct 2026", 1, label(LINKED, NOTLINKED),
        "Premium $9.90 a month or $99.90 a year", "Price alerts and large-mover alerts",
        "alerts on a watchlist, plus a warning when a coin makes a big move.",
        ["Its listing offers personalised price alerts and large market movement alerts for coins in your watchlist.", "Portfolio with profit and loss, and a widget; data from 700+ exchanges."],
        "English only, and the listing does not say how many alerts are free."),
    app("HODL Bitcoin & Crypto Tracker", 1253668876, "hodl", "HODL Media Inc.", 4.83, 35392, "10.0.3", "29 Oct 2026", 1, label(TRACK, LINKED, NOTLINKED),
        "Basic $4.99; Premium from $6.99 to $83.99 on the page; Bots $16.99 a month", "3 free; unlimited with Premium",
        "knowing exactly what is free: 3 alerts and 25 symbols.",
        ["Free plan: watchlist and portfolio with up to 25 symbols, 3 price alerts, charts, news and the widget, per its listing.", "Alerts for a price target or a percentage change, and bracket alerts that reset above and below the price automatically.", "It also tracks stocks, not only crypto."],
        "English only, and its privacy label includes Data Used to Track You."),
    app("CoinMarketCap: Crypto Tracker", 1282107098, "coinmarketcap", "CoinMarketCap, LLC", 4.81, 173129, "5.24.0", "1 Nov 2026", 21, label(TRACK, LINKED, NOTLINKED),
        "Essential $11.99 a month or $109.99 a year; Plus $23.99 a month; Max $119.99 a month", "Customisable price alerts",
        "the widest coverage, with alerts on the coins you follow.",
        ["Its listing offers customisable price alerts and tracks 45,000+ active markets.", "The most ratings here, about 173,000, in 21 languages."],
        "the most expensive plans here, and its privacy label includes Data Used to Track You."),
    app("Crypto Pro - Live Coin Tracker", 980888073, "crypto-pro", "Crypto Inc.", 4.72, 46618, "10.0.0", "28 Oct 2026", 66, NOTLINKED,
        "Premium $7.99, $31.99 or $47.99 (period not shown on the page)", "Custom price notifications",
        "an ad-free tracker across iPhone, Mac and Apple Watch.",
        ["Customisable price notifications with charts on a long press, per its listing.", "Free and ad-free; Premium adds candlestick charts and portfolio sync, with a 7-day trial.", "Apps for iPad, Mac and Apple Watch; 66 languages."],
        "the App Store page does not show how long each Premium price lasts."),
    app("The Crypto App: News & Alerts", 1339112917, "the-crypto-app", "12170639 Canada Inc", 4.71, 2497, "4.0.6", "26 Oct 2026", 12, NONE,
        "Pro $8.99, Pro+ $14.99, Pro+ yearly $143.99", "Price, condition and news alerts",
        "alerts on both prices and headlines, with the strictest privacy label here.",
        ["Real-time price alerts for tokens hitting a target or condition, and news alerts, per its listing.", "The only app here whose privacy label is Data Not Collected."],
        "the page does not say what Pro adds to alerts."),
    app("Crypto News: Prices, Alerts", 1267753692, "crypto-news", "ROCKETM FZCO", 4.83, 1757, "7.2.2", "13 Oct 2026", 5, label(TRACK, LINKED),
        "$9.99 a month, $47.99 for 6 months, $77.99 a year", "Price, market cap and BTC dominance alerts",
        "alerts on market-moving news as well as prices.",
        ["Push notifications for market-moving events, and for a coin's price, market cap or Bitcoin's share of the market, per its listing.", "The subscription removes ads and adds offline reading, with a 7-day trial."],
        "its privacy label includes Data Used to Track You."),
]

PAGES = [{
    "group": "crypto-alerts", "lang": "en", "store": "us", "path": "best-crypto-price-alert-apps-iphone/", "ct": "rl-crypto-alerts", "hide_from_related": True,
    "category": "FinanceApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best Crypto Price Alert Apps for iPhone (2026)", "h1": "Best crypto price alert apps for iPhone",
    "description": "Six iPhone apps that send crypto price alerts, compared by US price, alert type, privacy label, version and rating on the App Store on 2 November 2026.",
    "llms": "Six iPhone crypto price alert apps from the App Store: CoinGecko, HODL, CoinMarketCap, Crypto Pro, The Crypto App, Crypto News. Alert types, free limits, price, privacy label.",
    "answer": [
        "For alerts on a watchlist plus a warning when a coin moves sharply, <strong>CoinGecko</strong>. To know exactly what is free, <strong>HODL</strong>: 3 price alerts on the free plan, unlimited with Premium. For the widest coverage, <strong>CoinMarketCap</strong>. With no ads and an Apple Watch app, <strong>Crypto Pro</strong>.",
        "For alerts on headlines as well as prices, <strong>The Crypto App</strong> (privacy label: Data Not Collected) or <strong>Crypto News</strong>. All six are free to download; only HODL's listing gives a number of free alerts.",
    ],
    "columns": ["App", "Price (US)", "Alerts, per listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are those listed on each US App Store page on 2 November 2026; pages list only some purchases. Ratings are that day's App Store average and count.",
    "apps": APPS,
    "who": ["<strong>Big-move alerts on a watchlist:</strong> CoinGecko.", "<strong>A clear free limit:</strong> HODL.", "<strong>Most coins covered:</strong> CoinMarketCap.",
            "<strong>No ads, Apple Watch and Mac:</strong> Crypto Pro.", "<strong>Least data collected:</strong> The Crypto App.", "<strong>News-driven alerts:</strong> Crypto News."],
    "cases": ["Tell me when Bitcoin crosses a price: any of the six.", "Tell me when a coin jumps or drops 10%: HODL lists percentage-change alerts, CoinGecko large-mover alerts.", "Tell me about news before the price moves: The Crypto App or Crypto News."],
    "method": ["On 2 November 2026 we read each app's US App Store page and Apple's lookup data. An app is here only if its listing advertises price alerts; the alert types and free limits come from the listings. We did not install the apps or test how fast alerts arrive.",
               "This page is about alerts. None of the apps here is a crypto exchange, and nothing on it is investment advice."],
    "faq": [
        ("What is the best free crypto price alert app for iPhone?", "HODL is the only one here that states a free number: 3 price alerts. CoinGecko, CoinMarketCap, Crypto Pro and The Crypto App are free to download with alerts, without a stated limit."),
        ("Can I get an alert when a coin moves a percentage?", "HODL lists alerts for a percentage change, and CoinGecko lists large market movement alerts."),
        ("Which crypto alert app collects the least data?", "The Crypto App's privacy label is Data Not Collected. Crypto Pro's says Data Not Linked to You."),
        ("Do these apps let me buy crypto?", "Their listings describe tracking, alerts and news; this page did not compare trading features."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS],
}]
