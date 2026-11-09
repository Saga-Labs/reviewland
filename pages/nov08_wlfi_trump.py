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
         "row": [price, coins, alerts, widget, account, f"{ver} ({date})", f"{round(r, 1)}"]}
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
        "no price alerts in the live version, no Lock Screen widget or Apple Watch app, and no wallet or exchange sync. For alerts, see the " + ALERTS + "."
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


# ---- Translations (9 Nov 2026). Same facts as the English page: same apps, same order, same US prices and
# ratings, same links. Prices stay in US dollars on the US App Store (store "us"): no per-country prices are
# checked here. Ratings counts are dropped (star ratings only, no aggregateRating), as in pages/trlib.py.
import copy as _copy

TR_DAY = "2026-11-09"


def _translated(lang, prefix, ct, t):
    en = next(p for p in PAGES if p["lang"] == "en")
    p = _copy.deepcopy(en)
    for k in ("kicker", "title", "h1", "description", "llms", "answer", "context_html", "columns",
              "table_note", "who", "cases", "method", "faq"):
        p[k] = t[k]
    p["apps"] = _copy.deepcopy(en["apps"])
    for a, x in zip(p["apps"], t["apps"]):
        a["row"], a["best_for"], a["facts"], a["limits"] = x["row"], x["best_for"], x["facts"], x["limits"]
        a.pop("rating", None)
    assert len(t["sources"]) == len(en["sources"]), lang
    p["sources"] = [(lbl, url) for lbl, (_, url) in zip(t["sources"], en["sources"])]
    p["lang"], p["store"] = lang, "us"
    p["path"] = f"{prefix}/{en['path']}"
    p["ct"] = f"{en['ct']}-{ct}"
    p["published"] = p["updated"] = TR_DAY
    p["checked"] = DAY
    return p


_RU_WIDGETS = '<a href="/best-crypto-price-widget-apps-iphone/">виджеты для криптовалют</a>'
_RU_ALERTS = '<a href="/best-crypto-price-alert-apps-iphone/">приложения с оповещениями о криптоценах</a>'
_RU_NOCONNECT = '<a href="/crypto-portfolio-tracker-without-connecting-wallet-iphone/">трекеры, которым не нужен кошелёк или биржа</a>'

RU = dict(
    kicker="5 приложений · Рейтинг · Новости",
    title="Лучшие приложения для iPhone для курсов WLFI, TRUMP и USD1 (ноябрь 2026)",
    h1="Лучшие приложения для iPhone, чтобы следить за курсами WLFI, TRUMP и USD1 (ноябрь 2026)",
    description="Пять приложений для iPhone, которые отслеживают World Liberty Financial (WLFI), мем-монету TRUMP и USD1: сравнение по цене, оповещениям, виджетам и аккаунту на 8 ноября 2026 года.",
    llms="Пять приложений для iPhone, чтобы следить за WLFI, TRUMP и USD1 после промежуточных выборов в США в ноябре 2026 года: CoinGecko, CoinMarketCap, CoinStats, Crypton, Delta. Какие из них показывают три токена, оповещения, виджеты, аккаунт, цену в США и рейтинг. С ценами CoinGecko за 1-8 ноября 2026 года и датированным контекстом новостей. Не является финансовой рекомендацией.",
    answer=[
        "Чтобы следить за WLFI, TRUMP и USD1 с оповещениями о цене, подойдут <strong>CoinGecko</strong>, <strong>CoinMarketCap</strong> и <strong>CoinStats</strong>: все три показывают эти токены. CoinStats также подключает кошелёк и имеет виджеты на экране блокировки.",
        "Для бесплатного виджета на домашнем экране без аккаунта и без покупок <strong>Crypton</strong> находит все три токена через поиск, но без оповещений. <strong>Delta</strong> подойдёт, если в портфеле есть и криптовалюты, и акции.",
    ],
    context_html=f"""<h2 id="context">Что произошло (8 ноября 2026)</h2>
<p>После промежуточных выборов 3 ноября демократы получили большинство в Палате представителей по прогнозам NBC News и MS NOW и планируют расследовать криптобизнес семьи Трампа, в том числе World Liberty Financial (токен WLFI и стейблкоин USD1) и мем-монету TRUMP. <a href="{CNEWS}">Пишет crypto.news</a>: расследования могут начаться уже в феврале 2027 года. Белый дом отверг эти планы; до голосования, по тому же источнику, представитель администрации назвала повестку демократов «охотой на ведьм». <a href="{CNBC}">CNBC пишет</a>, что результат выборов ставит криптоиндустрию в оборону в Вашингтоне, а 8 ноября Financial Times вынесла эту историю на первую полосу под заголовком «Crypto industry braces for reckoning over Trump ties» (на английском).</p>
<div class="scroll"><table style="min-width:0">
<thead><tr><th>Токен</th><th>1 нояб. 2026</th><th>8 нояб. 2026</th><th>Изменение</th><th>Капитализация, 8 нояб.</th></tr></thead>
<tbody>
<tr><td>TRUMP (Official Trump)</td><td>$1.71</td><td>$1.16</td><td>около −32%</td><td>около $328 млн</td></tr>
<tr><td>WLFI (World Liberty Financial)</td><td>$0.050</td><td>$0.046</td><td>около −8%</td><td>около $1,47 млрд</td></tr>
<tr><td>USD1 (стейблкоин)</td><td>$0.998</td><td>$0.998</td><td>сохранил привязку к $1</td><td>около $3,44 млрд</td></tr>
<tr><td>Bitcoin, для сравнения</td><td>$78 294</td><td>$75 820</td><td>около −3%</td><td>около $1,52 трлн</td></tr>
</tbody></table></div>
<p class="note">Цены в долларах США по данным API CoinGecko: колонка за 1 ноября — закрытие этого дня, колонка за 8 ноября — цена во второй половине дня 8 ноября (по UTC). Самое сильное падение TRUMP за неделю пришлось на 4 ноября, день после выборов: примерно с $1.59 до $1.27. Ничто на этой странице не является финансовой рекомендацией.</p>
""",
    columns=["Приложение", "Цена (США)", "Есть WLFI, TRUMP, USD1", "Оповещения о цене", "Виджет", "Нужен аккаунт", "Версия (дата)", "Рейтинг (США)"],
    table_note="Цены, версии и рейтинги — как на американских страницах App Store на 8 ноября 2026 года; все пять приложений скачиваются бесплатно. Оповещения, виджеты и аккаунт — как их описывает каждая страница в App Store. Наличие токенов проверено на сайте каждой компании или по данным на 8 ноября.",
    apps=[
        dict(
            row=["Бесплатно; Premium $9.90 в месяц или $99.90 в год", "Да, все три", "Да: оповещения о цене и о резких движениях", "Да, на домашнем экране", "В описании не сказано, что нужен", "3.60.0 (27 окт. 2026)", "4.8"],
            best_for="следить за WLFI, TRUMP и USD1 по тем же данным, что и таблица цен выше, с оповещениями.",
            facts=[
                "Данные CoinGecko включают Official Trump, World Liberty Financial и USD1, так что все три можно добавить в список наблюдения.",
                "В описании: персональные оповещения о цене и оповещения о резких движениях для монет из списка наблюдения, портфель с прибылью и убытком, виджет на домашнем экране.",
                "Есть категории монет, например мем-монеты, к которым относится TRUMP.",
            ],
            limits="только английский язык, и в описании не сказано, сколько оповещений бесплатно.",
        ),
        dict(
            row=["Бесплатно; Essential $11.99 в месяц или $109.99 в год; Plus $23.99 в месяц или $229.99 в год; Max $119.99 в месяц", "Да, все три", "Да: настраиваемые оповещения о цене", "В описании не упомянут", "Нужен для портфеля; режим инкогнито без входа", "5.24.0 (1 нояб. 2026)", "4.8"],
            best_for="самый оцениваемый трекер: оповещения по любому из трёх токенов.",
            facts=[
                "У CoinMarketCap есть страницы Official Trump, World Liberty Financial и World Liberty Financial USD (USD1).",
                "Настраиваемые оповещения о цене и списки наблюдения; по описанию, отслеживает более 45 000 активных рынков.",
                "Около 173 000 оценок в США, больше всех в этой подборке, и 21 язык.",
            ],
            limits="в описании сказано зарегистрироваться, чтобы составить портфель (режим инкогнито хранит данные на телефоне), виджет не упомянут, а тарифы здесь самые дорогие.",
        ),
        dict(
            row=["Бесплатно; Pro $4.99 в месяц или $39.99 в год; Premium $15.99-$19.99 в месяц или $65.99-$164.99 в год", "Да, все три", "Да: по цене, объёму и капитализации, плюс Auto Alerts", "Да: домашний экран, экран блокировки и Apple Watch", "В описании не сказано, что нужен", "5.31.1 (30 окт. 2026)", "4.8"],
            best_for="тех, кто держит WLFI или TRUMP в кошельке или на бирже и хочет, чтобы они отслеживались автоматически, с оповещениями и виджетами на экране блокировки.",
            facts=[
                "У coinstats.app есть страницы Official Trump, World Liberty Financial и USD1.",
                "Подключает более 300 кошельков и бирж и показывает прибыль и убыток в реальном времени; по описанию, цены более 20 000 монет.",
                "Оповещения о цене, объёме или капитализации по любой монете и виджеты на домашнем экране, экране блокировки и Apple Watch.",
            ],
            limits="много платных тарифов, которые частично совпадают, а полный набор аналитики нужен Premium.",
        ),
        dict(
            row=["Бесплатно, покупок в приложении нет", "Да, поиском (данные CoinGecko)", "Нет", "Да: цены и портфель (домашний экран)", "Нет (необязательно, только для синхронизации)", "2.0.8 (24 окт. 2026)", "4.7"],
            best_for="бесплатного списка наблюдения WLFI, TRUMP и USD1 на домашнем экране, без аккаунта и без оплаты.",
            facts=[
                "Живые цены по 250 самым крупным монетам и поиск любой монеты из списка CoinGecko, так что WLFI, TRUMP и USD1 можно добавить в «Избранное», по описанию.",
                "Портфель с прибылью и убытком по каждой монете, виджеты на домашнем экране для цен и для портфеля.",
                "Покупок в приложении нет; только английский язык, iOS 18 или новее.",
            ],
            limits="в живой версии нет оповещений о цене, виджета на экран блокировки и приложения для Apple Watch, нет синхронизации с кошельками и биржами. Для оповещений см. " + _RU_ALERTS + ".",
        ),
        dict(
            row=["Бесплатно до 10 активов; PRO $6.99-$13.99 в месяц или $58.99-$99.90 в год; PRO+ $13.99 в месяц или $107.99 в год", "Не проверено (в описании: 10 000+ монет)", "Да: целевые цены и крупные движения", "В описании не упомянут", "В описании не сказано", "2026.3.2 (5 нояб. 2026)", "4.7"],
            best_for="отслеживания криптовалют и акций в одном портфеле с оповещениями.",
            facts=[
                "Отслеживает криптовалюты, акции, ETF, сырьевые товары и форекс вместе; по описанию, 10 000+ монет.",
                "Умные оповещения о целевых ценах и значительных движениях, а также свои уведомления о достижении вех портфеля.",
                "Бесплатный тариф ведёт до 10 активов; PRO до 40; PRO+ без ограничений.",
            ],
            limits="на сайте Delta мы не смогли подтвердить наличие WLFI, TRUMP и USD1; бесплатный тариф останавливается на 10 активах; а в метке конфиденциальности есть данные, используемые для отслеживания.",
        ),
    ],
    who=["<strong>Оповещения, когда TRUMP или WLFI резко движутся:</strong> CoinGecko (оповещения о крупных движениях) или CoinStats (Auto Alerts).",
         "<strong>Самый используемый трекер:</strong> CoinMarketCap.",
         "<strong>Токены в кошельке или на бирже:</strong> CoinStats.",
         "<strong>Просто взглянуть на три цены без аккаунта:</strong> Crypton.",
         "<strong>Криптовалюты и акции в одном месте:</strong> Delta."],
    cases=["Проверить, держится ли USD1 у $1: любое приложение из списка, где он есть; CoinGecko и CoinMarketCap показывают и его капитализацию.",
           "Получить уведомление, если TRUMP упадёт ещё на 10%: CoinGecko, CoinMarketCap, CoinStats или Delta (оповещения); Crypton — нет.",
           "Держать WLFI и TRUMP на домашнем экране: CoinGecko, CoinStats или Crypton. Больше в рейтингах " + _RU_WIDGETS + " и " + _RU_ALERTS + ".",
           "Следить за балансом без подключения кошелька: см. " + _RU_NOCONNECT + "."],
    method=["8 ноября 2026 года мы прочитали американскую страницу каждого приложения в App Store и данные Apple lookup (цена, покупки в приложении, версия, рейтинг и текст описания). Есть ли в приложении WLFI, TRUMP и USD1, проверяли по данным CoinGecko, по страницам монет на CoinMarketCap и CoinStats, а в Crypton по описанию (оно ищет через CoinGecko); сайт Delta проверить не удалось. Приложения мы не устанавливали и не проверяли, как быстро приходят оповещения.",
            "Новостной контекст приписан изданиям, на которые есть ссылки выше; эта страница не занимает позицию по расследованиям. Ни одно из приложений не является биржей, и ничто здесь не является финансовой рекомендацией."],
    faq=[
        ("В каком приложении на iPhone смотреть курс WLFI?", "CoinGecko, CoinMarketCap и CoinStats показывают World Liberty Financial (WLFI); Crypton находит его поиском, потому что использует данные CoinGecko."),
        ("Можно ли получить оповещение о цене мем-монеты TRUMP?", "Да, в CoinGecko, CoinMarketCap, CoinStats или Delta, где есть оповещения о цене. В Crypton оповещений о цене нет."),
        ("Стоит ли USD1 по-прежнему один доллар?", "По данным CoinGecko, с 1 по 8 ноября 2026 года он торговался примерно по $0.998, капитализация около $3,44 млрд."),
        ("Почему TRUMP и WLFI упали в ноябре 2026 года?", "По данным CoinGecko, с 1 по 8 ноября TRUMP упал примерно на 32%, а WLFI примерно на 8%, в ту неделю, когда демократы, получившие большинство в Палате, сообщили о планах расследовать криптобизнес семьи Трампа, по данным crypto.news и CNBC. Эта страница не связывает движение цены ни с какой причиной и не является финансовой рекомендацией."),
        ("Нужен ли аккаунт, чтобы следить за этими токенами?", "В Crypton нет (аккаунт нужен только для синхронизации). CoinMarketCap требует аккаунт для портфеля, но есть режим инкогнито; в других описаниях не сказано, что аккаунт нужен."),
    ],
    sources=["crypto.news, 4 нояб. 2026: демократы готовят расследование World Liberty Financial после победы в Палате",
             "CNBC, 5 нояб. 2026: победа демократов ставит криптоиндустрию в оборону в Вашингтоне",
             "Financial Times, 8 нояб. 2026, первая полоса: «Crypto industry braces for reckoning over Trump ties» (только заголовок)",
             "API CoinGecko: цены TRUMP, WLFI, USD1 и BTC",
             "CoinMarketCap: Official Trump",
             "CoinMarketCap: World Liberty Financial",
             "CoinMarketCap: USD1",
             "CoinStats: Official Trump",
             "CoinStats: World Liberty Financial",
             "CoinStats: USD1",
             "CoinGecko: Crypto Tracker (App Store)",
             "CoinMarketCap: Crypto Tracker (App Store)",
             "CoinStats: Crypto Portfolio (App Store)",
             "Crypto Tracker: Crypton (App Store)",
             "Delta by eToro (App Store)"],
)

