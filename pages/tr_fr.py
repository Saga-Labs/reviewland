from pages.trlib import make

# ---------------------------------------------------------------- simple-todo
TR_TODO = {
    "title": "Meilleures applis de to-do list simples pour iPhone (2026)",
    "h1": "Meilleures applications de liste de tâches simples pour iPhone en 2026",
    "description": "Six applis de to-do list simples pour iPhone comparées : 3 Tasks, Do!, MinimaList, Clear, Microsoft To Do et Todoist. Prix, compte et confidentialité vérifiés.",
    "llms": "Compare six applis de liste de tâches simples pour iPhone (3 Tasks, Do!, MinimaList, Clear, Microsoft To Do, Todoist) : prix, compte requis, rappels et widgets, étiquette de confidentialité.",
    "answer": [
        "La meilleure appli de to-do list simple sur iPhone est celle qui vous limite : 3 Tasks ne vous laisse écrire que trois priorités par jour et chronomètre chacune, gratuitement, sans compte ni abonnement (un Pro facultatif s’achète en une fois). Si vous voulez une liste classique qui reste simple, Do! et MinimaList ajoutent rappels et widgets, et Microsoft To Do est entièrement gratuit avec synchronisation via un compte Microsoft.",
        "Todoist est la plus complète des six, mais son offre Pro est un abonnement (6,99 € par mois ou 59,99 € par an en France).",
    ],
    "columns": ["App", "Prix (France)", "Ce qui la rend simple", "Compte", "Étiquette de confidentialité App Store", "Version (date)", "Note (France)"],
    "table_note": "Les prix sont ceux des achats intégrés de l’App Store français le 9 novembre 2026 ; les six applis se téléchargent gratuitement. Les notes sont la moyenne App Store de ce jour-là.",
    "apps": [
        {
            "row": [
                "Gratuit ; 3 Tasks Pro est un achat unique (affiché à 5,99 € et 9,99 €)",
                "Seulement 3 tâches par jour, un seul écran, un minuteur par tâche",
                "Sans compte",
                "Données utilisées pour vous suivre ; Données non liées à vous",
                "1.4.6 (5 nov. 2026)",
                "4,5",
            ],
            "best_for": "ceux qui se noient dans les longues listes et veulent choisir les trois choses qui comptent aujourd’hui.",
            "facts": [
                "Notez trois priorités par jour ; rien d’autre à configurer.",
                "Démarrez et mettez en pause chaque tâche, façon Pomodoro, et voyez le temps passé dessus.",
                "Pas de publicité ni de compte. L’appli utilise Firebase Analytics pour compter l’usage des tâches et des minuteurs, ce qui explique les données de suivi dans son étiquette de confidentialité.",
                "33 langues, iOS 18 ou ultérieur.",
            ],
            "limits": "pas de rappels ni de synchronisation entre appareils : c’est volontairement une liste d’un jour, limitée à trois (elle propose tout de même la répétition quotidienne et un widget d’écran d’accueil, gratuits).",
        },
        {
            "row": [
                "Gratuit avec publicités ; suppression des pubs 22,00 € en une fois ; pourboire 0,99 €",
                "On ajoute une tâche, double-tap quand c’est fait ; groupes et couleurs",
                "Non précisé",
                "Données utilisées pour vous suivre ; Données liées à vous ; Données non liées à vous",
                "7.9.0 (22 oct. 2026)",
                "4,7",
            ],
            "best_for": "une liste du quotidien façon papier, avec rappels et tâches récurrentes.",
            "facts": [
                "Thèmes, polices et sons de stylo sur papier.",
                "Groupes pour le travail, les études et les courses ; tâches épinglées.",
                "Tâches récurrentes (du quotidien à l’annuel) et rappels.",
                "5 langues, iOS 15 ou ultérieur.",
            ],
            "limits": "affiche des publicités sauf si vous payez 22,00 € une fois, et son étiquette de confidentialité inclut des données utilisées pour vous suivre.",
        },
        {
            "row": [
                "À vie à partir de 6,99 € (offres) jusqu’à 9,99 € ; famille 17,99 € ; ou 2,99 € par mois",
                "Listes colorées, saisie intelligente qui détecte les heures",
                "Non précisé",
                "Données non liées à vous",
                "2.27.9 (30 oct. 2026)",
                "4,7",
            ],
            "best_for": "une liste à l’allure minimaliste qui offre pourtant widgets, listes partagées et rappels géolocalisés.",
            "facts": [
                "Widgets d’écran d’accueil et d’écran verrouillé.",
                "Rappels selon l’heure ou le lieu, sous-tâches et listes partagées.",
                "Fonctionne avec Siri ; sur iPhone, iPad et Mac selon le développeur.",
                "10 langues, iOS 15 ou ultérieur.",
            ],
            "limits": "plusieurs prix qui se chevauchent pour la même formule à vie, ce qui rend difficile de savoir ce que vous paierez.",
        },
        {
            "row": [
                "Clear Pro 3,49 € ; Pro ancienne formule 2,99 € par mois ; packs de sons",
                "Listes entièrement gestuelles, carte thermique des priorités par couleur",
                "Non précisé",
                "Données utilisées pour vous suivre ; Données non liées à vous",
                "2.8.7 (31 oct. 2026)",
                "4,3",
            ],
            "best_for": "ceux qui aiment les listes qu’on balaye du doigt, sans aucun bouton à l’écran.",
            "facts": [
                "Balayez pour terminer, pincez et glissez pour réordonner ; une carte thermique montre la priorité.",
                "Kanban quotidien (aujourd’hui, demain, après-demain), routines et rappels.",
                "2 langues, iOS 16 ou ultérieur.",
            ],
            "limits": "les gestes demandent quelques minutes d’apprentissage, et son étiquette de confidentialité inclut des données utilisées pour vous suivre.",
        },
        {
            "row": [
                "Gratuit, sans achats intégrés",
                "Mon jour avec des tâches suggérées",
                "Compte Microsoft pour la synchronisation",
                "Données liées à vous",
                "2.177 (6 juil. 2026)",
                "4,7",
            ],
            "best_for": "une liste gratuite qui se synchronise partout, surtout si vous utilisez Outlook ou Microsoft 365.",
            "facts": [
                "Mon jour et les suggestions aident à planifier la journée à partir de toutes vos listes.",
                "Se synchronise avec Microsoft 365 ; les e-mails Outlook marqués peuvent devenir des tâches.",
                "Listes partagées pour les comptes personnels.",
                "34 langues, iOS 17.6 ou ultérieur.",
            ],
            "limits": "c’est un gestionnaire de tâches complet, avec listes, étapes et suggestions : il peut devenir les longues listes qu’une appli simple cherche à éviter.",
        },
        {
            "row": [
                "Pro 6,99 € par mois ou 59,99 € par an",
                "Ajout rapide en langage naturel et saisie vocale",
                "Oui",
                "Données liées à vous",
                "26.10.35 (2 nov. 2026)",
                "4,7",
            ],
            "best_for": "ceux dont la liste dépasse une appli simple et qui veulent projets, échéances et travail d’équipe.",
            "facts": [
                "L’ajout rapide comprend les dates en langage courant ; Ramble transforme la voix en tâches.",
                "Projets, vue calendrier et espaces d’équipe.",
                "Fonctionne avec Siri. 19 langues, iOS 17 ou ultérieur.",
            ],
            "limits": "Pro est un abonnement, et c’est l’appli la moins simple de cette sélection.",
        },
    ],
    "who": [
        "<strong>Vous écrivez des listes que vous ne finissez jamais :</strong> 3 Tasks, trois par jour et pas plus.",
        "<strong>Vous voulez des rappels et des tâches récurrentes dans un design calme :</strong> Do! ou MinimaList.",
        "<strong>Vous voulez tout gratuit et synchronisé :</strong> Microsoft To Do.",
        "<strong>Vous aimez les gestes et pas de boutons :</strong> Clear.",
        "<strong>Il vous faut des projets, des échéances et du travail partagé :</strong> Todoist.",
    ],
    "cases": [
        "Choisir les trois choses à faire absolument aujourd’hui avant d’ouvrir sa messagerie.",
        "Une liste de courses ou de commissions qui vous rappelle quand vous arrivez au magasin (MinimaList).",
        "Des tâches de travail issues d’e-mails Outlook marqués (Microsoft To Do).",
        "Chronométrer des blocs de travail concentré sur chaque priorité (3 Tasks).",
    ],
    "method": [
        "Le 9 novembre 2026, nous avons ouvert la page App Store France de chaque appli et les données de recherche d’Apple : achats intégrés, version et date de sortie, note, langues, version minimale d’iOS et étiquette de confidentialité. Les fonctionnalités sont celles que chaque développeur indique sur sa page App Store. « Non précisé » signifie que la fiche ne dit pas si un compte est nécessaire. Nous n’avons inventé ni notes ni avis."
    ],
    "faq": [
        ("Quelle est l’appli de to-do list la plus simple pour iPhone ?",
         "3 Tasks ne vous laisse écrire que trois tâches par jour sur un seul écran. Parmi les applis de listes classiques, Do! et Clear sont les plus minimalistes."),
        ("Existe-t-il une appli de to-do list gratuite sans abonnement ?",
         "Microsoft To Do est gratuit et sans achats intégrés, et 3 Tasks est gratuit avec un Pro facultatif en achat unique (sans abonnement). Do! est gratuit avec publicités et 22,00 € en une fois pour les supprimer ; MinimaList et Clear proposent aussi des formules à achat unique."),
        ("Quelle appli de tâches fonctionne sans compte ?",
         "3 Tasks n’exige aucun compte. Microsoft To Do utilise un compte Microsoft pour synchroniser, et Todoist son propre compte."),
        ("Pourquoi se limiter à trois tâches par jour ?",
         "Une liste courte oblige à choisir ce qui compte le plus, donc la liste se termine au lieu de s’allonger. C’est l’idée de 3 Tasks."),
        ("Quelle appli de tâches simple propose des widgets ?",
         "MinimaList a des widgets d’écran d’accueil et d’écran verrouillé. 3 Tasks a un widget d’écran d’accueil gratuit."),
    ],
}

