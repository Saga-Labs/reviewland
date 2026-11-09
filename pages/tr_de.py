"""German (de) translations of four ranking pages. Store: Germany, data of 9 Nov 2026."""
from pages.trlib import make

T = "Daten, die dich verfolgen"
L = "Mit dir verknüpfte Daten"
N = "Nicht mit dir verknüpfte Daten"
NC = "Daten werden nicht erfasst"


def lab(*parts):
    return "; ".join(parts)


# ------------------------------------------------------------------ 1. einfache To-do-Listen
TR_TODO = {
    "title": "Beste einfache To-do-Listen-Apps fürs iPhone (2026)",
    "h1": "Die besten einfachen To-do-Listen-Apps fürs iPhone 2026",
    "description": "Sechs einfache To-do-Apps fürs iPhone im Vergleich: 3 Tasks, Do!, MinimaList, Clear, Microsoft To Do und Todoist. Preis, Konto und Datenschutz geprüft.",
    "llms": "Vergleicht sechs einfache To-do-Listen-Apps fürs iPhone (3 Tasks, Do!, MinimaList, Clear, Microsoft To Do, Todoist) nach Preis, Kontopflicht, Erinnerungen, Widgets und Datenschutzlabel im deutschen App Store.",
    "answer": [
        "Die einfachste To-do-Liste fürs iPhone ist eine, die dich bremst: Bei 3 Tasks schreibst du nur drei Prioritäten pro Tag auf und stoppst die Zeit für jede einzelne – kostenlos, ohne Konto und ohne Abo (das optionale Pro ist ein Einmalkauf). Wenn du eine normale Liste willst, die trotzdem schlicht bleibt, bieten Do! und MinimaList Erinnerungen und Widgets, und Microsoft To Do ist komplett kostenlos und synchronisiert über ein Microsoft-Konto.",
        "Todoist ist die umfangreichste der sechs Apps, aber das Pro-Paket ist ein Abo (6,99 € im Monat oder 59,99 € im Jahr im deutschen App Store).",
    ],
    "columns": ["App", "Preis (DE)", "Was sie einfach macht", "Konto", "Datenschutzlabel im App Store", "Version (Datum)", "Bewertung (DE)"],
    "table_note": "Preise sind die In-App-Käufe im deutschen App Store am 9. November 2026; alle sechs Apps sind gratis zu laden. Bewertungen sind der Durchschnitt im App Store an diesem Tag; „–“ heißt, dass dort noch keine Bewertung angezeigt wird.",
    "apps": [
        {
            "row": [
                "Gratis; 3 Tasks Pro ist ein Einmalkauf (gelistet zu 5,99 € und 9,99 €)",
                "Nur 3 Aufgaben pro Tag, ein Bildschirm, ein Timer pro Aufgabe",
                "Kein Konto",
                lab(T, N),
                "1.4.6 (5.11.2026)",
                "–",
            ],
            "best_for": "Menschen, die in langen Listen untergehen und die drei Dinge auswählen wollen, die heute zählen.",
            "facts": [
                "Du schreibst drei Tagesprioritäten auf; sonst gibt es nichts einzustellen.",
                "Jede Aufgabe lässt sich wie bei Pomodoro starten und pausieren, und du siehst die verbrauchte Zeit.",
                "Keine Werbung und kein Konto. Die App nutzt Firebase Analytics, um zu zählen, wie Aufgaben und Timer verwendet werden – deshalb nennt das Datenschutzlabel Tracking-Daten.",
                "33 Sprachen, ab iOS 18.",
            ],
            "limits": "keine Erinnerungen und keine Synchronisierung zwischen Geräten: Es ist bewusst eine Tagesliste mit drei Einträgen (es gibt aber „Täglich wiederholen“ und ein kostenloses Widget für den Home-Bildschirm).",
        },
        {
            "row": [
                "Gratis mit Werbung; Werbung entfernen einmalig 22,00 €; Trinkgeld 0,99 €",
                "Aufgabe hinzufügen, zum Erledigen doppelt tippen; Gruppen und Farben",
                "Nicht angegeben",
                lab(T, L, N),
                "7.9.0 (22.10.2026)",
                "4.5",
            ],
            "best_for": "eine Tagesliste wie auf Papier, mit Erinnerungen und wiederkehrenden Aufgaben.",
            "facts": [
                "Designs, Schriften und Stift-und-Papier-Geräusche.",
                "Gruppen für Arbeit, Lernen und Einkauf; angeheftete Aufgaben.",
                "Wiederkehrende Aufgaben (täglich bis jährlich) und Erinnerungen.",
                "5 Sprachen, ab iOS 15.",
            ],
            "limits": "zeigt Werbung, solange du nicht einmalig 22,00 € zahlst, und das Datenschutzlabel nennt Daten, die dich verfolgen.",
        },
        {
            "row": [
                "Lifetime ab 6,99 € bis 9,99 €; Familie 17,99 €; oder 2,99 € im Monat",
                "Farbige Listen, smarte Eingabe, die Uhrzeiten erkennt",
                "Nicht angegeben",
                N,
                "2.27.9 (30.10.2026)",
                "4.7",
            ],
            "best_for": "eine minimalistisch wirkende Liste, die trotzdem Widgets, geteilte Listen und Ortserinnerungen bietet.",
            "facts": [
                "Widgets für den Home-Bildschirm und den Sperrbildschirm.",
                "Erinnerungen nach Zeit und Ort, Unteraufgaben und geteilte Listen.",
                "Funktioniert mit Siri; laut Entwickler auf iPhone, iPad und Mac.",
                "10 Sprachen, ab iOS 15.",
            ],
            "limits": "mehrere sich überschneidende Preise für dasselbe Lifetime-Upgrade, sodass kaum klar ist, was du am Ende zahlst.",
        },
        {
            "row": [
                "Legacy-Pro 2,99 € im Monat oder 29,99 € im Jahr; Soundpakete (1,99 € und 2,99 €)",
                "Listen nur mit Gesten, Farbverlauf zeigt die Priorität",
                "Nicht angegeben",
                lab(T, N),
                "2.8.7 (31.10.2026)",
                "4.2",
            ],
            "best_for": "Menschen, die Listen per Wischen bedienen wollen, ganz ohne Schaltflächen auf dem Bildschirm.",
            "facts": [
                "Zum Erledigen wischen, zum Sortieren zusammenziehen und ziehen; ein Farbverlauf zeigt die Priorität.",
                "Tägliches Kanban (Heute, Morgen, Übermorgen), Routinen und Erinnerungen.",
                "2 Sprachen, ab iOS 16.",
            ],
            "limits": "die Gesten muss man ein paar Minuten lernen, und das Datenschutzlabel nennt Daten, die dich verfolgen.",
        },
        {
            "row": [
                "Gratis, keine In-App-Käufe",
                "Mein Tag mit Aufgabenvorschlägen",
                "Microsoft-Konto zum Synchronisieren",
                L,
                "2.177 (6.7.2026)",
                "4.6",
            ],
            "best_for": "eine kostenlose Liste, die überall synchronisiert, besonders wenn du Outlook oder Microsoft 365 nutzt.",
            "facts": [
                "„Mein Tag“ und Vorschläge helfen, den Tag aus allen Listen zu planen.",
                "Synchronisiert mit Microsoft 365; markierte Outlook-Mails können zu Aufgaben werden.",
                "Geteilte Listen für private Konten.",
                "34 Sprachen, ab iOS 17.6.",
            ],
            "limits": "sie ist ein vollwertiger Aufgabenmanager mit Listen, Schritten und Vorschlägen und kann so zu den langen Listen werden, die eine einfache App vermeiden will.",
        },
        {
            "row": [
                "Pro 6,99 € im Monat oder 59,99 € im Jahr",
                "Schnelleingabe in natürlicher Sprache und Spracheingabe",
                "Ja",
                L,
                "26.10.35 (2.11.2026)",
                "4.7",
            ],
            "best_for": "Menschen, deren Liste einer einfachen App entwächst und die Projekte, Termine und Teams brauchen.",
            "facts": [
                "Die Schnelleingabe versteht Datumsangaben in normaler Sprache; Ramble macht aus Gesprochenem Aufgaben.",
                "Projekte, Kalenderansicht und Team-Arbeitsbereiche.",
                "Funktioniert mit Siri. 19 Sprachen, ab iOS 17.",
            ],
            "limits": "Pro ist ein Abo, und es ist die am wenigsten einfache App in dieser Liste.",
        },
    ],
    "who": [
        "<strong>Du schreibst ständig Listen, die du nie abarbeitest:</strong> 3 Tasks, drei pro Tag und nicht mehr.",
        "<strong>Du willst Erinnerungen und wiederkehrende Aufgaben, aber ein ruhiges Design:</strong> Do! oder MinimaList.",
        "<strong>Du willst alles kostenlos und synchronisiert:</strong> Microsoft To Do.",
        "<strong>Du magst Gesten und keine Schaltflächen:</strong> Clear.",
        "<strong>Du brauchst Projekte, Termine und gemeinsame Arbeit:</strong> Todoist.",
    ],
    "cases": [
        "Die drei Dinge festlegen, die heute passieren müssen, bevor du die E-Mails öffnest.",
        "Eine Einkaufs- oder Besorgungsliste, die dich erinnert, wenn du am Geschäft ankommst (MinimaList).",
        "Arbeitsaufgaben, die aus markierten Outlook-Mails entstehen (Microsoft To Do).",
        "Konzentrierte Arbeitsblöcke pro Priorität mit Zeitmessung (3 Tasks).",
    ],
    "method": [
        "Am 9. November 2026 haben wir die Seite jeder App im deutschen App Store und die Lookup-Daten von Apple geöffnet: In-App-Käufe, Version und Veröffentlichungsdatum, Bewertung, Sprachen, mindestens erforderliche iOS-Version und Datenschutzlabel. Die Funktionen sind die, die der jeweilige Entwickler auf seiner Seite angibt. „Nicht angegeben“ heißt, dass aus dem Eintrag nicht hervorgeht, ob ein Konto nötig ist. Bewertungen oder Rezensionen haben wir nicht erfunden.",
    ],
    "faq": [
        ("Welche To-do-Listen-App ist die einfachste fürs iPhone?",
         "Bei 3 Tasks kannst du nur drei Aufgaben pro Tag auf einem Bildschirm eintragen. Unter den klassischen Listen-Apps sind Do! und Clear am minimalistischsten."),
        ("Gibt es eine kostenlose To-do-Listen-App ohne Abo?",
         "Microsoft To Do ist gratis und ohne In-App-Käufe, und 3 Tasks ist gratis mit optionalem Einmalkauf Pro (kein Abo). Do! ist gratis mit Werbung und lässt sich einmalig für 22,00 € werbefrei machen; MinimaList und Clear bieten ebenfalls Einmal-Upgrades."),
        ("Welche To-do-App funktioniert ohne Konto?",
         "3 Tasks braucht kein Konto. Microsoft To Do nutzt zum Synchronisieren ein Microsoft-Konto, Todoist ein eigenes Konto."),
        ("Warum sich auf drei Aufgaben pro Tag beschränken?",
         "Eine kurze Liste zwingt dich, das Wichtigste zu wählen, sodass die Liste abgearbeitet wird, statt zu wachsen. Das ist die Idee hinter 3 Tasks."),
        ("Welche einfache To-do-App hat Widgets?",
         "MinimaList hat Widgets für den Home- und den Sperrbildschirm. 3 Tasks hat ein kostenloses Widget für den Home-Bildschirm."),
    ],
}

