from pages.trlib import make

# Best private AI companion apps for iPhone (EN: nov14_private_companions). Drafts, not reviewed by native speakers.
# Availability and price: each store's lookup run 15 Nov 2026 (itunes lookup, country = langs.py store).
# Apps not on sale in a country are left out with `keep`; the table note says which. Ratings are the US store's
# (14 Nov 2026), kept as in English. Store names are used where the local App Store name differs.
# Left out: ru (Pi, Tolan), de (Nomi), ja (Tolan), es (Nomi), pt-BR (Tolan), fr (Nomi). ar: all eight.

# ---------------------------------------------------------------- ru (Россия)
TR_RU = {
    "title": "Лучшие приложения для личного ИИ-компаньона на iPhone (2026)",
    "h1": "Лучшие приложения для личного ИИ-компаньона на iPhone (2026)",
    "description": "Восемь приложений ИИ-компаньонов и ИИ-друзей для iPhone: на устройстве или в облаке, работа без сети, аккаунт, цена и метка конфиденциальности в App Store. Проверено 14 ноября 2026 года.",
    "llms": "Сравнивает восемь приложений ИИ-компаньонов для iPhone (Talking Friday, Najimi, SOUL.AI, Nomi, Pi, Replika, Tolan, Character AI) по тому, остаются ли чаты на телефоне, работе без сети, аккаунту, цене, оценке и метке конфиденциальности в App Store. Пишет, что говорит каждое описание и чего в нём нет.",
    "answer": [
        "Если вам нужен ИИ-компаньон, чьи чаты остаются на телефоне, только три из восьми проверенных приложений прямо говорят об этом в описании в App Store: Talking Friday, Najimi и SOUL.AI запускают ИИ на iPhone, говорят, что работают без сети, и все три имеют метку «Данные не собираются». Пять крупных приложений (Nomi, Pi, Replika, Tolan, Character AI) имеют гораздо больше оценок, но их метки перечисляют собранные данные, связанные с вами, и ни одно не заявляет о работе на устройстве.",
        "Цена этого — размер: приложения на устройстве имеют от 0 до 11 оценок, поэтому их качество не подтверждено, а метка конфиденциальности — заявление самого разработчика. Мы проверили 14 ноября 2026 года и писали «Не указано» там, где описание молчит.",
    ],
    "keep": [0, 1, 2, 3, 5, 7],
    "day": "2026-11-15",
    "columns": ["Приложение", "Работает на iPhone", "Работает без сети", "Нужен аккаунт", "Цена (Россия)", "Оценка (США)"],
    "table_note": "Цены и наличие — из App Store России на 15 ноября 2026 года; оценки — из App Store США на 14 ноября 2026 года (это американские оценки, не российские). Остальные колонки — то, что написано в описании каждого приложения; «Не заявлено» значит, что описание не утверждает, что ИИ работает на устройстве, «Не указано» — что описание молчит. Pi и Tolan не продаются в App Store России на 15 ноября 2026 года, поэтому в таблице их нет. Оценка с очень малым числом голосов мало что говорит.",
    "apps": [
        {
            "row": ["Да, по описанию (речь в речь на Neural Engine)", "Да", "Нет", "Бесплатно; покупок в приложении нет, по описанию", "Оценок пока нет"],
            "best_for": "приватные голосовые разговоры, которые не покидают телефон.",
            "facts": [
                "По описанию весь цикл «речь в речь» работает на Neural Engine iPhone, без серверов, аккаунта и интернета.",
                "Метка в App Store: Данные не собираются.",
                "Вы говорите, а приложение отвечает вслух; это не приложение с персонажами или романтикой, а голосовой чат для размышлений вслух или тренировки разговоров.",
                "Версия 1.0, iOS 18.0 или новее, описание обновлено 14 июля 2026 года.",
            ],
            "limits": "оценок пока нет, поэтому нет публичных данных о качестве разговоров; только голос, и нужна iOS 18.",
        },
        {
            "row": ["Да, по описанию (локальные модели ИИ и голоса встроены)", "Да, по описанию («работает без сети»)", "Не указано", "Бесплатно", "4.0 (2 оценки)"],
            "best_for": "настраиваемый аватар-компаньон, который работает локально.",
            "facts": [
                "По описанию в приложение встроены локальная языковая модель и модель голоса для чата на устройстве, поэтому загрузка больше обычной.",
                "Можно менять характер, внешность, голос и фон, импортировать свой персонаж VRM и общаться с документами.",
                "Метка в App Store: Данные не собираются.",
                "Версия 1.1, iOS 18.6 или новее, обновлено 6 августа 2026 года.",
            ],
            "limits": "всего 2 оценки; большая загрузка; описание не говорит, нужен ли аккаунт.",
        },
        {
            "row": ["Да, по описанию", "Да", "Нет", "Бесплатно", "2.5 (11 оценок)"],
            "best_for": "простой чат-модель без сети на современном iPhone.",
            "facts": [
                "По описанию модель находится внутри приложения, работает полностью на устройстве и не отправляет чаты в облако; аккаунт не нужен.",
                "Метка в App Store: Данные не собираются.",
                "Рекомендует iPhone 15 Pro или новее; на старых устройствах может работать медленно или вылетать, устройства ниже iPhone 12 не поддерживаются.",
                "Версия 1.7.3, обновлено 10 июля 2026 года.",
            ],
            "limits": "оценка 2.5 от 11 человек; это скорее универсальный ассистент, чем компаньон с характером.",
        },
        {
            "row": ["Не заявлено", "Не указано", "Не указано", "Бесплатно", "4.6 (3,029 оценок)"],
            "best_for": "долгую память и ролевые отношения, если вы принимаете облачный сервис.",
            "facts": [
                "В описании делается упор на краткосрочную и долгосрочную память, групповые чаты, селфи и генерацию картинок; о работе ИИ на устройстве не сказано.",
                "Метка в App Store: Данные связаны с вами (покупки, контактная информация, пользовательский контент, идентификаторы, данные об использовании, диагностика). Отслеживание не указано.",
                "Версия 1.12.1, iOS 15.0 или новее, обновлено 31 марта 2026 года.",
            ],
            "limits": "пользовательский контент в метке связан с вами, поэтому считайте, что чаты хранит компания; политика конфиденциальности скажет, как долго. Это отвечает на частый вопрос «приватен ли Nomi AI»: метка говорит, что данные связаны с вами, а в описании нет заявлений о работе на устройстве.",
        },
        {
            "name": "Replika - AI Companion Chat",
            "row": ["Не заявлено", "Не указано", "Не указано", "Бесплатно", "4.4 (227,667 оценок)"],
            "best_for": "долгий компаньон со звонками и напоминаниями о себе по собственной инициативе.",
            "facts": [
                "В описании: текстовые, голосовые и видеозвонки, доступ в интернет, интеграции с приложениями и генерация изображений; сказано, что он помнит ваших близких и планы.",
                "Метка в App Store: Данные используются для отслеживания (идентификаторы, данные об использовании); Данные связаны с вами (местоположение, контактная информация, идентификаторы, данные об использовании); и часть диагностики, не связанной с вами.",
                "Версия 12.5.2 (5 нояб. 2026), iOS 17.0 или новее.",
            ],
            "limits": "в метке есть данные для отслеживания и местоположение, а в описании перечислены функции, которым нужен интернет.",
        },
        {
            "row": ["Не заявлено", "Не указано", "Не указано", "Бесплатно", "4.3 (561,523 оценки)"],
            "best_for": "миллионы созданных пользователями персонажей, если приватность не ваш главный критерий.",
            "facts": [
                "В описании: общение и звонки с огромной библиотекой созданных пользователями персонажей, а также создание своих и публикация их для сообщества.",
                "Метка в App Store: Данные используются для отслеживания (местоположение, контактная информация, идентификаторы, данные об использовании); Данные связаны с вами (покупки, финансовая информация, местоположение, контактная информация, пользовательский контент, история поиска, идентификаторы, данные об использовании, диагностика).",
                "Версия 1.17.4 (2 окт. 2026), iOS 15.1 или новее.",
            ],
            "limits": "самый длинный список данных из восьми, включая финансовую информацию, пользовательский контент и историю поиска, связанные с вами, и дизайн вокруг сообщества и публикации.",
        },
    ],
    "who": [
        "<strong>Вам нужны чаты, которые не покидают телефон:</strong> Talking Friday (голос), Najimi (аватар) или SOUL.AI (простой чат).",
        "<strong>Вам нужно проверенное качество, и вы принимаете облачный сервис:</strong> Nomi или Replika, с ограничениями меток, описанными выше.",
        "<strong>Вы хотите меньше данных среди больших приложений:</strong> Nomi не указывает отслеживания; Replika и Character AI указывают.",
        "<strong>Вам нужно пользоваться им в самолёте или без сигнала:</strong> Talking Friday, Najimi или SOUL.AI.",
    ],
    "cases": [
        "Выговориться или подумать вслух ночью без аккаунта (Talking Friday, SOUL.AI).",
        "Персонаж, которого можно настроить и который работает локально (Najimi).",
        "Долгие разговоры с памятью, если вы принимаете облачный сервис (Nomi, Replika).",
        "Общение с множеством созданных пользователями персонажей (Character AI).",
    ],
    "method": [
        "14 ноября 2026 года мы искали в App Store США «private ai companion», «offline ai companion», «ai friend to talk to» и «on-device ai chat private», открыли данные Apple о восьми приложениях (название, цена, оценка, описание) и прочитали на странице каждого приложения его метку конфиденциальности.",
        "Мы упорядочили приложения по тому, насколько описание и метка поддерживают приватный чат, а затем по оценке. Приложения на устройстве стоят первыми по приватности, но оценок у них слишком мало, чтобы судить о качестве, поэтому читайте это как «сначала приватность», а не «лучший компаньон».",
        "Функции и заявления о приватности взяты только из описаний и меток, а не из наших тестов; сетевые перехваты мы не делали. Мы не включили другие приложения из поиска (Kindroid, Solace, Red Angel и другие), чтобы список оставался из восьми; например, в описании Solace говорится об удалении аккаунта и ничего не сказано о том, что чаты остаются на устройстве. Cora не появилась в поиске App Store США.",
    ],
    "faq": [
        ("Приватен ли Nomi AI?",
         "В его описании не сказано, что ИИ работает на телефоне, а метка в App Store говорит о данных, связанных с вами, включая пользовательский контент, но не о трекинге. Политика конфиденциальности расскажет, как долго хранятся чаты."),
        ("Может ли ИИ-компаньон работать без сети?",
         "Да, если модель находится на телефоне. Talking Friday, Najimi и SOUL.AI говорят, что их модель работает без сети. Приложения, которые этого не говорят, например Nomi, Pi, Replika, Tolan и Character AI, в описаниях не названы работающими без сети."),
        ("Какое самое приватное приложение ИИ-друга для iPhone?",
         "Из восьми проверенных — те, у которых есть заявление о работе на устройстве и метка «Данные не собираются»: Talking Friday, Najimi и SOUL.AI. Оценок у них очень мало, поэтому проверьте сами в режиме «в самолёте»."),
        ("Что говорит метка конфиденциальности App Store?",
         "Это собственный перечень разработчика о собранных данных, разделённый на используемые для отслеживания, связанные с вами и не связанные с вами. Она не говорит, как долго хранятся чаты."),
    ],
}