PAGES.append(_translated("ru", "ru", "ru", RU))


_DE_WIDGETS = '<a href="/best-crypto-price-widget-apps-iphone/">Krypto-Widget-Apps</a>'
_DE_ALERTS = '<a href="/best-crypto-price-alert-apps-iphone/">Krypto-Kursalarm-Apps</a>'
_DE_NOCONNECT = '<a href="/crypto-portfolio-tracker-without-connecting-wallet-iphone/">Tracker ohne Wallet- oder Börsenverbindung</a>'

DE = dict(
    kicker="5 Apps · Ranking · Nachrichten",
    title="Beste iPhone-Apps für die Kurse von WLFI, TRUMP und USD1 (November 2026)",
    h1="Beste iPhone-Apps für die Kurse von WLFI, TRUMP und USD1 (November 2026)",
    description="Fünf iPhone-Apps, die World Liberty Financial (WLFI), die Meme-Münze TRUMP und USD1 verfolgen: Vergleich nach Preis, Warnungen, Widgets und Konto am 8. November 2026.",
    llms="Fünf iPhone-Apps, um WLFI, TRUMP und USD1 nach den US-Zwischenwahlen im November 2026 zu verfolgen: CoinGecko, CoinMarketCap, CoinStats, Crypton, Delta. Welche die drei Token führen, Warnungen, Widgets, Konto, US-Preis und Bewertung. Mit CoinGecko-Kursen vom 1. bis 8. November 2026 und datiertem Nachrichtenkontext. Keine Finanzberatung.",
    answer=[
        "Um WLFI, TRUMP und USD1 mit Kursalarmen zu verfolgen, führen <strong>CoinGecko</strong>, <strong>CoinMarketCap</strong> und <strong>CoinStats</strong> alle drei Token auf. CoinStats verbindet zusätzlich Ihre Wallet und hat Widgets für den Sperrbildschirm.",
        "Für ein kostenloses Widget auf dem Home-Bildschirm ohne Konto und ohne Kauf findet <strong>Crypton</strong> alle drei Token per Suche, hat aber keine Warnungen. <strong>Delta</strong> passt, wenn das Depot Krypto und Aktien mischt.",
    ],
    context_html=f"""<h2 id="context">Was passiert ist (8. November 2026)</h2>
<p>Nach den Zwischenwahlen am 3. November hat die Demokratische Partei laut Prognosen von NBC News und MS NOW die Mehrheit im Repräsentantenhaus gewonnen und plant, die Krypto-Geschäfte der Familie Trump zu untersuchen, darunter World Liberty Financial (der WLFI-Token und der Stablecoin USD1) und die Meme-Münze TRUMP. <a href="{CNEWS}">crypto.news berichtet</a>, die Ermittlungen könnten schon im Februar 2027 beginnen. Das Weiße Haus lehnt die Pläne ab; vor der Wahl hatte eine Sprecherin die Agenda der Demokraten laut demselben Bericht als „Hexenjagd“ bezeichnet. <a href="{CNBC}">CNBC schreibt</a>, das Ergebnis bringe die Kryptobranche in Washington in die Defensive, und am 8. November brachte die Financial Times die Geschichte auf die Titelseite unter der Überschrift „Crypto industry braces for reckoning over Trump ties“ (englische Überschrift).</p>
<div class="scroll"><table style="min-width:0">
<thead><tr><th>Token</th><th>1. Nov. 2026</th><th>8. Nov. 2026</th><th>Veränderung</th><th>Marktkapitalisierung, 8. Nov.</th></tr></thead>
<tbody>
<tr><td>TRUMP (Official Trump)</td><td>$1.71</td><td>$1.16</td><td>etwa −32 %</td><td>etwa 328 Mio. $</td></tr>
<tr><td>WLFI (World Liberty Financial)</td><td>$0.050</td><td>$0.046</td><td>etwa −8 %</td><td>etwa 1,47 Mrd. $</td></tr>
<tr><td>USD1 (Stablecoin)</td><td>$0.998</td><td>$0.998</td><td>hielt die Bindung an 1 $</td><td>etwa 3,44 Mrd. $</td></tr>
<tr><td>Bitcoin, zum Vergleich</td><td>$78.294</td><td>$75.820</td><td>etwa −3 %</td><td>etwa 1,52 Bio. $</td></tr>
</tbody></table></div>
<p class="note">Preise in US-Dollar laut CoinGecko-API: Die Spalte vom 1. November zeigt den Schlusskurs dieses Tages, die Spalte vom 8. November den Kurs am Nachmittag des 8. November (UTC). Der größte Tagesverlust von TRUMP in dieser Woche war am 4. November, dem Tag nach der Wahl, von etwa 1,59 $ auf 1,27 $. Nichts auf dieser Seite ist Finanzberatung.</p>
""",
    columns=["App", "Preis (USA)", "Führt WLFI, TRUMP, USD1", "Kurswarnungen", "Widget", "Konto nötig", "Version (Datum)", "Bewertung (USA)"],
    table_note="Preise, Versionen und Bewertungen wie auf den US-Seiten im App Store am 8. November 2026; alle fünf Apps sind kostenlos. Warnungen, Widgets und Konto so, wie es die jeweilige Store-Seite beschreibt. Die Token-Abdeckung wurde auf der Website jedes Anbieters bzw. anhand der Daten vom 8. November geprüft.",
    apps=[
        dict(
            row=["Kostenlos; Premium 9,90 $ im Monat oder 99,90 $ im Jahr", "Ja, alle drei", "Ja: Kurs- und Warnungen bei großen Bewegungen", "Ja, auf dem Home-Bildschirm", "In der Beschreibung nicht verlangt", "3.60.0 (27. Okt. 2026)", "4.8"],
            best_for="das Verfolgen von WLFI, TRUMP und USD1 mit denselben Daten wie in der Kurstabelle oben, mit Warnungen.",
            facts=[
                "Die CoinGecko-Daten führen Official Trump, World Liberty Financial und USD1, sodass Sie alle drei auf eine Beobachtungsliste setzen können.",
                "Laut Beschreibung gibt es persönliche Kursalarme und Warnungen bei starken Bewegungen für Coins auf der Beobachtungsliste, ein Portfolio mit Gewinn und Verlust und ein Widget auf dem Home-Bildschirm.",
                "Es gibt Kategorien wie Meme-Coins, zu denen TRUMP gehört.",
            ],
            limits="nur Englisch; in der Beschreibung steht nicht, wie viele Warnungen kostenlos sind.",
        ),
        dict(
            row=["Kostenlos; Essential 11,99 $ im Monat oder 109,99 $ im Jahr; Plus 23,99 $ im Monat oder 229,99 $ im Jahr; Max 119,99 $ im Monat", "Ja, alle drei", "Ja: anpassbare Kursalarme", "In der Beschreibung nicht erwähnt", "Für das Portfolio nötig; Inkognitomodus ohne Anmeldung", "5.24.0 (1. Nov. 2026)", "4.8"],
            best_for="den meistbewerteten Tracker: Warnungen für jeden der drei Token.",
            facts=[
                "CoinMarketCap hat Seiten für Official Trump, World Liberty Financial und World Liberty Financial USD (USD1).",
                "Anpassbare Kursalarme und Beobachtungslisten; laut Beschreibung über 45.000 aktive Märkte.",
                "Rund 173.000 Bewertungen in den USA, die meisten in dieser Liste, und 21 Sprachen.",
            ],
            limits="Die Beschreibung verlangt eine Anmeldung für ein Portfolio (der Inkognitomodus hält die Daten auf dem Telefon), ein Widget wird nicht erwähnt, und die Tarife sind hier die teuersten.",
        ),
        dict(
            row=["Kostenlos; Pro 4,99 $ im Monat oder 39,99 $ im Jahr; Premium 15,99–19,99 $ im Monat oder 65,99–164,99 $ im Jahr", "Ja, alle drei", "Ja: Kurs-, Volumen- und Marktkapitalisierungswarnungen, dazu Auto Alerts", "Ja: Home-Bildschirm, Sperrbildschirm und Apple Watch", "In der Beschreibung nicht verlangt", "5.31.1 (30. Okt. 2026)", "4.8"],
            best_for="wenn Sie WLFI oder TRUMP in einer Wallet oder an einer Börse halten und sie automatisch mitlaufen lassen möchten, mit Warnungen und Widgets für den Sperrbildschirm.",
            facts=[
                "coinstats.app hat Seiten für Official Trump, World Liberty Financial und USD1.",
                "Verbindet über 300 Wallets und Börsen und zeigt Gewinn und Verlust in Echtzeit; laut Beschreibung Kurse für über 20.000 Coins.",
                "Kurs-, Volumen- oder Marktkapitalisierungswarnungen für jeden Coin und Widgets auf dem Home-Bildschirm, dem Sperrbildschirm und der Apple Watch.",
            ],
            limits="viele sich überschneidende kostenpflichtige Tarife; für die vollständigen Auswertungen braucht man Premium.",
        ),
        dict(
            row=["Kostenlos, keine In-App-Käufe", "Ja, per Suche (CoinGecko-Daten)", "Nein", "Ja: Kurse und Portfolio (Home-Bildschirm)", "Nein (optional, nur zum Synchronisieren)", "2.0.8 (24. Okt. 2026)", "4.7"],
            best_for="eine kostenlose Beobachtungsliste von WLFI, TRUMP und USD1 auf dem Home-Bildschirm, ohne Konto und ohne Kosten.",
            facts=[
                "Live-Kurse für die 250 größten Coins und Suche nach jedem auf CoinGecko gelisteten Coin, sodass sich WLFI, TRUMP und USD1 als Favoriten speichern lassen, laut Beschreibung.",
                "Portfolio mit Gewinn und Verlust für jeden Coin sowie Widgets auf dem Home-Bildschirm für Kurse und für das Portfolio.",
                "Keine In-App-Käufe; nur Englisch, iOS 18 oder neuer.",
            ],
            limits="In der Live-Version gibt es keine Kursalarme, kein Widget für den Sperrbildschirm und keine App für die Apple Watch, und keine Synchronisierung mit Wallets oder Börsen. Für Warnungen siehe die " + _DE_ALERTS + ".",
        ),
        dict(
            row=["Kostenlos bis 10 Assets; PRO 6,99–13,99 $ im Monat oder 58,99–99,90 $ im Jahr; PRO+ 13,99 $ im Monat oder 107,99 $ im Jahr", "Nicht geprüft (Beschreibung: über 10.000 Coins)", "Ja: Zielkurse und große Bewegungen", "In der Beschreibung nicht erwähnt", "In der Beschreibung nicht angegeben", "2026.3.2 (5. Nov. 2026)", "4.7"],
            best_for="Krypto und Aktien in einem Portfolio, mit Warnungen.",
            facts=[
                "Verfolgt Krypto, Aktien, ETFs, Rohstoffe und Devisen zusammen; laut Beschreibung über 10.000 Coins.",
                "Intelligente Kursalarme für Zielkurse und deutliche Bewegungen sowie eigene Mitteilungen bei Portfolio-Meilensteinen.",
                "Der kostenlose Tarif umfasst bis zu 10 Assets; PRO bis zu 40; PRO+ unbegrenzt.",
            ],
            limits="Auf der Website von Delta konnten wir nicht bestätigen, dass WLFI, TRUMP und USD1 dort gelistet sind; der kostenlose Tarif endet bei 10 Assets; und das Datenschutzlabel nennt „Für Tracking verwendete Daten“.",
        ),
    ],
    who=["<strong>Warnungen, wenn TRUMP oder WLFI stark ausschlagen:</strong> CoinGecko (Warnungen bei großen Bewegungen) oder CoinStats (Auto Alerts).",
         "<strong>Der meistgenutzte Tracker:</strong> CoinMarketCap.",
         "<strong>Token in einer Wallet oder an einer Börse:</strong> CoinStats.",
         "<strong>Nur ein Blick auf die drei Kurse, ohne Konto:</strong> Crypton.",
         "<strong>Krypto und Aktien an einem Ort:</strong> Delta."],
    cases=["Prüfen, ob USD1 bei 1 $ bleibt: jede App aus der Liste, die ihn führt; CoinGecko und CoinMarketCap zeigen auch seine Marktkapitalisierung.",
           "Eine Benachrichtigung, falls TRUMP noch einmal 10 % fällt: CoinGecko, CoinMarketCap, CoinStats oder Delta (mit Warnungen); nicht Crypton.",
           "WLFI und TRUMP auf dem Home-Bildschirm halten: CoinGecko, CoinStats oder Crypton. Mehr in den Rankings " + _DE_WIDGETS + " und " + _DE_ALERTS + ".",
           "Bestände ohne Verbindung einer Wallet verfolgen: siehe " + _DE_NOCONNECT + "."],
    method=["Am 8. November 2026 haben wir die US-Seite jeder App im App Store und die Apple-Lookup-Daten gelesen (Preis, In-App-Käufe, Version, Bewertung und Beschreibungstext). Ob eine App WLFI, TRUMP und USD1 führt, haben wir anhand der CoinGecko-Daten, der Münzseiten von CoinMarketCap und CoinStats sowie der Beschreibung von Crypton geprüft (die Suche läuft über CoinGecko); die Website von Delta ließ sich nicht prüfen. Die Apps haben wir nicht installiert und nicht getestet, wie schnell Warnungen ankommen.",
            "Der Nachrichtenkontext ist den oben verlinkten Medien zugeschrieben; diese Seite bezieht keine Position zu den Ermittlungen. Keine dieser Apps ist eine Börse, und nichts hier ist Finanzberatung."],
    faq=[
        ("Welche App zeigt den WLFI-Kurs auf dem iPhone?", "CoinGecko, CoinMarketCap und CoinStats führen World Liberty Financial (WLFI); Crypton findet ihn per Suche, weil es CoinGecko-Daten nutzt."),
        ("Kann ich eine Warnung für den Kurs der Meme-Münze TRUMP bekommen?", "Ja, mit CoinGecko, CoinMarketCap, CoinStats oder Delta, die Kursalarme anbieten. Crypton hat keine Kursalarme."),
        ("Ist USD1 noch einen Dollar wert?", "Laut CoinGecko lag er vom 1. bis 8. November 2026 bei etwa 0,998 $, mit einer Marktkapitalisierung von etwa 3,44 Mrd. $."),
        ("Warum sind TRUMP und WLFI im November 2026 gefallen?", "Laut CoinGecko fiel TRUMP vom 1. bis 8. November um etwa 32 % und WLFI um etwa 8 %, in der Woche, in der die Demokraten, die das Repräsentantenhaus gewonnen haben, Ermittlungen zu den Krypto-Geschäften der Familie Trump ankündigten, laut crypto.news und CNBC. Diese Seite führt keine Kursbewegung auf eine Ursache zurück und ist keine Finanzberatung."),
        ("Brauche ich ein Konto, um diese Token zu verfolgen?", "Bei Crypton nicht (das Konto dient nur der Synchronisierung). CoinMarketCap braucht eines für das Portfolio, hat aber einen Inkognitomodus; bei den anderen Angaben steht nicht, dass ein Konto nötig ist."),
    ],
    sources=["crypto.news, 4. Nov. 2026: Demokraten bereiten Untersuchung von World Liberty Financial nach Wahlsieg im Repräsentantenhaus vor",
             "CNBC, 5. Nov. 2026: Demokraten-Sieg bringt Kryptobranche in Washington in die Defensive",
             "Financial Times, 8. Nov. 2026, Titelseite: „Crypto industry braces for reckoning over Trump ties“ (nur Überschrift)",
             "CoinGecko-API: Kurse von TRUMP, WLFI, USD1 und BTC",
             "CoinMarketCap: Official Trump",
             "CoinMarketCap: World Liberty Financial",
             "CoinMarketCap: USD1",
             "CoinStats: Official Trump",
             "CoinStats: World Liberty Financial",
             "CoinStats: USD1",
             "CoinGecko: Crypto Tracker (App Store)",
             "CoinMarketCap: Crypto Tracker (App Store)",
             "CoinStats: Crypto Portfolio (App Store)",
             "Crypto Tracker: Crypton (App Store)",
             "Delta by eToro (App Store)"],
)

