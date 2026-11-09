"""pt-BR translations of four English rankings (Brazilian App Store data checked 9 Nov 2026)."""
from pages.trlib import make

TR_TODO = {
    "title": "Melhores apps de lista de tarefas simples para iPhone (2026)",
    "h1": "Melhores apps de lista de tarefas simples para iPhone em 2026",
    "description": "Seis apps de lista de tarefas simples para iPhone comparados: 3 Tasks, Do!, MinimaList, Clear, Microsoft To Do e Todoist. Preço, conta e privacidade conferidos.",
    "llms": "Compara seis apps de lista de tarefas simples para iPhone (3 Tasks, Do!, MinimaList, Clear, Microsoft To Do, Todoist) por preço, necessidade de conta, lembretes, widgets e etiqueta de privacidade.",
    "answer": [
        "O melhor app de lista de tarefas simples para iPhone é o que limita você: o 3 Tasks só deixa anotar três prioridades por dia e cronometra cada uma, é grátis, sem conta e sem assinatura (o Pro opcional é uma compra única). Se você quer uma lista comum, mas sem complicação, o Do! e o MinimaList trazem lembretes e widgets, e o Microsoft To Do é totalmente grátis, com sincronização por conta Microsoft.",
        "O Todoist é o mais completo dos seis, mas o plano Pro é uma assinatura (R$ 24,90 por mês ou R$ 199,90 por ano no Brasil).",
    ],
    "columns": ["App", "Preço (Brasil)", "O que o torna simples", "Conta", "Etiqueta de privacidade da App Store", "Versão (data)", "Nota (Brasil)"],
    "table_note": "Os preços são das compras dentro do app na App Store brasileira em 9 de novembro de 2026; os seis são grátis para baixar. As notas são a média da App Store naquele dia. Quando um app ainda não tem avaliações no Brasil, a célula mostra um traço.",
    "apps": [
        {
            "row": ["Grátis; o 3 Tasks Pro é uma compra única (listado a R$ 29,90 e R$ 59,90)", "Só 3 tarefas por dia, uma tela, um cronômetro por tarefa", "Sem conta", "Dados usados para rastrear você; Dados não vinculados a você", "1.4.6 (5 nov 2026)", "—"],
            "best_for": "quem se afoga em listas longas e quer escolher as três coisas que importam hoje.",
            "facts": [
                "Anote três prioridades do dia; não há mais nada para configurar.",
                "Inicie e pause cada tarefa, no estilo Pomodoro, e veja o tempo gasto nela.",
                "Sem anúncios e sem conta. O app usa o Firebase Analytics para contar como tarefas e cronômetros são usados, e por isso a etiqueta de privacidade lista dados de rastreamento.",
                "33 idiomas, iOS 18 ou posterior.",
            ],
            "limits": "não tem lembretes nem sincronização entre aparelhos: é de propósito uma lista de um dia com três itens (tem Repetir diariamente e um widget de tela de início, grátis).",
        },
        {
            "row": ["Grátis com anúncios; remover anúncios R$ 129,90 (único); gorjeta R$ 6,90", "Adicione uma tarefa, toque duas vezes ao concluir; grupos e cores", "Não informado", "Dados usados para rastrear você; Dados vinculados a você; Dados não vinculados a você", "7.9.0 (22 out 2026)", "4.8"],
            "best_for": "uma lista diária com cara de papel, com lembretes e tarefas repetidas.",
            "facts": [
                "Temas, fontes e sons de caneta e papel.",
                "Grupos para trabalho, estudo e compras; tarefas fixadas.",
                "Tarefas repetidas (de diárias a anuais) e lembretes.",
                "5 idiomas, iOS 15 ou posterior.",
            ],
            "limits": "mostra anúncios, a menos que você pague R$ 129,90 uma vez, e a etiqueta de privacidade inclui dados usados para rastrear você.",
        },
        {
            "row": ["Vitalício de R$ 39,90 a R$ 59,90; família R$ 99,90; ou R$ 14,90 por mês", "Listas coloridas, entrada inteligente que reconhece horários", "Não informado", "Dados não vinculados a você", "2.27.9 (30 out 2026)", "4.8"],
            "best_for": "uma lista de aspecto minimalista que ainda tem widgets, listas compartilhadas e lembretes por local.",
            "facts": [
                "Widgets de tela de início e de tela bloqueada.",
                "Lembretes por horário e por local, subtarefas e listas compartilhadas.",
                "Funciona com a Siri; no iPhone, iPad e Mac, segundo o desenvolvedor.",
                "10 idiomas, iOS 15 ou posterior.",
            ],
            "limits": "vários preços diferentes para o mesmo upgrade vitalício, o que dificulta saber quanto você vai pagar.",
        },
        {
            "row": ["Clear Pro R$ 9,00; Pro antigo R$ 14,90 por mês; pacotes de sons", "Listas só com gestos, mapa de calor de cores para a prioridade", "Não informado", "Dados usados para rastrear você; Dados não vinculados a você", "2.8.7 (31 out 2026)", "4.9"],
            "best_for": "quem gosta de listas que se deslizam, sem botões na tela.",
            "facts": [
                "Deslize para concluir, belisque e arraste para reordenar; um mapa de calor mostra a prioridade.",
                "Kanban diário (Hoje, Amanhã, Depois de amanhã), rotinas e lembretes.",
                "2 idiomas, iOS 16 ou posterior.",
            ],
            "limits": "os gestos levam alguns minutos para aprender, e a etiqueta de privacidade inclui dados usados para rastrear você.",
        },
        {
            "row": ["Grátis, sem compras dentro do app", "Meu Dia com tarefas sugeridas", "Conta Microsoft para sincronizar", "Dados vinculados a você", "2.177 (6 jul 2026)", "4.9"],
            "best_for": "uma lista grátis que sincroniza em todo lugar, principalmente se você usa Outlook ou Microsoft 365.",
            "facts": [
                "Meu Dia e Sugestões ajudam a planejar o dia a partir de todas as listas.",
                "Sincroniza com o Microsoft 365; e-mails sinalizados do Outlook podem virar tarefas.",
                "Listas compartilhadas para contas pessoais.",
                "34 idiomas, iOS 17.6 ou posterior, 167 MB.",
            ],
            "limits": "é um gerenciador de tarefas completo, com listas, etapas e sugestões, e por isso pode virar as listas longas que um app simples evita.",
        },
        {
            "row": ["Pro R$ 24,90 por mês ou R$ 199,90 por ano", "Adição rápida em linguagem natural e captura por voz", "Sim", "Dados vinculados a você", "26.10.35 (2 nov 2026)", "4.9"],
            "best_for": "quem vê a lista crescer além de um app simples e quer projetos, datas e equipes.",
            "facts": [
                "A adição rápida entende datas em linguagem natural; o Ramble transforma fala em tarefas.",
                "Projetos, visualização de calendário e espaços de trabalho em equipe.",
                "Funciona com a Siri. 19 idiomas, iOS 17 ou posterior.",
            ],
            "limits": "o Pro é uma assinatura, e é o app menos simples desta lista.",
        },
    ],
    "who": [
        "<strong>Você vive escrevendo listas que nunca termina:</strong> 3 Tasks, três por dia e nada mais.",
        "<strong>Você quer lembretes e tarefas repetidas, mas com um visual calmo:</strong> Do! ou MinimaList.",
        "<strong>Você quer tudo grátis e sincronizado:</strong> Microsoft To Do.",
        "<strong>Você gosta de gestos e de tela sem botões:</strong> Clear.",
        "<strong>Você precisa de projetos, datas e trabalho em grupo:</strong> Todoist.",
    ],
    "cases": [
        "Escolher as três coisas que precisam acontecer hoje antes de abrir o e-mail.",
        "Uma lista de compras ou de recados que avisa quando você chega à loja (MinimaList).",
        "Tarefas de trabalho que vêm de e-mails sinalizados no Outlook (Microsoft To Do).",
        "Cronometrar blocos de trabalho focado em cada prioridade (3 Tasks).",
    ],
    "method": [
        "Em 9 de novembro de 2026 abrimos a página de cada app na App Store brasileira e os dados de consulta da Apple: preço, compras dentro do app, versão e data, nota, idiomas, iOS mínimo e etiqueta de privacidade. Os recursos são os que cada desenvolvedor lista na própria página. “Não informado” significa que a página não diz se é preciso ter conta. Não inventamos notas nem avaliações.",
    ],
    "faq": [
        ("Qual é o app de lista de tarefas mais simples para iPhone?", "O 3 Tasks só permite escrever três tarefas por dia em uma tela. Entre os apps de lista clássicos, Do! e Clear são os mais minimalistas."),
        ("Existe app de lista de tarefas grátis e sem assinatura?", "O Microsoft To Do é grátis e sem compras dentro do app, e o 3 Tasks é grátis com um Pro opcional de compra única (sem assinatura). O Do! é grátis com anúncios e uma compra única de R$ 129,90 para removê-los; o MinimaList e o Clear também oferecem upgrades de pagamento único."),
        ("Qual app de tarefas funciona sem conta?", "O 3 Tasks não precisa de conta. O Microsoft To Do usa uma conta Microsoft para sincronizar, e o Todoist usa conta própria."),
        ("Por que limitar a lista a três tarefas por dia?", "Uma lista curta obriga você a escolher o que mais importa, e assim a lista é concluída em vez de crescer sem fim. Essa é a ideia do 3 Tasks."),
        ("Qual app de tarefas simples tem widgets?", "O MinimaList tem widgets de tela de início e de tela bloqueada. O 3 Tasks tem um widget grátis de tela de início."),
    ],
}