# ---------------------------------------------------------------- de (Deutschland)
TR_DE = {
    "title": "Die besten Apps für private KI-Begleiter auf dem iPhone (2026)",
    "h1": "Die besten Apps für private KI-Begleiter auf dem iPhone (2026)",
    "description": "Acht KI-Begleiter- und KI-Freund-Apps für das iPhone im Vergleich nach Datenschutz: auf dem Gerät oder in der Cloud, offline nutzbar, Konto, Preis und Datenschutzhinweis im App Store. Geprüft am 14. November 2026.",
    "llms": "Vergleicht acht KI-Begleiter-Apps für das iPhone (Talking Friday, Najimi, SOUL.AI, Nomi, Pi, Replika, Tolan, Character AI) danach, ob Chats auf dem Telefon bleiben, ob sie offline laufen, Konto, Preis, Bewertung und Datenschutzhinweis im App Store. Sagt, was jede Beschreibung behauptet und was nicht.",
    "answer": [
        "Wenn du einen KI-Begleiter willst, dessen Chats auf deinem Telefon bleiben, sagen nur drei der acht geprüften Apps das in ihrem App-Store-Eintrag: Talking Friday, Najimi und SOUL.AI betreiben die KI auf dem iPhone und sagen, dass sie offline funktionieren, und alle drei tragen das Etikett „Keine Daten erfasst“. Die fünf größeren Apps (Nomi, Pi, Replika, Tolan, Character AI) haben weit mehr Bewertungen, aber ihre Etiketten listen erfasste Daten, die mit dir verknüpft sind, und keine behauptet, auf dem Gerät zu laufen.",
        "Der Preis dafür ist die Größe: Die Apps auf dem Gerät haben 0 bis 11 Bewertungen, daher ist ihre Qualität nicht belegt, und ein Datenschutzetikett ist die eigene Aussage des Entwicklers. Wir haben am 14. November 2026 geprüft und überall „Nicht angegeben“ geschrieben, wo ein Eintrag schweigt.",
    ],
    "keep": [0, 1, 2, 4, 5, 6, 7],
    "day": "2026-11-15",
    "columns": ["App", "Läuft auf dem iPhone", "Funktioniert offline", "Konto nötig", "Preis (Deutschland)", "Bewertung (USA)"],
    "table_note": "Preise und Verfügbarkeit stammen aus dem App Store Deutschland vom 15. November 2026; Bewertungen aus dem App Store USA vom 14. November 2026 (US-Bewertungen, nicht deutsche). Die übrigen Spalten sind das, was die Beschreibung jeder App sagt; „Nicht behauptet“ heißt, dass die Beschreibung nicht sagt, die KI laufe auf dem Gerät, „Nicht angegeben“ heißt, dass sie es nicht sagt. Nomi ist am 15. November 2026 nicht im App Store Deutschland erhältlich und fehlt deshalb in der Tabelle; die Texte unten beziehen sich auf die acht Apps, die wir im US-App-Store geprüft haben. Eine Bewertung mit sehr wenigen Stimmen sagt wenig.",
    "apps": [
        {
            "row": ["Ja, laut Eintrag (Sprache-zu-Sprache auf der Neural Engine)", "Ja", "Nein", "Gratis; laut Eintrag keine In-App-Käufe", "Noch keine Bewertungen"],
            "best_for": "private Sprachgespräche, die das Telefon nie verlassen.",
            "facts": [
                "Laut Eintrag läuft die gesamte Sprache-zu-Sprache-Schleife auf der Neural Engine des iPhones, ohne Server, ohne Konto und ohne Internet.",
                "Datenschutzetikett im App Store: Keine Daten erfasst.",
                "Du sprichst, und die App antwortet laut; sie ist keine Figuren- oder Liebes-App, sondern ein Sprachchat zum lauten Nachdenken oder Üben von Gesprächen.",
                "Version 1.0, iOS 18.0 oder neuer, Eintrag aktualisiert am 14. Juli 2026.",
            ],
            "limits": "noch keine Bewertungen, daher keine öffentlichen Belege, wie gut die Gespräche sind; nur Stimme, und sie braucht iOS 18.",
        },
        {
            "row": ["Ja, laut Eintrag (lokale KI- und Stimmmodelle enthalten)", "Ja, laut Eintrag („kann offline laufen“)", "Nicht angegeben", "Gratis", "4.0 (2 Bewertungen)"],
            "best_for": "ein anpassbarer Avatar-Begleiter, der lokal läuft.",
            "facts": [
                "Laut Eintrag enthält die App ein lokales Sprachmodell und ein Stimmmodell für Chat auf dem Gerät, deshalb ist der Download größer als üblich.",
                "Du kannst Persönlichkeit, Aussehen, Stimme und Hintergrund ändern, einen eigenen VRM-Charakter importieren und mit Dokumenten chatten.",
                "Datenschutzetikett im App Store: Keine Daten erfasst.",
                "Version 1.1, iOS 18.6 oder neuer, aktualisiert am 6. August 2026.",
            ],
            "limits": "nur 2 Bewertungen; großer Download; der Eintrag sagt nicht, ob ein Konto nötig ist.",
        },
        {
            "row": ["Ja, laut Eintrag", "Ja", "Nein", "Gratis", "2.5 (11 Bewertungen)"],
            "best_for": "ein schlichtes Offline-Chatmodell auf einem aktuellen iPhone.",
            "facts": [
                "Laut Eintrag steckt das Modell in der App, läuft vollständig auf dem Gerät und sendet keine Chats in die Cloud; kein Konto.",
                "Datenschutzetikett im App Store: Keine Daten erfasst.",
                "Empfohlen wird iPhone 15 Pro oder neuer; ältere Geräte können langsam sein oder abstürzen, Geräte unter dem iPhone 12 werden nicht unterstützt.",
                "Version 1.7.3, aktualisiert am 10. Juli 2026.",
            ],
            "limits": "eine Bewertung von 2.5 von 11 Personen; und eher ein allgemeiner Assistent als ein Begleiter mit Persönlichkeit.",
        },
        {
            "name": "Pi, your personal AI",
            "row": ["Nicht behauptet", "Nicht angegeben", "Nicht angegeben", "Gratis", "4.4 (2,555 Bewertungen)"],
            "best_for": "ein ruhiger Assistent zum Durchsprechen von Dingen, mit Sprachmodus.",
            "facts": [
                "Der Eintrag beschreibt das Durchsprechen von Dingen, den Sprachmodus und das Erledigen von Aufgaben; er sagt nicht, wo die KI läuft.",
                "Datenschutzetikett im App Store: Mit dir verknüpfte Daten (Kennungen, Nutzungsdaten, Diagnose) für Analysen, Personalisierung und App-Funktionen. Kein Tracking aufgeführt.",
                "Version 26.1109.0 (13. Nov. 2026), iOS 16 oder neuer.",
            ],
            "limits": "kein Anspruch auf Gerätebetrieb oder offline; das Etikett hat keine Kategorie für Nutzerinhalte, sagt aber nicht, wie Chats gespeichert werden.",
        },
        {
            "name": "Replika - KI Companion Chat",
            "row": ["Nicht behauptet", "Nicht angegeben", "Nicht angegeben", "Gratis", "4.4 (227,667 Bewertungen)"],
            "best_for": "ein langlebiger Begleiter mit Anrufen und proaktiven Check-ins.",
            "facts": [
                "Der Eintrag beschreibt Text-, Sprach- und Videoanrufe, Internetzugang, App-Integrationen und Bilderzeugung und sagt, dass er sich an deine Menschen und Pläne erinnert.",
                "Datenschutzetikett im App Store: Zum Tracking genutzte Daten (Kennungen, Nutzungsdaten); mit dir verknüpfte Daten (Standort, Kontaktdaten, Kennungen, Nutzungsdaten); und einige Diagnosedaten, die nicht mit dir verknüpft sind.",
                "Version 12.5.2 (5. Nov. 2026), iOS 17.0 oder neuer.",
            ],
            "limits": "das Etikett enthält Tracking-Daten und Standort, und der Eintrag beschreibt Funktionen, die Internet brauchen.",
        },
        {
            "row": ["Nicht behauptet", "Nicht angegeben", "Nicht angegeben", "Gratis", "4.8 (190,859 Bewertungen)"],
            "best_for": "ein freundlicher Begleiter im Alien-Stil, mit dem du über alles reden kannst.",
            "facts": [
                "Der Eintrag ist kurz: über Interessen, Gefühle und Gedanken sprechen, Fotos teilen und gemeinsam einen Planeten gestalten. Er sagt nichts darüber, wo die KI läuft.",
                "Datenschutzetikett im App Store: Zum Tracking genutzt (Käufe, Standort, Kontaktdaten, Kennungen, Nutzungsdaten, andere Daten); mit dir verknüpft (inklusive Nutzerinhalte); und weitere, nicht mit dir verknüpft.",
                "Version 26.46.1 (11. Nov. 2026), iOS 18.0 oder neuer.",
            ],
            "limits": "das Etikett listet Tracking und Standort sowie Nutzerinhalte als mit dir verknüpft; der Eintrag macht keine Datenschutzangaben.",
        },
        {
            "row": ["Nicht behauptet", "Nicht angegeben", "Nicht angegeben", "Gratis", "4.3 (561,523 Bewertungen)"],
            "best_for": "Millionen von Nutzern erstellter Figuren, wenn Datenschutz nicht an erster Stelle steht.",
            "facts": [
                "Der Eintrag beschreibt Chatten und Anrufe mit einer riesigen Bibliothek nutzergeschaffener Figuren, dazu das Erstellen eigener Figuren und das Teilen mit der Community.",
                "Datenschutzetikett im App Store: Zum Tracking genutzt (Standort, Kontaktdaten, Kennungen, Nutzungsdaten); mit dir verknüpft (Käufe, Finanzdaten, Standort, Kontaktdaten, Nutzerinhalte, Suchverlauf, Kennungen, Nutzungsdaten, Diagnose).",
                "Version 1.17.4 (2. Okt. 2026), iOS 15.1 oder neuer.",
            ],
            "limits": "die längste Datenliste der acht, mit Finanzdaten, Nutzerinhalten und Suchverlauf, die mit dir verknüpft sind, und einem Konzept rund um Community und Teilen.",
        },
    ],
    "who": [
        "<strong>Du willst Chats, die das Telefon nie verlassen:</strong> Talking Friday (Stimme), Najimi (Avatar) oder SOUL.AI (schlichter Chat).",
        "<strong>Du willst belegte Qualität und nimmst einen Cloud-Dienst in Kauf:</strong> Pi, Replika oder Tolan, mit den oben genannten Einschränkungen des Etiketts.",
        "<strong>Du willst unter den großen Apps am wenigsten Daten erfasst:</strong> Pi gibt kein Tracking an; Replika, Tolan und Character AI tun es.",
        "<strong>Du willst es im Flugzeug oder ohne Empfang nutzen:</strong> Talking Friday, Najimi oder SOUL.AI.",
    ],
    "cases": [
        "Nachts ohne Konto Dampf ablassen oder laut nachdenken (Talking Friday, SOUL.AI).",
        "Eine anpassbare Figur, die lokal läuft (Najimi).",
        "Lange Gespräche mit Gedächtnis, wenn du einen Cloud-Dienst akzeptierst (Replika, Pi).",
        "Chatten mit vielen nutzergeschaffenen Figuren (Character AI).",
    ],
    "method": [
        "Am 14. November 2026 haben wir den US-App-Store nach „private ai companion“, „offline ai companion“, „ai friend to talk to“ und „on-device ai chat private“ durchsucht, die acht Apps mit Apples Lookup-Daten zu Name, Preis, Bewertung und Beschreibung nachgeschlagen und auf der App-Store-Seite jeder App das Datenschutzetikett gelesen.",
        "Wir haben die Apps danach sortiert, wie stark Beschreibung und Etikett einen privaten Chat stützen, und dann nach Bewertung. Die Apps auf dem Gerät stehen beim Datenschutz vorn, aber ihre Bewertungen sind zu wenige, um die Qualität zu beurteilen; lies das also als „Datenschutz zuerst“, nicht als „bester Begleiter“.",
        "Funktionen und Datenschutzaussagen stammen nur aus den Einträgen und Etiketten, nicht aus eigenen Tests; Netzwerkmitschnitte haben wir nicht gemacht. Andere Apps aus den Suchen haben wir weggelassen (Kindroid, Solace, Red Angel und andere), damit die Liste bei acht bleibt; Solace etwa nennt im Eintrag die Kontolöschung und sagt nicht, dass Chats auf dem Gerät bleiben. Cora erschien in der Suche im US-App-Store nicht.",
    ],
    "faq": [
        ("Ist Nomi AI privat?",
         "Der Eintrag sagt nicht, dass die KI auf deinem Telefon läuft, und das Datenschutzetikett im App Store listet Daten, die mit dir verknüpft sind, darunter Nutzerinhalte, aber kein Tracking. Die Datenschutzerklärung sagt, wie lange Chats gespeichert bleiben."),
        ("Kann ein KI-Begleiter offline funktionieren?",
         "Ja, wenn das Modell auf dem Telefon liegt. Talking Friday, Najimi und SOUL.AI sagen, dass ihres offline läuft. Apps, die das nicht sagen, etwa Nomi, Pi, Replika, Tolan und Character AI, werden in ihren Einträgen nicht als offline beschrieben."),
        ("Was ist die privateste KI-Freund-App für das iPhone?",
         "Von den acht geprüften diejenigen mit Angaben zur Verarbeitung auf dem Gerät und dem Etikett „Keine Daten erfasst“: Talking Friday, Najimi und SOUL.AI. Sie haben sehr wenige Bewertungen, also probiere sie selbst im Flugzeugmodus aus."),
        ("Was sagt mir das Datenschutzetikett im App Store?",
         "Es ist die eigene Liste des Entwicklers über erfasste Daten, aufgeteilt in zum Tracking genutzt, mit dir verknüpft und nicht mit dir verknüpft. Es sagt nicht, wie lange Chats gespeichert werden."),
    ],
}