# ------------------------------------------------------------------ 2. kostenlose Einschlaf-Sounds
TR_SLEEP = {
    "title": "Kostenlose Einschlaf-Apps mit Geräuschen fürs iPhone (2026)",
    "h1": "Die besten kostenlosen Einschlaf-Sounds-Apps fürs iPhone 2026",
    "description": "Sechs Einschlafhilfe-Apps mit Naturgeräuschen und weißem Rauschen fürs iPhone im Vergleich, danach, was wirklich gratis ist: Drop, White Noise Lite, Rain Rain und mehr.",
    "llms": "Vergleicht sechs Einschlaf-Apps mit Geräuschen fürs iPhone (Drop, White Noise Lite, Rain Rain, White Noise Deep Sleep Sounds, Sleep Pillow, Dark Noise) danach, wie viel gratis ist, Werbung, Timer, Preis der Bezahlstufe und Datenschutzlabel im deutschen App Store.",
    "answer": [
        "Für die meisten Geräusche gratis sind White Noise Lite (50+ Sounds, keine Käufe gelistet) und Rain Rain (50+ Sounds, ein kleiner Werbebanner) am stärksten. Für weißes, rosa und braunes Rauschen im kostenlosen Angebot listen sowohl White Noise Lite als auch White Noise Deep Sleep Sounds diese Klänge. Wer kostenlose Einschlafgeräusche ganz ohne Werbung und mit Einschlaf-Timer möchte, bekommt bei Drop 9 der 53 Sounds gratis, darunter weißes Rauschen; rosa und braunes Rauschen gibt es nur mit Drop Pro.",
        "Alle sechs Apps sind gratis zu laden. Unterschiede gibt es dabei, wie viel kostenlos bleibt, ob es Werbung gibt und wie lange der Ton läuft; alles steht in der Tabelle.",
    ],
    "columns": ["App", "Preis (DE)", "Was gratis ist", "Datenschutzlabel im App Store", "Version (Datum)", "Bewertung (DE)"],
    "table_note": "Preise sind die In-App-Käufe im deutschen App Store am 9. November 2026 (eine App kann für denselben Tarif mehrere Preise listen). Bewertungen sind der Durchschnitt im App Store an diesem Tag.",
    "apps": [
        {
            "row": [
                "Gratis: 9 von 53 Sounds, keine Werbung; Drop Pro monatlich 5,99 € oder Lifetime-Optionen",
                "Weißes Rauschen, Kaminfeuer, Wald, Herzschlag, See, Café, fallender Schnee, Wüstenwind und Delfine; Einschlaf-Timer mit 30 Sekunden Ausblenden",
                lab(L, N),
                "2.15 (5.11.2026)",
                "5.0",
            ],
            "best_for": "kostenlose, werbefreie beruhigende Klänge mit richtigem Einschlaf-Timer und einer kurzen Atemübung.",
            "facts": [
                "9 kostenlose Sounds ohne Werbebanner: weißes Rauschen, Kaminfeuer, Wald, Herzschlag, See, Café, fallender Schnee, Wüstenwind und Delfine.",
                "Einschlaf-Timer mit 15, 30 oder 45 Minuten, 1, 2 oder 8 Stunden und 30 Sekunden Ausblenden; funktioniert offline.",
                "Atemübungen von 2 bis 20 Minuten und eine Pflanze, die mit deiner Übung wächst.",
                "33 Sprachen, ab iOS 18.",
            ],
            "limits": "nur 9 Sounds sind gratis, die übrigen 44 (darunter Regen, Meer, rosa und braunes Rauschen) brauchen Drop Pro; kein Mixer; erfordert iOS 18.",
        },
        {
            "row": [
                "Gratis, keine In-App-Käufe gelistet",
                "50+ Endlos-Sounds, darunter weißes, rosa und braunes Rauschen; Timer und Wecker mit Ein- und Ausblenden",
                lab(T, L, N),
                "9.0.6 (7.11.2026)",
                "4.6",
            ],
            "best_for": "die meisten Geräusche zum Nulltarif: echte Rauschfarben, ein Mixer und Timer.",
            "facts": [
                "50+ Endlos-Sounds, darunter weißes, rosa, braunes, blaues und violettes Rauschen.",
                "Mix Pad zum Zusammenstellen von Mischungen; Audio im Hintergrund, damit du andere Apps nutzen kannst.",
                "Timer und Wecker, die den Ton ein- und ausblenden.",
                "3 Sprachen (Englisch, Französisch, Spanisch), ab iOS 15.",
            ],
            "limits": "keine Meditation oder Atemübungen, und das Datenschutzlabel nennt Daten, die dich verfolgen.",
        },
        {
            "row": [
                "Gratis (50+ Sounds, kleiner Werbebanner); Premium gelistet ab 4,49 € (Jahresabo 30,99 € oder 39,99 €); Soundpakete 5,99 €",
                "50+ HD-Sounds gratis, keine Begrenzung der Spielzeit, alle Ausblend-Optionen, Mixer",
                lab(T, L, N),
                "6.9.10 (22.1.2025)",
                "4.8",
            ],
            "best_for": "viele Regen- und Naturgeräusche gratis und ohne Zeitlimit, wenn dich ein kleiner Werbebanner nicht stört.",
            "facts": [
                "Laut Eintrag hat die Gratis-Version 50+ HD-Sounds, keine Begrenzung der Spielzeit, alle Ausblend-Timer-Optionen und einen Mixer mit Lautstärke pro Sound.",
                "Keine Audio- oder Videowerbung, nur ein kleiner Bildbanner unten; Premium bringt 60+ Sounds dazu und entfernt ihn.",
                "4 Sprachen (Englisch, Französisch, Italienisch, Spanisch), ab iOS 12.",
            ],
            "limits": "zuletzt am 22. Januar 2025 aktualisiert, und das Datenschutzlabel nennt Daten, die dich verfolgen.",
        },
        {
            "row": [
                "Gratis (spielt 8 Stunden am Stück); Premium ab 1,99 € pro Woche bis 59,99 € (Familie)",
                "30+ kostenlose Sounds, darunter weißes, rosa und braunes Rauschen; Mixer, Einschlaf-Timer, Widget",
                lab(L, N),
                "3.45.0 (25.9.2026)",
                "4.7",
            ],
            "best_for": "eine große Bibliothek (250+ weitere Premium-Sounds) mit 30+ Gratis-Sounds, darunter weißes, rosa und braunes Rauschen, für Erwachsene und Babys.",
            "facts": [
                "Zu den gelisteten Gratis-Sounds gehören Ventilator, Baby-Shusher, Staubsauger, Flugzeugkabine, Regen, Donner, Meereswellen sowie weißes, rosa und braunes Rauschen.",
                "Einschlaf-Timer, Sounds mischen, Widget, AirPlay 2.",
                "Laut Eintrag spielt die Gratis-Version Töne acht Stunden lang; Dauerwiedergabe braucht ein Abo.",
                "33 Sprachen, ab iOS 15.",
            ],
            "limits": "die Gratis-Version hört nach acht Stunden auf – für eine Nacht reicht das, für den Dauerbetrieb am Tag nicht; sehr viele Preisstufen.",
        },
        {
            "row": [
                "Gratis; Soundpakete von 9,99 € bis 22,99 €; Abo „Alle Soundpakete“ 4,99 €",
                "Natürlich aufgenommene Klänge, bis zu 300.000 Mischungen, Einschlaf-Timer, Wecker",
                N,
                "8.0.4 (30.10.2023)",
                "4.6",
            ],
            "best_for": "eine klassische Einschlaf-App mit Einschlaf-Timer, Wecker und Mischungen.",
            "facts": [
                "Einschlaf-Timer mit langsamem Ausblenden und Wecker mit langsamem Einblenden.",
                "Läuft im Hintergrund und bei gesperrtem Bildschirm; Favoritenliste.",
                "Nur Englisch, ab iOS 12.",
            ],
            "limits": "zuletzt am 30. Oktober 2023 aktualisiert, fast drei Jahre vor dieser Prüfung; zusätzliche Sounds werden als Pakete verkauft.",
        },
        {
            "row": [
                "Gratis; Dark Noise Pro gelistet zu 0,99 €, 2,99 € und 22,99 €, Lifetime 59,99 €",
                "50+ Sounds, eigene Mischungen, Timer mit Ausblenden, Siri-Kurzbefehle, Widgets",
                N,
                "3.6.1 (17.10.2026)",
                "4.6",
            ],
            "best_for": "das gelungenste Design, mit Siri-Kurzbefehlen, Widgets und AirPlay.",
            "facts": [
                "50+ Sounds mit animierten Symbolen und eigenen Mischungen.",
                "Timer mit Ausblenden, Siri-Kurzbefehle (auch vom HomePod), interaktive Widgets und Widgets für den Sperrbildschirm.",
                "10 Designs; nur Englisch.",
            ],
            "limits": "erfordert iOS 26 oder neuer, sodass viele iPhones sie nicht installieren können.",
        },
    ],
    "who": [
        "<strong>Du willst die meisten Geräusche gratis:</strong> White Noise Lite oder Rain Rain.",
        "<strong>Du brauchst weißes, rosa oder braunes Rauschen:</strong> White Noise Lite oder White Noise Deep Sleep Sounds.",
        "<strong>Du willst keine Werbung und einen guten Einschlaf-Timer:</strong> Drop.",
        "<strong>Du magst ein gelungenes Design und Siri-Kurzbefehle und hast iOS 26:</strong> Dark Noise.",
        "<strong>Du willst eine klassische App mit Wecker und Mischungen:</strong> Sleep Pillow – bedenke, dass sie zuletzt 2023 aktualisiert wurde.",
    ],
    "cases": [
        "Bei Regen oder einem Ventilator einschlafen, mit einem Timer, der ausblendet (jede der sechs).",
        "Straßenlärm die ganze Nacht überdecken (White Noise Lite oder Rain Rain, ohne Zeitlimit).",
        "Ein Baby mit weißem Rauschen beruhigen (White Noise Deep Sleep Sounds listet Baby-Sounds und Shusher).",
        "Konzentriert lernen oder arbeiten mit Café-Geräuschen (Drop, White Noise Lite).",
    ],
    "method": [
        "Am 9. November 2026 haben wir die Seite jeder App im deutschen App Store und die Lookup-Daten von Apple geöffnet: In-App-Käufe, Version und Veröffentlichungsdatum, Bewertung, Sprachen, mindestens erforderliche iOS-Version und Datenschutzlabel. Was gratis ist, stammt aus der Beschreibung des jeweiligen Entwicklers; bei Drop zusätzlich aus der App selbst. Bewertungen oder Rezensionen haben wir nicht erfunden, und Klangqualität oder Akkuverbrauch haben wir nicht getestet.",
    ],
    "faq": [
        ("Welche ist die beste kostenlose Einschlaf-App fürs iPhone?",
         "Das hängt davon ab, was du gratis brauchst. White Noise Lite hat 50+ Sounds und keine gelisteten Käufe; Rain Rain hat 50+ kostenlose Sounds mit kleinem Werbebanner; Drop hat 9 kostenlose Sounds ohne Werbung und mit Einschlaf-Timer."),
        ("Welche kostenlose App hat weißes, rosa und braunes Rauschen?",
         "White Noise Lite listet weißes, rosa, braunes, blaues und violettes Rauschen; White Noise Deep Sleep Sounds listet weißes, rosa und braunes Rauschen unter den Gratis-Sounds. Bei Drop ist weißes Rauschen gratis; rosa und braunes Rauschen brauchen Drop Pro."),
        ("Hört die kostenlose Version einer Einschlaf-App nach ein paar Stunden auf?",
         "White Noise Deep Sleep Sounds gibt an, dass die Gratis-Version acht Stunden spielt und Dauerwiedergabe ein Abo braucht. Rain Rain nennt in der Gratis-Version keine Begrenzung der Spielzeit."),
        ("Gibt es eine Einschlaf-App ohne Werbung?",
         "Drop hat keine Werbung. Rain Rain gibt an, keine Audio- oder Videowerbung zu haben, nur einen kleinen Bildbanner. White Noise Lite listet keine Käufe; prüfe die Werbung nach der Installation."),
        ("Welche Einschlaf-App läuft auf älteren iPhones?",
         "Rain Rain und Sleep Pillow verlangen iOS 12 oder neuer, White Noise Lite iOS 15. Dark Noise braucht iOS 26 und Drop iOS 18."),
    ],
}

