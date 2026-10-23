"""Best apps to hide photos on iPhone. EN + ES.

Data checked on 2026-10-11 with the iTunes lookup API and the App Store web
pages (US store for EN, Spain for ES). Our app: Photo Vault (id1532670722).
Free tier of Photo Vault: 1 item (freeItemLimit in onlyfansgallery/Helper.swift).
"""

CHECKED = "2026-10-11"

SRC_COMMON = [
    ("Apple Support, Hide photos with the Hidden album", "https://support.apple.com/en-us/104987", True),
]


def src(cc):
    return [
        ("Photo Vault (App Store)", f"https://apps.apple.com/{cc}/app/id1532670722", True),
        ("Private Photo Vault - Pic Safe (App Store)", f"https://apps.apple.com/{cc}/app/id417571834", False),
        ("Keepsafe (App Store)", f"https://apps.apple.com/{cc}/app/id510873505", False),
        ("Safe Lock (App Store)", f"https://apps.apple.com/{cc}/app/id1195429570", False),
        ("Calculator# Hide Photos Videos (App Store)", f"https://apps.apple.com/{cc}/app/id1165276801", False),
        ("Privault (App Store)", f"https://apps.apple.com/{cc}/app/id1186436980", False),
    ]


EN = {
    "group": "hide-photos", "lang": "en",
    "path": "best-apps-to-hide-photos-iphone/",
    "ct": "rl-hide-photos", "store": "us",
    "category": "UtilitiesApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best apps to hide photos for iPhone users who want privacy (2026)",
    "h1": "Best apps to hide photos on iPhone in 2026",
    "description": "Seven ways to hide photos on iPhone compared: Photo Vault, the Hidden album, Private Photo Vault, Keepsafe and more. Prices and privacy labels checked.",
    "llms": "Compares seven ways to hide photos on iPhone by price, App Store privacy label, account and cloud requirements and disguise options.",
    "disclosure": "Photo Vault is made by Saga Labs, the company behind Reviewland. It is listed first because it is ours. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "To hide photos on iPhone without an account or a cloud copy, use a vault app that stores them only on the phone: Photo Vault (ours) and Safe Lock both have the App Store privacy label <em>Data Not Collected</em>. If you just want a few photos out of the main grid, the free Hidden album in Apple's Photos app is locked with Face ID, but it syncs to your other devices through iCloud Photos.",
        "If you want an online backup of the vault, Private Photo Vault and Keepsafe offer encrypted cloud storage as a paid option, and both show <em>Data Used to Track You</em> on their privacy labels.",
    ],
    "columns": ["App", "Price (US)", "Account or cloud", "App Store privacy label", "Disguise", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the in-app purchases listed on each App Store page in the US on 11 October 2026; all of them are free to download. Ratings are the App Store average and number of ratings on that day.",
    "apps": [
        {
            "name": "Photo Vault: Hide Pics Video", "id": 1532670722, "ours": True, "anchor": "photo-vault",
            "developer": "Saga Ltd.", "rating": (4.17, 6),
            "row": ["Free for 1 item; Premium $19.99 or $29.99 a year; lifetime $59.99", "No account; iCloud copy optional (encrypted, off by default)", "Data Not Collected",
                    "Icon can look like Calculator, Notes or Weather", "1.2.7 (7 Oct 2026)", "4.2 (6 ratings)"],
            "best_for": "people who want photos only on their iPhone, with no account and nothing uploaded unless they turn on the optional encrypted iCloud copy.",
            "facts": [
                "Opens with Face ID, Touch ID or a passcode, and each album can have its own password.",
                "Private Camera takes photos straight into the vault, so they never reach the camera roll.",
                "Face-down exit: turning the phone over switches to Safari, Calendar or Messages.",
                "The vault is left out of iCloud backups. To move it to a new iPhone you export one encrypted, password-locked file and restore it.",
                "Works offline. 19 languages. Needs iOS 17 or later; 17 MB.",
            ],
            "limits": "the free version holds only 1 photo or video, so in practice it is a paid app. It has only 6 ratings in the US so far. There is no automatic backup: if you delete the app without exporting a backup, the vault is gone.",
        },
        {
            "name": "Hidden album in Apple Photos", "anchor": "hidden-album", "developer": "Apple",
            "row": ["Free, built in", "Syncs with iCloud Photos if it is on", "n/a (part of iOS)", "Album can be hidden from the sidebar", "iOS 16 and later", "n/a"],
            "best_for": "hiding a few photos from the main grid when you trust everyone who uses your Apple account.",
            "facts": [
                "Since iOS 16 the Hidden album is locked by default and opens with Face ID, Touch ID or your passcode.",
                "With iCloud Photos on, photos you hide on one device are hidden on your other devices too.",
                "You can stop the album from showing in Photos in Settings, Apps, Photos.",
            ],
            "limits": "it uses the same Face ID or passcode as the phone, so anyone who knows your passcode can open it, and the photos stay in your main library and iCloud.",
        },
        {
            "name": "Private Photo Vault - Pic Safe", "id": 417571834, "anchor": "private-photo-vault", "developer": "Legendary Software Labs",
            "rating": (4.82, 1016855),
            "row": ["In-app purchases from $6.99 to $39.99", "Optional encrypted Cloud Vault (needs its own password)", "Data Used to Track You; Data Linked to You",
                    "Decoy password", "25.8 (17 Sep 2026)", "4.8 (1,016,855 ratings)"],
            "best_for": "people who want a long-established vault with an optional cloud backup.",
            "facts": [
                "PIN or pattern lock for the app, password-protected albums, decoy password and face-down lock.",
                "Break-in report with photo and GPS of whoever tries to get in.",
                "Built-in private browser, Wi-Fi transfer, and Cloud Vault encrypted backup.",
                "11 languages, iOS 15 or later, 172 MB. Rated 17+.",
            ],
            "limits": "its privacy label says it collects data used to track you. Cloud backup is a paid feature.",
        },
        {
            "name": "Secret Photo Vault: Keepsafe", "id": 510873505, "anchor": "keepsafe", "developer": "KeepSafe Software",
            "rating": (4.75, 384216),
            "row": ["Premium $9.99 a month or $23.99 a year; other plans up to $35.99", "Syncs across your Keepsafe installs; Private Cloud with Premium", "Data Used to Track You; Data Not Linked to You",
                    "Not stated", "13.33.0 (29 Sep 2026)", "4.8 (384,216 ratings)"],
            "best_for": "people who want the vault on several devices, including Android.",
            "facts": [
                "PIN and Touch ID lock, custom albums and a camera that saves straight into Keepsafe.",
                "Safe Send to share a photo for a limited time.",
                "Premium adds a PIN per album, Private Cloud for up to 10,000 items and Space Saver.",
                "15 languages, iOS 15 or later, 208 MB.",
            ],
            "limits": "the cloud and per-album PIN need Premium, and the privacy label says it collects data used to track you.",
        },
        {
            "name": "Safe Lock - Hidden Photo Vault", "id": 1195429570, "anchor": "safe-lock", "developer": "Katerina Akhlebinina",
            "rating": (4.81, 24834),
            "row": ["Premium $4.99, $19.99 or $29.99", "On the device; Wi-Fi transfer", "Data Not Collected",
                    "App icon can be changed", "3.1 (17 Aug 2026)", "4.8 (24,834 ratings)"],
            "best_for": "a local vault from a developer that, like ours, declares no data collected.",
            "facts": [
                "PIN, pattern, numeric or alphabetic password, Touch ID and Face ID.",
                "Hidden camera inside the app, secret folders for photos, videos and notes.",
                "The developer says photos and videos are saved only on your device.",
                "13 languages, iOS 12 or later, 69 MB.",
            ],
            "limits": "the listing does not describe an encrypted export for moving to a new iPhone.",
        },
        {
            "name": "Calculator# Hide Photos Videos", "id": 1165276801, "anchor": "calculator", "developer": "NewSoftwares.net",
            "rating": (4.39, 28907),
            "row": ["Yearly $4.99; feature pack $4.99", "Backup to iCloud, Dropbox, Google Drive or OneDrive", "Data Used to Track You; Data Not Linked to You",
                    "Looks and works like a calculator", "3.4.12 (29 Jul 2026)", "4.4 (28,907 ratings)"],
            "best_for": "people who want the vault to look like a working calculator and also hide documents, notes and passwords.",
            "facts": [
                "Can delete photos from the main library after moving them in (optional).",
                "Also stores documents, audio, notes, passwords, contacts and to-dos.",
                "Panic switch, disguise mode and break-in monitoring.",
                "6 languages, iOS 15 or later, 75 MB. Rated 17+.",
            ],
            "limits": "lowest rating in this list (4.4), and its privacy label says it collects data used to track you.",
        },
        {
            "name": "Privault - Private Photo Vault", "id": 1186436980, "anchor": "privault", "developer": "Binspir Technologies",
            "rating": (4.68, 76592),
            "row": ["Pro $3.49 a month, $24.99 a year or $45.99 once; remove ads $2.99", "On the device", "Data Used to Track You; Data Linked to You",
                    "Keypad-style lock screen", "10.2 (28 Feb 2025)", "4.7 (76,592 ratings)"],
            "best_for": "people who need a second passcode that opens a different, harmless folder.",
            "facts": [
                "Primary passcode, secondary passcode for a decoy space, and an erase-all passcode.",
                "Video player that the developer says opens about 150 media formats.",
                "12 languages, iOS 11 or later, 91 MB.",
            ],
            "limits": "last updated on 28 February 2025, over a year and a half before this check, and it shows ads unless you pay.",
        },
    ],
    "who": [
        "<strong>Nothing should leave the phone:</strong> Photo Vault (ours) or Safe Lock. Both declare Data Not Collected.",
        "<strong>You want a backup online:</strong> Private Photo Vault (Cloud Vault) or Keepsafe (Private Cloud), both paid.",
        "<strong>You also use Android:</strong> Keepsafe, which syncs between its installs.",
        "<strong>You only want a few photos off the main grid:</strong> the Hidden album in Photos, free and already on your iPhone.",
        "<strong>You want the app to look like something else:</strong> Calculator# (a working calculator) or Photo Vault (Calculator, Notes or Weather icon).",
    ],
    "cases": [
        "Copies of your passport, ID or cards that should not appear when you show someone your camera roll.",
        "Private photos you do not want synced to a shared or family iCloud account.",
        "Lending your phone to a child or friend without them scrolling into personal pictures.",
        "Taking a photo that should never be in the camera roll at all (Photo Vault's Private Camera, Safe Lock's hidden camera, Keepsafe's camera).",
    ],
    "method": [
        "On 11 October 2026 we read each app's US App Store page and Apple's lookup data: price list of in-app purchases, version and release date, rating and number of ratings, languages, size, minimum iOS and the privacy label. Features are the ones each developer lists on its App Store page. We did not invent ratings or reviews.",
        "We picked the apps that appear at the top of App Store search for \"hide photos\" and \"photo vault\" in the US, plus Apple's own Hidden album.",
    ],
    "faq": [
        ("Is the Hidden album on iPhone safe enough?",
         "It is locked with Face ID, Touch ID or the phone passcode since iOS 16, so it stops casual browsing. Anyone who knows your passcode can open it, and the photos still sync through iCloud Photos to your other devices."),
        ("Which photo vault apps do not upload my photos?",
         "Photo Vault and Safe Lock keep photos on the iPhone and both have the App Store privacy label Data Not Collected. Private Photo Vault and Keepsafe offer optional cloud storage."),
        ("Can I hide photos on iPhone without iCloud?",
         "Yes. A local vault such as Photo Vault keeps the photos on the device, leaves the vault out of iCloud backups and opens without internet."),
        ("What happens to hidden photos if I delete the vault app?",
         "With a local vault the photos are deleted with the app unless you exported a backup first. Photo Vault exports one encrypted, password-locked file you can keep in Files or on a computer."),
        ("Is there a free app to hide photos on iPhone?",
         "The Hidden album in Photos is free. All the vault apps here are free to download, but their extra features are paid, and Photo Vault's free version holds only one item."),
        ("How do I move a photo vault to a new iPhone?",
         "In Photo Vault, export an encrypted backup in Settings and restore it on the new iPhone. Apps with a cloud vault, such as Keepsafe or Private Photo Vault, restore from their cloud after you sign in."),
    ],
    "sources": SRC_COMMON + src("us"),
}