# ---------------------------------------------------------------- ja (日本)
TR_JA = {
    "title": "iPhone向けプライベートAIコンパニオンアプリのおすすめ（2026年版）",
    "h1": "iPhone向けプライベートAIコンパニオンアプリのおすすめ（2026年版）",
    "description": "iPhone向けのAIコンパニオン／AIフレンドアプリ8種をプライバシーで比較：端末内かクラウドか、オフラインで使えるか、アカウント、価格、App Storeのプライバシーラベル。2026年11月14日に確認。",
    "llms": "iPhone向けAIコンパニオンアプリ8種（Talking Friday、Najimi、SOUL.AI、Nomi、Pi、Replika、Tolan、Character AI）を、チャットが端末内に残るか、オフライン利用、アカウント、価格、評価、App Storeのプライバシーラベルで比較。各掲載情報の記載内容と、記載がないことを示す。",
    "answer": [
        "チャットが端末内に残るAIコンパニオンを探すなら、確認した8種のうち、App Storeの掲載情報でそう明記しているのは3つだけです。Talking Friday、Najimi、SOUL.AIはAIをiPhone上で動かし、オフラインで使えると説明しており、3つとも「データは収集されません」ラベルがあります。より大きな5つ（Nomi、Pi、Replika、Tolan、Character AI）は評価件数がずっと多いものの、ラベルには自分と紐づくデータの収集が並び、端末上で動くと主張するものはありません。",
        "代償はアプリの規模です。端末内で動くアプリの評価は0〜11件なので品質は実証されておらず、プライバシーラベルも開発者自身の申告です。2026年11月14日に確認し、掲載情報が触れていない箇所には「記載なし」と書いています。",
    ],
    "keep": [0, 1, 2, 3, 4, 5, 7],
    "day": "2026-11-15",
    "columns": ["アプリ", "iPhone上で動作", "オフラインで動作", "アカウント必須", "価格（日本）", "評価（米国）"],
    "table_note": "価格と提供状況は日本のApp Storeの2026年11月15日時点、評価は米国のApp Storeの2026年11月14日時点（米国の評価で、日本の評価ではありません）。その他の列は各アプリの掲載情報の記載内容です。「主張なし」は掲載情報がAIを端末上で動かすと書いていないこと、「記載なし」は何も書いていないことを意味します。Tolanは2026年11月15日時点で日本のApp Storeで販売されていないため、表から外しています。本文は米国のApp Storeで確認した8種についてのものです。評価件数が非常に少ない場合、評価はほとんど参考になりません。",
    "apps": [
        {
            "row": ["はい（掲載情報による。ニューラルエンジン上で音声から音声まで処理）", "はい", "いいえ", "無料。掲載情報によればアプリ内課金なし", "まだ評価なし"],
            "best_for": "端末の外に出ない、プライベートな音声会話。",
            "facts": [
                "掲載情報によると、音声から音声までの処理全体がiPhoneのニューラルエンジン上で動き、サーバー、アカウント、インターネットは不要です。",
                "App Storeのプライバシーラベル：データは収集されません。",
                "話しかけると声で答えます。キャラクターや恋愛のアプリではなく、考えを声に出して整理したり会話の練習に使える音声チャットです。",
                "バージョン1.0、iOS 18.0以降、掲載情報は2026年7月14日更新。",
            ],
            "limits": "評価がまだないため、会話の質についての公的な根拠はありません。音声のみで、iOS 18が必要です。",
        },
        {
            "row": ["はい（掲載情報による。ローカルのAIと音声モデルを同梱）", "はい（掲載情報に「オフラインで動作可能」）", "記載なし", "無料", "4.0（2件の評価）"],
            "best_for": "ローカルで動く、カスタマイズ可能なアバター型コンパニオン。",
            "facts": [
                "掲載情報によると、端末内チャット用のローカル言語モデルと音声モデルを同梱しているため、ダウンロードは通常より大きくなります。",
                "性格、外見、声、背景を変えられ、自分のVRMキャラクターを読み込んだり、文書と一緒にチャットしたりできます。",
                "App Storeのプライバシーラベル：データは収集されません。",
                "バージョン1.1、iOS 18.6以降、2026年8月6日更新。",
            ],
            "limits": "評価は2件のみ。ダウンロードサイズが大きい。アカウントが必要かどうかは掲載情報に記載がありません。",
        },
        {
            "row": ["はい（掲載情報による）", "はい", "いいえ", "無料", "2.5（11件の評価）"],
            "best_for": "新しめのiPhoneで使うシンプルなオフラインチャットモデル。",
            "facts": [
                "掲載情報によると、モデルはアプリ内にあり、完全に端末上で動作し、チャットをクラウドに送信しません。アカウント不要。",
                "App Storeのプライバシーラベル：データは収集されません。",
                "iPhone 15 Pro以降を推奨。古い機種では遅い、またはクラッシュすることがあり、iPhone 12未満は非対応。",
                "バージョン1.7.3、2026年7月10日更新。",
            ],
            "limits": "11人による2.5の評価。性格主導のコンパニオンというより汎用アシスタントに近いものです。",
        },
        {
            "row": ["主張なし", "記載なし", "記載なし", "無料", "4.6（3,029件の評価）"],
            "best_for": "長期的な記憶と関係性のロールプレイ。クラウドサービスを受け入れられる場合に。",
            "facts": [
                "掲載情報は短期・長期の記憶、グループチャット、自撮りやアート生成を強調しており、AIが端末上で動くとは述べていません。",
                "App Storeのプライバシーラベル：自分と紐づくデータ（購入、連絡先情報、ユーザーコンテンツ、識別子、利用データ、診断）。トラッキングは記載されていません。",
                "バージョン1.12.1、iOS 15.0以降、2026年3月31日更新。",
            ],
            "limits": "ユーザーコンテンツがあなたと紐づくものとしてラベルに記載されているため、チャットは企業が保存すると想定してください。保存期間はプライバシーポリシーで確認を。",
        },
        {
            "name": "Pi, your personal AI",
            "row": ["主張なし", "記載なし", "記載なし", "無料", "4.4（2,555件の評価）"],
            "best_for": "話して考えを整理できる落ち着いたアシスタント（音声モード付き）。",
            "facts": [
                "掲載情報は、話して考えを整理すること、音声モード、用事を進めることを説明しており、AIがどこで動くかは書いていません。",
                "App Storeのプライバシーラベル：自分と紐づくデータ（識別子、利用データ、診断）を分析、パーソナライズ、アプリの機能のために。トラッキングの記載なし。",
                "バージョン26.1109.0（2026年11月13日）、iOS 16以降。",
            ],
            "limits": "端末上・オフラインの主張はありません。ラベルにユーザーコンテンツの区分はありませんが、チャットの保存方法はラベルではわかりません。",
        },
        {
            "name": "Replika: 世界初のA Iフレンド・人工知能との会話",
            "row": ["主張なし", "記載なし", "記載なし", "無料", "4.4（227,667件の評価）"],
            "best_for": "通話と自発的なチェックインがある、長く続くコンパニオン。",
            "facts": [
                "掲載情報はテキスト、音声、ビデオ通話、インターネットアクセス、アプリ連携、画像生成を説明し、あなたの大切な人や予定を覚えると述べています。",
                "App Storeのプライバシーラベル：トラッキングに使われるデータ（識別子、利用データ）、自分と紐づくデータ（位置情報、連絡先情報、識別子、利用データ）、一部の自分と紐づかない診断データ。",
                "バージョン12.5.2（2026年11月5日）、iOS 17.0以降。",
            ],
            "limits": "ラベルにはトラッキングデータと位置情報が含まれ、掲載情報はインターネットが必要な機能を説明しています。",
        },
        {
            "row": ["主張なし", "記載なし", "記載なし", "無料", "4.3（561,523件の評価）"],
            "best_for": "ユーザー作成のキャラクターが何百万も。プライバシーを最優先しない場合に。",
            "facts": [
                "掲載情報は、膨大なユーザー作成キャラクターのライブラリとのチャットや通話、自分のキャラクターを作ってコミュニティと共有できることを説明しています。",
                "App Storeのプライバシーラベル：トラッキングに使われるデータ（位置情報、連絡先情報、識別子、利用データ）、自分と紐づくデータ（購入、金融情報、位置情報、連絡先情報、ユーザーコンテンツ、検索履歴、識別子、利用データ、診断）。",
                "バージョン1.17.4（2026年10月2日）、iOS 15.1以降。",
            ],
            "limits": "8種の中で最も長いデータリスト（金融情報、ユーザーコンテンツ、検索履歴があなたと紐づく）。共有とコミュニティ中心の設計。",
        },
    ],
    "who": [
        "<strong>端末の外に出ないチャットがほしい：</strong> Talking Friday（音声）、Najimi（アバター）、SOUL.AI（シンプルなチャット）。",
        "<strong>実績ある品質がほしく、クラウドサービスも受け入れられる：</strong> Nomi、Pi、Replika。上記のラベルの制限付き。",
        "<strong>大手アプリの中で収集されるデータを最小にしたい：</strong> NomiとPiはトラッキングを記載していません。ReplikaとCharacter AIは記載しています。",
        "<strong>飛行機内や電波がない場所で使いたい：</strong> Talking Friday、Najimi、SOUL.AI。",
    ],
    "cases": [
        "アカウントなしで夜に愚痴を言ったり、声に出して考えたりする（Talking Friday、SOUL.AI）。",
        "ローカルで動くカスタマイズ可能なキャラクター（Najimi）。",
        "クラウドサービスを受け入れた上での、記憶のある長い会話（Nomi、Replika、Pi）。",
        "多数のユーザー作成キャラクターとのチャット（Character AI）。",
    ],
    "method": [
        "2026年11月14日に米国App Storeで「private ai companion」「offline ai companion」「ai friend to talk to」「on-device ai chat private」を検索し、8種のアプリについてAppleのルックアップデータで名前、価格、評価、説明を確認し、各アプリのApp Storeページでプライバシーラベルを読みました。",
        "私たちは、掲載情報とラベルがプライベートなチャットをどの程度支えるかで並べ、次に評価で並べました。端末上で動くアプリはプライバシーで先頭ですが、評価件数が少なく品質は判断できません。「最良のコンパニオン」ではなく「まずプライバシー」として読んでください。",
        "機能とプライバシーの記述はアプリの掲載情報とラベルのみから取っており、自分たちのテストによるものではありません。ネットワークのキャプチャは行っていません。検索に出た他のアプリ（Kindroid、Solace、Red Angelなど）は8種に絞るため除外しました。例えばSolaceの掲載情報はアカウント削除に触れ、チャットが端末内に残るとは書いていません。Coraは米国App Storeの検索に出ませんでした。",
    ],
    "faq": [
        ("Nomi AIはプライベートですか？",
         "掲載情報はAIがスマホ上で動くとは述べておらず、App Storeのプライバシーラベルはユーザーコンテンツを含む自分と紐づくデータを挙げていますが、トラッキングは挙げていません。チャットの保存期間はプライバシーポリシーをご確認ください。"),
        ("AIコンパニオンはオフラインで使えますか？",
         "モデルが端末内にあれば使えます。Talking Friday、Najimi、SOUL.AIは、オフラインで動作すると述べています。そう述べていないアプリ（Nomi、Pi、Replika、Tolan、Character AIなど）は、掲載情報でオフライン対応とは説明されていません。"),
        ("iPhoneで最もプライベートなAIフレンドアプリは？",
         "確認した8種のうち、端末上での処理の記載があり、ラベルが「データは収集されません」のもの：Talking Friday、Najimi、SOUL.AI。評価件数が非常に少ないため、機内モードで自分で試してください。"),
        ("App Storeのプライバシーラベルは何を示しますか？",
         "開発者自身が申告した収集データの一覧で、トラッキングに使用、自分と紐づく、紐づかないに分かれています。チャットがどのくらい保存されるかは示しません。"),
    ],
}