TR_SLEEP = {
    "title": "Melhores apps grátis de sons para dormir no iPhone (2026)",
    "h1": "Melhores apps grátis de sons para dormir no iPhone em 2026",
    "description": "Seis apps de sons para dormir e ruído branco para iPhone comparados pelo que é realmente grátis: Drop, White Noise Lite, Rain Rain e mais. Conferidos na App Store.",
    "llms": "Compara seis apps de sons para dormir para iPhone (Drop, White Noise Lite, Rain Rain, White Noise Deep Sleep Sounds, Sleep Pillow, Dark Noise) por quanto é grátis, anúncios, timers, preço do plano pago e etiqueta de privacidade.",
    "answer": [
        "Para ter mais sons de graça, White Noise Lite (50+ sons, sem compras listadas) e Rain Rain (50+ sons, um pequeno banner de anúncio) são os mais fortes. Para ruído branco, rosa e marrom no plano grátis, White Noise Lite e White Noise Deep Sleep Sounds listam os três. Se você quer sons grátis sem nenhum anúncio e com timer para dormir, o Drop libera 9 dos seus 53 sons, incluindo ruído branco; ruído rosa e marrom exigem o Drop Pro.",
        "Os seis são grátis para baixar. O que muda é quanto continua grátis, se há anúncios e por quanto tempo o som toca; está tudo na tabela.",
    ],
    "columns": ["App", "Preço (Brasil)", "O que é grátis", "Etiqueta de privacidade da App Store", "Versão (data)", "Nota (Brasil)"],
    "table_note": "Os preços são das compras dentro do app na App Store brasileira em 9 de novembro de 2026 (um app pode listar vários preços para o mesmo plano). As notas são a média da App Store naquele dia; um traço indica que o app ainda não tem avaliações no Brasil.",
    "apps": [
        {
            "row": ["Grátis: 9 de 53 sons, sem anúncios; Drop Pro mensal R$ 29,90 ou opções vitalícias de R$ 59,90 a R$ 299,90", "Ruído branco, fogueira crepitando, floresta, batimentos cardíacos, lago, cafeteria, neve caindo, vento do deserto e golfinhos; timer para dormir com fade de 30 segundos", "Dados vinculados a você; Dados não vinculados a você", "2.15 (5 nov 2026)", "—"],
            "best_for": "sons calmantes grátis e sem anúncios, com um timer para dormir de verdade e um guia curto de respiração.",
            "facts": [
                "9 sons grátis sem banner de anúncio: ruído branco, fogueira crepitando, floresta, batimentos cardíacos, lago, cafeteria, neve caindo, vento do deserto e golfinhos.",
                "Timer para dormir de 15, 30 ou 45 minutos, 1, 2 ou 8 horas, com fade-out de 30 segundos; funciona offline.",
                "Sessões de respiração de 2 a 20 minutos e uma planta que cresce conforme você pratica.",
                "33 idiomas, iOS 18 ou posterior.",
            ],
            "limits": "só 9 sons são grátis e os outros 44 (chuva, oceano, ruído rosa e marrom, entre eles) exigem o Drop Pro; não tem mixer; exige iOS 18.",
        },
        {
            "row": ["Grátis, sem compras dentro do app listadas", "50+ sons em loop, incluindo ruído branco, rosa e marrom; timers e alarmes com fade", "Dados usados para rastrear você; Dados vinculados a você; Dados não vinculados a você", "9.0.6 (7 nov 2026)", "4.8"],
            "best_for": "o maior número de sons de graça: cores de ruído de verdade, mixer e timers.",
            "facts": [
                "50+ sons em loop, incluindo ruído branco, rosa, marrom, azul e violeta.",
                "Mix Pad para criar misturas; áudio em segundo plano para usar outros apps.",
                "Timers e alarmes que fazem fade-in e fade-out do áudio.",
                "3 idiomas (inglês, francês e espanhol), iOS 15 ou posterior.",
            ],
            "limits": "não tem meditação nem respiração, e a etiqueta de privacidade inclui dados usados para rastrear você.",
        },
        {
            "row": ["Grátis (50+ sons, um pequeno banner); Premium listado de R$ 12,90 a R$ 157,90 conforme o plano; pacotes de sons R$ 29,90", "50+ sons em HD grátis, sem limite de reprodução, todas as opções de fade-out, mixer", "Dados usados para rastrear você; Dados vinculados a você; Dados não vinculados a você", "6.9.10 (22 jan 2025)", "4.9"],
            "best_for": "muitos sons de chuva e natureza grátis e sem limite de tempo, se você aceita um pequeno banner de anúncio.",
            "facts": [
                "Segundo a página do app, a versão grátis tem 50+ sons em HD, sem limite de reprodução, todas as opções de fade-out do timer e um mixer com volume por som.",
                "Sem anúncios de áudio ou vídeo, só um pequeno banner de imagem na parte de baixo; o Premium acrescenta 60+ sons e remove o banner.",
                "4 idiomas (inglês, francês, italiano e espanhol), iOS 12 ou posterior, 105 MB.",
            ],
            "limits": "foi atualizado pela última vez em 22 de janeiro de 2025, e a etiqueta de privacidade inclui dados usados para rastrear você.",
        },
        {
            "row": ["Grátis (toca 8 horas por vez); Reprodução Contínua R$ 29,90; Premium a partir de R$ 4,90 por semana até R$ 147,90 no plano família", "30+ sons grátis, incluindo ruído branco, rosa e marrom; mixer, timer para dormir, widget", "Dados vinculados a você; Dados não vinculados a você", "3.45.0 (25 set 2026)", "4.8"],
            "best_for": "uma biblioteca grande (250+ sons premium extras) com 30+ sons grátis, incluindo ruído branco, rosa e marrom, para adultos e bebês.",
            "facts": [
                "Entre os sons grátis listados estão ventilador, shusher de bebê, aspirador de pó, cabine de avião, chuva, trovão, ondas do mar e ruído branco, rosa e marrom.",
                "Timer para dormir, mistura de sons, widget, AirPlay 2.",
                "Segundo a página do app, a versão grátis toca os sons por oito horas; a reprodução contínua exige assinatura.",
                "33 idiomas, iOS 15 ou posterior, 200 MB.",
            ],
            "limits": "a versão grátis para após oito horas, o que basta para uma noite de sono, mas não para uso o dia inteiro; há muitos preços diferentes.",
        },
        {
            "row": ["Grátis; pacotes de sons de R$ 59,90 a R$ 129,90; assinatura de Todos os Pacotes de Sons R$ 17,90", "Sons gravados na natureza, até 300.000 misturas, timer para dormir, despertador", "Dados não vinculados a você", "8.0.4 (30 out 2023)", "4.8"],
            "best_for": "um app clássico de sons para dormir com timer, despertador e misturas.",
            "facts": [
                "Timer para dormir com fade-out lento e despertador com fade-in lento.",
                "Funciona em segundo plano e com a tela bloqueada; lista de favoritos.",
                "Só em inglês, iOS 12 ou posterior, 182 MB.",
            ],
            "limits": "foi atualizado pela última vez em 30 de outubro de 2023, cerca de três anos antes desta verificação; os sons extras são vendidos em pacotes.",
        },
        {
            "row": ["Grátis; Dark Noise Pro listado a R$ 4,90, R$ 14,90, R$ 99,90 e vitalício R$ 299,90", "50+ sons, misturas personalizadas, timer com fade-out, Atalhos da Siri, widgets", "Dados não vinculados a você", "3.6.1 (17 out 2026)", "4.9"],
            "best_for": "o design mais polido, com Atalhos da Siri, widgets e AirPlay.",
            "facts": [
                "50+ sons com ícones animados e misturas personalizadas.",
                "Timer com fade-out, Atalhos da Siri (também pelo HomePod), widgets interativos e widgets de tela bloqueada.",
                "10 temas; só em inglês.",
            ],
            "limits": "exige iOS 26 ou posterior, então muitos iPhones não conseguem instalá-lo, e é o maior download desta lista.",
        },
    ],
    "who": [
        "<strong>Você quer o máximo de sons grátis:</strong> White Noise Lite ou Rain Rain.",
        "<strong>Você precisa de ruído branco, rosa ou marrom:</strong> White Noise Lite ou White Noise Deep Sleep Sounds.",
        "<strong>Você quer um app sem anúncios e com um bom timer para dormir:</strong> Drop.",
        "<strong>Você gosta de design polido e Atalhos da Siri, e tem iOS 26:</strong> Dark Noise.",
        "<strong>Você quer um app clássico com despertador e misturas:</strong> Sleep Pillow, lembrando que foi atualizado pela última vez em 2023.",
    ],
    "cases": [
        "Dormir ouvindo chuva ou um ventilador, com um timer que vai diminuindo o volume (qualquer um dos seis).",
        "Abafar o barulho da rua a noite toda (White Noise Lite ou Rain Rain, sem limite de tempo).",
        "Acalmar um bebê com ruído branco (o White Noise Deep Sleep Sounds lista sons de bebê e shushers).",
        "Foco ou estudo com som de cafeteria (Drop, White Noise Lite).",
    ],
    "method": [
        "Em 9 de novembro de 2026 abrimos a página de cada app na App Store brasileira e os dados de consulta da Apple: preço, compras dentro do app, versão e data, nota, idiomas, iOS mínimo e etiqueta de privacidade. O que é grátis vem da descrição de cada desenvolvedor; no caso do Drop, do próprio app. Não inventamos notas nem avaliações e não testamos a qualidade do áudio nem o consumo de bateria.",
    ],
    "faq": [
        ("Qual é o melhor app grátis de sons para dormir no iPhone?", "Depende do que você precisa de graça. O White Noise Lite tem 50+ sons e nenhuma compra listada; o Rain Rain tem 50+ sons grátis com um pequeno banner; o Drop tem 9 sons grátis, sem anúncios e com timer para dormir."),
        ("Qual app grátis tem ruído branco, rosa e marrom?", "O White Noise Lite lista ruído branco, rosa, marrom, azul e violeta; o White Noise Deep Sleep Sounds lista ruído branco, rosa e marrom entre os sons grátis. O Drop tem ruído branco grátis; o rosa e o marrom exigem o Drop Pro."),
        ("A versão grátis de um app de sons para dormir para depois de algumas horas?", "O White Noise Deep Sleep Sounds diz que a versão grátis toca por oito horas e que a reprodução contínua exige assinatura. O Rain Rain não lista limite de reprodução na versão grátis."),
        ("Existe app de sons para dormir sem anúncios?", "O Drop não tem anúncios. O Rain Rain diz que não tem anúncios de áudio nem de vídeo, só um pequeno banner de imagem. O White Noise Lite não lista compras; confira os anúncios ao instalar."),
        ("Qual app de sons para dormir funciona em iPhones mais antigos?", "Rain Rain e Sleep Pillow pedem iOS 12 ou posterior, White Noise Lite pede iOS 15. O Dark Noise exige iOS 26 e o Drop, iOS 18."),
    ],
}