PAGES.append(_translated("de", "de", "de", DE))


_JA_WIDGETS = '<a href="/best-crypto-price-widget-apps-iphone/">暗号資産ウィジェットアプリ</a>'
_JA_ALERTS = '<a href="/best-crypto-price-alert-apps-iphone/">暗号資産の価格アラートアプリ</a>'
_JA_NOCONNECT = '<a href="/crypto-portfolio-tracker-without-connecting-wallet-iphone/">ウォレットや取引所の接続が不要なトラッカー</a>'

JA = dict(
    kicker="5アプリ · ランキング · ニュース",
    title="WLFI・TRUMP・USD1の価格を追跡するおすすめiPhoneアプリ（2026年11月）",
    h1="WLFI・TRUMP・USD1の価格を追跡するおすすめiPhoneアプリ（2026年11月）",
    description="World Liberty Financial（WLFI）、ミームコインのTRUMP、USD1を追跡する5つのiPhoneアプリ。2026年11月8日時点の価格、価格アラート、ウィジェット、アカウントの有無を比較。",
    llms="2026年11月の米中間選挙後にWLFI、TRUMP、USD1を追うiPhoneアプリ5つ：CoinGecko、CoinMarketCap、CoinStats、Crypton、Delta。3つのトークンの掲載状況、アラート、ウィジェット、アカウント、米国の価格と評価。CoinGeckoの2026年11月1〜8日の価格と日付入りのニュース背景つき。投資助言ではありません。",
    answer=[
        "WLFI、TRUMP、USD1を価格アラート付きで追うなら、<strong>CoinGecko</strong>、<strong>CoinMarketCap</strong>、<strong>CoinStats</strong>の3つがいずれも3トークンを掲載しています。CoinStatsはウォレットとも連携でき、ロック画面ウィジェットもあります。",
        "アカウント不要・無料でホーム画面にウィジェットを置きたいなら、<strong>Crypton</strong>は検索で3つすべて見つかりますが、アラートはありません。<strong>Delta</strong>は暗号資産と株式をまとめて管理したい人向けです。",
    ],
    context_html=f"""<h2 id="context">何が起きたか（2026年11月8日）</h2>
<p>2026年11月3日の中間選挙後、NBC NewsとMS NOWの予測によると民主党が下院の過半数を獲得し、World Liberty Financial（WLFIトークンとステーブルコインUSD1）やミームコインのTRUMPを含む、トランプ一族の暗号資産事業の調査を計画しています。<a href="{CNEWS}">crypto.newsの報道</a>では、調査は早ければ2027年2月にも始まる可能性があります。ホワイトハウスはこの計画を退けており、同じ報道によると、投票前に報道官は民主党の議題を「魔女狩り」と呼んでいました。<a href="{CNBC}">CNBC</a>は、この結果によって暗号資産業界がワシントンで守勢に立たされたと書いています。11月8日にはFinancial Timesがこの話を一面に載せ、見出しは「Crypto industry braces for reckoning over Trump ties」（英語）でした。</p>
<div class="scroll"><table style="min-width:0">
<thead><tr><th>トークン</th><th>2026年11月1日</th><th>2026年11月8日</th><th>変化</th><th>時価総額（11月8日）</th></tr></thead>
<tbody>
<tr><td>TRUMP（Official Trump）</td><td>$1.71</td><td>$1.16</td><td>約−32%</td><td>約3億2,800万ドル</td></tr>
<tr><td>WLFI（World Liberty Financial）</td><td>$0.050</td><td>$0.046</td><td>約−8%</td><td>約14億7,000万ドル</td></tr>
<tr><td>USD1（ステーブルコイン）</td><td>$0.998</td><td>$0.998</td><td>1ドルのペッグを維持</td><td>約34億4,000万ドル</td></tr>
<tr><td>ビットコイン（比較用）</td><td>$78,294</td><td>$75,820</td><td>約−3%</td><td>約1兆5,200億ドル</td></tr>
</tbody></table></div>
<p class="note">CoinGecko APIのドル建て価格。11月1日の列はその日の終値、11月8日の列は11月8日午後（UTC）の価格です。この週のTRUMPの最大の1日下落は、選挙の翌日の11月4日に、約1.59ドルから1.27ドルへ下げたものでした。このページの内容は投資助言ではありません。</p>
""",
    columns=["アプリ", "価格（米国）", "WLFI・TRUMP・USD1の掲載", "価格アラート", "ウィジェット", "アカウント", "バージョン（日付）", "評価（米国）"],
    table_note="価格、バージョン、評価は2026年11月8日時点の米国App Storeのページどおり。5つのアプリはいずれも無料でダウンロードできます。アラート、ウィジェット、アカウントは各ストアの記載どおり。トークンの掲載は各社のサイトまたは11月8日時点のデータで確認しました。",
    apps=[
        dict(
            row=["無料；Premium 月額$9.90 または年額$99.90", "はい、3つすべて", "はい：価格アラートと大きな変動のアラート", "はい、ホーム画面", "説明文では必須とされていない", "3.60.0（2026年10月27日）", "4.8"],
            best_for="上の価格表と同じデータで、WLFI・TRUMP・USD1をアラート付きで追いたい人。",
            facts=[
                "CoinGeckoのデータにはOfficial Trump、World Liberty Financial、USD1が含まれるので、3つすべてをウォッチリストに入れられます。",
                "説明文によれば、ウォッチリストのコインに対する個別の価格アラートと大きな変動のアラート、損益のわかるポートフォリオ、ホーム画面ウィジェットがあります。",
                "TRUMPが属するミームコインなどのカテゴリで絞り込めます。",
            ],
            limits="英語のみ。説明文では無料で使えるアラートの数が書かれていません。",
        ),
        dict(
            row=["無料；Essential 月額$11.99 または年額$109.99；Plus 月額$23.99 または年額$229.99；Max 月額$119.99", "はい、3つすべて", "はい：カスタマイズ可能な価格アラート", "説明文に記載なし", "ポートフォリオに必要；ログインせずシークレットモードで利用可", "5.24.0（2026年11月1日）", "4.8"],
            best_for="最も評価の多いトラッカー。3トークンいずれにもアラートを設定できます。",
            facts=[
                "CoinMarketCapにはOfficial Trump、World Liberty Financial、World Liberty Financial USD（USD1）のページがあります。",
                "カスタマイズ可能な価格アラートとウォッチリスト。説明文によれば、45,000以上のアクティブな市場を追跡します。",
                "米国で約17万3,000件の評価があり、この一覧で最多。21言語対応。",
            ],
            limits="説明文ではポートフォリオを作るにはサインアップが必要とされ（シークレットモードなら端末にデータが残る）、ウィジェットには触れておらず、料金プランはここで最も高額です。",
        ),
        dict(
            row=["無料；Pro 月額$4.99 または年額$39.99；Premium 月額$15.99〜$19.99 または年額$65.99〜$164.99", "はい、3つすべて", "はい：価格、出来高、時価総額のアラートと、Auto Alerts", "はい：ホーム画面、ロック画面、Apple Watch", "説明文では必須とされていない", "5.31.1（2026年10月30日）", "4.8"],
            best_for="WLFIやTRUMPをウォレットや取引所で保有していて、自動で追跡したい人向け。アラートとロック画面ウィジェット付き。",
            facts=[
                "coinstats.appにはOfficial Trump、World Liberty Financial、USD1のページがあります。",
                "300以上のウォレットと取引所に接続し、リアルタイムの損益を表示。説明文によれば、20,000以上のコインの価格に対応。",
                "任意のコインに対する価格、出来高、時価総額のアラートと、ホーム画面、ロック画面、Apple Watchのウィジェット。",
            ],
            limits="有料プランが多数あり内容が一部重複する。すべての分析機能にはPremiumが必要。",
        ),
        dict(
            row=["無料、アプリ内課金なし", "はい、検索で（CoinGeckoのデータ）", "いいえ", "はい：価格とポートフォリオ（ホーム画面）", "いいえ（任意、同期する場合のみ）", "2.0.8（2026年10月24日）", "4.7"],
            best_for="アカウントもお金も不要で、ホーム画面に無料のウォッチリストを置きたい人向け（WLFI、TRUMP、USD1）。",
            facts=[
                "上位250コインのリアルタイム価格と、CoinGeckoに載っている任意のコインの検索。説明文によれば、WLFI、TRUMP、USD1もお気に入りに追加できます。",
                "各コインの損益付きポートフォリオ。価格とポートフォリオのホーム画面ウィジェット。",
                "アプリ内課金なし。英語のみ、iOS 18以降。",
            ],
            limits="ライブ版には価格アラート、ロック画面ウィジェット、Apple Watchアプリがなく、ウォレットや取引所との同期もありません。アラートについては、" + _JA_ALERTS + "をご覧ください。",
        ),
        dict(
            row=["無料（10資産まで）；PRO 月額$6.99〜$13.99 または年額$58.99〜$99.90；PRO+ 月額$13.99 または年額$107.99", "未確認（説明文：10,000以上のコイン）", "はい：目標価格と大きな変動", "説明文に記載なし", "説明文に記載なし", "2026.3.2（2026年11月5日）", "4.7"],
            best_for="暗号資産と株式を1つのポートフォリオで、アラート付きで管理したい人向け。",
            facts=[
                "暗号資産、株式、ETF、コモディティ、外為を一緒に追跡。説明文によれば10,000以上のコイン。",
                "目標価格と大きな変動のスマートな価格アラート、ポートフォリオの節目でのカスタム通知。",
                "無料プランは10資産まで、PROは40、PRO+は無制限。",
            ],
            limits="DeltaのサイトでWLFI、TRUMP、USD1が掲載されているかは確認できませんでした。無料プランは10資産で止まります。また、プライバシーラベルには「トラッキングに使用されるデータ」が含まれます。",
        ),
    ],
    who=["<strong>TRUMPやWLFIが大きく動いたときのアラート：</strong> CoinGecko（大きな変動のアラート）またはCoinStats（Auto Alerts）。",
         "<strong>最も使われているトラッカー：</strong> CoinMarketCap。",
         "<strong>ウォレットや取引所で保有しているトークン：</strong> CoinStats。",
         "<strong>3つの価格をアカウントなしでざっと見る：</strong> Crypton。",
         "<strong>暗号資産と株式を1か所に：</strong> Delta。"],
    cases=["USD1が1ドルを保っているか確認する：掲載しているどのアプリでも可。CoinGeckoとCoinMarketCapは時価総額も表示します。",
           "TRUMPがさらに10%下がったら通知を受け取る：CoinGecko、CoinMarketCap、CoinStats、Delta（アラート付き）。Cryptonは不可。",
           "WLFIとTRUMPをホーム画面に置く：CoinGecko、CoinStats、Crypton。詳しくは" + _JA_WIDGETS + "と" + _JA_ALERTS + "のランキングへ。",
           "ウォレットを接続せずに保有を追跡する：" + _JA_NOCONNECT + "をご覧ください。"],
    method=["2026年11月8日、各アプリの米国App Storeページと、Appleのlookupデータ（価格、アプリ内課金、バージョン、評価、説明文）を確認しました。アプリがWLFI、TRUMP、USD1を掲載しているかは、CoinGeckoのデータ、CoinMarketCapとCoinStatsのコインページ、Cryptonの説明文（検索はCoinGeckoを使用）で確認しました。Deltaのサイトは確認できませんでした。アプリのインストールや、アラートの到着速度の検証は行っていません。",
            "ニュースの背景は上記リンク先の媒体に帰属します。このページは捜査について立場をとりません。これらのアプリはいずれも取引所ではなく、ここに書かれた内容は投資助言ではありません。"],
    faq=[
        ("iPhoneでWLFIの価格を見られるアプリは？", "CoinGecko、CoinMarketCap、CoinStatsがWorld Liberty Financial（WLFI）を掲載しています。CryptonはCoinGeckoのデータを使うため、検索で見つかります。"),
        ("ミームコインTRUMPの価格のアラートは受け取れますか？", "はい。価格アラートがあるCoinGecko、CoinMarketCap、CoinStats、Deltaで可能です。Cryptonには価格アラートがありません。"),
        ("USD1は今も1ドルの価値がありますか？", "CoinGeckoによると、2026年11月1〜8日は約0.998ドルで取引され、時価総額は約34億4,000万ドルでした。"),
        ("2026年11月にTRUMPとWLFIが下落したのはなぜですか？", "CoinGeckoによると、11月1〜8日にTRUMPは約32%、WLFIは約8%下落しました。その週、下院の過半数を得た民主党が、トランプ一族の暗号資産事業の調査を計画していると発表しました（crypto.newsとCNBCによる）。このページは価格の動きを特定の原因に結びつけず、投資助言でもありません。"),
        ("これらのトークンを追うのにアカウントは必要ですか？", "Cryptonでは不要です（アカウントは同期のためだけに使われます）。CoinMarketCapはポートフォリオにアカウントが必要ですが、シークレットモードがあります。ほかのアプリの説明文では必須とは書かれていません。"),
    ],
    sources=["crypto.news、2026年11月4日：民主党、下院選勝利後にWorld Liberty Financialの調査を準備",
             "CNBC、2026年11月5日：民主党の勝利で、暗号資産業界がワシントンで守勢に",
             "Financial Times、2026年11月8日一面：「Crypto industry braces for reckoning over Trump ties」（見出しのみ）",
             "CoinGecko API：TRUMP、WLFI、USD1、BTCの価格",
             "CoinMarketCap：Official Trump",
             "CoinMarketCap：World Liberty Financial",
             "CoinMarketCap：USD1",
             "CoinStats：Official Trump",
             "CoinStats：World Liberty Financial",
             "CoinStats：USD1",
             "CoinGecko: Crypto Tracker (App Store)",
             "CoinMarketCap: Crypto Tracker (App Store)",
             "CoinStats: Crypto Portfolio (App Store)",
             "Crypto Tracker: Crypton (App Store)",
             "Delta by eToro (App Store)"],
)