# ---------------------------------------------------------------- es (España)
TR_ES = {
    "title": "Las mejores apps de compañero de IA privado para iPhone (2026)",
    "h1": "Las mejores apps de compañero de IA privado para iPhone (2026)",
    "description": "Ocho apps de compañero de IA y de amigo IA para iPhone, comparadas por privacidad: en el dispositivo o en la nube, funcionan sin conexión, cuenta, precio y etiqueta de privacidad de la App Store. Revisado el 14 de noviembre de 2026.",
    "llms": "Compara ocho apps de compañero de IA para iPhone (Talking Friday, Najimi, SOUL.AI, Nomi, Pi, Replika, Tolan, Character AI) según si los chats se quedan en el teléfono, si funcionan sin conexión, si piden cuenta, precio, valoración y etiqueta de privacidad de la App Store. Indica lo que dice cada ficha y lo que no dice.",
    "answer": [
        "Si quieres un compañero de IA cuyos chats se queden en tu teléfono, solo tres de las ocho apps que revisamos lo dicen en su ficha de la App Store: Talking Friday, Najimi y SOUL.AI ejecutan la IA en el iPhone y dicen que funciona sin conexión, y las tres tienen la etiqueta «No se recopilan datos». Las cinco apps más grandes (Nomi, Pi, Replika, Tolan, Character AI) tienen muchas más valoraciones, pero sus etiquetas listan datos recopilados vinculados a ti, y ninguna afirma que funcione en el dispositivo.",
        "La contrapartida es el tamaño: las apps en el dispositivo tienen entre 0 y 11 valoraciones, así que su calidad no está demostrada, y una etiqueta de privacidad es una declaración del propio desarrollador. Revisamos el 14 de noviembre de 2026 y escribimos «No indicado» siempre que una ficha calla.",
    ],
    "keep": [0, 1, 2, 4, 5, 6, 7],
    "day": "2026-11-15",
    "columns": ["App", "Funciona en el iPhone", "Funciona sin conexión", "Requiere cuenta", "Precio (España)", "Valoración (EE. UU.)"],
    "table_note": "Precio y disponibilidad: App Store de España el 15 de noviembre de 2026. Valoración: App Store de EE. UU. el 14 de noviembre de 2026 (son valoraciones estadounidenses, no españolas). Las demás columnas son lo que dice la ficha de cada app; «No declarado» significa que la ficha no afirma que la IA funcione en el dispositivo, y «No indicado» que no dice nada. Nomi no está a la venta en el App Store de España el 15 de noviembre de 2026, así que no aparece en la tabla; los textos se refieren a las ocho apps que revisamos en el App Store de EE. UU. Una valoración con muy pocos votos dice poco.",
    "apps": [
        {
            "row": ["Sí, según la ficha (conversación de voz a voz en el Neural Engine)", "Sí", "No", "Gratis; sin compras dentro de la app, según la ficha", "Aún sin valoraciones"],
            "best_for": "conversaciones de voz privadas que nunca salen del teléfono.",
            "facts": [
                "Según la ficha, todo el ciclo de voz a voz funciona en el Neural Engine del iPhone, sin servidores, sin cuenta y sin internet.",
                "Etiqueta de privacidad de la App Store: No se recopilan datos.",
                "Hablas y responde en voz alta; no es una app de personajes ni de romance, sino un chat de voz para pensar en voz alta o practicar conversaciones.",
                "Versión 1.0, iOS 18.0 o posterior, ficha actualizada el 14 de julio de 2026.",
            ],
            "limits": "aún sin valoraciones, así que no hay pruebas públicas de lo buenas que son las conversaciones; solo voz, y requiere iOS 18.",
        },
        {
            "row": ["Sí, según la ficha (modelos locales de IA y de voz incluidos)", "Sí, según la ficha («puede funcionar sin conexión»)", "No indicado", "Gratis", "4.0 (2 valoraciones)"],
            "best_for": "un compañero con avatar personalizable que funciona en local.",
            "facts": [
                "La ficha dice que incluye un modelo de lenguaje y un modelo de voz locales para chatear en el dispositivo, así que la descarga es más grande de lo habitual.",
                "Puedes cambiar personalidad, apariencia, voz y fondo, importar tu propio personaje VRM y chatear con documentos.",
                "Etiqueta de privacidad de la App Store: No se recopilan datos.",
                "Versión 1.1, iOS 18.6 o posterior, actualizada el 6 de agosto de 2026.",
            ],
            "limits": "solo 2 valoraciones; descarga grande; la ficha no dice si hace falta cuenta.",
        },
        {
            "row": ["Sí, según la ficha", "Sí", "No", "Gratis", "2.5 (11 valoraciones)"],
            "best_for": "un modelo de chat sin conexión sencillo en un iPhone reciente.",
            "facts": [
                "La ficha dice que el modelo está dentro de la app, funciona por completo en el dispositivo y no envía chats a la nube; no hace falta cuenta.",
                "Etiqueta de privacidad de la App Store: No se recopilan datos.",
                "Recomienda iPhone 15 Pro o posterior; los dispositivos antiguos pueden ir lentos o cerrarse, y los anteriores al iPhone 12 no son compatibles.",
                "Versión 1.7.3, actualizada el 10 de julio de 2026.",
            ],
            "limits": "una valoración de 2.5 de 11 personas, y es más un asistente general que un compañero con personalidad.",
        },
        {
            "name": "Pi: Talk to Your AI Friend",
            "row": ["No declarado", "No indicado", "No indicado", "Gratis", "4.4 (2,555 valoraciones)"],
            "best_for": "un asistente tranquilo para hablar de lo que te preocupa, con modo de voz.",
            "facts": [
                "La ficha describe hablar de las cosas, el modo de voz y hacer gestiones; no dice dónde se ejecuta la IA.",
                "Etiqueta de privacidad de la App Store: datos vinculados a ti (identificadores, datos de uso, diagnósticos), para analítica, personalización y funcionalidad de la app. No se indica rastreo.",
                "Versión 26.1109.0 (13 nov. 2026), iOS 16 o posterior.",
            ],
            "limits": "no declara funcionamiento en el dispositivo ni sin conexión; la etiqueta no tiene categoría de contenido del usuario, pero no dice cómo se guardan los chats.",
        },
        {
            "row": ["No declarado", "No indicado", "No indicado", "Gratis", "4.4 (227,667 valoraciones)"],
            "best_for": "un compañero de larga duración con llamadas y mensajes proactivos.",
            "facts": [
                "La ficha describe llamadas de texto, voz y vídeo, acceso a internet, integraciones con apps y generación de imágenes, y dice que recuerda a tus personas y planes.",
                "Etiqueta de privacidad de la App Store: datos usados para rastreo (identificadores, datos de uso); datos vinculados a ti (ubicación, información de contacto, identificadores, datos de uso); y algunos diagnósticos no vinculados a ti.",
                "Versión 12.5.2 (5 nov. 2026), iOS 17.0 o posterior.",
            ],
            "limits": "su etiqueta incluye datos de rastreo y ubicación, y la ficha describe funciones que necesitan internet.",
        },
        {
            "row": ["No declarado", "No indicado", "No indicado", "Gratis", "4.8 (190,859 valoraciones)"],
            "best_for": "un compañero amigable de estilo alienígena con quien hablar de cualquier tema.",
            "facts": [
                "La ficha es breve: hablar de intereses, sentimientos y pensamientos, compartir fotos y diseñar un planeta juntos. No dice nada sobre dónde se ejecuta la IA.",
                "Etiqueta de privacidad de la App Store: datos usados para rastreo (compras, ubicación, información de contacto, identificadores, datos de uso, otros datos); datos vinculados a ti (incluido el contenido del usuario); y más datos no vinculados a ti.",
                "Versión 26.46.1 (11 nov. 2026), iOS 18.0 o posterior.",
            ],
            "limits": "la etiqueta enumera rastreo y ubicación, y el contenido del usuario como vinculado a ti; la ficha no ofrece afirmaciones de privacidad.",
        },
        {
            "row": ["No declarado", "No indicado", "No indicado", "Gratis", "4.3 (561,523 valoraciones)"],
            "best_for": "millones de personajes creados por usuarios, si la privacidad no es tu primera preocupación.",
            "facts": [
                "La ficha describe chatear y llamar con una enorme biblioteca de personajes creados por usuarios, además de crear los tuyos y compartirlos con la comunidad.",
                "Etiqueta de privacidad de la App Store: datos usados para rastreo (ubicación, información de contacto, identificadores, datos de uso); datos vinculados a ti (compras, información financiera, ubicación, información de contacto, contenido del usuario, historial de búsqueda, identificadores, datos de uso, diagnósticos).",
                "Versión 1.17.4 (2 oct. 2026), iOS 15.1 o posterior.",
            ],
            "limits": "la lista de datos más larga de las ocho, con información financiera, contenido del usuario e historial de búsqueda vinculados a ti, y un diseño centrado en compartir con la comunidad.",
        },
    ],
    "who": [
        "<strong>Quieres chats que nunca salgan del teléfono:</strong> Talking Friday (voz), Najimi (avatar) o SOUL.AI (chat sencillo).",
        "<strong>Quieres calidad probada y aceptas un servicio en la nube:</strong> Pi, Replika o Tolan, con los límites de etiqueta de arriba.",
        "<strong>Quieres que se recopilen los menos datos entre las apps grandes:</strong> Pi no declara rastreo; Replika, Tolan y Character AI sí.",
        "<strong>Quieres usarlo en un avión o sin cobertura:</strong> Talking Friday, Najimi o SOUL.AI.",
    ],
    "cases": [
        "Desahogarte o pensar en voz alta por la noche sin cuenta (Talking Friday, SOUL.AI).",
        "Un personaje que puedes personalizar y que funciona en local (Najimi).",
        "Conversaciones largas con memoria, aceptando un servicio en la nube (Replika, Pi).",
        "Chatear con muchos personajes creados por usuarios (Character AI).",
    ],
    "method": [
        "El 14 de noviembre de 2026 buscamos en el App Store de EE. UU. «private ai companion», «offline ai companion», «ai friend to talk to» y «on-device ai chat private», consultamos los datos de búsqueda de Apple de las ocho apps (nombre, precio, valoración y descripción) y leímos en la página de cada app su etiqueta de privacidad.",
        "Ordenamos las apps según cuánto respaldan la descripción y la etiqueta un chat privado, y luego por valoración. Las apps en el dispositivo van primero en privacidad, pero tienen muy pocas valoraciones para juzgar su calidad; léelo como «privacidad primero», no como «mejor compañero».",
        "Las funciones y declaraciones de privacidad salen solo de las fichas y etiquetas, no de nuestras pruebas; no hicimos capturas de red. Dejamos fuera otras apps que aparecieron en las búsquedas (Kindroid, Solace, Red Angel y otras) para mantener la lista en ocho; la ficha de Solace, por ejemplo, menciona el borrado de cuenta y no dice que los chats se queden en el dispositivo. Cora no apareció en la búsqueda del App Store de EE. UU.",
    ],
    "faq": [
        ("¿Es privada Nomi AI?",
         "Su ficha no dice que la IA funcione en tu teléfono, y su etiqueta de privacidad de la App Store lista datos vinculados a ti, incluido el contenido del usuario, pero no rastreo. Lee su política de privacidad para saber cuánto tiempo se guardan los chats."),
        ("¿Puede un compañero de IA funcionar sin conexión?",
         "Sí, si el modelo está en el teléfono. Talking Friday, Najimi y SOUL.AI dicen que el suyo funciona sin conexión. Las apps que no lo dicen, como Nomi, Pi, Replika, Tolan y Character AI, no se describen como sin conexión en sus fichas."),
        ("¿Cuál es la app de amigo IA más privada para iPhone?",
         "De las ocho que revisamos, las que declaran funcionamiento en el dispositivo y tienen la etiqueta «No se recopilan datos»: Talking Friday, Najimi y SOUL.AI. Tienen muy pocas valoraciones, así que pruébalas tú mismo en modo avión."),
        ("¿Qué me dice la etiqueta de privacidad de la App Store?",
         "Es la lista propia del desarrollador de los datos recopilados, dividida en usados para rastreo, vinculados a ti y no vinculados a ti. No dice cuánto tiempo se guardan los chats."),
    ],
}