TR_CRYPTO = {
    "title": "Melhores apps grátis para acompanhar criptomoedas (iPhone 2026)",
    "h1": "Melhores apps grátis para acompanhar sua carteira de criptomoedas no iPhone em 2026",
    "description": "Seis apps de carteira de criptomoedas para iPhone comparados pelo que o plano grátis inclui: Crypton, Crypto Pro, Delta, HODL, CoinGecko e CoinMarketCap.",
    "llms": "Compara seis apps grátis para acompanhar a carteira de criptomoedas no iPhone (Crypton, Crypto Pro, Delta, HODL, CoinGecko, CoinMarketCap) por limites do plano grátis, planos pagos, necessidade de cadastro e etiqueta de privacidade. Não é recomendação financeira.",
    "answer": [
        "Os planos grátis diferem em um ponto que importa: os limites. Delta e HODL limitam o plano grátis a 10 ativos ou símbolos; o CoinGecko não lista limite e tem carteira manual; o CoinMarketCap exige cadastro para a carteira; o Crypto Pro não diz o que é grátis; o Crypton não tem limites nem anúncios, mas é uma lista manual simples, sem sincronização de carteiras e sem alertas.",
        "Se você só quer ver o que tem e as principais moedas, qualquer um serve. Se quer sincronização automática grátis com corretoras e carteiras, o plano grátis do Delta é o que mais se aproxima, dentro do limite de 10 ativos.",
    ],
    "columns": ["App", "Preço (Brasil)", "O que o plano grátis inclui", "Etiqueta de privacidade da App Store", "Versão (data)", "Nota (Brasil)"],
    "table_note": "Os seis são grátis para baixar. Os preços são as compras dentro do app listadas na App Store brasileira em 9 de novembro de 2026 (os apps listam vários preços para o mesmo plano). As notas são a média da App Store naquele dia.",
    "apps": [
        {
            "row": ["Grátis, sem anúncios, sem compras dentro do app", "Tudo: carteira preenchida à mão, lista de acompanhamento, gráficos; sem limite listado", "Dados vinculados a você; Dados não vinculados a você", "2.0.8 (24 out 2026)", "5.0"],
            "best_for": "uma visão grátis e sem anúncios das principais moedas e do que você tem, sem limites para estourar.",
            "facts": [
                "Carteira com as quantidades que você informa, valor e variação por moeda e gráficos de preço (1D a 1A).",
                "Favoritos e lista de acompanhamento; 250+ moedas, segundo a página do app.",
                "Conta opcional, sem anúncios, nada para comprar. Só em inglês, iOS 18 ou posterior, 19 MB.",
            ],
            "limits": "não conecta a carteiras nem corretoras e não tem alertas de preço (dois widgets de tela de início grátis desde a 2.0.6); os preços atualizam a cada poucas horas, então não serve para operar.",
        },
        {
            "row": ["Grátis; Premium listado a R$ 29,90, R$ 119,90 e R$ 167,90", "Carteira e preços; Premium para mais recursos", "Dados não vinculados a você", "10.0.0 (28 out 2026)", "4.8"],
            "best_for": "privacidade e aparelhos Apple: sem anúncios, dados guardados no seu aparelho, barra de menus do Mac e Apple Watch.",
            "facts": [
                "Importa o que você tem a partir de endereços de carteira ou chaves de API de corretoras; lucro e prejuízo.",
                "A página do app diz que não há análise nem monitoramento de usuários e que a sincronização com o iCloud é opcional; sem anúncios.",
                "Widgets, bloqueio com Face ID, atalhos da Siri; 66 idiomas, iOS 17 ou posterior.",
            ],
            "limits": "a página do app não diz exatamente o que o plano grátis inclui, então confira antes de depender dele.",
        },
        {
            "row": ["Grátis até 10 ativos; PRO a partir de R$ 24,90 por mês ou R$ 224,90 por ano; PRO+ com mais recursos", "10 ativos, conexões ilimitadas, alertas de preço, 3 usos de IA por mês", "Dados usados para rastrear você; Dados não vinculados a você", "2026.3.2 (5 nov 2026)", "4.8"],
            "best_for": "criptomoedas e ações juntas, com sincronização automática, em um plano grátis limitado a 10 ativos.",
            "facts": [
                "Sincroniza 200+ corretoras, bancos de investimento e carteiras; ações, ETFs, forex e 10.000+ moedas.",
                "Plano grátis: 10 ativos, conexões ilimitadas, alertas de preço e 3 usos de IA por mês.",
                "18 idiomas, iOS 16.4 ou posterior.",
            ],
            "limits": "o plano grátis para em 10 ativos, e a etiqueta de privacidade inclui dados usados para rastrear você.",
        },
        {
            "row": ["Grátis (até 10 símbolos); Premium listado de R$ 49,90 a R$ 499,90; Basic R$ 29,90", "Lista de acompanhamento e carteira de até 10 símbolos, preços, gráficos, notícias, posts sociais, widget", "Dados usados para rastrear você; Dados vinculados a você; Dados não vinculados a você", "10.0.6 (5 nov 2026)", "4.8"],
            "best_for": "criptomoedas e ações dos EUA em uma só lista de acompanhamento, com notícias e posts sociais.",
            "facts": [
                "Grátis: lista de acompanhamento e carteira de até 10 símbolos, preços, gráficos, notícias, posts sociais e um widget.",
                "Premium: símbolos ilimitados e alertas de preço com faixas inteligentes, além de resumos de análises de Wall Street.",
                "O Pro acrescenta um agente de IA chamado Hermes, segundo a página do app. Só em inglês, iOS 15.1 ou posterior.",
            ],
            "limits": "o plano grátis para em 10 símbolos, e a etiqueta de privacidade lista dados usados para rastrear você e dados vinculados a você.",
        },
        {
            "row": ["Grátis; Premium R$ 59,90 por mês ou R$ 599,90 por ano", "Dados de mercado, carteira, alertas, widgets e conversor; sem limite listado", "Dados vinculados a você; Dados não vinculados a você", "3.60.0 (27 out 2026)", "4.9"],
            "best_for": "pesquisar moedas e categorias, com carteira manual grátis e alertas.",
            "facts": [
                "Dados em tempo real de 10.000+ moedas, volumes de corretoras e 3.000+ coleções de NFT.",
                "Carteira com lucro e prejuízo, alertas de preço, widgets e conversor.",
                "Só em inglês, iOS 16 ou posterior.",
            ],
            "limits": "a carteira é manual (sem sincronização de conta), e o Premium custa R$ 59,90 por mês.",
        },
        {
            "row": ["Grátis; planos pagos de Essential R$ 79,90 por mês até Max R$ 799,90 por mês", "Preços, listas de acompanhamento, notícias, alertas de preço e carteira; a carteira exige cadastro", "Dados usados para rastrear você; Dados vinculados a você; Dados não vinculados a você", "5.24.0 (1 nov 2026)", "4.9"],
            "best_for": "o maior banco de preços e de notícias em um app grátis, se você aceita se cadastrar para usar a carteira.",
            "facts": [
                "Carteira em 90+ moedas fiduciárias, listas de acompanhamento e alertas de preço.",
                "Notícias e tendências do mercado cripto no mesmo app.",
                "21 idiomas, iOS 15 ou posterior.",
            ],
            "limits": "a carteira exige conta, a etiqueta de privacidade inclui dados usados para rastrear você e os planos pagos chegam a R$ 799,90 por mês.",
        },
    ],
    "who": [
        "<strong>Você quer zero limites e zero anúncios, e informa o que tem à mão:</strong> Crypton.",
        "<strong>Você quer privacidade e Apple Watch / Mac:</strong> Crypto Pro.",
        "<strong>Você quer sincronização automática e tem 10 ativos ou menos:</strong> Delta.",
        "<strong>Você tem criptomoedas e ações dos EUA:</strong> HODL ou Delta.",
        "<strong>Você pesquisa moedas tanto quanto acompanha:</strong> CoinGecko ou CoinMarketCap.",
    ],
    "cases": [
        "Uma olhada de manhã no valor do que você tem (Crypton, CoinGecko).",
        "Acompanhar 10 moedas ou menos com alertas (planos grátis de HODL e Delta).",
        "Acompanhar carteiras e corretoras sem pagar (Delta, dentro do limite).",
        "Pesquisar uma moeda antes de comprá-la (CoinGecko, CoinMarketCap).",
    ],
    "method": [
        "Em 9 de novembro de 2026 abrimos a página de cada app na App Store brasileira e os dados de consulta da Apple: preço, compras dentro do app, versão e data, nota, idiomas, iOS mínimo e etiqueta de privacidade. Os limites do plano grátis são os que cada desenvolvedor informa na própria página; os limites do Crypton vêm de testes próprios. Não inventamos notas nem avaliações, e nada disto é recomendação financeira.",
    ],
    "faq": [
        ("Qual é o melhor app grátis para acompanhar criptomoedas no iPhone?", "Depende de você precisar de sincronização. Para uma lista manual grátis e sem limites, Crypton ou CoinGecko; para sincronização automática, Delta (até 10 ativos); para notícias e pesquisa, CoinMarketCap."),
        ("Qual app grátis de criptomoedas não tem limite de ativos?", "Crypton e CoinGecko não listam limite no plano grátis. Delta e HODL limitam o plano grátis a 10."),
        ("Qual app grátis conecta a corretoras e carteiras?", "O plano grátis do Delta lista conexões ilimitadas dentro do limite de 10 ativos; o Crypto Pro lista importação por endereços de carteira e chaves de API de corretoras. O Crypton não conecta a nenhuma."),
        ("Qual app de criptomoedas não tem anúncios e coleta menos dados?", "O Crypton não tem anúncios, e a etiqueta de privacidade dele lista dados vinculados e não vinculados a você. O Crypto Pro diz que não tem análise nem anúncios, e a etiqueta dele lista apenas Dados não vinculados a você."),
        ("Isto é recomendação financeira?", "Não. Esta página compara recursos, preços e notas dos apps como aparecem na App Store."),
    ],
}

