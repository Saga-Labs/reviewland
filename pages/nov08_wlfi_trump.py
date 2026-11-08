"""Best iPhone apps to track WLFI, TRUMP and USD1 prices. EN. News page (8 Nov 2026). Our app: Crypton (id1143691286), live 2.0.8, 4th of 5.

Checked 2026-11-08: iTunes lookup API and US App Store pages (price, in-app purchases, version, rating, listing text).
Coin coverage: CoinGecko from its API (ids official-trump, world-liberty-financial, usd1-wlfi); CoinMarketCap and CoinStats
from their coin pages (coinmarketcap.com/currencies/..., coinstats.app/coins/...); Crypton searches CoinGecko (its listing).
Delta: delta.app returned 403, so its coverage of the three tokens is not verified and the page says so.
Crypton: live 2.0.8 has NO price alerts; widgets yes; account optional. Its privacy label today is Data Linked to You;
Data Not Linked to You (not "Data Not Collected"), so the page does not claim anything about it.
Prices: CoinGecko market_chart daily points (00:00 UTC, i.e. the previous day's close) and simple/price on 8 Nov.
News: crypto.news (4 Nov), CNBC (5 Nov), FT front page headline only (paywalled). Neutral and attributed.
hide_from_related until 11 Nov like the other new pages in sections with protected pages (GROWTH_LOG pending list)."""

DAY = "2026-11-08"
WIDGETS = '<a href="/best-crypto-price-widget-apps-iphone/">crypto widget apps</a>'
ALERTS = '<a href="/best-crypto-price-alert-apps-iphone/">crypto price alert apps</a>'
NOCONNECT = '<a href="/crypto-portfolio-tracker-without-connecting-wallet-iphone/">trackers that need no wallet or exchange</a>'

CNEWS = "https://crypto.news/democrats-prepare-to-investigate-world-liberty-financial-after-house-win/"
CNBC = "https://www.cnbc.com/2026/11/05/crypto-midterms-democrats-clarity-act.html"

CONTEXT = f"""<h2 id="context">What happened (8 November 2026)</h2>
<p>After the 3 November midterms, Democrats won a House majority according to NBC News and MS NOW projections, and plan to investigate the Trump family's crypto businesses, including World Liberty Financial (the WLFI token and the USD1 stablecoin) and the TRUMP meme coin, <a href="{CNEWS}">crypto.news reported</a>; investigations could begin as early as February 2027. The White House rejected the plans; before the vote a spokeswoman had called Democrats' agenda a "witch hunt", per the same report. <a href="{CNBC}">CNBC wrote</a> that the result puts the crypto industry on the defensive in Washington, and on 8 November the Financial Times ran the story on its front page under the headline "Crypto industry braces for reckoning over Trump ties".</p>
<div class="scroll"><table style="min-width:0">
<thead><tr><th>Token</th><th>1 Nov 2026</th><th>8 Nov 2026</th><th>Change</th><th>Market cap, 8 Nov</th></tr></thead>
<tbody>
<tr><td>TRUMP (Official Trump)</td><td>$1.71</td><td>$1.16</td><td>about −32%</td><td>about $328 million</td></tr>
<tr><td>WLFI (World Liberty Financial)</td><td>$0.050</td><td>$0.046</td><td>about −8%</td><td>about $1.47 billion</td></tr>
<tr><td>USD1 (stablecoin)</td><td>$0.998</td><td>$0.998</td><td>held its $1 peg</td><td>about $3.44 billion</td></tr>
<tr><td>Bitcoin, for comparison</td><td>$78,294</td><td>$75,820</td><td>about −3%</td><td>about $1.52 trillion</td></tr>
</tbody></table></div>
<p class="note">Prices in US dollars from the CoinGecko API: the 1 November column is that day's close, the 8 November column the price on the afternoon of 8 November (UTC). TRUMP's largest one-day fall in the week was on 4 November, the day after the election, from about $1.59 to $1.27. Nothing on this page is financial advice.</p>
"""