PAGES.append(_translated("ja", "ja", "ja", JA))


_PT_WIDGETS = '<a href="/best-crypto-price-widget-apps-iphone/">apps de widget de cripto</a>'
_PT_ALERTS = '<a href="/best-crypto-price-alert-apps-iphone/">apps de alerta de preço de cripto</a>'
_PT_NOCONNECT = '<a href="/crypto-portfolio-tracker-without-connecting-wallet-iphone/">rastreadores que não pedem carteira nem corretora</a>'

PT = dict(
    kicker="5 apps · Ranking · Notícias",
    title="Melhores apps para iPhone para acompanhar os preços de WLFI, TRUMP e USD1 (nov. 2026)",
    h1="Melhores apps para iPhone para acompanhar os preços de WLFI, TRUMP e USD1 (nov. 2026)",
    description="Cinco apps para iPhone que acompanham a World Liberty Financial (WLFI), a memecoin TRUMP e a USD1, comparados por preço, alertas, widgets e conta em 8 de novembro de 2026.",
    llms="Cinco apps para iPhone para acompanhar WLFI, TRUMP e USD1 depois das eleições legislativas dos EUA de novembro de 2026: CoinGecko, CoinMarketCap, CoinStats, Crypton, Delta. Quais listam os três tokens, alertas, widgets, conta, preço nos EUA e nota. Com preços da CoinGecko de 1 a 8 de novembro de 2026 e contexto de notícias datado. Não é recomendação financeira.",
    answer=[
        "Para acompanhar WLFI, TRUMP e USD1 com alertas de preço, <strong>CoinGecko</strong>, <strong>CoinMarketCap</strong> e <strong>CoinStats</strong> listam os três tokens; a CoinStats também conecta sua carteira e tem widgets na tela de bloqueio.",
        "Para um widget gratuito na tela inicial, sem conta e sem comprar nada, a <strong>Crypton</strong> encontra os três tokens pela busca, mas não tem alertas; a <strong>Delta</strong> serve para uma carteira que mistura criptomoedas e ações.",
    ],
    context_html=f"""<h2 id="context">O que aconteceu (8 de novembro de 2026)</h2>
<p>Depois das eleições legislativas de 3 de novembro, os democratas conquistaram a maioria na Câmara dos Representantes, segundo as projeções da NBC News e da MS NOW, e planejam investigar os negócios cripto da família Trump, incluindo a World Liberty Financial (o token WLFI e a stablecoin USD1) e a memecoin TRUMP. <a href="{CNEWS}">O crypto.news informou</a> que as investigações podem começar já em fevereiro de 2027. A Casa Branca rejeitou os planos; antes da votação, uma porta-voz havia chamado a agenda dos democratas de “caça às bruxas”, segundo a mesma reportagem. <a href="{CNBC}">A CNBC escreveu</a> que o resultado coloca a indústria cripto na defensiva em Washington, e em 8 de novembro o Financial Times publicou a história na primeira página com o título “Crypto industry braces for reckoning over Trump ties” (título em inglês).</p>
<div class="scroll"><table style="min-width:0">
<thead><tr><th>Token</th><th>1 nov. 2026</th><th>8 nov. 2026</th><th>Variação</th><th>Valor de mercado, 8 nov.</th></tr></thead>
<tbody>
<tr><td>TRUMP (Official Trump)</td><td>US$ 1,71</td><td>US$ 1,16</td><td>cerca de −32%</td><td>cerca de US$ 328 milhões</td></tr>
<tr><td>WLFI (World Liberty Financial)</td><td>US$ 0,050</td><td>US$ 0,046</td><td>cerca de −8%</td><td>cerca de US$ 1,47 bilhão</td></tr>
<tr><td>USD1 (stablecoin)</td><td>US$ 0,998</td><td>US$ 0,998</td><td>manteve a paridade de US$ 1</td><td>cerca de US$ 3,44 bilhões</td></tr>
<tr><td>Bitcoin, para comparação</td><td>US$ 78.294</td><td>US$ 75.820</td><td>cerca de −3%</td><td>cerca de US$ 1,52 trilhão</td></tr>
</tbody></table></div>
<p class="note">Preços em dólares americanos pela API da CoinGecko: a coluna de 1 de novembro é o fechamento daquele dia; a coluna de 8 de novembro, o preço da tarde de 8 de novembro (UTC). A maior queda diária do TRUMP na semana foi em 4 de novembro, o dia seguinte à eleição, de cerca de US$ 1,59 para US$ 1,27. Nada nesta página é recomendação de investimento.</p>
""",
    columns=["App", "Preço (EUA)", "Lista WLFI, TRUMP, USD1", "Alertas de preço", "Widget", "Conta necessária", "Versão (data)", "Nota (EUA)"],
    table_note="Preços, versões e notas são os das páginas dos EUA na App Store em 8 de novembro de 2026; os cinco apps são gratuitos para baixar. Alertas, widgets e conta conforme descritos em cada ficha. Os tokens foram conferidos no site de cada empresa ou nos dados de 8 de novembro.",
    apps=[
        dict(
            row=["Grátis; Premium US$ 9,90 por mês ou US$ 99,90 por ano", "Sim, os três", "Sim: alertas de preço e de grandes variações", "Sim, na tela inicial", "A ficha não diz que é preciso", "3.60.0 (27 out. 2026)", "4.8"],
            best_for="acompanhar WLFI, TRUMP e USD1 com os mesmos dados da tabela de preços acima, com alertas.",
            facts=[
                "Os dados da CoinGecko incluem Official Trump, World Liberty Financial e USD1, então dá para colocar os três numa lista de acompanhamento.",
                "Pela ficha, há alertas de preço personalizados e alertas de grandes movimentos para moedas da lista, carteira com lucro e prejuízo e widget na tela inicial.",
                "Tem categorias como memecoins, onde fica o TRUMP.",
            ],
            limits="só em inglês, e a ficha não diz quantos alertas são gratuitos.",
        ),
        dict(
            row=["Grátis; Essential US$ 11,99 por mês ou US$ 109,99 por ano; Plus US$ 23,99 por mês ou US$ 229,99 por ano; Max US$ 119,99 por mês", "Sim, os três", "Sim: alertas de preço personalizáveis", "A ficha não menciona", "Necessária para a carteira; modo anônimo sem entrar", "5.24.0 (1 nov. 2026)", "4.8"],
            best_for="o rastreador com mais avaliações: alertas para qualquer um dos três tokens.",
            facts=[
                "A CoinMarketCap tem páginas de Official Trump, World Liberty Financial e World Liberty Financial USD (USD1).",
                "Alertas de preço personalizáveis e listas de acompanhamento; segundo a ficha, acompanha mais de 45.000 mercados ativos.",
                "Cerca de 173.000 avaliações nos EUA, as mais numerosas aqui, e 21 idiomas.",
            ],
            limits="a ficha diz para criar conta para montar uma carteira (o modo anônimo mantém os dados no celular), não menciona widget, e os planos são os mais caros desta lista.",
        ),
        dict(
            row=["Grátis; Pro US$ 4,99 por mês ou US$ 39,99 por ano; Premium US$ 15,99 a US$ 19,99 por mês ou US$ 65,99 a US$ 164,99 por ano", "Sim, os três", "Sim: alertas de preço, de volume e de valor de mercado, além de Auto Alerts", "Sim: tela inicial, tela de bloqueio e Apple Watch", "A ficha não diz que é preciso", "5.31.1 (30 out. 2026)", "4.8"],
            best_for="quem tem WLFI ou TRUMP em uma carteira ou corretora e quer que sejam acompanhados automaticamente, com alertas e widgets na tela de bloqueio.",
            facts=[
                "O coinstats.app tem páginas de Official Trump, World Liberty Financial e USD1.",
                "Conecta mais de 300 carteiras e corretoras e mostra lucro e prejuízo em tempo real; segundo a ficha, preços de mais de 20.000 moedas.",
                "Alertas de preço, volume ou valor de mercado em qualquer moeda, e widgets na tela inicial, na tela de bloqueio e no Apple Watch.",
            ],
            limits="muitos planos pagos que se sobrepõem, e o conjunto completo de análises exige o Premium.",
        ),
        dict(
            row=["Grátis, sem compras no app", "Sim, pela busca (dados da CoinGecko)", "Não", "Sim: preços e carteira (tela inicial)", "Não (opcional, só para sincronizar)", "2.0.8 (24 out. 2026)", "4.7"],
            best_for="uma lista de acompanhamento gratuita de WLFI, TRUMP e USD1 na tela inicial, sem conta e sem pagar nada.",
            facts=[
                "Preços ao vivo das 250 maiores moedas e busca por qualquer moeda listada na CoinGecko, então WLFI, TRUMP e USD1 podem ir para Favoritos, segundo a ficha.",
                "Carteira com lucro e prejuízo em cada moeda, e widgets na tela inicial para preços e para a carteira.",
                "Sem compras no app; só em inglês, iOS 18 ou mais recente.",
            ],
            limits="a versão atual não tem alertas de preço, widget de tela de bloqueio nem app para Apple Watch, e não sincroniza com carteiras ou corretoras. Para alertas, veja a " + _PT_ALERTS + ".",
        ),
        dict(
            row=["Grátis até 10 ativos; PRO de US$ 6,99 a US$ 13,99 por mês ou US$ 58,99 a US$ 99,90 por ano; PRO+ US$ 13,99 por mês ou US$ 107,99 por ano", "Não verificado (ficha: mais de 10.000 moedas)", "Sim: preços-alvo e grandes movimentos", "A ficha não menciona", "A ficha não diz", "2026.3.2 (5 nov. 2026)", "4.7"],
            best_for="acompanhar cripto e ações numa mesma carteira, com alertas.",
            facts=[
                "Acompanha cripto, ações, ETFs, commodities e forex juntos; mais de 10.000 moedas, segundo a ficha.",
                "Alertas inteligentes para preços-alvo e movimentos relevantes, e notificações personalizadas para marcos da carteira.",
                "O plano gratuito acompanha até 10 ativos; PRO até 40; PRO+ sem limite.",
            ],
            limits="não conseguimos confirmar no site da Delta que ela lista WLFI, TRUMP e USD1; o plano gratuito para em 10 ativos; e o rótulo de privacidade inclui dados usados para rastreamento.",
        ),
    ],
    who=["<strong>Alertas quando TRUMP ou WLFI se movem forte:</strong> CoinGecko (alertas de grandes movimentos) ou CoinStats (Auto Alerts).",
         "<strong>O rastreador mais usado:</strong> CoinMarketCap.",
         "<strong>Tokens numa carteira ou corretora:</strong> CoinStats.",
         "<strong>Só olhar os três preços, sem conta:</strong> Crypton.",
         "<strong>Cripto e ações no mesmo lugar:</strong> Delta."],
    cases=["Ver se a USD1 continua em US$ 1: qualquer app da lista que a tenha; CoinGecko e CoinMarketCap mostram também o valor de mercado dela.",
           "Receber aviso se o TRUMP cair mais 10%: CoinGecko, CoinMarketCap, CoinStats ou Delta (com alertas); não a Crypton.",
           "Manter WLFI e TRUMP na tela inicial: CoinGecko, CoinStats ou Crypton. Mais nos rankings de " + _PT_WIDGETS + " e " + _PT_ALERTS + ".",
           "Acompanhar saldos sem conectar carteira: veja " + _PT_NOCONNECT + "."],
    method=["Em 8 de novembro de 2026 lemos a página dos EUA de cada app na App Store e os dados de consulta da Apple (preço, compras no app, versão, nota e texto da ficha). Para saber se cada app lista WLFI, TRUMP e USD1, conferimos nos dados da CoinGecko, nas páginas de moedas da CoinMarketCap e da CoinStats e na ficha da Crypton (que faz a busca pela CoinGecko); o site da Delta não permitiu a conferência. Não instalamos os apps nem testamos a velocidade dos alertas.",
            "O contexto de notícias é atribuído aos veículos linkados acima; esta página não toma posição sobre as investigações. Nenhum desses apps é uma corretora, e nada aqui é recomendação de investimento."],
    faq=[
        ("Qual app mostra o preço do WLFI no iPhone?", "CoinGecko, CoinMarketCap e CoinStats listam a World Liberty Financial (WLFI); a Crypton encontra pela busca, porque usa dados da CoinGecko."),
        ("Dá para receber alerta do preço da memecoin TRUMP?", "Sim, com CoinGecko, CoinMarketCap, CoinStats ou Delta, que têm alertas de preço. A Crypton não tem alertas de preço."),
        ("A USD1 ainda vale um dólar?", "Segundo a CoinGecko, de 1 a 8 de novembro de 2026 ela negociou por cerca de US$ 0,998, com valor de mercado de cerca de US$ 3,44 bilhões."),
        ("Por que TRUMP e WLFI caíram em novembro de 2026?", "Segundo a CoinGecko, de 1 a 8 de novembro o TRUMP caiu cerca de 32% e o WLFI cerca de 8%, na semana em que os democratas, que ganharam a Câmara, disseram que planejam investigar os negócios cripto da família Trump, segundo o crypto.news e a CNBC. Esta página não atribui a queda de preço a nenhuma causa e não é recomendação de investimento."),
        ("Preciso de conta para acompanhar esses tokens?", "Na Crypton, não (a conta só sincroniza). A CoinMarketCap pede conta para a carteira, mas tem modo anônimo; as demais fichas não dizem que é preciso conta."),
    ],
    sources=["crypto.news, 4 nov. 2026: democratas preparam investigação sobre a World Liberty Financial após vitória na Câmara",
             "CNBC, 5 nov. 2026: vitória democrata coloca cripto na defensiva em Washington",
             "Financial Times, 8 nov. 2026, primeira página: “Crypto industry braces for reckoning over Trump ties” (só o título)",
             "API da CoinGecko: preços de TRUMP, WLFI, USD1 e BTC",
             "CoinMarketCap: Official Trump",
             "CoinMarketCap: World Liberty Financial",
             "CoinMarketCap: USD1",
             "CoinStats: Official Trump",
             "CoinStats: World Liberty Financial",
             "CoinStats: USD1",
             "CoinGecko: Crypto Tracker (App Store)",
             "CoinMarketCap: Crypto Tracker (App Store)",
             "CoinStats: Crypto Portfolio (App Store)",
             "Crypto Tracker: Crypton (App Store)",
             "Delta by eToro (App Store)"],
)