# ------------------------------------------------------------------ 3. kostenlose Krypto-Tracker
TR_CRYPTO = {
    "title": "Beste kostenlose Krypto-Portfolio-Tracker fürs iPhone (2026)",
    "h1": "Die besten kostenlosen Krypto-Portfolio-Tracker fürs iPhone 2026",
    "description": "Sechs Krypto-Portfolio-Tracker fürs iPhone im Vergleich, danach, was der kostenlose Tarif enthält: Crypton, Crypto Pro, Delta, HODL, CoinGecko und CoinMarketCap.",
    "llms": "Vergleicht sechs kostenlose Krypto-Portfolio-Tracker-Apps fürs iPhone (Crypton, Crypto Pro, Delta, HODL, CoinGecko, CoinMarketCap) nach Grenzen des Gratis-Tarifs, Bezahlstufen, Anmeldepflicht und Datenschutzlabel im deutschen App Store. Keine Finanzberatung.",
    "answer": [
        "Die Gratis-Tarife unterscheiden sich in einem entscheidenden Punkt: den Grenzen. Delta und HODL begrenzen den kostenlosen Tarif auf 10 Assets oder Symbole; CoinGecko nennt keine Grenze und bietet ein manuelles Portfolio; CoinMarketCap verlangt für das Portfolio eine Anmeldung; Crypto Pro sagt nicht, was gratis ist; Crypton hat keine Grenzen und keine Werbung, ist aber eine einfache manuelle Liste ohne Wallet-Synchronisierung und ohne Kurswarnungen.",
        "Wenn du nur deinen Bestand und die Top-Coins sehen willst, reicht jede der Apps. Wenn du kostenlos automatisch mit Börsen und Wallets synchronisieren möchtest, kommt der Gratis-Tarif von Delta dem am nächsten, innerhalb seiner Grenze von 10 Assets.",
    ],
    "columns": ["App", "Preis (DE)", "Was der Gratis-Tarif enthält", "Datenschutzlabel im App Store", "Version (Datum)", "Bewertung (DE)"],
    "table_note": "Alle sechs Apps sind gratis zu laden. Preise sind die im deutschen App Store am 9. November 2026 gelisteten In-App-Käufe (Apps listen für denselben Tarif mehrere Preise). Bewertungen sind der Durchschnitt im App Store an diesem Tag.",
    "apps": [
        {
            "row": [
                "Gratis, keine Werbung, keine In-App-Käufe",
                "Alles: von Hand eingetragenes Portfolio, Watchlist, Charts; keine Grenze gelistet",
                lab(L, N),
                "2.0.8 (24.10.2026)",
                "4.5",
            ],
            "best_for": "ein kostenloser, werbefreier Blick auf die Top-Coins und deinen Bestand, ohne Grenzen, an die du stößt.",
            "facts": [
                "Portfolio mit den von dir eingegebenen Mengen, Wert und Veränderung pro Coin und Kurscharts (1 Tag bis 1 Jahr).",
                "Favoriten und eine Watchlist; laut Eintrag 250+ Coins.",
                "Konto optional, keine Werbung, nichts zu kaufen. Nur Englisch, ab iOS 18.",
            ],
            "limits": "keine Verbindung zu Wallets oder Börsen, keine Kurswarnungen (zwei kostenlose Home-Bildschirm-Widgets seit 2.0.6); die Kurse aktualisieren sich alle paar Stunden, daher nichts zum Handeln.",
        },
        {
            "row": [
                "Gratis; Premium gelistet zu 7,99 €, 31,99 € und 47,99 €",
                "Portfolio und Kurse; Premium für mehr",
                N,
                "10.0.0 (28.10.2026)",
                "4.6",
            ],
            "best_for": "Datenschutz und Apple-Geräte: keine Werbung, Daten auf deinem Gerät, Mac-Menüleiste und Apple Watch.",
            "facts": [
                "Importiert Bestände aus Wallet-Adressen oder Börsen-API-Schlüsseln; Gewinn und Verlust.",
                "Laut Eintrag keine Analyse und keine Nutzerüberwachung und eine optionale iCloud-Synchronisierung; keine Werbung.",
                "Widgets, Face-ID-Sperre, Siri-Kurzbefehle; 66 Sprachen, ab iOS 17.",
            ],
            "limits": "der Eintrag sagt nicht genau, was der Gratis-Tarif enthält; prüfe das, bevor du dich darauf verlässt.",
        },
        {
            "row": [
                "Gratis bis 10 Assets; PRO ab 6,99 € im Monat oder 61,99 € im Jahr; PRO+ mehr",
                "10 Assets, unbegrenzt viele Verbindungen, Kurswarnungen, 3 KI-Nutzungen im Monat",
                lab(T, N),
                "2026.3.2 (5.11.2026)",
                "4.6",
            ],
            "best_for": "Krypto und Aktien zusammen, mit automatischer Synchronisierung, in einem Gratis-Tarif mit höchstens 10 Assets.",
            "facts": [
                "Synchronisiert 200+ Börsen, Broker und Wallets; Aktien, ETFs, Devisen und 10.000+ Coins.",
                "Gratis-Tarif: 10 Assets, unbegrenzt viele Verbindungen, Kurswarnungen und 3 KI-Nutzungen im Monat.",
                "18 Sprachen, ab iOS 16.4.",
            ],
            "limits": "der Gratis-Tarif endet bei 10 Assets, und das Datenschutzlabel nennt Daten, die dich verfolgen.",
        },
        {
            "row": [
                "Gratis (bis 10 Symbole); Premium gelistet ab 6,99 € im Monat bis 83,99 €; Basic 5,99 €",
                "Watchlist und Portfolio bis 10 Symbole, Kurse, Charts, News, Social-Posts, Widget",
                lab(T, L, N),
                "10.0.6 (5.11.2026)",
                "4.7",
            ],
            "best_for": "Krypto und US-Aktien in einer Watchlist, mit News und Social-Posts.",
            "facts": [
                "Gratis: Watchlist und Portfolio mit bis zu 10 Symbolen, Kurse, Charts, News, Social-Posts und ein Widget.",
                "Premium: unbegrenzt viele Symbole und Kurswarnungen mit smarten Bereichen sowie Zusammenfassungen von Wall-Street-Analysen.",
                "Pro bringt laut Eintrag einen KI-Agenten namens Hermes dazu. Nur Englisch, ab iOS 15.1.",
            ],
            "limits": "der Gratis-Tarif endet bei 10 Symbolen, und das Datenschutzlabel nennt Daten, die dich verfolgen, und mit dir verknüpfte Daten.",
        },
        {
            "row": [
                "Gratis; Premium 9,90 € im Monat oder 99,90 € im Jahr",
                "Marktdaten, Portfolio, Warnungen, Widgets und Umrechner; keine Grenze gelistet",
                lab(L, N),
                "3.60.0 (27.10.2026)",
                "4.8",
            ],
            "best_for": "Coins und Kategorien recherchieren, mit einem kostenlosen manuellen Portfolio und Warnungen.",
            "facts": [
                "Echtzeitdaten zu 10.000+ Coins, Börsenvolumen und 3.000+ NFT-Kollektionen.",
                "Portfolio mit Gewinn und Verlust, Kurswarnungen, Widgets und Umrechner.",
                "Nur Englisch, ab iOS 16.",
            ],
            "limits": "das Portfolio ist manuell (keine Kontosynchronisierung), und Premium kostet 9,90 € im Monat.",
        },
        {
            "row": [
                "Gratis; Bezahltarife von Essential 12,99 € im Monat bis Max 129,99 €",
                "Kurse, Watchlists, News, Kurswarnungen und ein Portfolio-Tracker; das Portfolio braucht eine Anmeldung",
                lab(T, L, N),
                "5.24.0 (1.11.2026)",
                "4.7",
            ],
            "best_for": "die größte Kursdatenbank und News in einer kostenlosen App, wenn du dich fürs Portfolio anmeldest.",
            "facts": [
                "Portfolio-Tracker in 90+ Fiat-Währungen, Watchlists und Kurswarnungen.",
                "Krypto-News und Markttrends in derselben App.",
                "21 Sprachen, ab iOS 15.",
            ],
            "limits": "das Portfolio braucht ein Konto, das Datenschutzlabel nennt Daten, die dich verfolgen, und die Bezahltarife gehen bis 129,99 € im Monat.",
        },
    ],
    "who": [
        "<strong>Du willst null Grenzen und keine Werbung und trägst deinen Bestand von Hand ein:</strong> Crypton.",
        "<strong>Dir sind Datenschutz sowie Apple Watch und Mac wichtig:</strong> Crypto Pro.",
        "<strong>Du willst automatische Synchronisierung und hast höchstens 10 Assets:</strong> Delta.",
        "<strong>Du hältst Krypto und US-Aktien:</strong> HODL oder Delta.",
        "<strong>Du recherchierst Coins genauso viel, wie du sie trackst:</strong> CoinGecko oder CoinMarketCap.",
    ],
    "cases": [
        "Morgens kurz den Wert deines Bestands prüfen (Crypton, CoinGecko).",
        "Höchstens 10 Coins mit Warnungen im Blick behalten (Gratis-Tarife von HODL und Delta).",
        "Wallets und Börsen tracken, ohne zu zahlen (Delta, innerhalb der Grenze).",
        "Einen Coin nachschlagen, bevor du ihn kaufst (CoinGecko, CoinMarketCap).",
    ],
    "method": [
        "Am 9. November 2026 haben wir die Seite jeder App im deutschen App Store und die Lookup-Daten von Apple geöffnet: In-App-Käufe, Version und Veröffentlichungsdatum, Bewertung, Sprachen, mindestens erforderliche iOS-Version und Datenschutzlabel. Die Grenzen der Gratis-Tarife sind die, die der jeweilige Entwickler auf seiner Seite nennt; die Grenzen von Crypton stammen aus unserem eigenen Test der Version 2.0.4. Bewertungen oder Rezensionen haben wir nicht erfunden, und nichts davon ist Finanzberatung.",
    ],
    "faq": [
        ("Welcher ist der beste kostenlose Krypto-Portfolio-Tracker fürs iPhone?",
         "Das hängt davon ab, ob du Synchronisierung brauchst. Für eine kostenlose manuelle Liste ohne Grenzen Crypton oder CoinGecko; für automatische Synchronisierung Delta (bis 10 Assets); für News und Recherche CoinMarketCap."),
        ("Welcher kostenlose Krypto-Tracker hat keine Asset-Grenze?",
         "Crypton und CoinGecko nennen im Gratis-Tarif keine Obergrenze. Delta und HODL begrenzen den Gratis-Tarif auf 10."),
        ("Welcher kostenlose Tracker verbindet sich mit Börsen und Wallets?",
         "Der Gratis-Tarif von Delta listet unbegrenzt viele Verbindungen innerhalb seiner Grenze von 10 Assets; Crypto Pro listet Importe aus Wallet-Adressen und Börsen-API-Schlüsseln. Crypton verbindet sich mit keiner."),
        ("Welcher Krypto-Tracker hat keine Werbung und sammelt am wenigsten Daten?",
         "Crypto Pro hat das kürzeste Datenschutzlabel (nur nicht mit dir verknüpfte Daten) und gibt an, weder Analyse noch Werbung zu haben. Crypton hat keine Werbung; sein Label nennt mit dir verknüpfte und nicht verknüpfte Daten."),
        ("Ist das eine Finanzberatung?",
         "Nein. Diese Seite vergleicht Funktionen, Preise und Bewertungen, wie sie im App Store stehen."),
    ],
}