# ---------------------------------------------------------------- free-sleep-sounds
TR_SLEEP = {
    "title": "Meilleures applis gratuites de sons pour dormir sur iPhone (2026)",
    "h1": "Meilleures applications gratuites de sons pour dormir et bruit blanc sur iPhone en 2026",
    "description": "Six applis de sons pour dormir et de bruit blanc pour iPhone comparées selon ce qui est vraiment gratuit : Drop, White Noise Lite, Rain Rain et d’autres. Vérifiées sur l’App Store.",
    "llms": "Compare six applis de sons pour dormir sur iPhone (Drop, White Noise Lite, Rain Rain, White Noise Deep Sleep Sounds, Sleep Pillow, Dark Noise) : part gratuite, publicités, minuteurs, prix de l’offre payante et étiquette de confidentialité.",
    "answer": [
        "Pour avoir le plus de sons gratuitement, White Noise Lite (plus de 50 sons, aucun achat listé) et Rain Rain (plus de 50 sons, une petite bannière publicitaire) sont les plus généreuses. Pour du bruit blanc, rose et brun gratuit, White Noise Lite et White Noise Deep Sleep Sounds les listent toutes deux. Si vous voulez des sons gratuits sans aucune publicité et un minuteur de sommeil, Drop offre 9 de ses 53 sons, dont le bruit blanc ; les bruits rose et brun demandent Drop Pro.",
        "Les six se téléchargent gratuitement. Ce qui change, c’est la part qui reste gratuite, la présence de publicités et la durée de lecture du son ; tout figure dans le tableau.",
    ],
    "columns": ["App", "Prix (France)", "Ce qui est gratuit", "Étiquette de confidentialité App Store", "Version (date)", "Note (France)"],
    "table_note": "Les prix sont ceux des achats intégrés de l’App Store français le 9 novembre 2026 (une appli peut lister plusieurs prix pour la même formule). Les notes sont la moyenne App Store de ce jour-là.",
    "apps": [
        {
            "row": [
                "Gratuit : 9 sons sur 53, sans pub ; Drop Pro mensuel 5,99 € ou options à vie",
                "Bruit blanc, feu de cheminée, forêt, battements de cœur, lac, café, neige qui tombe, vent du désert et dauphins ; minuteur de sommeil avec fondu de 30 secondes",
                "Données liées à vous ; Données non liées à vous",
                "2.15 (5 nov. 2026)",
                "5,0",
            ],
            "best_for": "des sons apaisants gratuits et sans pub, avec un vrai minuteur de sommeil et un court guide de respiration.",
            "facts": [
                "9 sons gratuits sans bannière publicitaire : bruit blanc, feu de cheminée, forêt, battements de cœur, lac, café, neige qui tombe, vent du désert et dauphins.",
                "Minuteur de sommeil de 15, 30 ou 45 minutes, 1, 2 ou 8 heures, avec fondu de 30 secondes ; fonctionne hors connexion.",
                "Séances de respiration de 2 à 20 minutes et une plante qui pousse au fil de votre pratique.",
                "33 langues, iOS 18 ou ultérieur.",
            ],
            "limits": "seuls 9 sons sont gratuits et les 44 autres (pluie, océan, bruits rose et brun notamment) demandent Drop Pro ; pas de mixeur ; exige iOS 18.",
        },
        {
            "row": [
                "Gratuit, aucun achat intégré listé",
                "Plus de 50 sons en boucle dont bruits blanc, rose et brun ; minuteurs et alarmes avec fondus",
                "Données utilisées pour vous suivre ; Données liées à vous ; Données non liées à vous",
                "9.0.6 (7 nov. 2026)",
                "4,7",
            ],
            "best_for": "le plus de sons gratuits sans payer : de vraies couleurs de bruit, un mixeur et des minuteurs.",
            "facts": [
                "Plus de 50 sons en boucle, dont les bruits blanc, rose, brun, bleu et violet.",
                "Mix Pad pour créer des mélanges ; audio en arrière-plan pour utiliser d’autres applis.",
                "Minuteurs et alarmes avec fondu d’entrée et de sortie.",
                "3 langues (anglais, français, espagnol), iOS 15 ou ultérieur.",
            ],
            "limits": "pas de méditation ni de respiration, et son étiquette de confidentialité inclut des données utilisées pour vous suivre.",
        },
        {
            "row": [
                "Gratuit (plus de 50 sons, petite bannière) ; Premium à partir de 4,49 € (30,99 € ou 39,99 € par an) ; packs de sons 5,99 €",
                "Plus de 50 sons HD gratuits, sans limite de lecture, toutes les options de fondu, mixeur",
                "Données utilisées pour vous suivre ; Données liées à vous ; Données non liées à vous",
                "6.9.10 (22 janv. 2025)",
                "4,8",
            ],
            "best_for": "beaucoup de sons de pluie et de nature gratuits et sans limite de durée, si vous acceptez une petite bannière.",
            "facts": [
                "Selon sa fiche, la version gratuite offre plus de 50 sons HD, aucune limite de durée de lecture, toutes les options de minuteur avec fondu et un mixeur avec volume par son.",
                "Pas de pubs audio ni vidéo, seulement une petite bannière image en bas ; Premium ajoute plus de 60 sons et la retire.",
                "4 langues (anglais, français, italien, espagnol), iOS 12 ou ultérieur.",
            ],
            "limits": "dernière mise à jour le 22 janvier 2025, et son étiquette de confidentialité inclut des données utilisées pour vous suivre.",
        },
        {
            "row": [
                "Gratuit (lecture de 8 heures d’affilée) ; Lecture continue 5,99 € ; Premium de 1,99 € par semaine à 59,99 € en famille",
                "Plus de 30 sons gratuits dont bruits blanc, rose et brun ; mixeur, minuteur de sommeil, widget",
                "Données liées à vous ; Données non liées à vous",
                "3.45.0 (25 sept. 2026)",
                "4,6",
            ],
            "best_for": "une grande bibliothèque (plus de 250 sons premium en plus) avec plus de 30 sons gratuits, dont bruits blanc, rose et brun, pour adultes et bébés.",
            "facts": [
                "Parmi les sons gratuits listés : ventilateur, shh pour bébé, aspirateur, cabine d’avion, pluie, tonnerre, vagues, et bruits blanc, rose et brun.",
                "Minuteur de sommeil, mélange de sons, widget, AirPlay 2.",
                "Selon sa fiche, la version gratuite joue les sons pendant huit heures ; la lecture continue demande un abonnement.",
                "33 langues, iOS 15 ou ultérieur.",
            ],
            "limits": "la version gratuite s’arrête après huit heures : c’est suffisant pour une nuit, pas pour un usage toute la journée ; de nombreux prix différents.",
        },
        {
            "row": [
                "Gratuit ; packs de sons de 9,99 € à 22,99 € ; abonnement à tous les packs 4,99 €",
                "Sons enregistrés dans la nature, jusqu’à 300 000 mélanges, minuteur de sommeil, réveil",
                "Données non liées à vous",
                "8.0.4 (30 oct. 2023)",
                "4,9",
            ],
            "best_for": "une appli de sons pour dormir classique, avec minuteur de sommeil, réveil et mélanges.",
            "facts": [
                "Minuteur de sommeil avec fondu lent et réveil avec fondu d’entrée progressif.",
                "Fonctionne en arrière-plan et écran verrouillé ; liste de favoris.",
                "Anglais uniquement, iOS 12 ou ultérieur.",
            ],
            "limits": "dernière mise à jour le 30 octobre 2023, soit près de trois ans avant cette vérification ; les sons supplémentaires se vendent en packs.",
        },
        {
            "row": [
                "Gratuit ; Dark Noise Pro listé à 0,99 €, 2,99 €, 22,99 € et à vie 59,99 €",
                "Plus de 50 sons, mélanges personnalisés, minuteur avec fondu, raccourcis Siri, widgets",
                "Données non liées à vous",
                "3.6.1 (17 oct. 2026)",
                "4,6",
            ],
            "best_for": "le design le plus soigné, avec raccourcis Siri, widgets et AirPlay.",
            "facts": [
                "Plus de 50 sons avec icônes animées et mélanges personnalisés.",
                "Minuteur avec fondu de sortie, raccourcis Siri (aussi depuis un HomePod), widgets interactifs et widgets d’écran verrouillé.",
                "10 thèmes ; anglais uniquement.",
            ],
            "limits": "elle exige iOS 26 ou ultérieur, donc beaucoup d’iPhone ne peuvent pas l’installer.",
        },
    ],
    "who": [
        "<strong>Vous voulez le plus de sons gratuits :</strong> White Noise Lite ou Rain Rain.",
        "<strong>Il vous faut du bruit blanc, rose ou brun :</strong> White Noise Lite ou White Noise Deep Sleep Sounds.",
        "<strong>Vous voulez zéro pub et un bon minuteur de sommeil :</strong> Drop.",
        "<strong>Vous aimez le design soigné et les raccourcis Siri, et avez iOS 26 :</strong> Dark Noise.",
        "<strong>Vous voulez une appli classique avec réveil et mélanges :</strong> Sleep Pillow, en sachant qu’elle n’a pas été mise à jour depuis 2023.",
    ],
    "cases": [
        "S’endormir avec de la pluie ou un ventilateur et un minuteur qui s’éteint en fondu (n’importe laquelle des six).",
        "Masquer le bruit de la rue toute la nuit (White Noise Lite ou Rain Rain, sans limite de durée).",
        "Apaiser un bébé avec du bruit blanc (White Noise Deep Sleep Sounds liste des sons pour bébé et des shh).",
        "Se concentrer ou réviser avec un fond de café (Drop, White Noise Lite).",
    ],
    "method": [
        "Le 9 novembre 2026, nous avons ouvert la page App Store France de chaque appli et les données de recherche d’Apple : achats intégrés, version et date de sortie, note, langues, version minimale d’iOS et étiquette de confidentialité. Ce qui est gratuit vient de la description de chaque développeur ; pour Drop, de l’appli elle-même (version 2.10, mise à jour le 24 octobre 2026). Nous n’avons inventé ni notes ni avis et n’avons testé ni la qualité audio ni la consommation de batterie."
    ],
    "faq": [
        ("Quelle est la meilleure appli gratuite de sons pour dormir sur iPhone ?",
         "Cela dépend de ce dont vous avez besoin gratuitement. White Noise Lite offre plus de 50 sons sans achat listé ; Rain Rain, plus de 50 sons gratuits avec une petite bannière ; Drop, 9 sons gratuits sans pub et avec minuteur de sommeil."),
        ("Quelle appli gratuite propose bruit blanc, bruit rose et bruit brun ?",
         "White Noise Lite liste les bruits blanc, rose, brun, bleu et violet ; White Noise Deep Sleep Sounds liste les bruits blanc, rose et brun parmi ses sons gratuits. Drop offre le bruit blanc gratuitement ; ses bruits rose et brun demandent Drop Pro."),
        ("La version gratuite d’une appli de sons pour dormir s’arrête-t-elle au bout de quelques heures ?",
         "White Noise Deep Sleep Sounds indique que sa version gratuite joue huit heures et que la lecture continue demande un abonnement. Rain Rain ne liste aucune limite de lecture dans sa version gratuite."),
        ("Existe-t-il une appli de sons pour dormir sans publicité ?",
         "Drop n’a pas de pub. Rain Rain dit n’avoir ni pubs audio ni vidéo, seulement une petite bannière image. White Noise Lite ne liste aucun achat ; vérifiez ses publicités à l’installation."),
        ("Quelle appli de sons pour dormir fonctionne sur un ancien iPhone ?",
         "Rain Rain et Sleep Pillow demandent iOS 12 ou ultérieur, White Noise Lite iOS 15. Dark Noise exige iOS 26 et Drop iOS 18."),
    ],
}