ES = {
    "group": "hide-photos", "lang": "es",
    "path": "es/mejores-apps-para-ocultar-fotos-iphone/",
    "ct": "rl-hide-photos-es", "store": "es",
    "category": "UtilitiesApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Mejores apps para ocultar fotos para quien usa iPhone (2026)",
    "h1": "Mejores apps para ocultar fotos en iPhone en 2026",
    "description": "Siete formas de ocultar fotos en iPhone comparadas: Photo Vault, el álbum Oculto, Private Photo Vault, Keepsafe y más. Precios y privacidad comprobados.",
    "llms": "Compara siete formas de ocultar fotos en iPhone por precio en euros, etiqueta de privacidad del App Store, cuenta o nube y camuflaje.",
    "disclosure": "Photo Vault (en España se llama «Bóveda: Ocultar Fotos y Video») es de Saga Labs, la empresa que hace Reviewland. Va primera porque es nuestra. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store.",
    "answer": [
        "Para ocultar fotos en el iPhone sin cuenta y sin copia en la nube, usa una app bóveda que las guarde solo en el teléfono: Photo Vault (nuestra) y Safe Lock tienen las dos la etiqueta de privacidad <em>No se recopilan datos</em>. Si solo quieres sacar unas pocas fotos de la galería, el álbum Oculto de la app Fotos es gratis y se abre con Face ID, pero se sincroniza con tus otros dispositivos por Fotos de iCloud.",
        "Si quieres copia de la bóveda en internet, Private Photo Vault y Keepsafe tienen nube cifrada de pago, y las dos declaran datos utilizados para rastrearte en su etiqueta de privacidad.",
    ],
    "columns": ["App", "Precio (España)", "Cuenta o nube", "Etiqueta de privacidad", "Camuflaje", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Precios: compras dentro de la app que muestra cada ficha del App Store de España el 11 de octubre de 2026; todas se descargan gratis. Valoración: media y número de valoraciones en España ese día.",
    "apps": [
        {
            "name": "Photo Vault (Bóveda: Ocultar Fotos y Video)", "id": 1532670722, "ours": True, "anchor": "photo-vault",
            "developer": "Saga Ltd.", "rating": (1.0, 1),
            "row": ["Gratis con 1 elemento; Premium 22,99 € o 34,99 € al año; de por vida 69,99 €", "Sin cuenta; copia en iCloud opcional (cifrada, desactivada por defecto)", "No se recopilan datos",
                    "Icono como Calculadora, Notas o Tiempo", "1.2.7 (7 oct 2026)", "1,0 (1 valoración)"],
            "best_for": "quien quiere las fotos solo en su iPhone, sin cuenta y sin subir nada.",
            "facts": [
                "Se abre con Face ID, Touch ID o código, y cada álbum puede tener su propia contraseña.",
                "La Cámara privada guarda las fotos directamente en la bóveda, sin pasar por el carrete.",
                "Salida boca abajo: al girar el móvil salta a Safari, Calendario o Mensajes.",
                "La bóveda no entra en las copias de iCloud. Para pasarla a otro iPhone se exporta un archivo cifrado con contraseña y se restaura.",
                "Funciona sin conexión. 19 idiomas, español incluido. Pide iOS 17 o posterior; 17 MB.",
            ],
            "limits": "la versión gratis solo guarda 1 foto o vídeo, así que en la práctica es de pago. En España tiene una sola valoración, de 1 estrella. No hay copia automática: si borras la app sin exportar una copia, pierdes la bóveda.",
        },
        {
            "name": "Álbum Oculto de Fotos (Apple)", "anchor": "album-oculto", "developer": "Apple",
            "row": ["Gratis, viene en el iPhone", "Se sincroniza con Fotos de iCloud si está activado", "No aplica (parte de iOS)", "Se puede quitar de la barra lateral", "iOS 16 y posteriores", "No aplica"],
            "best_for": "sacar unas pocas fotos de la galería cuando te fías de quien usa tu cuenta de Apple.",
            "facts": [
                "Desde iOS 16 el álbum Oculto está bloqueado de serie y se abre con Face ID, Touch ID o el código.",
                "Con Fotos de iCloud activado, lo que ocultas en un dispositivo queda oculto en los demás.",
                "Se puede dejar de mostrar en Ajustes, Apps, Fotos.",
            ],
            "limits": "usa el mismo Face ID o código que el iPhone, así que quien sepa tu código lo abre, y las fotos siguen en tu fototeca y en iCloud.",
        },
        {
            "name": "Private Photo Vault (Ocultar Fotos - Photo Vault)", "id": 417571834, "anchor": "private-photo-vault", "developer": "Legendary Software Labs",
            "rating": (4.73, 21956),
            "row": ["Compras de 7,99 € a 44,99 €", "Cloud Vault cifrada opcional (con su propia contraseña)", "Datos utilizados para rastrearte; datos vinculados a ti",
                    "Contraseña señuelo", "25.8 (17 sep 2026)", "4,7 (21.956 valoraciones)"],
            "best_for": "quien quiere una bóveda veterana con copia en la nube opcional.",
            "facts": [
                "Bloqueo con PIN o patrón, álbumes con contraseña, contraseña señuelo y bloqueo boca abajo.",
                "Informe de intrusos con foto y GPS de quien intenta entrar.",
                "Navegador privado, transferencia por wifi y copia cifrada en su nube.",
                "11 idiomas, iOS 15 o posterior, 172 MB. Para mayores de 16 en España.",
            ],
            "limits": "su etiqueta de privacidad dice que recoge datos para rastrearte, y la nube es de pago.",
        },
        {
            "name": "Keepsafe (Keepsafe-Protege Fotos, Videos)", "id": 510873505, "anchor": "keepsafe", "developer": "KeepSafe Software",
            "rating": (4.69, 10905),
            "row": ["Premium 10,99 € al mes o 26,49 € al año; otros planes hasta 39,99 €", "Sincroniza entre tus instalaciones; nube privada con Premium", "Datos utilizados para rastrearte; datos no vinculados a ti",
                    "No lo indica", "13.33.0 (29 sep 2026)", "4,7 (10.905 valoraciones)"],
            "best_for": "quien quiere la bóveda en varios dispositivos, también Android.",
            "facts": [
                "Bloqueo con PIN y Touch ID, álbumes y cámara que guarda directamente en Keepsafe.",
                "Safe Send para compartir una foto por tiempo limitado.",
                "Premium añade un PIN por álbum, nube privada de hasta 10.000 elementos y ahorro de espacio.",
                "15 idiomas, iOS 15 o posterior, 208 MB.",
            ],
            "limits": "la nube y el PIN por álbum son de pago, y su etiqueta dice que recoge datos para rastrearte.",
        },
        {
            "name": "Safe Lock (Photo Vault - Galeria Secreta)", "id": 1195429570, "anchor": "safe-lock", "developer": "Katerina Akhlebinina",
            "rating": (4.71, 2013),
            "row": ["Premium 5,99 €, 22,99 € o 34,99 €", "En el dispositivo; transferencia por wifi", "No se recopilan datos",
                    "Se puede cambiar el icono", "3.1 (17 ago 2026)", "4,7 (2.013 valoraciones)"],
            "best_for": "una bóveda local de un desarrollador que, como nosotros, declara no recoger datos.",
            "facts": [
                "PIN, patrón, contraseña numérica o con letras, Touch ID y Face ID.",
                "Cámara oculta dentro de la app y carpetas secretas para fotos, vídeos y notas.",
                "Recuperación de la contraseña por correo.",
                "13 idiomas, iOS 12 o posterior, 69 MB.",
            ],
            "limits": "su ficha no describe una copia cifrada para pasar la bóveda a otro iPhone.",
        },
        {
            "name": "Calculator# Hide Photos Videos", "id": 1165276801, "anchor": "calculator", "developer": "NewSoftwares.net",
            "rating": (4.39, 583),
            "row": ["Anual 4,99 €; paquete de funciones 5,99 €", "Copia en iCloud, Dropbox, Google Drive u OneDrive", "Datos utilizados para rastrearte; datos no vinculados a ti",
                    "Parece y funciona como una calculadora", "3.4.12 (29 jul 2026)", "4,4 (583 valoraciones)"],
            "best_for": "quien quiere que la bóveda parezca una calculadora y guardar también documentos, notas y contraseñas.",
            "facts": [
                "Puede borrar las fotos de la galería al moverlas a la app (opcional).",
                "Guarda también documentos, audios, notas, contraseñas, contactos y tareas.",
                "Botón de pánico, modo disfraz y aviso de intrusos.",
                "6 idiomas (la ficha está en inglés), iOS 15 o posterior, 75 MB.",
            ],
            "limits": "la peor valoración de la lista (4,4), y su etiqueta dice que recoge datos para rastrearte.",
        },
        {
            "name": "Privault (Privault-Esconder video foto)", "id": 1186436980, "anchor": "privault", "developer": "Binspir Technologies",
            "row": ["PRO 3,99 € al mes, 29,99 € al año o 49,99 € para siempre; quitar anuncios 2,99 €", "En el dispositivo", "Datos utilizados para rastrearte; datos vinculados a ti",
                    "Pantalla de teclado", "10.2 (28 feb 2025)", "Sin valoraciones en España"],
            "best_for": "quien necesita un segundo código que abre otra carpeta inofensiva.",
            "facts": [
                "Código principal, código secundario para un espacio señuelo y código que lo borra todo.",
                "Reproductor que, según el desarrollador, abre unos 150 formatos.",
                "12 idiomas, iOS 11 o posterior, 91 MB.",
            ],
            "limits": "la última actualización es del 28 de febrero de 2025, más de año y medio antes de esta revisión, y lleva anuncios si no pagas.",
        },
    ],
    "who": [
        "<strong>Que nada salga del móvil:</strong> Photo Vault (nuestra) o Safe Lock. Las dos declaran que no recogen datos.",
        "<strong>Quieres copia en internet:</strong> Private Photo Vault o Keepsafe, las dos con nube de pago.",
        "<strong>También usas Android:</strong> Keepsafe, que sincroniza entre sus instalaciones.",
        "<strong>Solo quieres sacar unas fotos de la galería:</strong> el álbum Oculto de Fotos, gratis y ya instalado.",
        "<strong>Quieres que parezca otra cosa:</strong> Calculator# (una calculadora que funciona) o Photo Vault (icono de Calculadora, Notas o Tiempo).",
    ],
    "cases": [
        "Fotos del DNI, el pasaporte o las tarjetas que no quieres que salgan al enseñar el carrete.",
        "Fotos privadas que no quieres en una cuenta de iCloud compartida o familiar.",
        "Dejar el móvil a un niño o a un amigo sin que vea fotos personales.",
        "Hacer una foto que no pase nunca por el carrete (Cámara privada de Photo Vault, cámara oculta de Safe Lock o cámara de Keepsafe).",
    ],
    "method": [
        "El 11 de octubre de 2026 leímos la ficha de cada app en el App Store de España y los datos de Apple: compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño, iOS mínimo y etiqueta de privacidad. Las funciones son las que cada desarrollador pone en su ficha. No inventamos valoraciones ni reseñas.",
        "Elegimos las apps que salen arriba al buscar «hide photos» y «photo vault» en el App Store, más el álbum Oculto de Apple.",
    ],
    "faq": [
        ("¿Es seguro el álbum Oculto del iPhone?",
         "Desde iOS 16 se abre con Face ID, Touch ID o el código del iPhone, así que frena a quien cotillea. Pero quien sepa tu código lo abre, y las fotos siguen sincronizándose por Fotos de iCloud con tus otros dispositivos."),
        ("¿Qué apps para ocultar fotos no suben nada a internet?",
         "Photo Vault y Safe Lock guardan las fotos en el iPhone y las dos tienen la etiqueta «No se recopilan datos». Private Photo Vault y Keepsafe tienen nube opcional."),
        ("¿Se pueden ocultar fotos en el iPhone sin iCloud?",
         "Sí. Una bóveda local como Photo Vault guarda las fotos en el teléfono, no entra en las copias de iCloud y se abre sin conexión."),
        ("¿Qué pasa con las fotos ocultas si borro la app?",
         "Con una bóveda local se borran con la app si antes no exportaste una copia. Photo Vault exporta un archivo cifrado con contraseña que puedes guardar en Archivos o en el ordenador."),
        ("¿Hay alguna app gratis para ocultar fotos en el iPhone?",
         "El álbum Oculto de Fotos es gratis. Todas las bóvedas de esta lista se descargan gratis, pero lo extra es de pago, y la versión gratis de Photo Vault solo guarda un elemento."),
        ("¿Cómo paso la bóveda a un iPhone nuevo?",
         "En Photo Vault, exporta una copia cifrada desde Ajustes y restáurala en el iPhone nuevo. Las apps con nube, como Keepsafe o Private Photo Vault, recuperan la bóveda al iniciar sesión."),
    ],
    "sources": [("Apple, Ocultar fotos con el álbum Oculto", "https://support.apple.com/es-es/104987", True)] + src("es"),
}

PAGES = [EN, ES]


from pages.store_1016 import refresh_ours
for _p in PAGES:
    refresh_ours(_p, _p["store"], 2, 4, 5)