# ---------------------------------------------------------------- pt-BR (Brasil)
TR_PTBR = {
    "title": "Melhores apps de companheiro de IA privado para iPhone (2026)",
    "h1": "Melhores apps de companheiro de IA privado para iPhone (2026)",
    "description": "Oito apps de companheiro de IA e amigo de IA para iPhone comparados por privacidade: no aparelho ou na nuvem, funciona offline, conta, preço e rótulo de privacidade da App Store. Verificado em 14 de novembro de 2026.",
    "llms": "Compara oito apps de companheiro de IA para iPhone (Talking Friday, Najimi, SOUL.AI, Nomi, Pi, Replika, Tolan, Character AI) por se os chats ficam no celular, se funcionam offline, se pedem conta, preço, avaliação e rótulo de privacidade da App Store. Diz o que cada ficha afirma e o que não afirma.",
    "answer": [
        "Se você quer um companheiro de IA cujos chats fiquem no celular, só três das oito apps que verificamos dizem isso na ficha da App Store: Talking Friday, Najimi e SOUL.AI rodam a IA no iPhone e dizem que funcionam offline, e as três têm o rótulo «Nenhum dado coletado». As cinco maiores (Nomi, Pi, Replika, Tolan, Character AI) têm muito mais avaliações, mas os rótulos listam dados coletados vinculados a você, e nenhuma afirma rodar no aparelho.",
        "O custo é o tamanho: os apps no aparelho têm de 0 a 11 avaliações, então a qualidade deles não está comprovada, e um rótulo de privacidade é uma declaração do próprio desenvolvedor. Verificamos em 14 de novembro de 2026 e escrevemos «Não informado» sempre que uma ficha não diz nada.",
    ],
    "keep": [0, 1, 2, 3, 4, 5, 7],
    "day": "2026-11-15",
    "columns": ["App", "Roda no iPhone", "Funciona offline", "Exige conta", "Preço (Brasil)", "Avaliação (EUA)"],
    "table_note": "Preço e disponibilidade: App Store do Brasil em 15 de novembro de 2026. Avaliação: App Store dos EUA em 14 de novembro de 2026 (avaliações americanas, não brasileiras). As demais colunas são o que a ficha de cada app diz; «Não afirmado» quer dizer que a ficha não diz que a IA roda no aparelho, e «Não informado», que ela não diz nada. Tolan não está à venda na App Store do Brasil em 15 de novembro de 2026, então não aparece na tabela; os textos se referem às oito apps que verificamos na App Store dos EUA. Uma avaliação com poucos votos diz pouco.",
    "apps": [
        {
            "row": ["Sim, segundo a ficha (conversa de voz para voz no Neural Engine)", "Sim", "Não", "Grátis; sem compras no app, segundo a ficha", "Ainda sem avaliações"],
            "best_for": "conversas de voz privadas que nunca saem do celular.",
            "facts": [
                "Segundo a ficha, todo o ciclo de voz para voz roda no Neural Engine do iPhone, sem servidores, sem conta e sem internet.",
                "Rótulo de privacidade da App Store: Nenhum dado coletado.",
                "Você fala e ele responde em voz alta; não é um app de personagens ou romance, e sim um chat de voz para pensar em voz alta ou treinar conversas.",
                "Versão 1.0, iOS 18.0 ou mais recente, ficha atualizada em 14 de julho de 2026.",
            ],
            "limits": "ainda sem avaliações, então não há prova pública da qualidade das conversas; só voz, e exige iOS 18.",
        },
        {
            "row": ["Sim, segundo a ficha (modelos locais de IA e de voz incluídos)", "Sim, segundo a ficha («pode funcionar offline»)", "Não informado", "Grátis", "4.0 (2 avaliações)"],
            "best_for": "um companheiro com avatar personalizável que roda localmente.",
            "facts": [
                "A ficha diz que inclui um modelo de linguagem local e um modelo de voz para conversar no aparelho, então o download é maior que o normal.",
                "Você pode mudar personalidade, aparência, voz e fundo, importar seu próprio personagem VRM e conversar com documentos.",
                "Rótulo de privacidade da App Store: Nenhum dado coletado.",
                "Versão 1.1, iOS 18.6 ou mais recente, atualizada em 6 de agosto de 2026.",
            ],
            "limits": "só 2 avaliações; download grande; a ficha não diz se é preciso conta.",
        },
        {
            "row": ["Sim, segundo a ficha", "Sim", "Não", "Grátis", "2.5 (11 avaliações)"],
            "best_for": "um modelo de chat offline simples em um iPhone recente.",
            "facts": [
                "A ficha diz que o modelo fica dentro do app, roda inteiramente no aparelho e não envia conversas para a nuvem; sem conta.",
                "Rótulo de privacidade da App Store: Nenhum dado coletado.",
                "Recomenda iPhone 15 Pro ou mais recente; aparelhos antigos podem ficar lentos ou travar, e os anteriores ao iPhone 12 não são compatíveis.",
                "Versão 1.7.3, atualizada em 10 de julho de 2026.",
            ],
            "limits": "nota 2.5 de 11 pessoas; e é mais um assistente geral do que um companheiro com personalidade.",
        },
        {
            "row": ["Não afirmado", "Não informado", "Não informado", "Grátis", "4.6 (3,029 avaliações)"],
            "best_for": "memória de longo prazo e roleplay de relacionamento, se você aceita um serviço na nuvem.",
            "facts": [
                "A ficha destaca memória de curto e longo prazo, conversas em grupo, selfies e geração de arte, e não diz que a IA roda no aparelho.",
                "Rótulo de privacidade da App Store: Dados vinculados a você (compras, informações de contato, conteúdo do usuário, identificadores, dados de uso, diagnósticos). Não lista rastreamento.",
                "Versão 1.12.1, iOS 15.0 ou mais recente, atualizada em 31 de março de 2026.",
            ],
            "limits": "o conteúdo do usuário aparece no rótulo como vinculado a você, então considere que a empresa armazena as conversas; leia a política de privacidade para saber por quanto tempo. Isso responde à pergunta comum «o Nomi AI é privado?»: o rótulo diz que os dados estão vinculados a você e a ficha não faz nenhuma afirmação sobre o aparelho.",
        },
        {
            "name": "Pi, your personal AI",
            "row": ["Não afirmado", "Não informado", "Não informado", "Grátis", "4.4 (2,555 avaliações)"],
            "best_for": "um assistente calmo para conversar sobre o que você está pensando, com modo de voz.",
            "facts": [
                "A ficha descreve conversar sobre as coisas, o modo de voz e resolver tarefas; não diz onde a IA roda.",
                "Rótulo de privacidade da App Store: Dados vinculados a você (identificadores, dados de uso, diagnósticos), para análise, personalização e funcionalidade do app. Nenhum rastreamento listado.",
                "Versão 26.1109.0 (13 de nov. de 2026), iOS 16 ou mais recente.",
            ],
            "limits": "nenhuma afirmação de aparelho ou offline; o rótulo não tem categoria de conteúdo do usuário, mas não diz como os chats são guardados.",
        },
        {
            "row": ["Não afirmado", "Não informado", "Não informado", "Grátis", "4.4 (227,667 avaliações)"],
            "best_for": "um companheiro de longa duração com chamadas e check-ins proativos.",
            "facts": [
                "A ficha descreve chamadas de texto, voz e vídeo, acesso à internet, integrações com apps e geração de imagens, e diz que ele lembra das suas pessoas e planos.",
                "Rótulo de privacidade da App Store: Dados usados para rastreamento (identificadores, dados de uso); Dados vinculados a você (localização, informações de contato, identificadores, dados de uso); e alguns diagnósticos não vinculados a você.",
                "Versão 12.5.2 (5 de nov. de 2026), iOS 17.0 ou mais recente.",
            ],
            "limits": "o rótulo inclui dados de rastreamento e localização, e a ficha descreve recursos que precisam de internet.",
        },
        {
            "row": ["Não afirmado", "Não informado", "Não informado", "Grátis", "4.3 (561,523 avaliações)"],
            "best_for": "milhões de personagens criados por usuários, se a privacidade não é sua principal preocupação.",
            "facts": [
                "A ficha descreve conversar e ligar com uma enorme biblioteca de personagens criados por usuários, além de criar os seus e compartilhá-los com a comunidade.",
                "Rótulo de privacidade da App Store: Dados usados para rastreamento (localização, informações de contato, identificadores, dados de uso); Dados vinculados a você (compras, informações financeiras, localização, informações de contato, conteúdo do usuário, histórico de pesquisa, identificadores, dados de uso, diagnósticos).",
                "Versão 1.17.4 (2 de out. de 2026), iOS 15.1 ou mais recente.",
            ],
            "limits": "a lista de dados mais longa das oito, com informações financeiras, conteúdo do usuário e histórico de pesquisa vinculados a você, e um desenho voltado a compartilhamento e comunidade.",
        },
    ],
    "who": [
        "<strong>Você quer chats que nunca saiam do celular:</strong> Talking Friday (voz), Najimi (avatar) ou SOUL.AI (chat simples).",
        "<strong>Você quer qualidade comprovada e aceita um serviço na nuvem:</strong> Nomi, Pi ou Replika, com os limites de rótulo acima.",
        "<strong>Você quer o menor volume de dados entre os apps grandes:</strong> Nomi e Pi não listam rastreamento; Replika e Character AI listam.",
        "<strong>Você quer usar em um avião ou sem sinal:</strong> Talking Friday, Najimi ou SOUL.AI.",
    ],
    "cases": [
        "Desabafar ou pensar em voz alta à noite, sem conta (Talking Friday, SOUL.AI).",
        "Um personagem que você pode personalizar e que roda localmente (Najimi).",
        "Conversas longas com memória, aceitando um serviço na nuvem (Nomi, Replika, Pi).",
        "Conversar com muitos personagens criados por usuários (Character AI).",
    ],
    "method": [
        "Em 14 de novembro de 2026 pesquisamos na App Store dos EUA por «private ai companion», «offline ai companion», «ai friend to talk to» e «on-device ai chat private», consultamos os dados de busca da Apple das oito apps (nome, preço, avaliação e descrição) e lemos o rótulo de privacidade na página de cada app.",
        "Ordenamos as apps pelo quanto a ficha e o rótulo sustentam um chat privado e, depois, pela avaliação. As apps no aparelho vêm primeiro em privacidade, mas têm avaliações insuficientes para julgar a qualidade; leia isso como «privacidade primeiro», não como «melhor companheiro».",
        "Funções e declarações de privacidade vêm só das fichas e rótulos, não de testes nossos; não fizemos capturas de rede. Deixamos de fora outros apps que apareceram nas buscas (Kindroid, Solace, Red Angel e outros) para manter a lista em oito; a ficha da Solace, por exemplo, menciona exclusão de conta e não diz que os chats ficam no aparelho. A Cora não apareceu na busca da App Store dos EUA.",
    ],
    "faq": [
        ("O Nomi AI é privado?",
         "A ficha não diz que a IA roda no seu celular, e o rótulo de privacidade da App Store lista dados vinculados a você, incluindo conteúdo do usuário, mas nenhum rastreamento. Leia a política de privacidade para saber por quanto tempo os chats são guardados."),
        ("Um companheiro de IA pode funcionar offline?",
         "Sim, se o modelo estiver no celular. Talking Friday, Najimi e SOUL.AI dizem que o deles funciona offline. Apps que não dizem isso, como Nomi, Pi, Replika, Tolan e Character AI, não são descritas como offline nas fichas."),
        ("Qual é o app de amigo de IA mais privado para iPhone?",
         "Entre as oito verificadas, os que têm afirmações de funcionamento no aparelho e o rótulo Nenhum dado coletado: Talking Friday, Najimi e SOUL.AI. Têm pouquíssimas avaliações, então teste você mesmo no modo avião."),
        ("O que o rótulo de privacidade da App Store me diz?",
         "É a lista do próprio desenvolvedor sobre os dados coletados, dividida em usados para rastreamento, vinculados a você e não vinculados a você. Não diz por quanto tempo os chats são armazenados."),
    ],
}