# ---------------------------------------------------------------- free-crypto-trackers
TR_CRYPTO = {
    "title": "Meilleures applis gratuites de suivi de portefeuille crypto iPhone",
    "h1": "Meilleures applications gratuites de suivi de portefeuille crypto pour iPhone en 2026",
    "description": "Six applis de suivi de portefeuille crypto pour iPhone comparées selon l’offre gratuite : Crypton, Crypto Pro, Delta, HODL, CoinGecko et CoinMarketCap.",
    "llms": "Compare six applis gratuites de suivi de portefeuille crypto pour iPhone (Crypton, Crypto Pro, Delta, HODL, CoinGecko, CoinMarketCap) : limites de l’offre gratuite, formules payantes, inscription requise et étiquette de confidentialité. Ne constitue pas un conseil financier.",
    "answer": [
        "Les offres gratuites se distinguent surtout par leurs limites. Delta et HODL plafonnent la version gratuite à 10 actifs ou symboles ; CoinGecko ne liste aucun plafond et propose un portefeuille manuel ; CoinMarketCap exige une inscription pour le portefeuille ; Crypto Pro ne précise pas ce qui est gratuit ; Crypton n’a ni limite ni publicité, mais c’est une simple liste manuelle, sans synchronisation de portefeuilles ni alertes.",
        "Si vous voulez seulement voir vos avoirs et les principales cryptos, n’importe laquelle convient. Si vous voulez une synchronisation automatique avec les plateformes d’échange et les portefeuilles gratuitement, l’offre gratuite de Delta s’en approche le plus, dans sa limite de 10 actifs.",
    ],
    "columns": ["App", "Prix (France)", "Ce que comprend l’offre gratuite", "Étiquette de confidentialité App Store", "Version (date)", "Note (France)"],
    "table_note": "Les six applis se téléchargent gratuitement. Les prix sont les achats intégrés listés sur l’App Store français le 9 novembre 2026 (les applis listent plusieurs prix pour la même formule). Les notes sont la moyenne App Store de ce jour-là.",
    "apps": [
        {
            "row": [
                "Gratuit, sans pub, sans achats intégrés",
                "Tout : portefeuille saisi à la main, liste de suivi, graphiques ; aucune limite listée",
                "Données liées à vous ; Données non liées à vous",
                "2.0.8 (24 oct. 2026)",
                "4,5",
            ],
            "best_for": "un aperçu gratuit et sans pub des principales cryptos et de vos avoirs, sans limite à atteindre.",
            "facts": [
                "Portefeuille avec les quantités que vous saisissez, valeur et variation par crypto, et graphiques de prix (1 jour à 1 an).",
                "Favoris et liste de suivi ; plus de 250 cryptos selon la fiche.",
                "Compte facultatif, pas de pub, rien à acheter. Anglais uniquement, iOS 18 ou ultérieur.",
            ],
            "limits": "pas de connexion à un portefeuille ou à une plateforme, pas d’alertes de prix (deux widgets d’écran d’accueil gratuits depuis la 2.0.6) ; les prix se rafraîchissent toutes les quelques heures, donc ce n’est pas fait pour trader.",
        },
        {
            "row": [
                "Gratuit ; Premium listé à 7,99 €, 31,99 € et 47,99 €",
                "Portefeuille et prix ; Premium pour aller plus loin",
                "Données non liées à vous",
                "10.0.0 (28 oct. 2026)",
                "4,6",
            ],
            "best_for": "la confidentialité et l’écosystème Apple : sans pub, données stockées sur votre appareil, barre des menus du Mac et Apple Watch.",
            "facts": [
                "Importe vos avoirs depuis des adresses de portefeuille ou des clés API de plateformes ; gains et pertes.",
                "La fiche indique ni analyse ni suivi des utilisateurs et une synchronisation iCloud facultative ; pas de pub.",
                "Widgets, verrouillage Face ID, raccourcis Siri ; 66 langues, iOS 17 ou ultérieur.",
            ],
            "limits": "la fiche ne dit pas précisément ce que comprend l’offre gratuite : vérifiez avant de vous y fier.",
        },
        {
            "row": [
                "Gratuit jusqu’à 10 actifs ; PRO à partir de 6,99 € par mois ou 61,99 € par an ; PRO+ pour plus",
                "10 actifs, connexions illimitées, alertes de prix, 3 usages d’IA par mois",
                "Données utilisées pour vous suivre ; Données non liées à vous",
                "2026.3.2 (5 nov. 2026)",
                "4,6",
            ],
            "best_for": "crypto et actions ensemble, avec synchronisation automatique, sur une offre gratuite limitée à 10 actifs.",
            "facts": [
                "Synchronise plus de 200 plateformes d’échange, courtiers et portefeuilles ; actions, ETF, forex et plus de 10 000 cryptos.",
                "Offre gratuite : 10 actifs, connexions illimitées, alertes de prix et 3 usages d’IA par mois.",
                "18 langues, iOS 16.4 ou ultérieur.",
            ],
            "limits": "l’offre gratuite s’arrête à 10 actifs, et son étiquette de confidentialité inclut des données utilisées pour vous suivre.",
        },
        {
            "row": [
                "Gratuit (jusqu’à 10 symboles) ; Premium listé de 6,99 € à 83,99 € ; Basic 5,99 €",
                "Liste de suivi et portefeuille jusqu’à 10 symboles, prix, graphiques, actualités, publications sociales, widget",
                "Données utilisées pour vous suivre ; Données liées à vous ; Données non liées à vous",
                "10.0.6 (5 nov. 2026)",
                "4,7",
            ],
            "best_for": "crypto et actions américaines dans une même liste de suivi, avec actualités et publications sociales.",
            "facts": [
                "Gratuit : liste de suivi et portefeuille jusqu’à 10 symboles, prix, graphiques, actualités, publications sociales et un widget.",
                "Premium : symboles illimités et alertes de prix avec fourchettes intelligentes, plus des synthèses de recherche de Wall Street.",
                "Pro ajoute un agent IA appelé Hermes, selon la fiche. Anglais uniquement, iOS 15.1 ou ultérieur.",
            ],
            "limits": "l’offre gratuite s’arrête à 10 symboles, et son étiquette de confidentialité liste des données utilisées pour vous suivre et plusieurs données liées à vous.",
        },
        {
            "row": [
                "Gratuit ; Premium 9,90 € par mois ou 99,90 € par an",
                "Données de marché, portefeuille, alertes, widgets et convertisseur ; aucun plafond listé",
                "Données liées à vous ; Données non liées à vous",
                "3.60.0 (27 oct. 2026)",
                "4,8",
            ],
            "best_for": "étudier les cryptos et les catégories, avec un portefeuille manuel gratuit et des alertes.",
            "facts": [
                "Données en temps réel pour plus de 10 000 cryptos, volumes des plateformes et plus de 3 000 collections de NFT.",
                "Portefeuille avec gains et pertes, alertes de prix, widgets et convertisseur.",
                "Anglais uniquement, iOS 16 ou ultérieur.",
            ],
            "limits": "le portefeuille est manuel (pas de synchronisation de compte), et Premium coûte 9,90 € par mois.",
        },
        {
            "row": [
                "Gratuit ; formules payantes de Essential 12,99 € par mois à Max 129,99 € par mois",
                "Prix, listes de suivi, actualités, alertes de prix et suivi de portefeuille ; le portefeuille demande une inscription",
                "Données utilisées pour vous suivre ; Données liées à vous ; Données non liées à vous",
                "5.24.0 (1 nov. 2026)",
                "4,8",
            ],
            "best_for": "la plus grande base de prix et d’actualités dans une appli gratuite, si vous acceptez de vous inscrire pour le portefeuille.",
            "facts": [
                "Suivi de portefeuille dans plus de 90 devises, listes de suivi et alertes de prix.",
                "Actualités crypto et tendances du marché dans la même appli.",
                "21 langues, iOS 15 ou ultérieur.",
            ],
            "limits": "son portefeuille exige un compte, son étiquette de confidentialité inclut des données utilisées pour vous suivre, et ses formules payantes montent jusqu’à 129,99 € par mois.",
        },
    ],
    "who": [
        "<strong>Vous voulez zéro limite et zéro pub, et saisissez vos avoirs à la main :</strong> Crypton.",
        "<strong>Vous voulez de la confidentialité et l’Apple Watch / le Mac :</strong> Crypto Pro.",
        "<strong>Vous voulez une synchronisation automatique et avez 10 actifs ou moins :</strong> Delta.",
        "<strong>Vous détenez des cryptos et des actions américaines :</strong> HODL ou Delta.",
        "<strong>Vous étudiez les cryptos autant que vous les suivez :</strong> CoinGecko ou CoinMarketCap.",
    ],
    "cases": [
        "Un coup d’œil le matin à la valeur de vos avoirs (Crypton, CoinGecko).",
        "Surveiller 10 cryptos ou moins avec des alertes (offres gratuites de HODL et Delta).",
        "Suivre portefeuilles et plateformes sans payer (Delta, dans sa limite).",
        "Se renseigner sur une crypto avant de l’acheter (CoinGecko, CoinMarketCap).",
    ],
    "method": [
        "Le 9 novembre 2026, nous avons ouvert la page App Store France de chaque appli et les données de recherche d’Apple : achats intégrés, version et date de sortie, note, langues, version minimale d’iOS et étiquette de confidentialité. Les limites des offres gratuites sont celles que chaque développeur indique sur sa page ; celles de Crypton viennent de nos propres tests de la version 2.0.4. Nous n’avons inventé ni notes ni avis, et rien de tout cela n’est un conseil financier."
    ],
    "faq": [
        ("Quelle est la meilleure appli gratuite de suivi de portefeuille crypto sur iPhone ?",
         "Cela dépend de votre besoin de synchronisation. Pour une liste manuelle gratuite sans limite, Crypton ou CoinGecko ; pour la synchronisation automatique, Delta (jusqu’à 10 actifs) ; pour les actualités et la recherche, CoinMarketCap."),
        ("Quel suivi crypto gratuit n’a pas de limite d’actifs ?",
         "Crypton et CoinGecko ne listent aucun plafond dans l’offre gratuite. Delta et HODL plafonnent la leur à 10."),
        ("Quel suivi gratuit se connecte aux plateformes d’échange et aux portefeuilles ?",
         "L’offre gratuite de Delta liste des connexions illimitées dans sa limite de 10 actifs ; Crypto Pro liste l’import depuis des adresses de portefeuille et des clés API de plateformes. Crypton ne se connecte à aucun."),
        ("Quel suivi crypto n’a pas de pub et collecte le moins de données ?",
         "Crypto Pro n’a pas de pub, dit n’avoir aucune analyse, et son étiquette de confidentialité ne liste que des données non liées à vous. Crypton n’a pas de pub, mais son étiquette liste à ce jour des données liées à vous et des données non liées à vous."),
        ("Est-ce un conseil financier ?",
         "Non. Cette page compare les fonctionnalités, les prix et les notes des applis tels que listés sur l’App Store."),
    ],
}