PAGES.append(_translated("pt-BR", "pt-br", "ptbr", PT))


_FR_WIDGETS = "<a href=\"/best-crypto-price-widget-apps-iphone/\">applications de widgets crypto</a>"
_FR_ALERTS = "<a href=\"/best-crypto-price-alert-apps-iphone/\">applications d’alerte de prix crypto</a>"
_FR_NOCONNECT = "<a href=\"/crypto-portfolio-tracker-without-connecting-wallet-iphone/\">suivis qui ne demandent ni portefeuille ni plateforme</a>"

FR = dict(
    kicker="5 apps · Classement · Actualités",
    title="Meilleures apps iPhone pour suivre les cours de WLFI, TRUMP et USD1 (nov. 2026)",
    h1="Meilleures apps iPhone pour suivre les cours de WLFI, TRUMP et USD1 (novembre 2026)",
    description="Cinq apps iPhone qui suivent World Liberty Financial (WLFI), la memecoin TRUMP et USD1, comparées par prix, alertes, widgets et compte au 8 novembre 2026.",
    llms="Cinq apps iPhone pour suivre WLFI, TRUMP et USD1 après les élections de mi-mandat américaines de novembre 2026 : CoinGecko, CoinMarketCap, CoinStats, Crypton, Delta. Lesquelles listent les trois jetons, alertes, widgets, compte, prix américain et note. Avec les cours CoinGecko du 1er au 8 novembre 2026 et un contexte d’actualité daté. Ce n’est pas un conseil financier.",
    answer=[
        "Pour suivre WLFI, TRUMP et USD1 avec des alertes de prix, <strong>CoinGecko</strong>, <strong>CoinMarketCap</strong> et <strong>CoinStats</strong> listent les trois jetons ; CoinStats connecte aussi votre portefeuille et propose des widgets sur l’écran verrouillé.",
        "Pour un widget gratuit sur l’écran d’accueil, sans compte ni achat, <strong>Crypton</strong> trouve les trois jetons par recherche mais n’a pas d’alertes ; <strong>Delta</strong> convient à un portefeuille qui mêle cryptos et actions.",
    ],
    context_html=f"""<h2 id="context">Ce qui s’est passé (8 novembre 2026)</h2>
<p>Après les élections de mi-mandat du 3 novembre, les démocrates ont remporté la majorité à la Chambre des représentants selon les projections de NBC News et de MS NOW, et prévoient d’enquêter sur les activités crypto de la famille Trump, notamment World Liberty Financial (le jeton WLFI et le stablecoin USD1) et la memecoin TRUMP. <a href="{CNEWS}">Crypto.news rapporte</a> que ces enquêtes pourraient commencer dès février 2027. La Maison-Blanche a rejeté ces projets ; avant le vote, une porte-parole avait qualifié le programme des démocrates de « chasse aux sorcières », selon le même article. <a href="{CNBC}">CNBC écrit</a> que le résultat place l’industrie crypto sur la défensive à Washington, et le 8 novembre le Financial Times a publié l’histoire en une sous le titre « Crypto industry braces for reckoning over Trump ties » (titre en anglais).</p>
<div class="scroll"><table style="min-width:0">
<thead><tr><th>Jeton</th><th>1er nov. 2026</th><th>8 nov. 2026</th><th>Variation</th><th>Capitalisation, 8 nov.</th></tr></thead>
<tbody>
<tr><td>TRUMP (Official Trump)</td><td>US$ 1,71</td><td>US$ 1,16</td><td>environ −32 %</td><td>environ 328 millions US$</td></tr>
<tr><td>WLFI (World Liberty Financial)</td><td>US$ 0,050</td><td>US$ 0,046</td><td>environ −8 %</td><td>environ 1,47 milliard US$</td></tr>
<tr><td>USD1 (stablecoin)</td><td>US$ 0,998</td><td>US$ 0,998</td><td>a gardé son ancrage à 1 $</td><td>environ 3,44 milliards US$</td></tr>
<tr><td>Bitcoin, pour comparaison</td><td>US$ 78 294</td><td>US$ 75 820</td><td>environ −3 %</td><td>environ 1,52 billion US$</td></tr>
</tbody></table></div>
<p class="note">Prix en dollars américains selon l’API CoinGecko : la colonne du 1er novembre correspond à la clôture de ce jour, celle du 8 novembre au prix de l’après-midi du 8 novembre (UTC). La plus forte baisse journalière de TRUMP de la semaine a eu lieu le 4 novembre, le lendemain de l’élection, d’environ 1,59 $ à 1,27 $. Rien sur cette page ne constitue un conseil financier.</p>
""",
    columns=["App", "Prix (US)", "Liste WLFI, TRUMP, USD1", "Alertes de prix", "Widget", "Compte requis", "Version (date)", "Note (US)"],
    table_note="Prix, versions et notes sont ceux des pages américaines de l’App Store au 8 novembre 2026 ; les cinq apps se téléchargent gratuitement. Alertes, widgets et compte sont décrits comme sur chaque fiche. La présence des jetons a été vérifiée sur le site de chaque société ou sur les données du 8 novembre.",
    apps=[
        dict(
            row=["Gratuit ; Premium US$ 9,90 par mois ou US$ 99,90 par an", "Oui, les trois", "Oui : alertes de prix et de fortes variations", "Oui, sur l’écran d’accueil", "La fiche ne l’indique pas comme obligatoire", "3.60.0 (27 oct. 2026)", "4.8"],
            best_for="suivre WLFI, TRUMP et USD1 avec les mêmes données que le tableau de prix ci-dessus, avec alertes.",
            facts=[
                "Les données de CoinGecko incluent Official Trump, World Liberty Financial et USD1 : vous pouvez les ajouter tous les trois à une liste de suivi.",
                "Selon la fiche : alertes de prix personnalisées et alertes de fortes variations pour les jetons suivis, portefeuille avec gains et pertes, widget sur l’écran d’accueil.",
                "Il existe des catégories comme les memecoins, où se trouve TRUMP.",
            ],
            limits="en anglais uniquement ; la fiche n’indique pas combien d’alertes sont gratuites.",
        ),
        dict(
            row=["Gratuit ; Essential US$ 11,99 par mois ou US$ 109,99 par an ; Plus US$ 23,99 par mois ou US$ 229,99 par an ; Max US$ 119,99 par mois", "Oui, les trois", "Oui : alertes de prix personnalisables", "Non mentionné dans la fiche", "Requis pour le portefeuille ; mode incognito sans connexion", "5.24.0 (1er nov. 2026)", "4.8"],
            best_for="le suivi le plus noté : alertes sur chacun des trois jetons.",
            facts=[
                "CoinMarketCap a des pages pour Official Trump, World Liberty Financial et World Liberty Financial USD (USD1).",
                "Alertes de prix personnalisables et listes de suivi ; selon la fiche, plus de 45 000 marchés actifs.",
                "Environ 173 000 notes aux États-Unis, le plus grand nombre ici, et 21 langues.",
            ],
            limits="la fiche indique qu’il faut créer un compte pour établir un portefeuille (le mode incognito garde les données sur le téléphone), ne mentionne pas de widget, et ses formules sont les plus chères de cette liste.",
        ),
        dict(
            row=["Gratuit ; Pro US$ 4,99 par mois ou US$ 39,99 par an ; Premium US$ 15,99 à US$ 19,99 par mois ou US$ 65,99 à US$ 164,99 par an", "Oui, les trois", "Oui : alertes de prix, de volume et de capitalisation, plus Auto Alerts", "Oui : écran d’accueil, écran verrouillé et Apple Watch", "La fiche ne l’indique pas comme obligatoire", "5.31.1 (30 oct. 2026)", "4.8"],
            best_for="ceux qui détiennent WLFI ou TRUMP dans un portefeuille ou sur une plateforme et veulent un suivi automatique, avec alertes et widgets sur l’écran verrouillé.",
            facts=[
                "coinstats.app a des pages pour Official Trump, World Liberty Financial et USD1.",
                "Connecte plus de 300 portefeuilles et plateformes et affiche gains et pertes en temps réel ; selon la fiche, prix de plus de 20 000 monnaies.",
                "Alertes de prix, de volume ou de capitalisation sur n’importe quelle monnaie, et widgets sur l’écran d’accueil, l’écran verrouillé et l’Apple Watch.",
            ],
            limits="beaucoup de formules payantes qui se chevauchent ; l’ensemble complet des analyses exige Premium.",
        ),
        dict(
            row=["Gratuit, sans achats intégrés", "Oui, par recherche (données CoinGecko)", "Non", "Oui : cours et portefeuille (écran d’accueil)", "Non (facultatif, seulement pour la synchronisation)", "2.0.8 (24 oct. 2026)", "4.7"],
            best_for="une liste de suivi gratuite de WLFI, TRUMP et USD1 sur l’écran d’accueil, sans compte ni dépense.",
            facts=[
                "Cours en direct des 250 premières monnaies et recherche de toute monnaie listée sur CoinGecko : WLFI, TRUMP et USD1 peuvent donc être ajoutés aux favoris, selon la fiche.",
                "Portefeuille avec gains et pertes pour chaque monnaie, et widgets sur l’écran d’accueil pour les cours et pour le portefeuille.",
                "Aucun achat intégré ; anglais uniquement, iOS 18 ou plus récent.",
            ],
            limits="la version actuelle n’a ni alertes de prix, ni widget d’écran verrouillé, ni application Apple Watch, et ne synchronise pas avec les portefeuilles ni les plateformes. Pour les alertes, voir les " + _FR_ALERTS + ".",
        ),
        dict(
            row=["Gratuit jusqu’à 10 actifs ; PRO de US$ 6,99 à US$ 13,99 par mois ou US$ 58,99 à US$ 99,90 par an ; PRO+ US$ 13,99 par mois ou US$ 107,99 par an", "Non vérifié (fiche : plus de 10 000 monnaies)", "Oui : prix cibles et fortes variations", "Non mentionné dans la fiche", "Non précisé dans la fiche", "2026.3.2 (5 nov. 2026)", "4.7"],
            best_for="suivre cryptos et actions dans un même portefeuille, avec alertes.",
            facts=[
                "Suit ensemble cryptos, actions, ETF, matières premières et devises ; plus de 10 000 monnaies, selon la fiche.",
                "Alertes intelligentes sur prix cibles et mouvements importants, et notifications personnalisées pour les étapes du portefeuille.",
                "La formule gratuite suit jusqu’à 10 actifs ; PRO jusqu’à 40 ; PRO+ sans limite.",
            ],
            limits="nous n’avons pas pu confirmer sur le site de Delta qu’il liste WLFI, TRUMP et USD1 ; la formule gratuite s’arrête à 10 actifs ; et l’étiquette de confidentialité inclut des données utilisées pour le suivi.",
        ),
    ],
    who=["<strong>Alertes quand TRUMP ou WLFI bougent fortement :</strong> CoinGecko (alertes de fortes variations) ou CoinStats (Auto Alerts).",
         "<strong>Le suivi le plus utilisé :</strong> CoinMarketCap.",
         "<strong>Jetons dans un portefeuille ou sur une plateforme :</strong> CoinStats.",
         "<strong>Voir les trois cours d’un coup d’œil, sans compte :</strong> Crypton.",
         "<strong>Cryptos et actions au même endroit :</strong> Delta."],
    cases=["Vérifier si USD1 reste à 1 $ : toute app de la liste qui le suit ; CoinGecko et CoinMarketCap affichent aussi sa capitalisation.",
           "Être averti si TRUMP baisse encore de 10 % : CoinGecko, CoinMarketCap, CoinStats ou Delta (avec alertes) ; pas Crypton.",
           "Garder WLFI et TRUMP sur l’écran d’accueil : CoinGecko, CoinStats ou Crypton. Plus de détails dans les classements " + _FR_WIDGETS + " et " + _FR_ALERTS + ".",
           "Suivre ses avoirs sans connecter de portefeuille : voir " + _FR_NOCONNECT + "."],
    method=["Le 8 novembre 2026, nous avons lu la page américaine de chaque app sur l’App Store et les données de recherche d’Apple (prix, achats intégrés, version, note et texte de la fiche). Pour savoir si chaque app liste WLFI, TRUMP et USD1, nous avons vérifié dans les données de CoinGecko, sur les pages de monnaies de CoinMarketCap et de CoinStats, et dans la fiche de Crypton (qui fait sa recherche via CoinGecko) ; le site de Delta n’a pas permis de vérifier. Nous n’avons pas installé les apps ni testé la rapidité des alertes.",
            "Le contexte d’actualité est attribué aux médias liés ci-dessus ; cette page ne prend pas position sur les enquêtes. Aucune de ces apps n’est une plateforme d’échange, et rien ici ne constitue un conseil financier."],
    faq=[
        ("Quelle app affiche le cours de WLFI sur iPhone ?", "CoinGecko, CoinMarketCap et CoinStats listent World Liberty Financial (WLFI) ; Crypton le trouve par recherche, car il utilise les données de CoinGecko."),
        ("Peut-on recevoir une alerte sur le cours de la memecoin TRUMP ?", "Oui, avec CoinGecko, CoinMarketCap, CoinStats ou Delta, qui proposent des alertes de prix. Crypton n’a pas d’alertes de prix."),
        ("L’USD1 vaut-il toujours un dollar ?", "Selon CoinGecko, du 1er au 8 novembre 2026 il s’est échangé autour de 0,998 US$, avec une capitalisation d’environ 3,44 milliards US$."),
        ("Pourquoi TRUMP et WLFI ont-ils baissé en novembre 2026 ?", "Selon CoinGecko, du 1er au 8 novembre TRUMP a perdu environ 32 % et WLFI environ 8 %, la semaine où les démocrates, qui ont remporté la Chambre, ont annoncé vouloir enquêter sur les activités crypto de la famille Trump, selon crypto.news et CNBC. Cette page n’attribue la baisse des cours à aucune cause et n’est pas un conseil financier."),
        ("Faut-il un compte pour suivre ces jetons ?", "Pas dans Crypton (le compte ne sert qu’à la synchronisation). CoinMarketCap en demande un pour le portefeuille, mais propose un mode incognito ; les autres fiches n’indiquent pas qu’un compte est nécessaire."),
    ],
    sources=["crypto.news, 4 nov. 2026 : les démocrates préparent une enquête sur World Liberty Financial après leur victoire à la Chambre",
             "CNBC, 5 nov. 2026 : la victoire démocrate met la crypto sur la défensive à Washington",
             "Financial Times, 8 nov. 2026, une : « Crypto industry braces for reckoning over Trump ties » (titre seulement)",
             "API CoinGecko : cours de TRUMP, WLFI, USD1 et BTC",
             "CoinMarketCap : Official Trump",
             "CoinMarketCap : World Liberty Financial",
             "CoinMarketCap : USD1",
             "CoinStats : Official Trump",
             "CoinStats : World Liberty Financial",
             "CoinStats : USD1",
             "CoinGecko: Crypto Tracker (App Store)",
             "CoinMarketCap: Crypto Tracker (App Store)",
             "CoinStats: Crypto Portfolio (App Store)",
             "Crypto Tracker: Crypton (App Store)",
             "Delta by eToro (App Store)"],
)