TR_VAULT = {
    "title": "Melhores apps para esconder fotos no iPhone: privacidade (2026)",
    "h1": "Melhores apps de cofre de fotos para iPhone comparados pela privacidade em 2026",
    "description": "Seis apps de cofre de fotos para iPhone comparados pela etiqueta de privacidade da App Store; só um declara Dados não coletados. Safe Lock, Keepsafe e mais.",
    "llms": "Compara seis apps de cofre de fotos para iPhone (Photo Vault, Safe Lock, Keepsafe, Private Photo Vault, Privault, PV) por etiqueta de privacidade da App Store, preço e backup na nuvem. Só o Safe Lock declara Dados não coletados.",
    "answer": [
        "Para esconder fotos no iPhone, só um dos seis apps declara <em>Dados não coletados</em> na etiqueta de privacidade da App Store: o Safe Lock - Hidden Photo Vault. Em seguida vem o Photo Vault: Hide Pics Video, que lista apenas compras, em Dados não vinculados a você, sem rastreamento. Os outros quatro listam dados usados para rastrear você, dados vinculados a você, ou os dois. A etiqueta de privacidade é o que o desenvolvedor declara, não uma auditoria independente.",
        "Se você também quer uma nuvem privada, as opções são Keepsafe (Private Cloud), Private Photo Vault (Cloud Vault) e PV (planos de nuvem); o Safe Lock e o Photo Vault: Hide Pics Video guardam as fotos no aparelho, com uma cópia opcional no iCloud no caso do segundo.",
    ],
    "columns": ["App", "Preço (Brasil)", "Backup na nuvem", "Etiqueta de privacidade da App Store", "Versão (data)", "Nota (Brasil)"],
    "table_note": "Os seis são grátis para baixar. Os preços são as compras dentro do app listadas na App Store brasileira em 9 de novembro de 2026 (os apps listam vários preços para o mesmo plano). As notas são a média da App Store naquele dia; um traço indica que o app ainda não tem avaliações no Brasil. A etiqueta de privacidade é o que cada desenvolvedor declara à Apple.",
    "apps": [
        {
            "row": ["Grátis para baixar; Premium anual R$ 129,90 ou R$ 199,90, vitalício R$ 99,90 ou R$ 199,90", "Sem conta; cópia opcional criptografada de ponta a ponta no seu próprio iCloud (Premium, desativada por padrão)", "Dados não vinculados a você (compras)", "1.4 (6 nov 2026)", "—"],
            "best_for": "uma etiqueta de privacidade enxuta, com Face ID, senha por álbum, ícone disfarçado e câmera privada.",
            "facts": [
                "Etiqueta: Dados não vinculados a você (só compras); nada vinculado a você e nada usado para rastrear você. Abre com Face ID, Touch ID ou código; cada álbum pode ter sua própria senha; um código falso (Premium) abre um cofre separado.",
                "Ícone disfarçado (Calculadora, Notas ou Clima) e saída ao virar o aparelho para baixo.",
                "Sem conta; uma cópia opcional criptografada de ponta a ponta no seu próprio iCloud (desativada por padrão); para trocar de iPhone, você exporta um arquivo protegido por senha. 19 idiomas, iOS 17 ou posterior.",
            ],
            "limits": "não faz backup automático, a menos que você ative a cópia no iCloud; a versão grátis é limitada; e a etiqueta de privacidade não é Dados não coletados.",
        },
        {
            "row": ["Grátis; Premium R$ 24,90, R$ 99,90 ou R$ 199,90", "Nenhum listado: o desenvolvedor diz que as fotos ficam no aparelho", "Dados não coletados", "3.1 (17 ago 2026)", "4.8"],
            "best_for": "o app de cofre com etiqueta Dados não coletados, com vários tipos de bloqueio e câmera oculta.",
            "facts": [
                "Etiqueta: Dados não coletados. Bloqueios: PIN, DotLock, senha numérica ou alfabética, Touch ID e Face ID.",
                "Câmera oculta dentro do app; pastas secretas para fotos, vídeos e notas.",
                "O desenvolvedor diz que fotos e vídeos são salvos apenas no seu aparelho. 13 idiomas, iOS 12 ou posterior, 69 MB.",
            ],
            "limits": "a página do app não descreve uma exportação criptografada para trocar de iPhone.",
        },
        {
            "row": ["Grátis; Premium de R$ 15,90 a R$ 177,90 (anual R$ 77,90, mensal R$ 31,90)", "Private Cloud opcional (Premium)", "Dados usados para rastrear você; Dados não vinculados a você", "13.35.0 (26 out 2026)", "4.8"],
            "best_for": "uma etiqueta com poucos tipos de dado e uma nuvem privada opcional.",
            "facts": [
                "Etiqueta: dados usados para rastrear você e dados não vinculados a você.",
                "PIN, Touch ID, bloqueio de álbum com PINs separados (Premium), Safe Send.",
                "16 idiomas, iOS 17 ou posterior.",
            ],
            "limits": "a etiqueta inclui dados usados para rastrear você, e a nuvem e os bloqueios por álbum exigem Premium.",
        },
        {
            "row": ["Grátis; Premium de R$ 28,90 a R$ 299,90 conforme o plano", "Cloud Vault criptografado opcional", "Dados usados para rastrear você; Dados vinculados a você", "26.1 (5 nov 2026)", "4.9"],
            "best_for": "o cofre mais conhecido e com mais recursos, se você aceita uma etiqueta de privacidade com dados vinculados a você.",
            "facts": [
                "Etiqueta: dados usados para rastrear você e dados vinculados a você.",
                "Relatório de invasão com foto e GPS, senha falsa, bloqueio ao virar o aparelho para baixo, navegador privado.",
                "11 idiomas, iOS 15 ou posterior.",
            ],
            "limits": "a etiqueta inclui dados vinculados a você e dados usados para rastrear você, e vários recursos exigem Premium.",
        },
        {
            "row": ["Grátis (com anúncios); Pro R$ 18,90 por mês, R$ 129,90 por ano ou R$ 299,90 uma vez; remover anúncios R$ 19,90", "Nenhum: fica no aparelho", "Dados usados para rastrear você; Dados vinculados a você; Dados não vinculados a você", "10.2 (28 fev 2025)", "4.6"],
            "best_for": "uma segunda senha que abre uma pasta falsa.",
            "facts": [
                "Senha principal, uma senha secundária para um espaço falso e uma senha que apaga tudo.",
                "Player de vídeo que, segundo o desenvolvedor, abre cerca de 150 formatos de mídia.",
                "12 idiomas, iOS 11 ou posterior, 91 MB.",
            ],
            "limits": "foi atualizado pela última vez em 28 de fevereiro de 2025, mostra anúncios a menos que você pague, e a etiqueta lista dados de rastreamento.",
        },
        {
            "row": ["Grátis (com anúncios); Pro R$ 24,90 por mês ou R$ 119,90 por ano, vitalício R$ 299,90", "Planos de backup na nuvem opcionais", "Dados usados para rastrear você; Dados vinculados a você; Dados não vinculados a você", "7.7.9 (26 out 2026)", "4.8"],
            "best_for": "a lista de recursos mais longa.",
            "facts": [
                "Armazenamento grátis ilimitado, segundo a página do app; senha e Face ID, senha falsa, ícone personalizável.",
                "Tags, notas e busca, editor de fotos e Nearby Drop.",
                "12 idiomas, iOS 17 ou posterior.",
            ],
            "limits": "a versão grátis mostra anúncios, e a etiqueta tem dados de rastreamento, vinculados e não vinculados.",
        },
    ],
    "who": [
        "<strong>Você quer que nada seja coletado:</strong> Safe Lock, o único com etiqueta Dados não coletados.",
        "<strong>Você quer uma etiqueta enxuta e sem conta:</strong> Photo Vault: Hide Pics Video.",
        "<strong>Você quer uma nuvem privada:</strong> Keepsafe.",
        "<strong>Você quer mais recursos e aceita uma etiqueta mais longa:</strong> Private Photo Vault.",
        "<strong>Você quer um código falso de graça:</strong> Privault (o Photo Vault tem um com o Premium).",
        "<strong>Você quer a lista de recursos mais longa:</strong> PV.",
    ],
    "cases": [
        "Manter fotos privadas fora do rolo da câmera compartilhado e fora da nuvem (Photo Vault, Safe Lock).",
        "Entregar o celular a alguém sem que veja o app (ícones disfarçados, senhas falsas).",
        "Fazer backup de um cofre para que um celular perdido não leve as fotos junto (Keepsafe, Private Photo Vault, PV, com suas nuvens).",
        "Conferir o que um app diz coletar antes de colocar fotos privadas nele (a etiqueta de privacidade na tabela).",
    ],
    "method": [
        "Em 9 de novembro de 2026 abrimos a página de cada app na App Store brasileira e os dados de consulta da Apple: preço, compras dentro do app, versão e data, nota, idiomas, iOS mínimo e a etiqueta de privacidade exatamente como declarada. Os recursos são os que cada desenvolvedor lista na própria página; não verificamos a criptografia nem auditamos práticas de dados. Não inventamos notas nem avaliações.",
    ],
    "faq": [
        ("Quais apps de cofre de fotos dizem Dados não coletados?", "Em 9 de novembro de 2026, apenas o Safe Lock - Hidden Photo Vault. O Photo Vault: Hide Pics Video lista apenas compras, em Dados não vinculados a você; Keepsafe, Private Photo Vault, Privault e PV listam dados usados para rastrear você, dados vinculados a você, ou os dois."),
        ("A etiqueta Dados não coletados significa que minhas fotos estão seguras?", "Significa que o desenvolvedor declara à Apple que não coleta dados do app. Não é uma auditoria e não diz nada sobre o quanto suas fotos ficam protegidas no celular."),
        ("Qual cofre de fotos tem nuvem privada?", "Keepsafe (Private Cloud, Premium), Private Photo Vault (Cloud Vault) e PV (planos de nuvem). Safe Lock guarda as fotos no aparelho; o Photo Vault: Hide Pics Video também, com cópia opcional no seu iCloud."),
        ("O Photo Vault: Hide Pics Video é o mesmo que o Private Photo Vault?", "Não. São apps diferentes, de desenvolvedores diferentes. O Photo Vault: Hide Pics Video é da Saga Ltd.; o Private Photo Vault - Pic Safe é da Legendary Software Labs."),
        ("Preciso mesmo de um app de cofre de fotos?", "Nem sempre. O iPhone tem o álbum Ocultas no app Fotos, que pode ser bloqueado com Face ID ou código nas versões recentes do iOS; um app de cofre acrescenta álbuns separados, ícones disfarçados e outros recursos."),
    ],
}

PAGES = [
    make("simple-todo", "pt-BR", TR_TODO, "ptbr"),
    make("free-sleep-sounds", "pt-BR", TR_SLEEP, "ptbr"),
    make("free-crypto-trackers", "pt-BR", TR_CRYPTO, "ptbr"),
    make("vault-no-data", "pt-BR", TR_VAULT, "ptbr"),
]
