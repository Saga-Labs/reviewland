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