# ---------------------------------------------------------------- fr (France)
TR_FR = {
    "title": "Meilleures applis de compagnon IA privé pour iPhone (2026)",
    "h1": "Meilleures applis de compagnon IA privé pour iPhone (2026)",
    "description": "Huit applis de compagnon IA et d'ami IA pour iPhone comparées sur la confidentialité : sur l'appareil ou dans le cloud, fonctionnement hors ligne, compte, prix et étiquette de confidentialité de l'App Store. Vérifié le 14 novembre 2026.",
    "llms": "Compare huit applis de compagnon IA pour iPhone (Talking Friday, Najimi, SOUL.AI, Nomi, Pi, Replika, Tolan, Character AI) selon que les discussions restent sur le téléphone, le fonctionnement hors ligne, la création de compte, le prix, la note et l'étiquette de confidentialité de l'App Store. Indique ce que dit chaque fiche et ce qu'elle ne dit pas.",
    "answer": [
        "Si vous voulez un compagnon IA dont les discussions restent sur votre téléphone, seules trois des huit applis vérifiées le disent dans leur fiche App Store : Talking Friday, Najimi et SOUL.AI exécutent l'IA sur l'iPhone et disent qu'elle fonctionne hors ligne, et les trois portent l'étiquette « Aucune donnée collectée ». Les cinq plus grandes (Nomi, Pi, Replika, Tolan, Character AI) ont beaucoup plus de notes, mais leurs étiquettes listent des données collectées liées à vous, et aucune ne prétend fonctionner sur l'appareil.",
        "Le revers est la taille : les applis sur l'appareil ont de 0 à 11 notes, donc leur qualité n'est pas démontrée, et une étiquette de confidentialité est la déclaration du développeur lui-même. Nous avons vérifié le 14 novembre 2026 et écrit « Non indiqué » partout où une fiche se tait.",
    ],
    "keep": [0, 1, 2, 4, 5, 6, 7],
    "day": "2026-11-15",
    "columns": ["Application", "Fonctionne sur l'iPhone", "Fonctionne hors ligne", "Compte requis", "Prix (France)", "Note (États-Unis)"],
    "table_note": "Prix et disponibilité : App Store France le 15 novembre 2026. Note : App Store États-Unis le 14 novembre 2026 (notes américaines, pas françaises). Les autres colonnes reprennent ce que dit la fiche de chaque appli ; « Non revendiqué » signifie que la fiche ne dit pas que l'IA tourne sur l'appareil, et « Non indiqué » qu'elle ne dit rien. Nomi n'est pas disponible à la vente sur l'App Store France le 15 novembre 2026 ; elle n'apparaît donc pas dans le tableau, et les textes portent sur les huit applis vérifiées sur l'App Store américain. Une note avec très peu de votes dit peu de choses.",
    "apps": [
        {
            "row": ["Oui, selon la fiche (conversation voix à voix sur le Neural Engine)", "Oui", "Non", "Gratuite ; pas d'achats intégrés selon la fiche", "Pas encore de notes"],
            "best_for": "des conversations vocales privées qui ne quittent jamais le téléphone.",
            "facts": [
                "Selon la fiche, toute la boucle voix à voix tourne sur le Neural Engine de l'iPhone, sans serveur, sans compte et sans internet.",
                "Étiquette de confidentialité de l'App Store : Aucune donnée collectée.",
                "Vous parlez, elle répond à voix haute ; ce n'est pas une appli de personnages ou de romance, mais un chat vocal pour réfléchir à voix haute ou s'entraîner à la conversation.",
                "Version 1.0, iOS 18.0 ou ultérieur, fiche mise à jour le 14 juillet 2026.",
            ],
            "limits": "pas encore de notes, donc aucune preuve publique de la qualité des conversations ; voix uniquement, et iOS 18 requis.",
        },
        {
            "row": ["Oui, selon la fiche (modèles locaux d'IA et de voix inclus)", "Oui, selon la fiche (« peut fonctionner hors ligne »)", "Non indiqué", "Gratuite", "4.0 (2 notes)"],
            "best_for": "un compagnon avatar personnalisable qui tourne en local.",
            "facts": [
                "La fiche indique qu'elle embarque un modèle de langage local et un modèle de voix pour discuter sur l'appareil, donc le téléchargement est plus lourd que d'habitude.",
                "Vous pouvez changer la personnalité, l'apparence, la voix et le fond, importer votre propre personnage VRM et discuter avec des documents.",
                "Étiquette de confidentialité de l'App Store : Aucune donnée collectée.",
                "Version 1.1, iOS 18.6 ou ultérieur, mise à jour le 6 août 2026.",
            ],
            "limits": "seulement 2 notes ; téléchargement lourd ; la fiche ne dit pas si un compte est nécessaire.",
        },
        {
            "row": ["Oui, selon la fiche", "Oui", "Non", "Gratuite", "2.5 (11 notes)"],
            "best_for": "un modèle de discussion hors ligne simple sur un iPhone récent.",
            "facts": [
                "La fiche indique que le modèle est dans l'appli, tourne entièrement sur l'appareil et n'envoie aucune discussion dans le cloud ; pas de compte.",
                "Étiquette de confidentialité de l'App Store : Aucune donnée collectée.",
                "Elle recommande un iPhone 15 Pro ou plus récent ; les appareils plus anciens peuvent être lents ou planter, et ceux en dessous de l'iPhone 12 ne sont pas pris en charge.",
                "Version 1.7.3, mise à jour le 10 juillet 2026.",
            ],
            "limits": "une note de 2.5 donnée par 11 personnes, et c'est un assistant généraliste plutôt qu'un compagnon à personnalité.",
        },
        {
            "name": "Pi, your personal AI",
            "row": ["Non revendiqué", "Non indiqué", "Non indiqué", "Gratuite", "4.4 (2,555 notes)"],
            "best_for": "un assistant calme pour parler de ce qui vous préoccupe, avec mode voix.",
            "facts": [
                "La fiche décrit le fait d'en parler, le mode voix et l'aide pour avancer ; elle ne dit pas où l'IA tourne.",
                "Étiquette de confidentialité de l'App Store : données liées à vous (identifiants, données d'utilisation, diagnostics), pour l'analyse, la personnalisation et le fonctionnement de l'appli. Aucun suivi listé.",
                "Version 26.1109.0 (13 nov. 2026), iOS 16 ou ultérieur.",
            ],
            "limits": "aucune revendication sur l'appareil ou le hors ligne ; l'étiquette n'a pas de catégorie de contenu utilisateur, mais elle ne dit pas comment les discussions sont conservées.",
        },
        {
            "name": "Replika - IA Companion Chat",
            "row": ["Non revendiqué", "Non indiqué", "Non indiqué", "Gratuite", "4.4 (227,667 notes)"],
            "best_for": "un compagnon de longue durée avec appels et contacts proactifs.",
            "facts": [
                "La fiche décrit les appels texte, voix et vidéo, l'accès à internet, les intégrations d'applis et la génération d'images, et dit qu'il se souvient de vos proches et de vos projets.",
                "Étiquette de confidentialité de l'App Store : données utilisées pour le suivi (identifiants, données d'utilisation) ; données liées à vous (localisation, coordonnées, identifiants, données d'utilisation) ; et certains diagnostics non liés à vous.",
                "Version 12.5.2 (5 nov. 2026), iOS 17.0 ou ultérieur.",
            ],
            "limits": "son étiquette inclut des données de suivi et de localisation, et la fiche décrit des fonctions qui nécessitent internet.",
        },
        {
            "row": ["Non revendiqué", "Non indiqué", "Non indiqué", "Gratuite", "4.8 (190,859 notes)"],
            "best_for": "un compagnon amical au style extraterrestre avec qui parler de tout.",
            "facts": [
                "La fiche est brève : parler de vos centres d'intérêt, de vos sentiments et de vos idées, partager des photos et concevoir une planète ensemble. Elle ne dit rien sur l'endroit où tourne l'IA.",
                "Étiquette de confidentialité de l'App Store : données utilisées pour le suivi (achats, localisation, coordonnées, identifiants, données d'utilisation, autres données) ; données liées à vous (dont le contenu utilisateur) ; et d'autres données non liées à vous.",
                "Version 26.46.1 (11 nov. 2026), iOS 18.0 ou ultérieur.",
            ],
            "limits": "l'étiquette liste le suivi et la localisation, ainsi que le contenu utilisateur comme lié à vous ; la fiche ne donne aucune garantie de confidentialité.",
        },
        {
            "row": ["Non revendiqué", "Non indiqué", "Non indiqué", "Gratuite", "4.3 (561,523 notes)"],
            "best_for": "des millions de personnages créés par les utilisateurs, si la confidentialité n'est pas votre priorité.",
            "facts": [
                "La fiche décrit le fait de discuter et d'appeler une immense bibliothèque de personnages créés par les utilisateurs, ainsi que la création des vôtres et leur partage avec la communauté.",
                "Étiquette de confidentialité de l'App Store : données utilisées pour le suivi (localisation, coordonnées, identifiants, données d'utilisation) ; données liées à vous (achats, informations financières, localisation, coordonnées, contenu utilisateur, historique de recherche, identifiants, données d'utilisation, diagnostics).",
                "Version 1.17.4 (2 oct. 2026), iOS 15.1 ou ultérieur.",
            ],
            "limits": "la liste de données la plus longue des huit, avec informations financières, contenu utilisateur et historique de recherche liés à vous, et une conception axée sur le partage et la communauté.",
        },
    ],
    "who": [
        "<strong>Vous voulez des discussions qui ne quittent jamais le téléphone :</strong> Talking Friday (voix), Najimi (avatar) ou SOUL.AI (discussion simple).",
        "<strong>Vous voulez une qualité éprouvée et acceptez un service cloud :</strong> Pi, Replika ou Tolan, avec les limites d'étiquette ci-dessus.",
        "<strong>Vous voulez le moins de données collectées parmi les grandes applis :</strong> Pi ne liste aucun suivi ; Replika, Tolan et Character AI en listent.",
        "<strong>Vous voulez l'utiliser dans un avion ou sans réseau :</strong> Talking Friday, Najimi ou SOUL.AI.",
    ],
    "cases": [
        "Se défouler ou réfléchir à voix haute la nuit, sans compte (Talking Friday, SOUL.AI).",
        "Un personnage personnalisable qui tourne en local (Najimi).",
        "De longues conversations avec mémoire, en acceptant un service cloud (Replika, Pi).",
        "Discuter avec de nombreux personnages créés par les utilisateurs (Character AI).",
    ],
    "method": [
        "Le 14 novembre 2026, nous avons cherché sur l'App Store américain « private ai companion », « offline ai companion », « ai friend to talk to » et « on-device ai chat private », consulté les données de recherche d'Apple pour les huit applis (nom, prix, note et description) et lu l'étiquette de confidentialité sur la page de chaque appli.",
        "Nous avons classé les applis selon le degré de soutien de la fiche et de l'étiquette à une discussion privée, puis selon la note. Les applis sur l'appareil viennent en tête pour la confidentialité, mais leurs notes sont trop peu nombreuses pour juger la qualité ; lisez-le comme « la confidentialité d'abord », pas comme « le meilleur compagnon ».",
        "Les fonctions et déclarations de confidentialité viennent uniquement des fiches et étiquettes, pas de nos tests ; nous n'avons pas fait de captures réseau. Nous avons écarté d'autres applis apparues dans les recherches (Kindroid, Solace, Red Angel et d'autres) pour rester à huit ; la fiche de Solace, par exemple, mentionne la suppression de compte et ne dit pas que les discussions restent sur l'appareil. Cora n'est pas apparue dans la recherche de l'App Store américain.",
    ],
    "faq": [
        ("Nomi AI est-elle privée ?",
         "Sa fiche ne dit pas que l'IA tourne sur votre téléphone, et son étiquette de confidentialité de l'App Store liste des données liées à vous, dont le contenu utilisateur, mais aucun suivi. Lisez sa politique de confidentialité pour savoir combien de temps les discussions sont conservées."),
        ("Un compagnon IA peut-il fonctionner hors ligne ?",
         "Oui, si le modèle est sur le téléphone. Talking Friday, Najimi et SOUL.AI disent que le leur fonctionne hors ligne. Les applis qui ne le disent pas, comme Nomi, Pi, Replika, Tolan et Character AI, ne sont pas décrites comme hors ligne dans leurs fiches."),
        ("Quelle est l'appli d'ami IA la plus privée sur iPhone ?",
         "Parmi les huit vérifiées, celles qui revendiquent un fonctionnement sur l'appareil et portent l'étiquette « Aucune donnée collectée » : Talking Friday, Najimi et SOUL.AI. Elles ont très peu de notes, testez-les vous-même en mode avion."),
        ("Que m'indique l'étiquette de confidentialité de l'App Store ?",
         "C'est la liste, établie par le développeur, des données collectées, réparties en données utilisées pour le suivi, liées à vous et non liées à vous. Elle ne dit pas combien de temps les discussions sont conservées."),
    ],
}

