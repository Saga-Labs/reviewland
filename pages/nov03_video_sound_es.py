"""Mejores apps de vídeo con IA con sonido para iPhone. ES, tienda de España. Nuestra app: Dora (id6754180384), 4.ª de 6.
Comprobado el 2026-11-03 (JST): iTunes lookup (country=es) y páginas del App Store de España. Etiquetas de privacidad, las mismas que en EE. UU.
Gemini Omni (audio nativo, 10 s, plan Google AI, mayores de 18) en gemini.google; Kling 4.0 con sonido en klingai.com (la ficha no lo dice).
Dora: ficha 1.4.2 «Vídeos con sonido, en los modelos que lo admiten»; Seedance 2 Mini con sonido, 31 monedas por 8 s (doravideo.com/models).
Versión inglesa: nov03_video_sound.py."""

DAY = "2026-11-03"
TRACK = "Datos usados para rastrearte"
LINKED = "Datos vinculados contigo"
NOTLINKED = "Datos no vinculados contigo"


def label(*x):
    return "; ".join(x)


def rating(r, n):
    return "Sin valoraciones en España" if not n else str(round(r, 1)).replace('.', ',')


def app(name, i, anchor, dev, r, n, ver, date, labels, price, sound, length, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, sound, length, labels, f"{ver} ({date})", rating(r, n)]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("Grok", 6670324846, "grok", "X Corp.", 4.81, 75204, "1.4.61", "1 nov 2026", label(TRACK, LINKED, NOTLINKED),
        "SuperGrok Lite 10 €, SuperGrok 35 €, Plus 100 €, Heavy 349 €; créditos de 6 € a 100 €",
        "«Vídeos cortos con sonido», desde texto o una foto", "Cortos; la ficha no da la duración",
        "un clip rápido con sonido dentro de una app de chat que quizá ya usas.",
        ["Su ficha dice que Grok Imagine crea vídeos cortos con sonido y convierte tus fotos en vídeos.", "38 idiomas, entre ellos el español."],
        "el vídeo es una función más de una app de chat, y la ficha no dice cuánto dura ni cuánto cuesta cada vídeo."),
    app("Google Gemini", 6477489729, "gemini", "Google LLC", 4.69, 215922, "1.2026.4262206", "29 oct 2026", LINKED,
        "Google AI Plus 4,99 € o Pro 21,99 € al mes", "Audio nativo con Gemini Omni, según la web de Google", "Hasta 10 s",
        "quien paga un plan de Google AI y quiere vídeo con sonido desde texto o hasta cinco fotos.",
        ["Su ficha dice que Gemini Omni convierte ideas en vídeos para usuarios de Google AI Plus, Pro y Ultra; la web de Gemini habla de audio nativo, vídeos de 10 segundos y de foto a vídeo con hasta cinco fotos.", "Según la web de Google, Gemini Omni sustituyó a Veo en la app de Gemini.", "La única etiqueta de privacidad de la lista sin «Datos usados para rastrearte»."],
        "el vídeo necesita un plan de pago de Google AI, y la web de Google dice que es para mayores de 18 años."),
    app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.62, 1750, "3.9.32", "2 nov 2026", label(TRACK, LINKED, NOTLINKED),
        "Standard 10 €, Pro 39 €, Premier 99 € al mes; una semana desde 0,99 €; créditos desde 1,99 €",
        "Kling 4.0 con sonido, según la web de Kling; la ficha no lo dice", "Hasta 15 s, ampliable",
        "clips nítidos, con sonido en el modelo más nuevo.",
        ["La web de Kling presenta Kling 4.0 como un modelo que hace imagen y sonido a la vez.", "La app hace vídeo desde texto o fotos, hasta 15 segundos en 1080p o 4K, según su ficha; mira en el selector que el modelo que eliges tenga sonido."],
        "su ficha del App Store no habla de sonido y está en inglés, en 5 idiomas sin el español."),
    app("DORA · Generador Vídeo IA", 6754180384, "dora", "Saga Ltd.", 0, 0, "1.4.2", "26 oct 2026", label(TRACK, NOTLINKED),
        "Pro 7,99 € a la semana o 129,99 € al año; monedas de 5,99 € (300) a 249,99 € (25.000)",
        "«Vídeos con sonido, en los modelos que lo admiten»", "8 s con sonido por 31 monedas en el modelo por defecto",
        "un clip corto con sonido por un precio conocido, con el coste a la vista antes de tocar.",
        ["Su ficha dice que los vídeos llevan sonido en los modelos que lo admiten. La web de Dora dice que el modelo por defecto, Seedance 2 Mini, incluye sonido: 31 monedas por 8 segundos, unos 0,62 € con el paquete de 300 monedas.",
         "En la versión 1.4.2 ese modelo aún aparece como «SeeDance 1.5 Pro» en el selector; la web de Dora dice que esas peticiones ya van a Seedance 2 Mini.",
         "De texto o foto a vídeo, vertical 9:16 y sin marca de agua, según su ficha, que está en español."],
        "solo clips cortos, es una suscripción y no hay vídeo gratis.", True),
    app("invideo: Editor de vídeo IA", 6471394316, "invideo", "Invideo Inc", 4.61, 1293, "4.5.63", "27 oct 2026", label(TRACK, LINKED, NOTLINKED),
        "Plus 22 € a 29,99 €, Max 69,99 €, Generative 129,99 €; paquetes de 29 € a 60 €",
        "Genera voz, sonido y música con más de 200 modelos de IA", "Vídeos completos y montados",
        "un vídeo entero con locución, música y efectos de sonido mezclados en una línea de tiempo.",
        ["Su ficha dice que genera imágenes, vídeo, voz, sonido y música con más de 200 modelos de IA.", "Editor con línea de tiempo y agentes que ayudan a montar el vídeo."],
        "la app solo está en inglés, aunque la ficha está en español, y los planes cuestan más que los de un solo clip."),
    app("Pollo AI: Video e Imagen IA", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.28, 536, "4.3.1", "30 oct 2026", label(TRACK, LINKED),
        "6,99 € a la semana, 99,99 € al año; Lite 17 € o Pro 35 € al mes; créditos de 7,99 € a 79,99 €",
        "Vídeos multiescena «con movimiento cinematográfico y audio»", "Depende del modelo",
        "elegir entre muchos modelos de vídeo, algunos con audio nativo, en una sola app.",
        ["Su ficha nombra modelos como Seedance, Veo 3.1, Kling, Hailuo, Vidu y PixVerse, y dice que puedes elegir uno con audio nativo.", "De texto, foto, referencia o vídeo a vídeo, y avatares y voces con IA."],
        "la app solo está en inglés, y la ficha no dice qué modelos tienen sonido ni cuánto cuesta cada uno."),
]