PAGES.append(_translated("fr", "fr", "fr", FR))


_AR_WIDGETS = '<a href="/best-crypto-price-widget-apps-iphone/">تطبيقات أدوات أسعار العملات المشفرة</a>'
_AR_ALERTS = '<a href="/best-crypto-price-alert-apps-iphone/">تطبيقات تنبيهات أسعار العملات المشفرة</a>'
_AR_NOCONNECT = '<a href="/crypto-portfolio-tracker-without-connecting-wallet-iphone/">متتبّعات لا تطلب محفظة أو منصة</a>'

AR = dict(
    kicker="5 تطبيقات · تصنيف · أخبار",
    title="أفضل تطبيقات iPhone لتتبع أسعار WLFI وTRUMP وUSD1 (نوفمبر 2026)",
    h1="أفضل تطبيقات iPhone لتتبع أسعار WLFI وTRUMP وUSD1 (نوفمبر 2026)",
    description="خمسة تطبيقات iPhone تتابع World Liberty Financial (WLFI) وعملة TRUMP الميمية وUSD1، مقارنة حسب السعر والتنبيهات والأدوات والحساب في 8 نوفمبر 2026.",
    llms="خمسة تطبيقات iPhone لمتابعة WLFI وTRUMP وUSD1 بعد الانتخابات النصفية الأمريكية في نوفمبر 2026: CoinGecko وCoinMarketCap وCoinStats وCrypton وDelta. أيها يدرج الرموز الثلاثة، والتنبيهات، والأدوات، والحساب، والسعر في الولايات المتحدة، والتقييم. مع أسعار CoinGecko من 1 إلى 8 نوفمبر 2026 وسياق أخبار مؤرخ. ليست توصية مالية.",
    answer=[
        "لمتابعة WLFI وTRUMP وUSD1 مع تنبيهات الأسعار، تُدرج <strong>CoinGecko</strong> و<strong>CoinMarketCap</strong> و<strong>CoinStats</strong> الرموز الثلاثة جميعها؛ وCoinStats يربط محفظتك أيضًا ويوفر أدوات على شاشة القفل.",
        "لأداة مجانية على الشاشة الرئيسية دون حساب أو شراء، تجد <strong>Crypton</strong> الرموز الثلاثة بالبحث لكنها بلا تنبيهات؛ و<strong>Delta</strong> مناسب لمحفظة تجمع العملات المشفرة والأسهم.",
    ],
    context_html=f"""<h2 id="context">ما الذي حدث (8 نوفمبر 2026)</h2>
<p>بعد الانتخابات النصفية في 3 نوفمبر، فاز الديمقراطيون بأغلبية في مجلس النواب وفق توقعات NBC News وMS NOW، ويخططون للتحقيق في الأنشطة المشفرة لعائلة ترامب، بما فيها World Liberty Financial (رمز WLFI والعملة المستقرة USD1) وعملة TRUMP الميمية. <a href="{CNEWS}">ذكر موقع crypto.news</a> أن التحقيقات قد تبدأ في فبراير 2027. رفض البيت الأبيض هذه الخطط؛ وقبل التصويت وصفت متحدثة جدول أعمال الديمقراطيين بأنه «مطاردة ساحرات» وفق التقرير نفسه. <a href="{CNBC}">وكتبت CNBC</a> أن النتيجة تضع صناعة العملات المشفرة في موقف دفاعي في واشنطن، ونشرت صحيفة Financial Times القصة في صفحتها الأولى في 8 نوفمبر تحت عنوان «Crypto industry braces for reckoning over Trump ties» (بالإنجليزية).</p>
<div class="scroll"><table style="min-width:0">
<thead><tr><th>الرمز</th><th>1 نوفمبر 2026</th><th>8 نوفمبر 2026</th><th>التغير</th><th>القيمة السوقية، 8 نوفمبر</th></tr></thead>
<tbody>
<tr><td>TRUMP (Official Trump)</td><td>$1.71</td><td>$1.16</td><td>نحو −32%</td><td>نحو 328 مليون $</td></tr>
<tr><td>WLFI (World Liberty Financial)</td><td>$0.050</td><td>$0.046</td><td>نحو −8%</td><td>نحو 1.47 مليار $</td></tr>
<tr><td>USD1 (عملة مستقرة)</td><td>$0.998</td><td>$0.998</td><td>حافظت على ربطها بالدولار</td><td>نحو 3.44 مليار $</td></tr>
<tr><td>Bitcoin للمقارنة</td><td>$78,294</td><td>$75,820</td><td>نحو −3%</td><td>نحو 1.52 تريليون $</td></tr>
</tbody></table></div>
<p class="note">الأسعار بالدولار الأمريكي من واجهة CoinGecko: عمود 1 نوفمبر هو سعر إغلاق ذلك اليوم، وعمود 8 نوفمبر هو السعر بعد ظهر 8 نوفمبر (UTC). وكان أكبر انخفاض يومي لـ TRUMP في الأسبوع يوم 4 نوفمبر، أي اليوم التالي للانتخابات، من نحو 1.59 دولار إلى 1.27 دولار. لا شيء في هذه الصفحة نصيحة مالية.</p>
""",
    columns=["التطبيق", "السعر (الولايات المتحدة)", "يدرج WLFI وTRUMP وUSD1", "تنبيهات الأسعار", "أداة", "الحساب مطلوب", "الإصدار (التاريخ)", "التقييم (الولايات المتحدة)"],
    table_note="الأسعار والإصدارات والتقييمات كما هي في صفحات App Store الأمريكية في 8 نوفمبر 2026؛ والتطبيقات الخمسة مجانية للتنزيل. التنبيهات والأدوات والحساب كما تصفها كل صفحة. وقد جرى التحقق من الرموز على موقع كل شركة أو من بيانات 8 نوفمبر.",
    apps=[
        dict(
            row=["مجاني؛ Premium بسعر 9.90$ شهريًا أو 99.90$ سنويًا", "نعم، الثلاثة", "نعم: تنبيهات السعر وتنبيهات التحركات الكبيرة", "نعم، على الشاشة الرئيسية", "لا تذكر الصفحة أنه مطلوب", "3.60.0 (27 أكتوبر 2026)", "4.8"],
            best_for="متابعة WLFI وTRUMP وUSD1 بالبيانات نفسها الموجودة في جدول الأسعار أعلاه، مع التنبيهات.",
            facts=[
                "تضم بيانات CoinGecko الرموز Official Trump وWorld Liberty Financial وUSD1، لذا يمكنك إضافتها جميعًا إلى قائمة المراقبة.",
                "بحسب الصفحة: تنبيهات سعر مخصصة وتنبيهات للتحركات الكبيرة للعملات في قائمة المراقبة، ومحفظة بالأرباح والخسائر، وأداة على الشاشة الرئيسية.",
                "تصنيف حسب فئات مثل العملات الميمية، وفيها TRUMP.",
            ],
            limits="باللغة الإنجليزية فقط، ولا تذكر الصفحة عدد التنبيهات المجانية.",
        ),
        dict(
            row=["مجاني؛ Essential بسعر 11.99$ شهريًا أو 109.99$ سنويًا؛ Plus بسعر 23.99$ شهريًا أو 229.99$ سنويًا؛ Max بسعر 119.99$ شهريًا", "نعم، الثلاثة", "نعم: تنبيهات سعر قابلة للتخصيص", "لا تذكر الصفحة ذلك", "مطلوب للمحفظة؛ وضع التصفح الخاص بلا تسجيل دخول", "5.24.0 (1 نوفمبر 2026)", "4.8"],
            best_for="المتتبّع الأكثر تقييمًا: تنبيهات لأي من الرموز الثلاثة.",
            facts=[
                "لدى CoinMarketCap صفحات لـ Official Trump وWorld Liberty Financial وWorld Liberty Financial USD (USD1).",
                "تنبيهات سعر قابلة للتخصيص وقوائم مراقبة؛ بحسب الصفحة تتابع أكثر من 45,000 سوق نشط.",
                "نحو 173,000 تقييم في الولايات المتحدة، وهو الأعلى في هذه القائمة، و21 لغة.",
            ],
            limits="تطلب الصفحة إنشاء حساب لإعداد المحفظة (وضع التصفح الخاص يُبقي البيانات على الهاتف)، ولا تذكر أداة، وخططها هي الأغلى في هذه القائمة.",
        ),
        dict(
            row=["مجاني؛ Pro بسعر 4.99$ شهريًا أو 39.99$ سنويًا؛ Premium بسعر 15.99$ إلى 19.99$ شهريًا أو 65.99$ إلى 164.99$ سنويًا", "نعم، الثلاثة", "نعم: تنبيهات السعر والحجم والقيمة السوقية، إضافة إلى Auto Alerts", "نعم: الشاشة الرئيسية وشاشة القفل وApple Watch", "لا تذكر الصفحة أنه مطلوب", "5.31.1 (30 أكتوبر 2026)", "4.8"],
            best_for="من يحتفظ بـ WLFI أو TRUMP في محفظة أو منصة تداول ويريد متابعتها تلقائيًا، مع تنبيهات وأدوات على شاشة القفل.",
            facts=[
                "لدى coinstats.app صفحات لـ Official Trump وWorld Liberty Financial وUSD1.",
                "يتصل بأكثر من 300 محفظة ومنصة ويعرض الأرباح والخسائر فوريًا؛ وبحسب الصفحة يغطي أسعار أكثر من 20,000 عملة.",
                "تنبيهات سعر أو حجم أو قيمة سوقية لأي عملة، وأدوات على الشاشة الرئيسية وشاشة القفل وApple Watch.",
            ],
            limits="خطط مدفوعة كثيرة تتداخل مع بعضها، ولا تكتمل التحليلات إلا بخطة Premium.",
        ),
        dict(
            row=["مجاني، بلا مشتريات داخل التطبيق", "نعم، بالبحث (بيانات CoinGecko)", "لا", "نعم: الأسعار والمحفظة (الشاشة الرئيسية)", "لا (اختياري، فقط للمزامنة)", "2.0.8 (24 أكتوبر 2026)", "4.7"],
            best_for="قائمة مراقبة مجانية لـ WLFI وTRUMP وUSD1 على الشاشة الرئيسية، دون حساب ودون دفع أي شيء.",
            facts=[
                "أسعار مباشرة لأكبر 250 عملة، والبحث عن أي عملة مدرجة في CoinGecko، لذا يمكن إضافة WLFI وTRUMP وUSD1 إلى المفضلة، بحسب الصفحة.",
                "محفظة بالأرباح والخسائر لكل عملة، وأدوات على الشاشة الرئيسية للأسعار وللمحفظة.",
                "بلا مشتريات داخل التطبيق؛ باللغة الإنجليزية فقط، ويتطلب iOS 18 أو أحدث.",
            ],
            limits="لا توجد تنبيهات أسعار في النسخة الحالية، ولا أداة لشاشة القفل ولا تطبيق لـ Apple Watch، ولا مزامنة مع المحافظ أو المنصات. للتنبيهات راجع " + _AR_ALERTS + ".",
        ),
        dict(
            row=["مجاني حتى 10 أصول؛ PRO بسعر 6.99$ إلى 13.99$ شهريًا أو 58.99$ إلى 99.90$ سنويًا؛ PRO+ بسعر 13.99$ شهريًا أو 107.99$ سنويًا", "غير مُتحقَّق منه (الصفحة: أكثر من 10,000 عملة)", "نعم: أسعار مستهدفة وتحركات كبيرة", "لا تذكر الصفحة ذلك", "لا تذكر الصفحة ذلك", "2026.3.2 (5 نوفمبر 2026)", "4.7"],
            best_for="متابعة العملات المشفرة والأسهم في محفظة واحدة مع التنبيهات.",
            facts=[
                "تتابع معًا العملات المشفرة والأسهم والصناديق المتداولة والسلع والعملات الأجنبية؛ أكثر من 10,000 عملة بحسب الصفحة.",
                "تنبيهات ذكية للأسعار المستهدفة والتحركات الكبيرة، وإشعارات مخصصة لمعالم المحفظة.",
                "الخطة المجانية تتابع حتى 10 أصول؛ وPRO حتى 40؛ وPRO+ بلا حد.",
            ],
            limits="لم نتمكن من التأكد من موقع Delta أنه يدرج WLFI وTRUMP وUSD1؛ والخطة المجانية تتوقف عند 10 أصول؛ وتضم ملصقة الخصوصية بيانات مستخدمة للتتبع.",
        ),
    ],
    who=["<strong>تنبيهات عند تحرك TRUMP أو WLFI بقوة:</strong> CoinGecko (تنبيهات التحركات الكبيرة) أو CoinStats (Auto Alerts).",
         "<strong>المتتبّع الأكثر استخدامًا:</strong> CoinMarketCap.",
         "<strong>رموز في محفظة أو منصة:</strong> CoinStats.",
         "<strong>نظرة سريعة على الأسعار الثلاثة دون حساب:</strong> Crypton.",
         "<strong>العملات المشفرة والأسهم في مكان واحد:</strong> Delta."],
    cases=["معرفة هل تبقى USD1 عند دولار واحد: أي تطبيق في القائمة يتابعها؛ وCoinGecko وCoinMarketCap تعرضان قيمتها السوقية أيضًا.",
           "استلام إشعار إذا انخفض TRUMP 10% أخرى: CoinGecko أو CoinMarketCap أو CoinStats أو Delta (مع التنبيهات)؛ لا Crypton.",
           "إبقاء WLFI وTRUMP على الشاشة الرئيسية: CoinGecko أو CoinStats أو Crypton. المزيد في تصنيفات " + _AR_WIDGETS + " و" + _AR_ALERTS + ".",
           "متابعة الأرصدة دون ربط محفظة: راجع " + _AR_NOCONNECT + "."],
    method=["في 8 نوفمبر 2026 قرأنا صفحة كل تطبيق الأمريكية في App Store وبيانات البحث من Apple (السعر والمشتريات داخل التطبيق والإصدار والتقييم ونص الوصف). وللتحقق مما إذا كان كل تطبيق يدرج WLFI وTRUMP وUSD1، راجعنا بيانات CoinGecko وصفحات العملات في CoinMarketCap وCoinStats وصفحة Crypton (الذي يبحث عبر CoinGecko)؛ ولم يسمح موقع Delta بالتحقق. لم نثبّت التطبيقات ولم نختبر سرعة وصول التنبيهات.",
            "سياق الأخبار منسوب إلى المواقع المرتبطة أعلاه؛ ولا تتخذ هذه الصفحة موقفًا من التحقيقات. لا يُعد أي من هذه التطبيقات منصة تداول، ولا شيء هنا نصيحة مالية."],
    faq=[
        ("أي تطبيق يعرض سعر WLFI على iPhone؟", "تدرج CoinGecko وCoinMarketCap وCoinStats شركة World Liberty Financial (WLFI)، ويجدها Crypton بالبحث لأنه يستخدم بيانات CoinGecko."),
        ("هل يمكنني تلقي تنبيه بسعر عملة TRUMP الميمية؟", "نعم، مع CoinGecko أو CoinMarketCap أو CoinStats أو Delta، وكلها تتيح تنبيهات الأسعار. Crypton لا يملك تنبيهات أسعار."),
        ("هل ما زالت USD1 تساوي دولارًا واحدًا؟", "بحسب CoinGecko، تداولت بنحو 0.998 دولار من 1 إلى 8 نوفمبر 2026، وبلغت قيمتها السوقية نحو 3.44 مليار دولار."),
        ("لماذا انخفض TRUMP وWLFI في نوفمبر 2026؟", "بحسب CoinGecko، انخفض TRUMP بنحو 32% وWLFI بنحو 8% من 1 إلى 8 نوفمبر، في الأسبوع الذي قال فيه الديمقراطيون، الذين فازوا بالأغلبية في المجلس، إنهم يخططون للتحقيق في الأنشطة المشفرة لعائلة ترامب، بحسب crypto.news وCNBC. لا تنسب هذه الصفحة تحرك الأسعار إلى سبب محدد، وليست نصيحة مالية."),
        ("هل أحتاج إلى حساب لمتابعة هذه الرموز؟", "ليس في Crypton (الحساب للمزامنة فقط). تتطلب CoinMarketCap حسابًا للمحفظة لكن لديها وضع تصفح خاص؛ ولا تذكر الصفحات الأخرى أن الحساب مطلوب."),
    ],
    sources=["crypto.news، 4 نوفمبر 2026: الديمقراطيون يستعدون للتحقيق في World Liberty Financial بعد فوزهم في مجلس النواب",
             "CNBC، 5 نوفمبر 2026: فوز الديمقراطيين يضع العملات المشفرة في موقف دفاعي في واشنطن",
             "Financial Times، 8 نوفمبر 2026، الصفحة الأولى: «Crypto industry braces for reckoning over Trump ties» (العنوان فقط)",
             "واجهة CoinGecko: أسعار TRUMP وWLFI وUSD1 وBTC",
             "CoinMarketCap: Official Trump",
             "CoinMarketCap: World Liberty Financial",
             "CoinMarketCap: USD1",
             "CoinStats: Official Trump",
             "CoinStats: World Liberty Financial",
             "CoinStats: USD1",
             "CoinGecko: Crypto Tracker (App Store)",
             "CoinMarketCap: Crypto Tracker (App Store)",
             "CoinStats: Crypto Portfolio (App Store)",
             "Crypto Tracker: Crypton (App Store)",
             "Delta by eToro (App Store)"],
)