def app(name, i, anchor, dev, r, n, ver, date, price, coins, alerts, widget, account, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, coins, alerts, widget, account, f"{ver} ({date})", f"{round(r, 1)} ({n:,} ratings)"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("CoinGecko: Crypto Tracker", 1390323960, "coingecko", "Gecko Labs Pte. Ltd.", 4.81, 27234, "3.60.0", "27 Oct 2026",
        "Free; Premium $9.90 a month or $99.90 a year", "Yes, all three", "Yes: price alerts and large-mover alerts", "Yes, Home Screen",
        "Listing does not say one is required",
        "following WLFI, TRUMP and USD1 from the same source as the price table above, with alerts.",
        ["CoinGecko's own data lists Official Trump, World Liberty Financial and USD1, so you can add all three to a watchlist.",
         "Its listing offers personalised price alerts and large market movement alerts for watchlist coins, a portfolio with profit and loss, and a Home Screen widget.",
         "Tracks categories such as meme coins, which is where TRUMP sits."],
        "English only, and the listing does not say how many alerts are free."),
    app("CoinMarketCap: Crypto Tracker", 1282107098, "coinmarketcap", "CoinMarketCap, LLC", 4.81, 173172, "5.24.0", "1 Nov 2026",
        "Free; Essential $11.99 a month or $109.99 a year; Plus $23.99 a month or $229.99 a year; Max $119.99 a month", "Yes, all three", "Yes: customisable price alerts",
        "Listing does not mention one", "Needed for the portfolio; incognito mode without logging in",
        "the most-rated tracker, with alerts on any of the three tokens.",
        ["CoinMarketCap has pages for Official Trump, World Liberty Financial and World Liberty Financial USD (USD1).",
         "Customisable price alerts and watchlists; tracks 45,000+ active markets, per its listing.",
         "About 173,000 US ratings, the most here, and 21 languages."],
        "its listing says to sign up to make a portfolio (incognito mode keeps data on the phone), it does not mention a widget, and its plans are the most expensive here."),
    app("CoinStats: Crypto Portfolio", 1247849330, "coinstats", "COINSTATSAPP LLC", 4.76, 86114, "5.31.1", "30 Oct 2026",
        "Free; Pro $4.99 a month or $39.99 a year; Premium $15.99 to $19.99 a month or $65.99 to $164.99 a year", "Yes, all three",
        "Yes: price, volume and market-cap alerts, plus Auto Alerts", "Yes: Home Screen, Lock Screen and Apple Watch",
        "Listing does not say one is required",
        "holding WLFI or TRUMP in a wallet or exchange and wanting it tracked automatically, with alerts and Lock Screen widgets.",
        ["coinstats.app has pages for Official Trump, World Liberty Financial and USD1.",
         "Connects 300+ wallets and exchanges and shows real-time profit and loss; prices for 20,000+ coins, per its listing.",
         "Price, volume or market-cap alerts on any coin, and widgets on the Home Screen, Lock Screen and Apple Watch."],
        "many overlapping paid plans, and the full set of insights needs Premium."),
    app("Crypto Tracker: Crypton", 1143691286, "crypton", "Saga Ltd.", 4.70, 186, "2.0.8", "24 Oct 2026",
        "Free, no in-app purchases", "Yes, by search (CoinGecko data)", "No", "Yes: prices and portfolio (Home Screen)", "No (optional, only to sync)",
        "a free watchlist of WLFI, TRUMP and USD1 on the Home Screen, with no account and nothing to pay.",
        ["Live prices for the top 250 coins, plus search for any coin listed on CoinGecko, so WLFI, TRUMP and USD1 can go into Favorites, per its listing.",
         "Portfolio with profit and loss on every coin, and Home Screen widgets for prices and for your portfolio.",
         "No in-app purchases; English only, iOS 18 or later."],
        "no price alerts in the live version, no Lock Screen widget or Apple Watch app, and no wallet or exchange sync; fewest ratings here (186). For alerts, see the " + ALERTS + "."
        , ours=True),
    app("Delta by eToro", 1288676542, "delta", "Opus Labs CVBA", 4.71, 11362, "2026.3.2", "5 Nov 2026",
        "Free up to 10 assets; PRO $6.99 to $13.99 a month or $58.99 to $99.90 a year; PRO+ $13.99 a month or $107.99 a year", "Not verified (listing: 10,000+ coins)",
        "Yes: price targets and big moves", "Listing does not mention one", "Listing does not say",
        "tracking crypto and stocks in one portfolio, with alerts.",
        ["Tracks crypto, stocks, ETFs, commodities and forex together; 10,000+ coins, per its listing.",
         "Smart price alerts for target prices and significant moves, and custom notifications for portfolio milestones.",
         "Free plan tracks up to 10 assets; PRO up to 40; PRO+ unlimited."],
        "we could not confirm on Delta's site that it lists WLFI, TRUMP and USD1, the free plan stops at 10 assets, and its privacy label includes Data Used to Track You."),
]