# ------------------------------------------------------------------ 4. Foto-Tresor
TR_VAULT = {
    "title": "Fotos verstecken am iPhone: Tresor-Apps im Datenschutzvergleich",
    "h1": "Die besten Foto-Tresor-Apps zum Fotos verstecken am iPhone 2026: Datenschutzlabel im Vergleich",
    "description": "Sechs Foto-Tresor-Apps fürs iPhone nach Datenschutzlabel verglichen; nur eine sagt „Daten werden nicht erfasst“. Safe Lock, Photo Vault, Keepsafe und mehr.",
    "llms": "Vergleicht sechs Foto-Tresor-Apps fürs iPhone (Photo Vault, Safe Lock, Keepsafe, Private Photo Vault, Privault, PV) nach Datenschutzlabel, Preis und Cloud-Backup im deutschen App Store. Nur Safe Lock gibt „Daten werden nicht erfasst“ an.",
    "answer": [
        "Um Fotos auf dem iPhone zu verstecken, gibt von den sechs Apps heute nur Safe Lock im Datenschutzlabel <em>Daten werden nicht erfasst</em> an. Die anderen fünf nennen Daten, die dich verfolgen, mit dir verknüpfte Daten oder beides – auch Photo Vault: Hide Pics Video, dessen Label mit dir verknüpfte Daten aufführt. Ein Datenschutzlabel ist die Angabe des Entwicklers, kein unabhängiges Audit.",
        "Wenn du zusätzlich eine private Cloud willst, hat Keepsafe unter den Cloud-Optionen das kürzeste Label (zwei Einträge, ohne mit dir verknüpfte Daten); Private Photo Vault hat die meisten Funktionen, und sein Label enthält mit dir verknüpfte Daten.",
    ],
    "columns": ["App", "Preis (DE)", "Cloud-Backup", "Datenschutzlabel im App Store", "Version (Datum)", "Bewertung (DE)"],
    "table_note": "Alle sechs Apps sind gratis zu laden. Preise sind die im deutschen App Store am 9. November 2026 gelisteten In-App-Käufe (Apps listen für denselben Tarif mehrere Preise). Bewertungen sind der Durchschnitt im App Store an diesem Tag; „–“ heißt, dass dort noch keine Bewertung angezeigt wird. Das Datenschutzlabel ist das, was jeder Entwickler gegenüber Apple angibt.",
    "apps": [
        {
            "row": [
                "Gratis zu laden; Premium jährlich 22,99 € oder 34,99 €, Lifetime 17,99 € oder 34,99 €",
                "Kein Konto; optionale Ende-zu-Ende-verschlüsselte Kopie in deiner eigenen iCloud (Premium, standardmäßig aus)",
                L,
                "1.4 (6.11.2026)",
                "–",
            ],
            "best_for": "Face ID, Passwörter pro Album, getarntes Symbol und eine private Kamera, mit einem Label, das nur mit dir verknüpfte Daten nennt.",
            "facts": [
                "Label: Mit dir verknüpfte Daten. Entsperren mit Face ID, Touch ID oder Code; jedes Album kann ein eigenes Passwort haben; ein Ködercode (Premium) öffnet einen separaten Tresor.",
                "Getarntes Symbol (Taschenrechner, Notizen oder Wetter) und Beenden durch Umdrehen des Geräts.",
                "Kein Konto; eine optionale Ende-zu-Ende-verschlüsselte Kopie in deiner eigenen iCloud (standardmäßig aus); für ein neues iPhone exportierst du eine passwortgeschützte Datei. 19 Sprachen, ab iOS 17.",
            ],
            "limits": "kein automatisches Backup, solange du die iCloud-Kopie nicht einschaltest; die Gratis-Version ist eingeschränkt.",
        },
        {
            "row": [
                "Gratis; Premium 5,99 €, 22,99 € oder 34,99 €",
                "Keines gelistet: Laut Entwickler bleiben die Fotos auf dem Gerät",
                NC,
                "3.1 (17.8.2026)",
                "4.8",
            ],
            "best_for": "die einzige Tresor-App hier mit dem Label „Daten werden nicht erfasst“, mit vielen Sperrarten und einer versteckten Kamera.",
            "facts": [
                "Label: Daten werden nicht erfasst. Sperren: PIN, DotLock, numerisches oder alphabetisches Passwort, Touch ID und Face ID.",
                "Versteckte Kamera in der App; geheime Ordner für Fotos, Videos und Notizen.",
                "Laut Entwickler werden Fotos und Videos nur auf deinem Gerät gespeichert. 13 Sprachen, ab iOS 12.",
            ],
            "limits": "der Eintrag beschreibt keinen verschlüsselten Export für den Umzug auf ein neues iPhone.",
        },
        {
            "row": [
                "Gratis; Premium von 4,99 € bis 38,99 € (Jahresprämie 26,49 €, Monatsprämie 10,99 €)",
                "Optionale Private Cloud (Premium)",
                lab(T, N),
                "13.35.0 (26.10.2026)",
                "4.6",
            ],
            "best_for": "ein kurzes Label (zwei Einträge) mit optionaler privater Cloud.",
            "facts": [
                "Label: Daten, die dich verfolgen, und nicht mit dir verknüpfte Daten; keine Kontaktdaten oder Fotos gelistet.",
                "PIN, Touch ID, Albumsperre mit getrennten PINs (Premium), Safe Send.",
                "16 Sprachen, ab iOS 17.",
            ],
            "limits": "das Label enthält Tracking-Daten, und Cloud sowie Albumsperren brauchen Premium.",
        },
        {
            "row": [
                "Gratis; Premium 7,99 €, 12,99 €, 35,99 € und 39,99 €",
                "Optionaler verschlüsselter Cloud Vault",
                lab(T, L),
                "26.1 (5.11.2026)",
                "4.7",
            ],
            "best_for": "der bekannteste Tresor mit den meisten Funktionen, wenn du ein langes Datenschutzlabel akzeptierst.",
            "facts": [
                "Label: Daten, die dich verfolgen, und mit dir verknüpfte Daten.",
                "Einbruchsbericht mit Foto und GPS, Ködercode, Sperre beim Umdrehen des Geräts, privater Browser.",
                "11 Sprachen, ab iOS 15.",
            ],
            "limits": "das Label enthält mit dir verknüpfte Daten, und mehrere Funktionen brauchen Premium.",
        },
        {
            "row": [
                "Gratis (mit Werbung); Pro 3,49 € im Monat, 29,99 € im Jahr oder 49,99 € einmalig; Werbung entfernen 2,99 €",
                "Keines: auf dem Gerät",
                lab(T, L, N),
                "10.2 (28.2.2025)",
                "–",
            ],
            "best_for": "ein zweiter Code, der einen Köderordner öffnet.",
            "facts": [
                "Hauptcode, ein zweiter Code für einen Köderbereich und ein Code, der alles löscht.",
                "Videoplayer, der laut Entwickler rund 150 Medienformate öffnet.",
                "12 Sprachen, ab iOS 11.",
            ],
            "limits": "zuletzt am 28. Februar 2025 aktualisiert, zeigt Werbung, solange du nicht zahlst, und das Label nennt Tracking-Daten.",
        },
        {
            "row": [
                "Gratis (mit Werbung); Pro 3,99 € im Monat oder 19,99 € im Jahr, Lifetime 49,99 €",
                "Optionale Cloud-Backup-Tarife",
                lab(T, L, N),
                "7.7.9 (26.10.2026)",
                "4.6",
            ],
            "best_for": "die längste Funktionsliste zu niedrigen Abo-Preisen.",
            "facts": [
                "Laut Eintrag unbegrenzter Gratis-Speicher; Passwort und Face ID, Fake-Passwort, anpassbares Symbol.",
                "Tags, Notizen und Suche, Fotoeditor und Nearby Drop.",
                "12 Sprachen, ab iOS 17.",
            ],
            "limits": "die Gratis-Version zeigt Werbung, und das Label enthält Tracking-Daten sowie verknüpfte und nicht verknüpfte Daten.",
        },
    ],
    "who": [
        "<strong>Du willst, dass nichts erfasst wird:</strong> Safe Lock.",
        "<strong>Du willst eine private Cloud mit dem kürzesten Label:</strong> Keepsafe.",
        "<strong>Du willst die meisten Funktionen und akzeptierst ein langes Label:</strong> Private Photo Vault.",
        "<strong>Du willst einen Ködercode:</strong> Privault oder Photo Vault: Hide Pics Video (dort mit Premium).",
        "<strong>Du willst niedrige Abo-Preise:</strong> PV.",
    ],
    "cases": [
        "Private Fotos aus dem gemeinsamen Fotoarchiv und aus der Cloud heraushalten (Safe Lock, Photo Vault: Hide Pics Video).",
        "Dein Handy jemandem geben, ohne dass er die App sieht (getarnte Symbole, Ködercodes).",
        "Einen Tresor sichern, damit ein verlorenes Handy nicht die Fotos kostet (Keepsafe, Private Photo Vault, PV mit ihrer Cloud).",
        "Prüfen, was eine App laut Label erfasst, bevor du private Fotos hineinlegst (das Datenschutzlabel in der Tabelle).",
    ],
    "method": [
        "Am 9. November 2026 haben wir die Seite jeder App im deutschen App Store und die Lookup-Daten von Apple geöffnet: In-App-Käufe, Version und Veröffentlichungsdatum, Bewertung, Sprachen, mindestens erforderliche iOS-Version und das Datenschutzlabel genau so, wie es angegeben ist. Die Funktionen sind die, die der jeweilige Entwickler auf seiner Seite nennt; Verschlüsselung haben wir nicht überprüft und Datenpraktiken nicht auditiert. Bewertungen oder Rezensionen haben wir nicht erfunden.",
    ],
    "faq": [
        ("Welche Foto-Tresor-Apps sagen „Daten werden nicht erfasst“?",
         "Am 9. November 2026 nur Safe Lock - Hidden Photo Vault. Photo Vault: Hide Pics Video, Keepsafe, Private Photo Vault, Privault und PV nennen Daten, die dich verfolgen, oder mit dir verknüpfte Daten."),
        ("Heißt „Daten werden nicht erfasst“, dass meine Fotos sicher sind?",
         "Es heißt, dass der Entwickler gegenüber Apple angibt, keine Daten aus der App zu erfassen. Es ist kein Audit und sagt nichts darüber, wie gut deine Fotos auf dem Handy geschützt sind."),
        ("Welcher Foto-Tresor hat eine private Cloud?",
         "Keepsafe (Private Cloud, Premium), Private Photo Vault (Cloud Vault) und PV (Cloud-Tarife). Safe Lock behält die Fotos auf dem Gerät; Photo Vault: Hide Pics Video bietet eine optionale verschlüsselte Kopie in deiner eigenen iCloud."),
        ("Ist Photo Vault: Hide Pics Video dasselbe wie Private Photo Vault?",
         "Nein. Es sind verschiedene Apps von verschiedenen Entwicklern."),
        ("Brauche ich überhaupt eine Tresor-App?",
         "Nicht immer. Das iPhone hat in Fotos ein Album „Ausgeblendet“, das du bei neueren iOS-Versionen mit Face ID oder Code sperren kannst; eine Tresor-App bietet zusätzlich getrennte Alben, getarnte Symbole und weitere Funktionen."),
    ],
}

PAGES = [
    make("simple-todo", "de", TR_TODO, "de"),
    make("free-sleep-sounds", "de", TR_SLEEP, "de"),
    make("free-crypto-trackers", "de", TR_CRYPTO, "de"),
    make("vault-no-data", "de", TR_VAULT, "de"),
]