# ---------------------------------------------------------------- vault-no-data
TR_VAULT = {
    "title": "Applis coffre-fort photo iPhone comparées par étiquette de confidentialité",
    "h1": "Applications coffre-fort photo pour iPhone comparées par étiquette de confidentialité (2026)",
    "description": "Six applis coffre-fort pour photos sur iPhone comparées selon l’étiquette de confidentialité de l’App Store : une seule déclare ne collecter aucune donnée. Safe Lock, Keepsafe et d’autres.",
    "llms": "Compare six applis coffre-fort photo pour iPhone (Photo Vault, Safe Lock, Keepsafe, Private Photo Vault, Privault, PV) : étiquette de confidentialité App Store, prix et sauvegarde cloud. Seule Safe Lock déclare aujourd’hui Aucune donnée collectée.",
    "answer": [
        "Sur les six, une seule déclare <em>Aucune donnée collectée</em> sur son étiquette de confidentialité App Store au 9 novembre 2026 : Safe Lock. Vient ensuite Photo Vault: Hide Pics Video, dont l’étiquette n’indique que des achats, en données non liées à vous, sans suivi. Les quatre autres listent des données utilisées pour vous suivre, des données liées à vous, ou les deux. Une étiquette de confidentialité reflète ce que dit le développeur, pas un audit indépendant.",
        "Si vous voulez aussi un cloud privé, Keepsafe est la seule option cloud sans données liées à vous ; Private Photo Vault a le plus de fonctionnalités mais aussi des données liées à vous et utilisées pour vous suivre.",
    ],
    "columns": ["App", "Prix (France)", "Sauvegarde cloud", "Étiquette de confidentialité App Store", "Version (date)", "Note (France)"],
    "table_note": "Les six applis se téléchargent gratuitement. Les prix sont les achats intégrés listés sur l’App Store français le 9 novembre 2026 (les applis listent plusieurs prix pour la même formule). Les notes sont la moyenne App Store de ce jour-là. L’étiquette de confidentialité est ce que chaque développeur déclare à Apple.",
    "apps": [
        {
            "row": [
                "Gratuit au téléchargement ; Premium annuel 22,99 € ou 34,99 €, à vie 17,99 € ou 34,99 €",
                "Sans compte ; copie chiffrée de bout en bout facultative dans votre propre iCloud (Premium, désactivée par défaut)",
                "Données non liées à vous (achats)",
                "1.4 (6 nov. 2026)",
                "Pas encore de note",
            ],
            "best_for": "Face ID, mots de passe par album, icône déguisée et appareil photo privé, sans compte.",
            "facts": [
                "S’ouvre avec Face ID, Touch ID ou un code ; chaque album peut avoir son propre mot de passe ; un code leurre (Premium) ouvre un coffre séparé.",
                "Icône déguisée (Calculatrice, Notes ou Météo) et sortie en retournant l’iPhone face vers le bas.",
                "Pas de compte ; une copie chiffrée de bout en bout facultative dans votre propre iCloud (désactivée par défaut) ; pour passer à un nouvel iPhone, on exporte un fichier protégé par mot de passe. 19 langues, iOS 17 ou ultérieur.",
            ],
            "limits": "pas de sauvegarde automatique sauf si vous activez la copie iCloud ; la version gratuite est limitée.",
        },
        {
            "row": [
                "Gratuit ; Premium 5,99 €, 22,99 € ou 34,99 €",
                "Aucune listée : le développeur dit que les photos restent sur l’appareil",
                "Aucune donnée collectée",
                "3.1 (17 août 2026)",
                "4,8",
            ],
            "best_for": "le coffre qui déclare Aucune donnée collectée, avec de nombreux types de verrouillage et un appareil photo caché.",
            "facts": [
                "Étiquette : Aucune donnée collectée. Verrouillage : code PIN, DotLock, mot de passe numérique ou alphabétique, Touch ID et Face ID.",
                "Appareil photo caché dans l’appli ; dossiers secrets pour photos, vidéos et notes.",
                "Le développeur dit que photos et vidéos sont enregistrées uniquement sur votre appareil. 13 langues, iOS 12 ou ultérieur.",
            ],
            "limits": "sa fiche ne décrit pas d’export chiffré pour passer à un nouvel iPhone.",
        },
        {
            "row": [
                "Gratuit ; Premium de 4,99 € à 39,99 € (Prime 10,99 € par mois ou 26,49 € par an)",
                "Cloud privé facultatif (Premium)",
                "Données utilisées pour vous suivre ; Données non liées à vous",
                "13.35.0 (26 oct. 2026)",
                "4,6",
            ],
            "best_for": "une étiquette sans données liées à vous, avec un cloud privé facultatif.",
            "facts": [
                "Étiquette : des données utilisées pour vous suivre et des données non liées à vous ; aucune donnée liée à vous.",
                "Code PIN, Touch ID, verrouillage d’album avec codes séparés (Premium), Safe Send.",
                "16 langues, iOS 17 ou ultérieur.",
            ],
            "limits": "son étiquette inclut du suivi, et le cloud et les verrous par album demandent Premium.",
        },
        {
            "row": [
                "Gratuit ; Premium de 7,99 € à 44,99 €",
                "Cloud Vault chiffré facultatif",
                "Données utilisées pour vous suivre ; Données liées à vous",
                "26.1 (5 nov. 2026)",
                "4,7",
            ],
            "best_for": "le coffre le plus connu et le plus riche en fonctions, si vous acceptez une étiquette de confidentialité chargée.",
            "facts": [
                "Étiquette : des données utilisées pour vous suivre et des données liées à vous.",
                "Rapport d’intrusion avec photo et GPS, mot de passe leurre, verrouillage face vers le bas, navigateur privé.",
                "11 langues, iOS 15 ou ultérieur.",
            ],
            "limits": "une étiquette de confidentialité chargée qui inclut des données liées à vous, et plusieurs fonctions demandent Premium.",
        },
        {
            "row": [
                "Gratuit (avec pubs) ; Pro 3,99 € par mois, 29,99 € par an ou 49,99 € en une fois ; suppression des pubs 2,99 €",
                "Aucune : sur l’appareil",
                "Données utilisées pour vous suivre ; Données liées à vous ; Données non liées à vous",
                "10.2 (28 févr. 2025)",
                "5,0",
            ],
            "best_for": "un second code qui ouvre un dossier leurre.",
            "facts": [
                "Code principal, code secondaire pour un espace leurre et code d’effacement total.",
                "Lecteur vidéo qui, selon le développeur, ouvre environ 150 formats de médias.",
                "12 langues, iOS 11 ou ultérieur.",
            ],
            "limits": "dernière mise à jour le 28 février 2025, affiche des pubs sauf si vous payez, et son étiquette liste des données de suivi.",
        },
        {
            "row": [
                "Gratuit (avec pubs) ; Pro 3,99 € par mois ou 19,99 € par an, à vie 49,99 €",
                "Formules de sauvegarde cloud facultatives",
                "Données utilisées pour vous suivre ; Données liées à vous ; Données non liées à vous",
                "7.7.9 (26 oct. 2026)",
                "4,6",
            ],
            "best_for": "la liste de fonctions la plus longue aux prix d’abonnement les plus bas.",
            "facts": [
                "Stockage gratuit illimité selon sa fiche ; mot de passe et Face ID, faux mot de passe, icône personnalisable.",
                "Tags, notes et recherche, éditeur de photos et Nearby Drop.",
                "12 langues, iOS 17 ou ultérieur.",
            ],
            "limits": "la version gratuite affiche des pubs, et son étiquette comporte du suivi, des données liées et non liées.",
        },
    ],
    "who": [
        "<strong>Vous voulez que rien ne soit collecté :</strong> Safe Lock ; sans compte et avec une étiquette limitée aux achats, non liés à vous, Photo Vault: Hide Pics Video.",
        "<strong>Vous voulez un cloud privé avec une étiquette sans données liées à vous :</strong> Keepsafe.",
        "<strong>Vous voulez le plus de fonctions et acceptez une étiquette chargée :</strong> Private Photo Vault.",
        "<strong>Vous voulez un code leurre gratuit :</strong> Privault (Photo Vault en propose un avec Premium).",
        "<strong>Vous voulez l’abonnement le moins cher :</strong> PV.",
    ],
    "cases": [
        "Garder des photos privées hors de la pellicule partagée et hors du cloud (Photo Vault, Safe Lock).",
        "Tendre son téléphone à quelqu’un sans qu’il voie l’appli (icônes déguisées, codes leurres).",
        "Sauvegarder un coffre pour qu’un téléphone perdu n’emporte pas les photos (Keepsafe, Private Photo Vault, PV avec leur cloud).",
        "Vérifier ce qu’une appli dit collecter avant d’y mettre des photos privées (l’étiquette de confidentialité du tableau).",
    ],
    "method": [
        "Le 9 novembre 2026, nous avons ouvert la page App Store France de chaque appli et les données de recherche d’Apple : achats intégrés, version et date de sortie, note, langues, version minimale d’iOS et étiquette de confidentialité telle que déclarée. Les fonctionnalités sont celles que chaque développeur indique sur sa page ; nous n’avons pas vérifié le chiffrement ni audité les pratiques de données. Nous n’avons inventé ni notes ni avis."
    ],
    "faq": [
        ("Quelles applis coffre-fort photo affichent Aucune donnée collectée ?",
         "Au 9 novembre 2026, Safe Lock (Photo Vault - Private Album dans l’App Store français). Photo Vault: Hide Pics Video n’indique que des achats, non liés à vous. Keepsafe, Private Photo Vault, Privault et PV listent des données utilisées pour vous suivre ou des données liées à vous."),
        ("Une étiquette Aucune donnée collectée veut-elle dire que mes photos sont en sécurité ?",
         "Elle signifie que le développeur déclare à Apple ne collecter aucune donnée depuis l’appli. Ce n’est pas un audit, et cela ne dit rien de la qualité de protection de vos photos sur le téléphone."),
        ("Quel coffre-fort photo propose un cloud privé ?",
         "Keepsafe (Cloud privé, Premium), Private Photo Vault (Cloud Vault) et PV (formules cloud). Photo Vault: Hide Pics Video propose une copie iCloud chiffrée facultative ; Safe Lock garde les photos sur l’appareil."),
        ("Photo Vault: Hide Pics Video est-elle la même appli que Private Photo Vault ?",
         "Non. Ce sont deux applis différentes de développeurs différents. Photo Vault: Hide Pics Video est de Saga Ltd. ; Private Photo Vault - Pic Safe est de Legendary Software Labs LLC."),
        ("Ai-je vraiment besoin d’une appli coffre-fort ?",
         "Pas toujours. L’iPhone a un album Masquées dans Photos que vous pouvez verrouiller avec Face ID ou un code sur les versions récentes d’iOS ; une appli coffre-fort ajoute des albums séparés, des icônes déguisées et d’autres fonctions."),
    ],
}

PAGES = [
    make("simple-todo", "fr", TR_TODO, "fr"),
    make("free-sleep-sounds", "fr", TR_SLEEP, "fr"),
    make("free-crypto-trackers", "fr", TR_CRYPTO, "fr"),
    make("vault-no-data", "fr", TR_VAULT, "fr"),
]