PAGES = [{
    "group": "wlfi-trump-trackers", "lang": "en", "store": "us", "path": "best-apps-to-track-wlfi-trump-coin-iphone/", "ct": "rl-wlfi-trump",
    "category": "FinanceApplication", "cover": "crypto-widgets", "hide_from_related": True,
    "published": DAY, "updated": DAY, "checked": DAY,
    "kicker": "5 apps · Ranking · News",
    "title": "Best iPhone Apps to Track WLFI, TRUMP and USD1 Prices (Nov 2026)",
    "h1": "Best iPhone apps to track WLFI, TRUMP and USD1 prices (Nov 2026)",
    "description": "Five iPhone apps that track World Liberty Financial (WLFI), the TRUMP meme coin and USD1, compared by price, alerts, widgets and account on 8 Nov 2026.",
    "llms": "Five iPhone apps to follow WLFI, TRUMP and USD1 after the November 2026 midterms: CoinGecko, CoinMarketCap, CoinStats, Crypton, Delta. Which list the three tokens, alerts, widgets, account, US price, rating. With CoinGecko prices 1-8 Nov 2026 and dated news context. Not financial advice.",
    "answer": [
        "To follow WLFI, TRUMP and USD1 with price alerts, <strong>CoinGecko</strong>, <strong>CoinMarketCap</strong> and <strong>CoinStats</strong> all list the three tokens; CoinStats also connects your wallet and has Lock Screen widgets.",
        "For a free Home Screen widget with no account and nothing to buy, <strong>Crypton</strong> finds all three by search but has no alerts, and <strong>Delta</strong> suits a portfolio that mixes crypto with stocks.",
    ],
    "context_html": CONTEXT,
    "columns": ["App", "Price (US)", "Lists WLFI, TRUMP, USD1", "Price alerts", "Widget", "Account needed", "Version (date)", "Rating (US)"],
    "table_note": "Prices, versions and ratings are those on each US App Store page on 8 November 2026; all five are free to download. Alerts, widgets and account are as each listing describes them. Token coverage checked on each company's website or data on 8 November.",
    "apps": APPS,
    "who": ["<strong>Alerts when TRUMP or WLFI moves sharply:</strong> CoinGecko (large-mover alerts) or CoinStats (Auto Alerts).",
            "<strong>The most-used tracker:</strong> CoinMarketCap.",
            "<strong>Tokens held in a wallet or on an exchange:</strong> CoinStats.",
            "<strong>Just a glance at the three prices, no account:</strong> Crypton.",
            "<strong>Crypto and stocks in one place:</strong> Delta."],
    "cases": ["See whether USD1 stays at $1: any app that lists it; CoinGecko and CoinMarketCap show its market cap too.",
              "Get a notification if TRUMP falls another 10%: CoinGecko, CoinMarketCap, CoinStats or Delta (alerts); not Crypton.",
              "Keep WLFI and TRUMP on the Home Screen: CoinGecko, CoinStats or Crypton. More in our " + WIDGETS + " and " + ALERTS + " rankings.",
              "Track holdings without linking a wallet: see the " + NOCONNECT + "."],
    "method": ["On 8 November 2026 we read each app's US App Store page and Apple's lookup data (price, in-app purchases, version, rating and listing text). Whether an app lists WLFI, TRUMP and USD1 was checked on CoinGecko's data, on CoinMarketCap's and CoinStats' coin pages, and in Crypton's listing (it searches CoinGecko); Delta's site did not let us check. We did not install the apps or test how fast alerts arrive.",
               "The news context is attributed to the outlets linked above; this page takes no position on the investigations. None of these apps is an exchange, and nothing here is financial advice."],
    "faq": [
        ("Which app shows the WLFI price on iPhone?", "CoinGecko, CoinMarketCap and CoinStats list World Liberty Financial (WLFI), and Crypton finds it by search because it uses CoinGecko data."),
        ("Can I get an alert for the TRUMP meme coin price?", "Yes, with CoinGecko, CoinMarketCap, CoinStats or Delta, which list price alerts. Crypton has no price alerts."),
        ("Is USD1 still worth one dollar?", "On CoinGecko it traded at about $0.998 from 1 to 8 November 2026, with a market cap of about $3.44 billion."),
        ("Why did TRUMP and WLFI fall in November 2026?", "On CoinGecko, TRUMP fell about 32% and WLFI about 8% from 1 to 8 November, the week Democrats who won the House said they plan to investigate the Trump family's crypto businesses, according to crypto.news and CNBC. This page does not attribute any price move to a cause, and it is not financial advice."),
        ("Do I need an account to track these tokens?", "Not in Crypton (the account only syncs). CoinMarketCap needs one for its portfolio but has an incognito mode; the other listings do not say one is required."),
    ],
    "sources": [("crypto.news, 4 Nov 2026: Democrats prepare to investigate World Liberty Financial after House win", CNEWS),
                ("CNBC, 5 Nov 2026: Democratic sweep puts crypto on defensive in Washington", CNBC),
                ("Financial Times, 8 Nov 2026 front page: Crypto industry braces for reckoning over Trump ties (headline only)", "https://www.ft.com/"),
                ("CoinGecko API: TRUMP, WLFI, USD1 and BTC prices", "https://www.coingecko.com/en/api"),
                ("CoinMarketCap: Official Trump", "https://coinmarketcap.com/currencies/official-trump/"),
                ("CoinMarketCap: World Liberty Financial", "https://coinmarketcap.com/currencies/world-liberty-financial-wlfi/"),
                ("CoinMarketCap: USD1", "https://coinmarketcap.com/currencies/usd1/"),
                ("CoinStats: Official Trump", "https://coinstats.app/coins/official-trump/"),
                ("CoinStats: World Liberty Financial", "https://coinstats.app/coins/world-liberty-financial/"),
                ("CoinStats: USD1", "https://coinstats.app/coins/usd1-wlfi/")]
               + [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS],
}]