# ---------------------------------------------------------------- ar (السعودية)
TR_AR = {
    "title": "أفضل تطبيقات رفيق الذكاء الاصطناعي الخاص لآيفون (2026)",
    "h1": "أفضل تطبيقات رفيق الذكاء الاصطناعي الخاص لآيفون (2026)",
    "description": "ثمانية تطبيقات رفيق ذكاء اصطناعي وصديق افتراضي لآيفون، مقارنة من حيث الخصوصية: على الجهاز أو في السحابة، والعمل دون اتصال، والحساب، والسعر، وملصق الخصوصية في App Store. تم التحقق في 14 نوفمبر 2026.",
    "llms": "يقارن ثمانية تطبيقات رفيق ذكاء اصطناعي لآيفون (Talking Friday وNajimi وSOUL.AI وNomi وPi وReplika وTolan وCharacter AI) حسب بقاء المحادثات على الهاتف، والعمل دون اتصال، والحاجة إلى حساب، والسعر والتقييم وملصق الخصوصية في App Store. يوضح ما تقوله كل صفحة وما لا تقوله.",
    "answer": [
        "إذا كنت تريد رفيقًا ذكيًا تبقى محادثاته على هاتفك، فإن ثلاثة فقط من التطبيقات الثمانية التي تحققنا منها تقول ذلك في صفحتها على App Store: Talking Friday وNajimi وSOUL.AI تشغّل الذكاء الاصطناعي على الآيفون وتقول إنه يعمل دون اتصال، وجميعها تحمل ملصق «لا تُجمع بيانات». أما التطبيقات الخمسة الأكبر (Nomi وPi وReplika وTolan وCharacter AI) فلديها تقييمات أكثر بكثير، لكن ملصقاتها تسرد بيانات مجمّعة مرتبطة بك، ولا يدّعي أيٌّ منها التشغيل على الجهاز.",
        "الثمن هو الحجم: تطبيقات التشغيل على الجهاز لديها من 0 إلى 11 تقييمًا، لذلك فجودتها غير مثبتة، وملصق الخصوصية تصريح من المطوّر نفسه. تحققنا في 14 نوفمبر 2026 وكتبنا «غير مذكور» حيثما تصمت الصفحة.",
    ],
    "keep": [0, 1, 2, 3, 4, 5, 6, 7],
    "day": "2026-11-15",
    "columns": ["التطبيق", "يعمل على الآيفون", "يعمل دون اتصال", "يتطلب حسابًا", "السعر (السعودية)", "التقييم (الولايات المتحدة)"],
    "table_note": "السعر والتوفر من App Store السعودية في 15 نوفمبر 2026، والتطبيقات الثمانية جميعها متاحة فيه. التقييم من App Store الولايات المتحدة في 14 نوفمبر 2026 (تقييمات أمريكية، لا سعودية). الأعمدة الأخرى هي ما تقوله صفحة كل تطبيق؛ «غير مدّعى» يعني أن الصفحة لا تقول إن الذكاء الاصطناعي يعمل على الجهاز، و«غير مذكور» يعني أنها لا تذكر شيئًا. التقييم الذي يحمل أصواتًا قليلة لا يدل على كثير.",
    "apps": [
        {
            "row": ["نعم، حسب الصفحة (محادثة صوتية إلى صوتية على Neural Engine)", "نعم", "لا", "مجاني؛ لا مشتريات داخل التطبيق حسب الصفحة", "لا تقييمات بعد"],
            "best_for": "محادثات صوتية خاصة لا تغادر الهاتف أبدًا.",
            "facts": [
                "تقول الصفحة إن الحلقة الصوتية كاملة تعمل على Neural Engine في الآيفون، دون خوادم ودون حساب ودون إنترنت.",
                "ملصق الخصوصية في App Store: لا تُجمع بيانات.",
                "تتحدث فيرد بصوت مسموع؛ وليس تطبيق شخصيات أو علاقات، بل محادثة صوتية للتفكير بصوت عالٍ أو لممارسة الحوارات.",
                "الإصدار 1.0، iOS 18.0 أو أحدث، صفحة مُحدّثة في 14 يوليو 2026.",
            ],
            "limits": "لا تقييمات بعد، لذلك لا يوجد دليل عام على جودة المحادثات؛ الصوت فقط، ويحتاج iOS 18.",
        },
        {
            "row": ["نعم، حسب الصفحة (نماذج لغة وصوت محلية مضمّنة)", "نعم، حسب الصفحة («يمكن أن يعمل دون اتصال»)", "غير مذكور", "مجاني", "4.0 (تقييمان)"],
            "best_for": "رفيق بصورة رمزية قابلة للتخصيص يعمل محليًا.",
            "facts": [
                "تقول الصفحة إنها تتضمن نموذج لغة محليًا ونموذج صوت للمحادثة على الجهاز، لذلك التنزيل أكبر من المعتاد.",
                "يمكنك تغيير الشخصية والمظهر والصوت والخلفية، واستيراد شخصيتك الخاصة بصيغة VRM، والمحادثة مع المستندات.",
                "ملصق الخصوصية في App Store: لا تُجمع بيانات.",
                "الإصدار 1.1، iOS 18.6 أو أحدث، حُدّث في 6 أغسطس 2026.",
            ],
            "limits": "تقييمان فقط؛ تنزيل كبير؛ الصفحة لا تذكر إن كانت تتطلب حسابًا.",
        },
        {
            "row": ["نعم، حسب الصفحة", "نعم", "لا", "مجاني", "2.5 (11 تقييمًا)"],
            "best_for": "نموذج محادثة بسيط دون اتصال على آيفون حديث.",
            "facts": [
                "تقول الصفحة إن النموذج موجود داخل التطبيق ويعمل بالكامل على الجهاز ولا يرسل المحادثات إلى السحابة؛ لا حاجة إلى حساب.",
                "ملصق الخصوصية في App Store: لا تُجمع بيانات.",
                "توصي بـ iPhone 15 Pro أو أحدث؛ الأجهزة الأقدم قد تكون بطيئة أو تتعطل، والأجهزة الأقدم من iPhone 12 غير مدعومة.",
                "الإصدار 1.7.3، حُدّث في 10 يوليو 2026.",
            ],
            "limits": "تقييم 2.5 من 11 شخصًا، وهو مساعد عام أكثر منه رفيقًا ذا شخصية.",
        },
        {
            "row": ["غير مدّعى", "غير مذكور", "غير مذكور", "مجاني", "4.6 (3,029 تقييمًا)"],
            "best_for": "ذاكرة طويلة الأمد ولعب أدوار علاقاتي، إذا كنت تقبل خدمة سحابية.",
            "facts": [
                "تركز الصفحة على الذاكرة قصيرة وطويلة الأمد والمحادثات الجماعية والصور الذاتية وتوليد الفن، ولا تقول إن الذكاء الاصطناعي يعمل على الجهاز.",
                "ملصق الخصوصية في App Store: بيانات مرتبطة بك (مشتريات، معلومات اتصال، محتوى المستخدم، معرّفات، بيانات استخدام، تشخيصات). لا يُذكر أي تتبع.",
                "الإصدار 1.12.1، iOS 15.0 أو أحدث، حُدّث في 31 مارس 2026.",
            ],
            "limits": "محتوى المستخدم مصنّف في الملصق كمرتبط بك، لذا افترض أن الشركة تحفظ المحادثات؛ اقرأ سياسة الخصوصية لمعرفة مدة الحفظ. هذا يجيب عن السؤال الشائع «هل Nomi AI خاص؟»: ملصقه يقول إن البيانات مرتبطة بك، وصفحته لا تدّعي أي تشغيل على الجهاز.",
        },
        {
            "row": ["غير مدّعى", "غير مذكور", "غير مذكور", "مجاني", "4.4 (2,555 تقييمًا)"],
            "best_for": "مساعد هادئ للحديث عن الأمور مع وضع صوتي.",
            "facts": [
                "تصف الصفحة الحديث عن الأمور والوضع الصوتي والمساعدة على إنجاز المهام، ولا تذكر أين يعمل الذكاء الاصطناعي.",
                "ملصق الخصوصية في App Store: بيانات مرتبطة بك (معرّفات، بيانات استخدام، تشخيصات) للتحليلات والتخصيص ووظائف التطبيق. لا يُذكر تتبع.",
                "الإصدار 26.1109.0 (13 نوفمبر 2026)، iOS 16 أو أحدث.",
            ],
            "limits": "لا ادعاء بالتشغيل على الجهاز أو دون اتصال؛ الملصق لا يحتوي فئة لمحتوى المستخدم، لكنه لا يوضح كيف تُحفظ المحادثات.",
        },
        {
            "row": ["غير مدّعى", "غير مذكور", "غير مذكور", "مجاني", "4.4 (227,667 تقييمًا)"],
            "best_for": "رفيق طويل الأمد مع مكالمات وتواصل استباقي.",
            "facts": [
                "تصف الصفحة المكالمات النصية والصوتية والمرئية والوصول إلى الإنترنت وتكامل التطبيقات وتوليد الصور، وتقول إنه يتذكر أشخاصك وخططك.",
                "ملصق الخصوصية في App Store: بيانات تُستخدم للتتبع (معرّفات، بيانات استخدام)؛ وبيانات مرتبطة بك (موقع، معلومات اتصال، معرّفات، بيانات استخدام)؛ وبعض التشخيصات غير المرتبطة بك.",
                "الإصدار 12.5.2 (5 نوفمبر 2026)، iOS 17.0 أو أحدث.",
            ],
            "limits": "يتضمن ملصقه بيانات تتبع وموقعًا، وتصف الصفحة ميزات تحتاج إلى الإنترنت.",
        },
        {
            "row": ["غير مدّعى", "غير مذكور", "غير مذكور", "مجاني", "4.8 (190,859 تقييمًا)"],
            "best_for": "رفيق ودود بأسلوب كائن فضائي يمكنك التحدث معه في أي موضوع.",
            "facts": [
                "الصفحة قصيرة: الحديث عن الاهتمامات والمشاعر والأفكار، ومشاركة الصور، وتصميم كوكب معًا. ولا تذكر شيئًا عن مكان تشغيل الذكاء الاصطناعي.",
                "ملصق الخصوصية في App Store: بيانات تُستخدم للتتبع (مشتريات، موقع، معلومات اتصال، معرّفات، بيانات استخدام، بيانات أخرى)؛ وبيانات مرتبطة بك (بما فيها محتوى المستخدم)؛ وبيانات أخرى غير مرتبطة بك.",
                "الإصدار 26.46.1 (11 نوفمبر 2026)، iOS 18.0 أو أحدث.",
            ],
            "limits": "يسرد الملصق التتبع والموقع، ومحتوى المستخدم بوصفه مرتبطًا بك؛ والصفحة لا تقدم ادعاءات خصوصية.",
        },
        {
            "row": ["غير مدّعى", "غير مذكور", "غير مذكور", "مجاني", "4.3 (561,523 تقييمًا)"],
            "best_for": "ملايين الشخصيات التي أنشأها المستخدمون، إذا لم تكن الخصوصية أولويتك الأولى.",
            "facts": [
                "تصف الصفحة الدردشة والمكالمات مع مكتبة ضخمة من الشخصيات التي أنشأها المستخدمون، إضافة إلى إنشاء شخصياتك الخاصة ومشاركتها مع المجتمع.",
                "ملصق الخصوصية في App Store: بيانات تُستخدم للتتبع (موقع، معلومات اتصال، معرّفات، بيانات استخدام)؛ وبيانات مرتبطة بك (مشتريات، معلومات مالية، موقع، معلومات اتصال، محتوى المستخدم، سجل البحث، معرّفات، بيانات استخدام، تشخيصات).",
                "الإصدار 1.17.4 (2 أكتوبر 2026)، iOS 15.1 أو أحدث.",
            ],
            "limits": "أطول قائمة بيانات بين الثمانية، وتشمل معلومات مالية ومحتوى المستخدم وسجل البحث المرتبطة بك، وتصميمًا قائمًا على المشاركة والمجتمع.",
        },
    ],
    "who": [
        "<strong>تريد محادثات لا تغادر الهاتف:</strong> Talking Friday (صوت)، أو Najimi (صورة رمزية)، أو SOUL.AI (دردشة بسيطة).",
        "<strong>تريد جودة مثبتة وتقبل خدمة سحابية:</strong> Nomi أو Pi أو Replika أو Tolan، مع حدود الملصقات أعلاه.",
        "<strong>تريد أقل قدر من البيانات المجمعة بين التطبيقات الكبيرة:</strong> Nomi وPi لا تعلنان أي تتبع؛ وReplika وTolan وCharacter AI تعلنانه.",
        "<strong>تريد استخدامه في الطائرة أو دون إشارة:</strong> Talking Friday أو Najimi أو SOUL.AI.",
    ],
    "cases": [
        "التنفيس أو التفكير بصوت عالٍ ليلًا دون حساب (Talking Friday، SOUL.AI).",
        "شخصية قابلة للتخصيص تعمل محليًا (Najimi).",
        "محادثات طويلة مع الذاكرة، مع قبول خدمة سحابية (Nomi، Replika، Pi).",
        "الدردشة مع كثير من الشخصيات التي أنشأها المستخدمون (Character AI).",
    ],
    "method": [
        "في 14 نوفمبر 2026 بحثنا في App Store الولايات المتحدة عن «private ai companion» و«offline ai companion» و«ai friend to talk to» و«on-device ai chat private»، واطلعنا على بيانات البحث من Apple للتطبيقات الثمانية (الاسم والسعر والتقييم والوصف)، وقرأنا ملصق الخصوصية في صفحة كل تطبيق.",
        "رتّبنا التطبيقات حسب مدى دعم الصفحة والملصق للدردشة الخاصة، ثم حسب التقييم. تأتي تطبيقات التشغيل على الجهاز أولًا من حيث الخصوصية، لكن تقييماتها قليلة جدًا للحكم على الجودة؛ فاقرأ ذلك بوصفه «الخصوصية أولًا»، لا «أفضل رفيق».",
        "الميزات والتصريحات المتعلقة بالخصوصية مأخوذة من الصفحات والملصقات فقط، لا من اختباراتنا؛ ولم نجرِ تحليلًا لحركة الشبكة. استبعدنا تطبيقات أخرى ظهرت في عمليات البحث (Kindroid وSolace وRed Angel وغيرها) للإبقاء على القائمة من ثمانية؛ فصفحة Solace مثلًا تذكر حذف الحساب ولا تقول إن المحادثات تبقى على الجهاز. ولم يظهر Cora في بحث App Store الولايات المتحدة.",
    ],
    "faq": [
        ("هل Nomi AI خاص؟",
         "صفحته لا تقول إن الذكاء الاصطناعي يعمل على هاتفك، وملصق الخصوصية في App Store يسرد بيانات مرتبطة بك، بما فيها محتوى المستخدم، لكن دون تتبع. اقرأ سياسة الخصوصية لمعرفة مدة حفظ المحادثات."),
        ("هل يمكن لرفيق الذكاء الاصطناعي أن يعمل دون اتصال؟",
         "نعم، إذا كان النموذج على الهاتف. تقول Talking Friday وNajimi وSOUL.AI إن نموذجها يعمل دون اتصال. أما التطبيقات التي لا تقول ذلك، مثل Nomi وPi وReplika وTolan وCharacter AI، فلا توصف في صفحاتها بأنها تعمل دون اتصال."),
        ("ما أكثر تطبيق صديق ذكاء اصطناعي خصوصية لآيفون؟",
         "من بين الثمانية التي تحققنا منها، التطبيقات التي تدّعي التشغيل على الجهاز ولها ملصق «لا تُجمع بيانات»: Talking Friday وNajimi وSOUL.AI. لديها تقييمات قليلة جدًا، فجرّبها بنفسك في وضع الطيران."),
        ("ماذا يخبرني ملصق الخصوصية في App Store؟",
         "هو قائمة يضعها المطوّر نفسه للبيانات المجمّعة، مقسّمة إلى بيانات تُستخدم للتتبع، ومرتبطة بك، وغير مرتبطة بك. ولا يوضح مدة حفظ المحادثات."),
    ],
}

PAGES = [
    make("private-ai-companions", "ru", TR_RU, "ru"),
    make("private-ai-companions", "de", TR_DE, "de"),
    make("private-ai-companions", "ja", TR_JA, "ja"),
    make("private-ai-companions", "es", TR_ES, "es"),
    make("private-ai-companions", "pt-BR", TR_PTBR, "pt-br"),
    make("private-ai-companions", "fr", TR_FR, "fr"),
    make("private-ai-companions", "ar", TR_AR, "ar"),
]