PAGES.append(_translated("ar", "ar", "ar", AR))


_ES_WIDGETS = '<a href="/best-crypto-price-widget-apps-iphone/">apps de widgets de cripto</a>'
_ES_ALERTS = '<a href="/best-crypto-price-alert-apps-iphone/">apps de alertas de precio de cripto</a>'
_ES_NOCONNECT = '<a href="/crypto-portfolio-tracker-without-connecting-wallet-iphone/">rastreadores que no piden cartera ni exchange</a>'

ES = dict(
    kicker="5 apps · Ranking · Noticias",
    title="Mejores apps de iPhone para seguir los precios de WLFI, TRUMP y USD1 (nov 2026)",
    h1="Mejores apps de iPhone para seguir los precios de WLFI, TRUMP y USD1 (nov 2026)",
    description="Cinco apps de iPhone que siguen World Liberty Financial (WLFI), la memecoin TRUMP y USD1, comparadas por precio, alertas, widgets y cuenta el 8 de noviembre de 2026.",
    llms="Cinco apps de iPhone para seguir WLFI, TRUMP y USD1 tras las elecciones de mitad de mandato de EE. UU. de noviembre de 2026: CoinGecko, CoinMarketCap, CoinStats, Crypton, Delta. Cuáles listan los tres tokens, alertas, widgets, cuenta, precio en EE. UU. y valoración. Con precios de CoinGecko del 1 al 8 de noviembre de 2026 y contexto de noticias fechado. No es asesoramiento financiero.",
    answer=[
        "Para seguir WLFI, TRUMP y USD1 con alertas de precio, <strong>CoinGecko</strong>, <strong>CoinMarketCap</strong> y <strong>CoinStats</strong> listan los tres tokens; CoinStats además conecta tu cartera y tiene widgets en la pantalla de bloqueo.",
        "Para un widget gratuito en la pantalla de inicio, sin cuenta y sin comprar nada, <strong>Crypton</strong> encuentra los tres tokens por búsqueda, pero no tiene alertas; <strong>Delta</strong> sirve para una cartera que mezcla criptomonedas y acciones.",
    ],
    context_html=f"""<h2 id="context">Qué pasó (8 de noviembre de 2026)</h2>
<p>Tras las elecciones de mitad de mandato del 3 de noviembre, los demócratas ganaron la mayoría en la Cámara de Representantes según las proyecciones de NBC News y MS NOW, y planean investigar los negocios cripto de la familia Trump, incluida World Liberty Financial (el token WLFI y la stablecoin USD1) y la memecoin TRUMP. <a href="{CNEWS}">Informa crypto.news</a> que las investigaciones podrían empezar ya en febrero de 2027. La Casa Blanca rechazó los planes; antes de la votación, una portavoz había calificado la agenda demócrata de «caza de brujas», según el mismo reportaje. <a href="{CNBC}">CNBC escribe</a> que el resultado pone a la industria cripto a la defensiva en Washington, y el 8 de noviembre el Financial Times llevó la historia a portada con el titular «Crypto industry braces for reckoning over Trump ties» (en inglés).</p>
<div class="scroll"><table style="min-width:0">
<thead><tr><th>Token</th><th>1 nov 2026</th><th>8 nov 2026</th><th>Variación</th><th>Capitalización, 8 nov</th></tr></thead>
<tbody>
<tr><td>TRUMP (Official Trump)</td><td>US$ 1,71</td><td>US$ 1,16</td><td>unos −32 %</td><td>unos 328 millones de US$</td></tr>
<tr><td>WLFI (World Liberty Financial)</td><td>US$ 0,050</td><td>US$ 0,046</td><td>unos −8 %</td><td>unos 1.470 millones de US$</td></tr>
<tr><td>USD1 (stablecoin)</td><td>US$ 0,998</td><td>US$ 0,998</td><td>mantuvo su paridad de 1 US$</td><td>unos 3.440 millones de US$</td></tr>
<tr><td>Bitcoin, para comparar</td><td>US$ 78.294</td><td>US$ 75.820</td><td>unos −3 %</td><td>unos 1,52 billones de US$</td></tr>
</tbody></table></div>
<p class="note">Precios en dólares según la API de CoinGecko: la columna del 1 de noviembre es el cierre de ese día, y la del 8 de noviembre, el precio de la tarde del 8 (UTC). La mayor caída diaria de TRUMP en la semana fue el 4 de noviembre, el día después de la elección, de unos 1,59 $ a 1,27 $. Nada de esta página es asesoramiento financiero.</p>
""",
    columns=["App", "Precio (EE. UU.)", "Lista WLFI, TRUMP, USD1", "Alertas de precio", "Widget", "Cuenta necesaria", "Versión (fecha)", "Valoración (EE. UU.)"],
    table_note="Precios, versiones y valoraciones son los de cada página de App Store de EE. UU. el 8 de noviembre de 2026; las cinco apps se descargan gratis. Alertas, widgets y cuenta según describe cada ficha. Los tokens se comprobaron en la web de cada empresa o en los datos del 8 de noviembre.",
    apps=[
        dict(
            row=["Gratis; Premium US$ 9,90 al mes o US$ 99,90 al año", "Sí, los tres", "Sí: alertas de precio y de grandes movimientos", "Sí, en la pantalla de inicio", "La ficha no dice que sea necesaria", "3.60.0 (27 oct 2026)", "4.8"],
            best_for="seguir WLFI, TRUMP y USD1 con los mismos datos de la tabla de precios de arriba, con alertas.",
            facts=[
                "Los datos de CoinGecko incluyen Official Trump, World Liberty Financial y USD1, así que puedes añadir los tres a una lista de seguimiento.",
                "Según su ficha, ofrece alertas de precio personalizadas y de grandes movimientos para monedas de la lista, cartera con ganancias y pérdidas y widget en la pantalla de inicio.",
                "Tiene categorías como las memecoins, donde está TRUMP.",
            ],
            limits="solo en inglés, y la ficha no dice cuántas alertas son gratis.",
        ),
        dict(
            row=["Gratis; Essential US$ 11,99 al mes o US$ 109,99 al año; Plus US$ 23,99 al mes o US$ 229,99 al año; Max US$ 119,99 al mes", "Sí, los tres", "Sí: alertas de precio personalizables", "La ficha no lo menciona", "Necesaria para la cartera; modo incógnito sin iniciar sesión", "5.24.0 (1 nov 2026)", "4.8"],
            best_for="el rastreador más valorado: alertas para cualquiera de los tres tokens.",
            facts=[
                "CoinMarketCap tiene páginas de Official Trump, World Liberty Financial y World Liberty Financial USD (USD1).",
                "Alertas de precio personalizables y listas de seguimiento; según su ficha, sigue más de 45.000 mercados activos.",
                "Unas 173.000 valoraciones en EE. UU., las más de esta lista, y 21 idiomas.",
            ],
            limits="la ficha pide crear una cuenta para hacer una cartera (el modo incógnito mantiene los datos en el teléfono), no menciona widget y sus planes son los más caros de la lista.",
        ),
        dict(
            row=["Gratis; Pro US$ 4,99 al mes o US$ 39,99 al año; Premium US$ 15,99 a US$ 19,99 al mes o US$ 65,99 a US$ 164,99 al año", "Sí, los tres", "Sí: alertas de precio, volumen y capitalización, más Auto Alerts", "Sí: pantalla de inicio, pantalla de bloqueo y Apple Watch", "La ficha no dice que sea necesaria", "5.31.1 (30 oct 2026)", "4.8"],
            best_for="quien tiene WLFI o TRUMP en una cartera o un exchange y quiere seguirlos automáticamente, con alertas y widgets en la pantalla de bloqueo.",
            facts=[
                "coinstats.app tiene páginas de Official Trump, World Liberty Financial y USD1.",
                "Conecta más de 300 carteras y exchanges y muestra ganancias y pérdidas en tiempo real; según su ficha, precios de más de 20.000 monedas.",
                "Alertas de precio, volumen o capitalización sobre cualquier moneda, y widgets en la pantalla de inicio, la de bloqueo y el Apple Watch.",
            ],
            limits="muchos planes de pago que se solapan, y el conjunto completo de análisis exige Premium.",
        ),
        dict(
            row=["Gratis, sin compras dentro de la app", "Sí, por búsqueda (datos de CoinGecko)", "No", "Sí: precios y cartera (pantalla de inicio)", "No (opcional, solo para sincronizar)", "2.0.8 (24 oct 2026)", "4.7"],
            best_for="una lista de seguimiento gratis de WLFI, TRUMP y USD1 en la pantalla de inicio, sin cuenta y sin pagar nada.",
            facts=[
                "Precios en vivo de las 250 principales monedas y búsqueda de cualquier moneda listada en CoinGecko, así que WLFI, TRUMP y USD1 pueden ir a Favoritos, según su ficha.",
                "Cartera con ganancias y pérdidas en cada moneda, y widgets en la pantalla de inicio para precios y para la cartera.",
                "Sin compras dentro de la app; solo en inglés, iOS 18 o posterior.",
            ],
            limits="la versión actual no tiene alertas de precio, ni widget de pantalla de bloqueo, ni app para Apple Watch, y no sincroniza con carteras ni exchanges. Para alertas, mira las " + _ES_ALERTS + ".",
        ),
        dict(
            row=["Gratis hasta 10 activos; PRO de US$ 6,99 a US$ 13,99 al mes o de US$ 58,99 a US$ 99,90 al año; PRO+ US$ 13,99 al mes o US$ 107,99 al año", "Sin verificar (ficha: más de 10.000 monedas)", "Sí: precios objetivo y grandes movimientos", "La ficha no lo menciona", "La ficha no lo indica", "2026.3.2 (5 nov 2026)", "4.7"],
            best_for="seguir cripto y acciones en una misma cartera, con alertas.",
            facts=[
                "Sigue juntos cripto, acciones, ETF, materias primas y divisas; más de 10.000 monedas, según su ficha.",
                "Alertas inteligentes para precios objetivo y movimientos relevantes, y notificaciones personalizadas para hitos de la cartera.",
                "El plan gratuito sigue hasta 10 activos; PRO hasta 40; PRO+ sin límite.",
            ],
            limits="no pudimos confirmar en la web de Delta que liste WLFI, TRUMP y USD1; el plan gratis se queda en 10 activos; y su etiqueta de privacidad incluye datos usados para seguimiento.",
        ),
    ],
    who=["<strong>Alertas cuando TRUMP o WLFI se mueven mucho:</strong> CoinGecko (alertas de grandes movimientos) o CoinStats (Auto Alerts).",
         "<strong>El rastreador más usado:</strong> CoinMarketCap.",
         "<strong>Tokens en una cartera o exchange:</strong> CoinStats.",
         "<strong>Ver los tres precios de un vistazo, sin cuenta:</strong> Crypton.",
         "<strong>Cripto y acciones en un solo sitio:</strong> Delta."],
    cases=["Comprobar si USD1 sigue en 1 $: cualquier app de la lista que la siga; CoinGecko y CoinMarketCap muestran también su capitalización.",
           "Recibir un aviso si TRUMP cae otro 10 %: CoinGecko, CoinMarketCap, CoinStats o Delta (con alertas); no Crypton.",
           "Tener WLFI y TRUMP en la pantalla de inicio: CoinGecko, CoinStats o Crypton. Más en los rankings de " + _ES_WIDGETS + " y " + _ES_ALERTS + ".",
           "Seguir tus saldos sin conectar una cartera: mira " + _ES_NOCONNECT + "."],
    method=["El 8 de noviembre de 2026 leímos la página de App Store de EE. UU. de cada app y los datos de búsqueda de Apple (precio, compras dentro de la app, versión, valoración y texto de la ficha). Para ver si cada app lista WLFI, TRUMP y USD1, lo comprobamos en los datos de CoinGecko, en las páginas de monedas de CoinMarketCap y CoinStats y en la ficha de Crypton (que busca a través de CoinGecko); la web de Delta no nos dejó comprobarlo. No instalamos las apps ni probamos la rapidez de las alertas.",
            "El contexto de noticias se atribuye a los medios enlazados arriba; esta página no toma postura sobre las investigaciones. Ninguna de estas apps es un exchange, y nada de esto es asesoramiento financiero."],
    faq=[
        ("¿Qué app muestra el precio de WLFI en el iPhone?", "CoinGecko, CoinMarketCap y CoinStats listan World Liberty Financial (WLFI); Crypton lo encuentra por búsqueda porque usa datos de CoinGecko."),
        ("¿Puedo recibir una alerta del precio de la memecoin TRUMP?", "Sí, con CoinGecko, CoinMarketCap, CoinStats o Delta, que tienen alertas de precio. Crypton no tiene alertas de precio."),
        ("¿USD1 sigue valiendo un dólar?", "Según CoinGecko, entre el 1 y el 8 de noviembre de 2026 cotizó en torno a 0,998 US$, con una capitalización de unos 3.440 millones de US$."),
        ("¿Por qué bajaron TRUMP y WLFI en noviembre de 2026?", "Según CoinGecko, entre el 1 y el 8 de noviembre TRUMP cayó unos 32 % y WLFI unos 8 %, la semana en que los demócratas, que ganaron la Cámara, dijeron que planean investigar los negocios cripto de la familia Trump, según crypto.news y CNBC. Esta página no atribuye la caída de precios a ninguna causa y no es asesoramiento financiero."),
        ("¿Necesito cuenta para seguir estos tokens?", "En Crypton, no (la cuenta solo sincroniza). CoinMarketCap pide cuenta para la cartera, pero tiene modo incógnito; las demás fichas no dicen que haga falta cuenta."),
    ],
    sources=["crypto.news, 4 nov 2026: los demócratas preparan una investigación sobre World Liberty Financial tras ganar la Cámara",
             "CNBC, 5 nov 2026: la victoria demócrata pone al sector cripto a la defensiva en Washington",
             "Financial Times, 8 nov 2026, portada: «Crypto industry braces for reckoning over Trump ties» (solo el titular)",
             "API de CoinGecko: precios de TRUMP, WLFI, USD1 y BTC",
             "CoinMarketCap: Official Trump",
             "CoinMarketCap: World Liberty Financial",
             "CoinMarketCap: USD1",
             "CoinStats: Official Trump",
             "CoinStats: World Liberty Financial",
             "CoinStats: USD1",
             "CoinGecko: Crypto Tracker (App Store)",
             "CoinMarketCap: Crypto Tracker (App Store)",
             "CoinStats: Crypto Portfolio (App Store)",
             "Crypto Tracker: Crypton (App Store)",
             "Delta by eToro (App Store)"],
)

PAGES.append(_translated("es", "es", "es", ES))
