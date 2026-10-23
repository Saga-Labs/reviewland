"""Versiones en español (App Store de España, 16 oct 2026) de las 4 páginas de alternativas.

Datos de precio, valoración, versión y privacidad: pages/store_1016.py (DATA["es"]).
Las funciones de cada app salen de las páginas EN (mismas fuentes); aquí solo se traduce y se ponen precios en euros.
"""

from pages.store_1016 import refresh
from pages import calm_alternatives as C, todoist_alternatives as T, coinstats_alternatives as K, photo_vault_alternatives as P

CHECKED = "2026-10-16"
COMMON = {"lang": "es", "store": "es", "published": CHECKED, "updated": CHECKED, "checked": CHECKED}
DATE = "16 de octubre de 2026"


def app(en_app, **kw):
    a = {k: v for k, v in en_app.items() if k not in ("row", "facts", "best_for", "limits", "rating")}
    a.update(kw)
    a.setdefault("rating", (0, 0))
    return a


def en(page, i):
    return page["apps"][i]


# ---------------------------------------------------------------- Calm
CALM = dict(COMMON, **{
    "group": "calm-alternatives", "cover": "sleep-sounds",
    "path": "es/alternativas-a-calm-iphone/", "ct": "rl-calm-alt-es",
    "category": "HealthApplication",
    "title": "Mejores alternativas a Calm para dormir y meditar en iPhone (2026)",
    "h1": "Alternativas a Calm para iPhone en 2026",
    "description": "Siete alternativas a Calm en iPhone: Headspace, Insight Timer, BetterSleep, Medito, White Noise Lite y Drop. Precios, valoraciones y privacidad.",
    "llms": "Compara Calm con seis alternativas para iPhone (Headspace, Insight Timer, BetterSleep, Medito, White Noise Lite, Drop) por precio en euros, tipo de contenido (meditación, cuentos para dormir, sonidos, ruido blanco), etiqueta de privacidad y valoración.",
    "disclosure": "Drop es de Saga Labs, la empresa que hace Reviewland. Es una opción más de la lista, no va primera por ser nuestra, y es una app mucho más pequeña que Calm. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store.",
    "answer": [
        "La mejor alternativa a Calm depende de para qué uses Calm. Para meditación guiada sin pagar, Medito es totalmente gratis e Insight Timer tiene una biblioteca gratuita enorme. Para sonidos y cuentos para dormir, BetterSleep es lo más parecido de pago. Para ruido blanco a secas, White Noise Lite es gratis y trae más de 50 sonidos. Si solo quieres sonidos relajantes con temporizador y sesiones cortas de respiración, sin anuncios, eso hace Drop, y nada más.",
        "Calm se descarga gratis y tiene suscripción Premium (en España, de 12,99 € a 64,99 € según el plan); Headspace cobra 12,99 € al mes o 69,99 € al año. Todos los precios son los que lista el App Store de España el 16 de octubre de 2026.",
    ],
    "columns": ["App", "Precio (España)", "En qué destaca", "Sonidos para dormir / ruido blanco", "Etiqueta de privacidad", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Las siete se descargan gratis. Precios: compras dentro de la app listadas en el App Store de España el 16 de octubre de 2026 (una app puede listar varios precios para el mismo plan). Valoración: media y número de valoraciones en España ese día.",
    "apps": [
        app(en(C.EN, 0), name="Sonidos para Dormir: Drop",
            row=["Gratis (9 sonidos); Drop Pro listado a 5,99 € al mes, 17,99 € de acceso y varias opciones de pago único", "Sesiones cortas de respiración guiada (de 2 a 20 minutos) y sonidos relajantes con temporizador", "53 sonidos de naturaleza, ambiente y ruido, 9 gratis; ruido blanco gratis, rosa y marrón con Drop Pro", "", "", ""],
            best_for="una app tranquila y sin anuncios, con sonidos relajantes, temporizador de sueño y respiración corta, cuando una biblioteca de meditación completa es demasiado.",
            facts=[
                "Sesiones de respiración de 2, 5, 10 y 20 minutos con guía visual.",
                "53 sonidos en tres grupos (naturaleza, ambiente, ruido); 9 son gratis: ruido blanco, fuego, bosque, latido, lago, cafetería, nieve, desierto y delfines. La lluvia, el mar y el ruido rosa y marrón piden Drop Pro.",
                "Temporizador de 15, 30 o 45 minutos, 1, 2 u 8 horas, con fundido de 30 segundos.",
                "Una planta crece en cinco fases mientras practicas; rachas y logros.",
                "Widgets, funciona sin conexión y sin anuncios.",
                "6 idiomas (inglés, japonés, chino, francés, alemán y turco; no está en español), iOS 18 o posterior.",
            ],
            limits="no tiene cuentos para dormir, ni biblioteca de meditación con profesores, ni seguimiento del sueño, ni mezclador: suena un sonido cada vez, y el ruido rosa y el marrón piden Drop Pro. Solo 7 valoraciones en España y pide iOS 18."),
        app(en(C.EN, 1), name="Calm: Meditación y Sueño",
            row=["Gratis; suscripción Calm Premium (listada de 12,99 € a 64,99 € según el plan)", "Cuentos para dormir, meditación guiada, respiración y música", "Sonidos y paisajes sonoros (océano, lluvia fuerte, hoguera)", "", "", ""],
            best_for="cuentos para dormir narrados por voces conocidas y una biblioteca amplia y muy cuidada.",
            facts=[
                "Más de 100 cuentos para dormir (la ficha dice que añaden nuevos cada mes), algunos narrados por Matthew McConaughey y Stephen Fry.",
                "Sesiones diarias, programas de 7 y 21 días y ejercicios de respiración.",
                "Guarda las sesiones en Salud de Apple (minutos de atención plena).",
                "10 idiomas, iOS 18 o posterior, 179 MB.",
            ],
            limits="casi todo el contenido pide Premium, y su etiqueta de privacidad lista varios tipos de datos vinculados contigo, incluidos datos de salud y forma física."),
        app(en(C.EN, 2), name="Headspace: Sueño y Meditación",
            row=["Gratis; 12,99 € al mes o 69,99 € al año (Plus listado hasta 94,99 €)", "Meditaciones y cursos guiados, con terapia y coaching opcionales", "Sonidos, sleepcasts y meditaciones para dormir", "", "", ""],
            best_for="un enfoque de meditación con cursos y estructura, con apoyo humano disponible.",
            facts=[
                "Más de 500 meditaciones guiadas, desde reinicios de 3 minutos hasta sesiones largas.",
                "Herramientas de sueño: sleepcasts, meditaciones para dormir y sonidos.",
                "Terapia y coaching opcionales, y un acompañante con IA llamado Ebb, según su ficha.",
                "Solo inglés, iOS 15.6 o posterior, 451 MB, la más pesada de la lista.",
            ],
            limits="la ficha está solo en inglés, la terapia y el coaching son servicios de pago aparte, y es la que recoge más datos de las de aquí."),
        app(en(C.EN, 3), name="Insight Timer - Meditación",
            row=["Gratis; Premium listado a 7,49 €, 45,00 € y 62,99 €; familiar 59,99 €", "Enorme biblioteca gratuita de meditaciones guiadas, charlas y música", "Miles de pistas de música y sonidos ambientales", "", "", ""],
            best_for="meditación guiada gratis de muchos profesores distintos, más un temporizador de meditación.",
            facts=[
                "Miles de meditaciones y charlas gratis; la ficha dice que añaden más de 80 nuevas gratis al día.",
                "Temporizador de meditación, estadísticas, grupos de debate y minutos de atención plena en Salud.",
                "Miles de pistas de música y sonidos ambientales.",
                "10 idiomas, iOS 15 o posterior, 243 MB.",
            ],
            limits="tanto contenido cuesta de elegir; Premium desbloquea funciones extra y su etiqueta de privacidad lista muchos tipos de datos."),
        app(en(C.EN, 4), name="BetterSleep: Relax and Sleep",
            row=["Gratis; Premium listado de 9,99 € a 99,99 € según el plan", "Sonidos para dormir, cuentos, seguimiento y grabadora del sueño", "Más de 300 sonidos y pistas de música, incluido ruido blanco", "", "", ""],
            best_for="quien prioriza el sueño y quiere mezclador de sonidos, cuentos y seguimiento del sueño en una sola app.",
            facts=[
                "Más de 300 sonidos y pistas (naturaleza, ASMR, ruido blanco, sonidos binaurales) que se pueden mezclar.",
                "Más de 250 meditaciones y sesiones de hipnosis, y más de 100 cuentos para dormir.",
                "Seguimiento y grabadora del sueño; integración opcional con Salud; recordatorios y temporizadores.",
                "10 idiomas, iOS 15 o posterior, 317 MB.",
            ],
            limits="los sonidos y contenidos premium piden suscripción, y lista muchos precios distintos."),
        app(en(C.EN, 5), name="Medito: Mindfulness Meditación",
            row=["Gratis, sin compras dentro (organización sin ánimo de lucro)", "Meditación guiada, cursos y cuentos para dormir gratis", "Paisajes sonoros: lluvia, océano, ruido blanco", "", "", ""],
            best_for="meditación guiada totalmente gratis de una organización sin ánimo de lucro.",
            facts=[
                "Cursos de calma diaria, concentración, ansiedad y sueño; programas de inicio de 7 días y de 30 días.",
                "Cuentos para dormir y paisajes sonoros; modo sin conexión; temporizadores de respiración y escaneos corporales.",
                "Solo inglés, iOS 15 o posterior, 87 MB.",
            ],
            limits="una biblioteca más pequeña que la de Calm o Headspace, y solo en inglés."),
        app(en(C.EN, 6), name="White Noise Lite",
            row=["Gratis, sin compras dentro listadas", "Sonidos en bucle, mezclador y temporizador de sueño", "Más de 50 sonidos, con ruido blanco, rosa, marrón, azul y violeta", "", "", ""],
            best_for="ruido blanco, rosa o marrón puro y sonidos de ventilador, lluvia o tren, con temporizadores y alarmas.",
            facts=[
                "Más de 50 sonidos en bucle, incluidos ruido blanco, rosa, marrón, azul y violeta.",
                "Mezclador para crear tus propias mezclas; audio de fondo para usar otras apps.",
                "Temporizadores y alarmas con fundido de entrada y salida; reloj a pantalla completa.",
                "3 idiomas (inglés, francés y español), iOS 14 o posterior, 94 MB.",
            ],
            limits="no tiene meditación, respiración ni cuentos para dormir: es solo una máquina de sonidos."),
    ],
    "who": [
        "<strong>Quieres meditación guiada y no quieres pagar:</strong> Medito o Insight Timer.",
        "<strong>Quieres cuentos para dormir y una biblioteca cuidada:</strong> Calm, o BetterSleep si lo tuyo es sobre todo dormir.",
        "<strong>Quieres cursos, y quizá un terapeuta o coach:</strong> Headspace.",
        "<strong>Solo necesitas ruido blanco o marrón:</strong> White Noise Lite.",
        "<strong>Quieres sonidos relajantes con temporizador, respiración corta y nada de ruido:</strong> Drop.",
    ],
    "cases": [
        "Conciliar el sueño: cuentos para dormir (Calm), seguimiento y mezclador (BetterSleep), ruido blanco constante (White Noise Lite).",
        "Un reinicio de dos minutos entre reuniones (la sesión de 2 minutos de Drop o una meditación corta de Headspace).",
        "Meditación diaria con poco presupuesto (Medito, Insight Timer).",
        "Tapar el ruido de la calle o de casa por la noche (White Noise Lite, BetterSleep).",
    ],
    "method": [
        f"El {DATE} abrimos la ficha de cada app en el App Store de España y los datos de búsqueda de Apple: compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño, iOS mínimo y etiqueta de privacidad. Las funciones son las que cada desarrollador lista en su ficha; en Drop, que es nuestra, la lista de sonidos sale de la propia app (versión 2.10, actualizado el 24 de octubre de 2026), porque su ficha solo nombra cinco. No inventamos valoraciones ni reseñas, y no probamos la calidad del audio de cada app.",
    ],
    "faq": [
        ("¿Cuál es la mejor alternativa a Calm en iPhone?",
         "Headspace es la más parecida para meditación guiada, BetterSleep para sonidos y cuentos para dormir, Medito si quieres algo totalmente gratis e Insight Timer por la mayor biblioteca gratuita. Depende de si usas Calm para meditar, dormir o escuchar sonidos."),
        ("¿Hay una alternativa gratis a Calm?",
         "Sí. Medito es gratis y sin compras dentro, Insight Timer tiene una gran biblioteca gratuita con Premium opcional, y White Noise Lite es gratis para sonidos."),
        ("¿Qué alternativa a Calm tiene ruido blanco?",
         "White Noise Lite tiene ruido blanco, rosa, marrón, azul y violeta. BetterSleep lista ruido blanco entre más de 300 sonidos. Medito lo lista en sus paisajes sonoros. Drop, desde la versión 2.10, tiene ruido blanco gratis y ruido rosa, marrón y marrón profundo con Drop Pro."),
        ("¿Drop tiene cuentos para dormir como Calm?",
         "No. Drop ofrece sesiones cortas de respiración guiada y 53 sonidos relajantes (9 gratis) con temporizador de sueño. No tiene cuentos para dormir ni biblioteca de meditación."),
        ("¿Cuánto cuesta Calm?",
         "Calm se descarga gratis y lista suscripciones Premium de 12,99 € a 64,99 € en el App Store de España, según el plan. Mira la oferta dentro de la app antes de suscribirte."),
    ],
    "sources": C.src("es"),
})

# ---------------------------------------------------------------- Todoist
TODO = dict(COMMON, **{
    "group": "todoist-alternatives", "cover": "simple-todo",
    "path": "es/alternativas-a-todoist-iphone/", "ct": "rl-todoist-alt-es",
    "category": "ProductivityApplication",
    "title": "Mejores alternativas a Todoist para iPhone (2026)",
    "h1": "Alternativas a Todoist para iPhone en 2026",
    "description": "Cinco alternativas a Todoist en iPhone comparadas: TickTick, Things 3, Microsoft To Do, Structured y 3 Tasks. Precios, valoraciones y privacidad.",
    "llms": "Compara Todoist con cinco alternativas para iPhone (TickTick, Things 3, Microsoft To Do, Structured, 3 Tasks) por precio en euros, si piden cuenta, funciones clave y etiqueta de privacidad.",
    "disclosure": "3 Tasks es de Saga Labs, la empresa que hace Reviewland. Es una opción más de la lista, no va primera por ser nuestra, y es una app deliberadamente mínima, no un sustituto completo de Todoist. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store.",
    "answer": [
        "Si buscas un sustituto completo de Todoist, TickTick es lo más parecido (plan gratis, Premium a 4,99 € al mes o 49,99 € al año, con hábitos, calendario y temporizador Pomodoro), Things 3 es la compra única bien pulida (9,99 €, sin suscripción) y Microsoft To Do es gratis. Si Todoist te parece demasiado, 3 Tasks hace lo contrario: tres tareas al día, un cronómetro por tarea, gratis.",
        "Todoist Pro cuesta 6,99 € al mes o 59,99 € al año en España; el plan gratis sigue siendo una cuenta normal de Todoist.",
    ],
    "columns": ["App", "Precio (España)", "En qué destaca", "Cuenta", "Etiqueta de privacidad", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Precios: los del App Store de España y sus compras dentro de la app el 16 de octubre de 2026 (una app puede listar varios precios para el mismo plan). Valoración: media y número de valoraciones en España ese día. «No lo indica» significa que la ficha no dice si hace falta cuenta.",
    "apps": [
        app(en(T.EN, 0), name="3 Tasks: Lista de Tareas",
            row=["Gratis; 3 Tasks Pro es una compra única (listada a 5,99 € y 9,99 €)", "Solo tres prioridades al día, con un cronómetro en cada una", "Sin cuenta", "", "", ""],
            best_for="quien se agobia con un gestor de tareas completo y quiere elegir las tres cosas que importan hoy.",
            facts=[
                "Tres prioridades diarias en una pantalla; cronómetro de inicio y pausa en cada tarea, al estilo Pomodoro, que sigue contando con la pantalla bloqueada.",
                "Repetir a diario para lo que haces cada día, un widget y modo oscuro, todo gratis.",
                "Pro (pago único, sin suscripción): historial de días terminados, rachas, exportar a CSV y cuatro temas de color.",
                "Sin anuncios y sin cuenta. Solo en inglés, iOS 18 o posterior, 16 MB.",
            ],
            limits="no tiene proyectos, fechas límite, recordatorios, compartir ni sincronización entre dispositivos: es una lista de tres para un día. Solo 2 valoraciones en España."),
        app(en(T.EN, 1), name="Todoist: To do list–Calendario",
            row=["Plan gratis; Pro a 6,99 € al mes o 59,99 € al año", "Proyectos, fechas en lenguaje natural, calendario y equipos", "Sí", "", "", ""],
            best_for="el punto de referencia: proyectos, fechas recurrentes y trabajo compartido en muchas plataformas.",
            facts=[
                "La entrada rápida entiende fechas escritas con tus palabras.",
                "Proyectos, vista de calendario y espacios de equipo.",
                "19 idiomas, iOS 17 o posterior, 385 MB.",
            ],
            limits="Pro es una suscripción, y es la app menos sencilla de la lista."),
        app(en(T.EN, 2), name="TickTick: Listas de tareas",
            row=["Gratis; Premium a 4,99 € o 5,99 € al mes, 49,99 € al año", "Tareas, vistas de calendario, hábitos, temporizador Pomodoro", "Sí (sincronización en la nube)", "", "", ""],
            best_for="la alternativa más parecida función por función, con una suscripción más barata.",
            facts=[
                "Tareas recurrentes, varios recordatorios, vistas de calendario, etiquetas, listas de comprobación y listas compartidas.",
                "Temporizador Pomo y seguimiento de hábitos incluidos; compatible con Siri.",
                "Premium sube los límites (299 listas, 999 tareas por lista y hasta 5 recordatorios por tarea, según la ficha).",
                "41 idiomas, iOS 15.5 o posterior, 329 MB.",
            ],
            limits="es tan completa como Todoist, así que no resuelve el problema de una lista demasiado grande. Algunas funciones piden Premium."),
        app(en(T.EN, 3), name="Things 3",
            row=["9,99 € una vez en iPhone, sin suscripción", "Proyectos, áreas, vistas Hoy y Próximamente con eventos del calendario", "No lo indica", "", "", ""],
            best_for="quien prefiere pagar una vez por un gestor de tareas pulido y bien diseñado.",
            facts=[
                "Tareas con notas, etiquetas y fechas límite; Proyectos y Áreas para las distintas partes de la vida.",
                "Recordatorios, tareas repetidas e integración con el calendario.",
                "9 idiomas, iOS 16.4 o posterior, 124 MB.",
            ],
            limits="la app de iPhone se paga por adelantado y no hay versión gratis para probarla."),
        app(en(T.EN, 4), name="Microsoft To Do",
            row=["Gratis, sin compras dentro", "Plan Mi día y listas sincronizadas con Microsoft 365", "Cuenta de Microsoft", "", "", ""],
            best_for="una lista totalmente gratis que funciona con Outlook y Microsoft 365.",
            facts=[
                "Mi día y sugerencias para planificar la jornada con todas tus listas.",
                "Listas compartidas con cuentas personales; los correos marcados de Outlook pueden convertirse en tareas.",
                "34 idiomas, iOS 17.6 o posterior, 168 MB.",
            ],
            limits="pide una cuenta de Microsoft, y su etiqueta de privacidad lista más tipos de datos que las otras de aquí."),
        app(en(T.EN, 5), name="Structured – Agenda del día",
            row=["Gratis; Pro mensual (listado a 2,99 € y 4,99 €), anual (9,99 € y 19,99 €) o de por vida 59,99 €", "Una línea de tiempo visual del día con tareas y eventos del calendario", "No lo indica", "", "", ""],
            best_for="quien piensa en bloques de tiempo y no en listas, incluida la gente que quiere una rutina diaria visual.",
            facts=[
                "Línea de tiempo del día con arrastrar y soltar, bandeja de entrada, subtareas con notas y temporizador de concentración Pomodoro, gratis.",
                "Sincroniza entre iPhone, iPad, Apple Watch y Mac según su ficha; widgets y Actividades en directo.",
                "Pro añade la conexión con el calendario y Recordatorios, tareas recurrentes y rutinas, y planificación del día con IA.",
                "28 idiomas, iOS 18 o posterior, 291 MB.",
            ],
            limits="las tareas recurrentes y la conexión con el calendario son de Pro, y Pro lista muchos precios, incluida una opción de por vida a 59,99 €."),
    ],
    "who": [
        "<strong>Quieres las mismas funciones por menos al mes:</strong> TickTick.",
        "<strong>Quieres pagar una vez y no suscribirte nunca:</strong> Things 3.",
        "<strong>Quieres todo gratis y usas Outlook:</strong> Microsoft To Do.",
        "<strong>Tu día es una agenda de bloques de tiempo:</strong> Structured.",
        "<strong>Tus listas no paran de crecer y nunca las terminas:</strong> 3 Tasks, tres al día y nada más.",
    ],
    "cases": [
        "Pasar de una configuración de Todoist con muchos proyectos a algo con precio único (Things 3).",
        "Un equipo o una familia que comparte listas (Todoist, TickTick, Microsoft To Do).",
        "Elegir las tres cosas que deben pasar hoy antes de abrir el correo (3 Tasks).",
        "Cronometrar bloques de trabajo concentrado por tarea (el Pomodoro de TickTick o el cronómetro por tarea de 3 Tasks).",
    ],
    "method": [
        f"El {DATE} abrimos la ficha de cada app en el App Store de España y los datos de búsqueda de Apple: precio y compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño, iOS mínimo y etiqueta de privacidad. Las funciones son las que cada desarrollador lista en su ficha. No inventamos valoraciones ni reseñas. La app Recordatorios del iPhone también es gratis y no hace falta descargarla, pero no tiene ficha en el App Store para comparar.",
    ],
    "faq": [
        ("¿Cuál es la mejor alternativa gratis a Todoist?",
         "Microsoft To Do es gratis y sin compras dentro. TickTick tiene un plan gratis con una mejora Premium con límites más altos, y 3 Tasks es gratis si quieres una lista mucho más simple."),
        ("¿Hay una alternativa a Todoist con pago único?",
         "Things 3 cuesta 9,99 € una vez en iPhone, sin suscripción. 3 Tasks es gratis, con una compra Pro única opcional para historial, rachas, exportación a CSV y temas de color."),
        ("¿Qué alternativa a Todoist se parece más?",
         "TickTick: tareas recurrentes, recordatorios, vistas de calendario, etiquetas y listas compartidas, con una suscripción Premium de 4,99 € al mes o 49,99 € al año."),
        ("¿3 Tasks sustituye a Todoist?",
         "No. 3 Tasks solo guarda tres tareas al día, con un cronómetro en cada una. No tiene proyectos, recordatorios, fechas límite, compartir ni sincronización. Es para quien quiere menos tareas, no más."),
        ("¿Estas apps piden cuenta?",
         "Todoist, TickTick y Microsoft To Do la piden para sincronizar. 3 Tasks no necesita cuenta."),
    ],
    "sources": T.src("es"),
})

# ---------------------------------------------------------------- CoinStats / Delta
COIN = dict(COMMON, **{
    "group": "coinstats-alternatives", "cover": "crypto-widgets",
    "path": "es/alternativas-a-coinstats-y-delta-iphone/", "ct": "rl-coinstats-alt-es",
    "category": "FinanceApplication",
    "title": "Mejores alternativas a CoinStats y Delta para seguir cripto en iPhone (2026)",
    "h1": "Alternativas a CoinStats y Delta para iPhone en 2026",
    "description": "Cinco apps para seguir tu cartera cripto en iPhone comparadas: CoinStats, Delta, CoinGecko, CoinMarketCap y Crypton. Precios y privacidad.",
    "llms": "Compara CoinStats y Delta con tres alternativas para iPhone (CoinGecko, CoinMarketCap, Crypton) por precio en euros, conexión con carteras y exchanges, alertas, límites del plan gratis y etiqueta de privacidad.",
    "disclosure": "Crypton es de Saga Labs, la empresa que hace Reviewland. Es una opción más de la lista, no va primera por ser nuestra, y es mucho más simple que CoinStats o Delta. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store. Nada de esto es asesoramiento financiero.",
    "answer": [
        "Si quieres un seguimiento que se conecte a tus exchanges y carteras, CoinStats y Delta son las pesadas, y las dos tienen planes de pago (CoinStats lista suscripciones Premium de 134,99 € a 184,99 € al año; el plan gratis de Delta sigue 10 activos). Si solo quieres precios, noticias y una lista de seguimiento, CoinGecko y CoinMarketCap son gratis y mucho más grandes. Si solo quieres una lista rápida, gratis y sin anuncios de las principales monedas con tus tenencias apuntadas a mano, Crypton hace eso y nada más.",
        "Crypton no se conecta a carteras ni a exchanges y no tiene alertas de precio, así que no sustituye a CoinStats ni a Delta si necesitas sincronización automática.",
    ],
    "columns": ["App", "Precio (España)", "En qué destaca", "Conexión con carteras / exchanges", "Etiqueta de privacidad", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Las cinco se descargan gratis. Precios: compras dentro de la app listadas en el App Store de España el 16 de octubre de 2026 (las apps listan varios precios para el mismo plan). Valoración: media y número de valoraciones en España ese día.",
    "apps": [
        app(en(K.EN, 0), name="Crypton: Precios Cripto",
            row=["Gratis, sin anuncios y sin compras dentro", "Una lista rápida y simple de las principales monedas con una cartera manual", "No", "", "", ""],
            best_for="un vistazo gratis y sin anuncios a las principales monedas y a tus tenencias, una o dos veces al día.",
            facts=[
                "Cartera con las cantidades que apuntas, su valor y el cambio por moneda, y un gráfico de precio con vistas de 1D, 1W, 1M, 3M y 1Y.",
                "Favoritas y lista de seguimiento; sigue más de 250 monedas según la ficha.",
                "Cuenta opcional (solo para sincronizar), sin anuncios y nada que comprar.",
                "Solo en inglés, iOS 18 o posterior, 19 MB.",
            ],
            limits="no se conecta a carteras ni exchanges, no tiene alertas de precio y en la versión actual no tiene widgets ni app para Apple Watch; los precios se actualizan cada pocas horas, así que no sirve para operar; y los gráficos cargan desde Binance, que bloquea conexiones desde EE. UU., por lo que allí pueden fallar (lo vimos al comprobarlo el 11 de octubre). No calcula ganancias y pérdidas por precio de compra."),
        app(en(K.EN, 1), name="Crypto Tracker - Coin Stats",
            row=["Gratis; Premium listado de 134,99 € a 184,99 € al año o 17,99 € a 21,99 € al mes; Pro desde 41,99 € al año", "Cartera con más de 300 carteras y exchanges, con ganancias y pérdidas e información con IA", "Sí: más de 300 carteras y exchanges, o pegando la dirección de una cartera", "", "", ""],
            best_for="quien tiene varias carteras y exchanges y quiere verlo todo en una sola cartera.",
            facts=[
                "Conecta más de 300 carteras y exchanges (MetaMask, Phantom, Binance, Coinbase y otros), o desde una dirección pegada.",
                "Ganancias y pérdidas realizadas y no realizadas, coste base y exportación para informes fiscales.",
                "Precios de más de 20.000 monedas, alertas personalizadas y automáticas, noticias de más de 140 fuentes y un asistente de IA sobre tus tenencias.",
                "13 idiomas, iOS 15 o posterior, 197 MB.",
            ],
            limits="lo mejor está en planes de pago con muchos precios distintos, y es una app grande que te pide conectar tus cuentas."),
        app(en(K.EN, 2), name="Delta by eToro",
            row=["Gratis (hasta 10 activos); PRO listado desde 6,99 € al mes o 61,99 € al año; PRO+ hasta 107,99 € al año", "Cripto, acciones, ETF y divisas en una sola cartera", "Sí: más de 200 exchanges, brókeres y carteras", "", "", ""],
            best_for="seguir cripto y acciones juntas, con sincronización automática.",
            facts=[
                "Sincroniza más de 200 exchanges, brókeres y carteras; sigue acciones, ETF, divisas, materias primas y más de 10.000 monedas.",
                "Plan gratis: hasta 10 activos, conexiones ilimitadas, alertas de precio y 3 usos de IA al mes.",
                "PRO sube el límite a 40 activos; PRO+ es ilimitado, según la ficha.",
                "18 idiomas, iOS 16.4 o posterior, 131 MB.",
            ],
            limits="el plan gratis se queda en 10 activos y sus precios tienen muchos niveles (PRO, PRO+)."),
        app(en(K.EN, 3), name="CoinGecko: Crypto Tracker, NFT",
            row=["Gratis; Premium 9,90 € al mes o 99,90 € al año", "Datos de mercado de más de 10.000 monedas, NFT y categorías, más una cartera", "No (la cartera se apunta a mano)", "", "", ""],
            best_for="investigar monedas y categorías, con una cartera gratis de apoyo.",
            facts=[
                "Datos en tiempo real de más de 10.000 criptomonedas, volúmenes de exchanges y más de 3.000 colecciones de NFT.",
                "Cartera con ganancias y pérdidas, alertas de precio, widgets de pantalla de inicio y conversor.",
                "Solo inglés, iOS 16 o posterior, 161 MB.",
            ],
            limits="está pensada para investigar el mercado más que para sincronizar tus cuentas; la cartera es manual."),
        app(en(K.EN, 4), name="CoinMarketCap: Crypto Tracker",
            row=["Gratis; planes de pago Essential desde 12,99 € al mes hasta Max a 129,99 € al mes", "Precios, listas de seguimiento, noticias y una cartera en tiempo real", "No lo indica", "", "", ""],
            best_for="la mayor base de datos de precios y noticias en una app gratis.",
            facts=[
                "Seguimiento de cartera en más de 90 divisas, listas de seguimiento personalizadas y alertas de precio.",
                "Noticias y tendencias del mercado cripto en la misma app.",
                "21 idiomas, iOS 15 o posterior, 224 MB.",
            ],
            limits="una app grande con noticias y muchos extras; sus planes de pago llegan a 129,99 € al mes."),
    ],
    "who": [
        "<strong>Tienes monedas en varios exchanges y carteras:</strong> CoinStats o Delta.",
        "<strong>Sigues acciones y cripto a la vez:</strong> Delta.",
        "<strong>Investigas monedas y quieres una cartera gratis:</strong> CoinGecko o CoinMarketCap.",
        "<strong>Solo quieres echar un vistazo a las principales monedas y a tus tenencias, gratis y sin anuncios:</strong> Crypton.",
    ],
    "cases": [
        "Ver el valor total de carteras y exchanges en un solo sitio (CoinStats, Delta).",
        "Mirar el precio de una moneda y por qué se movió (CoinGecko, CoinMarketCap).",
        "Un vistazo rápido por la mañana a las principales monedas y a tus tenencias (Crypton).",
        "Exportar transacciones para la declaración de impuestos (CoinStats lista informes fiscales).",
    ],
    "method": [
        f"El {DATE} abrimos la ficha de cada app en el App Store de España y los datos de búsqueda de Apple: compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño, iOS mínimo y etiqueta de privacidad. Las funciones son las que cada desarrollador lista en su ficha. Los límites de Crypton salen de nuestras propias pruebas de la versión 2.0.4. No inventamos valoraciones ni reseñas, y nada de esto es asesoramiento financiero.",
    ],
    "faq": [
        ("¿Cuál es la mejor alternativa a CoinStats en iPhone?",
         "Delta es la más parecida para sincronizar exchanges y carteras. CoinGecko y CoinMarketCap son gratis para precios y una cartera manual, y Crypton es una lista simple y gratis."),
        ("¿Hay una alternativa gratis a Delta?",
         "CoinGecko y CoinMarketCap se descargan gratis con planes de pago opcionales, y Crypton es gratis sin compras. El propio Delta tiene un plan gratis limitado a 10 activos."),
        ("¿Qué app de criptomonedas se conecta a exchanges y carteras?",
         "CoinStats lista más de 300 carteras y exchanges y Delta más de 200. Crypton no se conecta a ninguno."),
        ("¿Crypton tiene alertas de precio o widgets?",
         "No en la versión actual (2.0.4). Tiene favoritas, lista de seguimiento y una cartera manual con gráficos."),
        ("¿Es esto asesoramiento financiero?",
         "No. Esta página compara funciones, precios y valoraciones de apps tal como aparecen en el App Store."),
    ],
    "sources": K.src("es"),
})

# ---------------------------------------------------------------- Private Photo Vault
VAULT = dict(COMMON, **{
    "group": "photo-vault-alternatives", "cover": "hide-photos",
    "path": "es/alternativas-a-private-photo-vault-iphone/", "ct": "rl-vault-alt-es",
    "category": "PhotographyApplication",
    "title": "Mejores alternativas a Private Photo Vault para iPhone (2026)",
    "h1": "Alternativas a Private Photo Vault para iPhone en 2026",
    "description": "Cinco alternativas a Private Photo Vault en iPhone: Keepsafe, PV Secret Photo Album, Secret Photo Album SA y Photo Vault. Precios y privacidad.",
    "llms": "Compara Private Photo Vault - Pic Safe (en España «Ocultar Fotos - Photo Vault») con cuatro alternativas para iPhone (Keepsafe, PV, Secret Photo Album SA, Photo Vault) por precio, copia en la nube, funciones de señuelo y alerta de intrusos y etiqueta de privacidad.",
    "disclosure": "Photo Vault: Hide Pics Video (en España, «Boveda: Ocultar Fotos y Video») es de Saga Labs, la empresa que hace Reviewland. Es una opción más de la lista, no va primera por ser nuestra. Ojo: es una app distinta de «Private Photo Vault - Pic Safe», que no es nuestra. Las demás tampoco son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store.",
    "answer": [
        "Private Photo Vault - Pic Safe es la app de bóveda más grande del App Store (más de un millón de valoraciones en total, 4,8 estrellas en EE. UU.). Si buscas alternativa, Keepsafe es la grande más parecida con nube privada opcional, PV - Secret Photo Album tiene más funciones y la suscripción más barata, y Photo Vault: Hide Pics Video no pide cuenta y lo guarda todo en el teléfono salvo que actives su copia cifrada opcional en iCloud.",
        "iOS ya trae un álbum Oculto gratis en Fotos; para una privacidad casual puede bastar. La guía de Apple está enlazada en las fuentes.",
    ],
    "columns": ["App", "Precio (España)", "Copia en la nube", "Funciones de privacidad", "Etiqueta de privacidad", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Las cinco se descargan gratis. Precios: compras dentro de la app listadas en el App Store de España el 16 de octubre de 2026 (las apps listan varios precios para el mismo plan, y la de Photo Vault aún incluye un producto antiguo llamado «Keeper Pro»). Valoración: media y número de valoraciones en España ese día; en España las apps pequeñas tienen muy pocas.",
    "apps": [
        app(en(P.EN, 0), name="Boveda: Ocultar Fotos y Video",
            row=["Gratis; Premium anual (listado a 22,99 € y 34,99 €) o de por vida (17,99 €, 34,99 € y 69,99 €)", "Opcional: una copia cifrada de extremo a extremo en tu propio iCloud, desactivada por defecto; sin cuenta; o un archivo cifrado que exportas tú", "Face ID, contraseña por álbum, código señuelo (Premium), icono disfrazado, salida boca abajo, cámara privada", "", "", ""],
            best_for="quien quiere las fotos solo en el iPhone, sin cuenta y sin subir nada.",
            facts=[
                "Se abre con Face ID, Touch ID o código, y cada álbum puede tener su propia contraseña.",
                "Icono disfrazado (Calculadora, Notas o Tiempo) y salida boca abajo que salta a Safari, Calendario o Mensajes.",
                "La cámara privada hace las fotos directamente en la bóveda, sin pasar por el carrete.",
                "Queda fuera de las copias de iCloud; para cambiar de iPhone exportas un archivo protegido con contraseña y lo restauras. Funciona sin conexión.",
                "19 idiomas, iOS 17 o posterior, 17 MB.",
            ],
            limits="sin la copia opcional en iCloud no hay copia automática: si borras la app sin exportar la bóveda, se pierde. La versión gratis es limitada (guardaba un solo elemento cuando lo comprobamos el 11 de octubre), así que en la práctica es de pago. Solo 1 valoración en España (de 1 estrella) y es una app mucho más joven que las demás."),
        app(en(P.EN, 1), name="Ocultar Fotos - Photo Vault",
            row=["Gratis; Premium listado a 7,99 €, 12,99 €, 35,99 €, 37,99 € y 43,99 €", "Cloud Vault cifrado opcional", "Bloqueo con PIN o patrón, contraseña por álbum, informe de intrusión con foto y GPS, contraseña señuelo, bloqueo boca abajo", "", "", ""],
            best_for="la bóveda más conocida, con una lista larga de funciones que incluye un navegador privado.",
            facts=[
                "Informe de intrusión con foto y GPS, contraseña señuelo y bloqueo boca abajo, según su ficha.",
                "Navegador web privado que puede descargar fotos a la app; importar y exportar, y transferencia inalámbrica de fotos.",
                "Copia en la nube cifrada opcional («Cloud Vault»); la ficha dice que sus empleados no pueden ver tus fotos.",
                "11 idiomas, iOS 15 o posterior, 172 MB.",
            ],
            limits="su etiqueta de privacidad lista varios tipos de datos vinculados contigo, y varias funciones piden Premium."),
        app(en(P.EN, 2), name="Keepsafe-Protege Fotos, Videos",
            row=["Gratis; Premium listado de 4,99 € a 39,99 € (anual 23,99 € o 26,49 €, mensual 10,99 €)", "Nube privada opcional (Premium)", "PIN, Touch ID, bloqueo de álbum con PIN independiente, Safe Send", "", "", ""],
            best_for="una bóveda fácil con sincronización opcional en la nube entre dispositivos.",
            facts=[
                "Bloqueo con PIN y huella; el bloqueo de álbum da a cada álbum su propio PIN con Premium.",
                "La nube privada guarda hasta 10.000 elementos y sincroniza entre dispositivos (Premium); Safe Send comparte imágenes durante un tiempo limitado.",
                "Cámara integrada y recuperación de la papelera.",
                "16 idiomas, iOS 17 o posterior, 210 MB.",
            ],
            limits="la copia en la nube y el bloqueo por álbum piden Premium, y tus fotos van a su nube si la activas."),
        app(en(P.EN, 3), name="foto privadas - proteger album",
            row=["Gratis (con anuncios); membresía anual 19,99 €, mensual 3,99 €, permanente 49,99 €; planes de nube de 13,99 € a 89,99 € al año", "Planes de copia en la nube opcionales", "Face ID, contraseña falsa, interruptor de emergencia boca abajo, icono personalizable", "", "", ""],
            best_for="la lista de funciones más larga con las suscripciones más baratas.",
            facts=[
                "Almacenamiento gratis e ilimitado, según su ficha, con contraseña y Face ID, contraseña falsa e icono personalizable.",
                "Etiquetas, notas y búsqueda, editor de fotos, audio y Nearby Drop entre teléfonos.",
                "La transferencia por Wi-Fi a un PC y la copia en nubes de terceros son de Pro; los anuncios se quitan con una compra.",
                "12 idiomas, iOS 15 o posterior, 157 MB.",
            ],
            limits="la versión gratis muestra anuncios, y su etiqueta de privacidad incluye datos de contacto e identificadores vinculados contigo."),
        app(en(P.EN, 4), name="SA - Ocultar fotos secretas",
            row=["Gratis; Premium listado de 2,49 € a 51,99 € según el plan", "Copia en la nube segura (almacenamiento ilimitado con Premium)", "PIN, Touch ID y Face ID, PIN señuelo, alertas de intrusión con fotos del intruso, PIN independiente por álbum", "", "", ""],
            best_for="una bóveda simple si te da igual una lista larga de tipos de datos en su etiqueta de privacidad.",
            facts=[
                "Bóveda cifrada con PIN, PIN señuelo, alertas de intrusión con foto del intruso y un PIN aparte para álbumes seleccionados.",
                "Navegador privado con bloqueador de anuncios y cámara integrada; el almacenamiento ilimitado en la nube es de Premium. Aparte, una compra de Secret Calculator Photo Vault figura a 9,99 €.",
                "12 idiomas, iOS 15 o posterior, 80 MB, la más ligera de la competencia.",
            ],
            limits="tiene la etiqueta de privacidad más larga de las cinco, con ubicación incluida, y su Premium lista muchos precios distintos."),
    ],
    "who": [
        "<strong>No quieres que se suba nada ni tener cuenta:</strong> Photo Vault: Hide Pics Video.",
        "<strong>Quieres la app más conocida y un informe de intrusión:</strong> Private Photo Vault - Pic Safe.",
        "<strong>Quieres tus fotos sincronizadas en una nube privada:</strong> Keepsafe o Private Photo Vault.",
        "<strong>Quieres más funciones por menos dinero:</strong> PV - Secret Photo Album.",
        "<strong>Solo necesitas esconder unas fotos de miradas casuales:</strong> el álbum Oculto de iOS, que no necesita app.",
    ],
    "cases": [
        "Mantener las fotos privadas fuera del carrete compartido y fuera de iCloud (una app sin cuenta y con nube solo si la activas, como la nuestra).",
        "Hacer copia de la bóveda para no perder las fotos si pierdes el teléfono (la nube de Keepsafe o de Private Photo Vault).",
        "Dejar el teléfono a alguien sin que vea la app (iconos disfrazados y salida boca abajo).",
        "Cambiar de iPhone: con la nuestra exportas y restauras un archivo tú; las apps con nube restauran desde su nube.",
    ],
    "method": [
        f"El {DATE} abrimos la ficha de cada app en el App Store de España y los datos de búsqueda de Apple: compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño, iOS mínimo y etiqueta de privacidad. Las funciones son las que cada desarrollador lista en su ficha; no verificamos su cifrado. No inventamos valoraciones ni reseñas.",
    ],
    "faq": [
        ("¿Cuál es la mejor alternativa a Private Photo Vault?",
         "Keepsafe es la grande más parecida, con nube privada opcional. PV - Secret Photo Album tiene más funciones por la suscripción más barata. Photo Vault: Hide Pics Video es la opción sin cuenta, y su copia en iCloud es opcional y viene desactivada."),
        ("¿Photo Vault: Hide Pics Video es lo mismo que Private Photo Vault?",
         "No. Son apps distintas de desarrolladores distintos. Photo Vault: Hide Pics Video es de Saga Ltd.; Private Photo Vault - Pic Safe es de Legendary Software Labs."),
        ("¿Qué bóveda de fotos no usa la nube?",
         "Photo Vault: Hide Pics Video lo guarda todo en el iPhone, sin cuenta y sin sincronización, y su etiqueta de privacidad dice «No se recopilan datos». En Private Photo Vault, Keepsafe y PV la copia en la nube es opcional."),
        ("¿Necesito una app de bóveda?",
         "No siempre. El iPhone tiene un álbum Oculto en Fotos que puedes bloquear con Face ID o código en las versiones recientes de iOS; una app añade álbumes separados, iconos disfrazados y otras funciones. Mira la guía de Apple en las fuentes."),
        ("¿Puedo pasar mi bóveda a un iPhone nuevo?",
         "Con Photo Vault: Hide Pics Video exportas un archivo protegido con contraseña y lo restauras en el teléfono nuevo, porque la bóveda queda fuera de las copias de iCloud. Las bóvedas con nube restauran desde su propia nube."),
    ],
    "sources": P.src("es"),
})

for _p in (CALM, TODO, COIN, VAULT):
    refresh(_p, "es")

PAGES = [CALM, TODO, COIN, VAULT]