PAGES = [{
    "group": "video-sound", "lang": "es", "store": "es", "path": "es/mejores-apps-video-ia-con-sonido-iphone/", "ct": "rl-video-sound-es",
    "category": "PhotoVideoApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Mejores apps de vídeo con IA con sonido para iPhone (2026)", "h1": "Mejores apps de vídeo con IA con sonido para iPhone",
    "description": "Seis apps de iPhone que hacen vídeo con IA con sonido, no clips mudos, comparadas por precio en España, duración, privacidad y valoración el 3 de noviembre de 2026.",
    "llms": "Seis apps de iPhone que generan vídeo con IA con sonido, con datos del App Store de España: Grok, Google Gemini, Kling AI, Dora, invideo, Pollo AI. De dónde sale que tienen sonido, precio en euros, duración, privacidad.",
    "answer": [
        "Muchos vídeos con IA siguen saliendo mudos. Estas seis apps de iPhone dicen que hacen vídeo con sonido. Para un clip rápido dentro de un chat, <strong>Grok</strong>. Si pagas un plan de Google AI, <strong>Gemini</strong> (Gemini Omni, hasta 10 segundos con audio nativo). Para un clip corto con sonido a un precio conocido (unos 0,62 € por 8 segundos con su modelo por defecto, Seedance 2 Mini), <strong>Dora</strong>. Para un vídeo entero con locución y música, <strong>invideo</strong>.",
        "El sonido suele depender del modelo que eliges, y algunas fichas ni lo mencionan: mira el modelo antes de generar. La web de Kling dice que Kling 4.0 hace sonido; su ficha del App Store no lo dice.",
    ],
    "columns": ["App", "Precio (España)", "Sonido, y dónde lo dice", "Duración", "Etiqueta de privacidad del App Store", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Precios de las compras dentro de la app en la página de cada app del App Store de España el 3 de noviembre de 2026; las páginas solo muestran algunas. Todas se descargan gratis. El sonido sale de la ficha salvo cuando la columna nombra la web de la empresa.",
    "apps": APPS,
    "who": ["<strong>Un clip con sonido desde un chat:</strong> Grok.", "<strong>Pagas Google AI:</strong> Gemini.", "<strong>Clips nítidos con el modelo más nuevo:</strong> Kling AI.",
            "<strong>El coste en monedas a la vista antes de cada clip:</strong> Dora.", "<strong>Locución, música y montaje:</strong> invideo.", "<strong>Probar muchos modelos:</strong> Pollo AI."],
    "cases": ["Un vídeo de tu perro en el que se le oiga ladrar: Dora, Grok o Gemini, y describe el sonido en el texto.", "Una escena con diálogo: Gemini o el modelo más nuevo de Kling; escribe la frase entre comillas.", "Un anuncio de 30 segundos con locución y música: invideo."],
    "method": ["El 3 de noviembre de 2026 leímos la página de cada app en el App Store de España y los datos de Apple, y para Gemini y Kling la web de la propia empresa, porque sus fichas no dicen si los vídeos llevan sonido. No generamos nada ni comparamos el sonido.",
               "Orden: primero las apps cuya ficha o web dice claramente que el vídeo lleva sonido, luego el editor y la app de muchos modelos. Esta página también existe en inglés, con precios de EE. UU."],
    "faq": [
        ("¿Qué app de iPhone hace vídeos con IA con sonido?", "Grok y Dora lo dicen en su ficha del App Store, invideo genera voz, sonido y música, y Pollo AI tiene modelos con audio nativo. Gemini y Kling lo dicen en su web."),
        ("¿Hay alguna app gratis de vídeo con IA con sonido?", "Ninguna de estas fichas promete vídeos gratis con sonido. Gemini necesita un plan de Google AI para el vídeo y las demás venden suscripciones o créditos."),
        ("¿Cómo consigo que un vídeo con IA tenga sonido?", "Elige un modelo con audio y describe el sonido en el texto, por ejemplo «lluvia suave y un perro ladrando»; las frases que se dicen, entre comillas."),
        ("¿Cuánto duran los vídeos con IA con sonido?", "Gemini Omni hace hasta 10 segundos, el modelo por defecto de Dora 8 segundos y Kling hasta 15 segundos por clip. La ficha de Grok solo dice que son cortos."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/es/app/id{a['id']}") for a in APPS] + [
        ("Gemini Omni (Google)", "https://gemini.google/overview/video-generation/"), ("Kling AI", "https://klingai.com/global/"), ("Dora: modelos y monedas", "https://doravideo.com/models")],
}]
