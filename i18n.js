const translations = {
  pt: {
    "brand": "Acampamento Farroupilha",
    "header.tag": "Campeonato de Truco",
    "music.play": "Clique pra ouvir explicação",
    "music.pause": "Pausar",
    "nav.foundations": "Fundamentos",
    "nav.howitplays": "Como se joga",
    "nav.envido": "Envido",
    "nav.flor": "Flor",
    "nav.scoring": "Pontuação",

    "hero.top": "A arte da mentira",
    "hero.title": "Truco",
    "hero.lede": "O lendário jogo latino-americano de blefe, coragem e cálculo rápido.",
    "hero.sub": "Domine as manilhas e comande a mesa.",
    "hero.cta": "Comece sua jornada",

    "foundations.label": "Fundamentos",
    "foundations.title": "Blueprint de início rápido",
    "foundations.desc": "O Truco é mais que um jogo de sorte; é um campo de batalha tático de guerra psicológica, onde uma mão fraca pode vencer uma mão forte pela pura confiança.",

    "qs1.title": "Alianças 2v2",
    "qs1.body": "Jogado em duplas. Coordene-se silenciosamente com seu parceiro do outro lado da mesa usando expressões faciais tradicionais.",
    "qs2.title": "Baralho espanhol",
    "qs2.body": "Jogado com um baralho tradicional de 40 cartas (sem 8, 9 ou coringas). Cada carta tem um peso único na batalha.",
    "qs3.title": "Corrida aos 30",
    "qs3.body": "Ganhe pontos ao longo de várias mãos. A primeira equipe a somar 30 pontos conquista a honra máxima da mesa.",

    "hierarchy.title": "A hierarquia da baralha",
    "hierarchy.body": "Diferente dos jogos tradicionais, as cartas do Truco não seguem a ordem numérica. Memorizar essa hierarquia incomum é a chave para sobreviver às rodadas.",
    "hierarchy.note": "As manilhas no topo são as cartas únicas do jogo; os 3 e os 2 também são ativos críticos.",

    "howitplays.label": "Como se joga",
    "rhythm.title": "O ritmo da rodada",
    "rhythm.body": "Uma mão consiste em até três cartas jogadas em sequência por cada jogador. Vencer rodadas cedo dá vantagem, mas segurar a carta certa para a hora certa é o que decide o jogo.",

    "deal.title": "A distribuição",
    "deal.body": "Cada jogador recebe 3 cartas, avaliadas para Envido e Flor.",
    "tricks.title": "Três rodadas",
    "tricks.body": "Vence a mão quem ganhar 2 das 3 rodadas.",
    "handwin.title": "Vitória da mão",
    "handwin.body": "O vencedor leva os pontos em disputa (ou mais, se houve Truco).",

    "calling.title": "Chamando Truco!",
    "calling.body": "A qualquer momento durante uma rodada, você pode cantar Truco! para aumentar a aposta. A escada de escalada é um teste de nervos.",
    "fold.title": "Desistir (Não quero)",
    "fold.body": "A mão termina imediatamente. A equipe que desistiu concede os pontos.",
    "accept.title": "Aceitar (Quero)",
    "accept.body": "A batalha continua, e o vencedor do desafio leva os pontos.",
    "reraise.title": "Aumentar (Retruco)",
    "reraise.body": "Contra-ataque para Retruco (3 pts) ou Vale 4 (4 pts).",
    "flow.truco": "Truco",
    "flow.retruco": "Retruco",
    "flow.vale4": "Vale 4",

    "envido.label": "A aposta lateral",
    "envido.title": "Envido: sinergia de naipes",
    "envido.body": "Os pontos são declarados e contados antes de as rodadas de cartas começarem.",
    "envido.calcTitle": "Como calcular o Envido",
    "envido.calc1": "Duas cartas do mesmo naipe: Carta A + Carta B + 20",
    "envido.calc2": "Naipes diferentes: apenas o valor da carta mais alta",
    "envido.calc3": "As cartas 10, 11 e 12 não somam valor (valem 0).",
    "envido.tie": "Empate: vence o jogador mão (quem joga primeiro na rodada).",
    "envido.examples": "Exemplos",
    "ex.e1.value": "7 + 5 + 20 = 32",
    "ex.e1.note": "Duas cartas do mesmo naipe",
    "ex.e2.value": "7 + 6 + 20 = 33",
    "ex.e2.note": "Maior Envido possível",
    "ex.e3.value": "3 + 0 + 20 = 23",
    "ex.e3.note": "O 12 não conta",
    "ex.e4.value": "0 pontos",
    "ex.e4.note": "Sem par: 10 e 11 valem zero",
    "flor.badge": "Privilégio raro",
    "flor.title": "A Flor sagrada",
    "flor.body": "Se você receber as três cartas do mesmo naipe, anuncie imediatamente \"Flor!\" antes de a rodada começar. A Flor vale 3 pontos e anula qualquer Envido. Se os dois lados tiverem Flor, a equipe da melhor Flor ganha 3 pontos por cada Flor anunciada. Em caso de empate no valor, vence o jogador mão (mesma lógica do Envido). Contra Flor só pode ser chamada se os dois lados tiverem Flor: se aceita, 6 pontos ao vencedor; se recusada, 4 pontos para quem chamou.",
    "flor.examples": "Exemplos de Flor",
    "flor.ex1.value": "7 + 6 + 5 + 20 = 38",
    "flor.ex1.note": "Flor muito forte",
    "flor.ex2.value": "1 + 0 + 0 + 20 = 21",
    "flor.ex2.note": "10 e 12 valem zero",
    "flor.duel.wins": "vence",
    "flor.duel.note": "As duas têm Flor: vence a maior, que leva 3 pontos por cada Flor anunciada.",

    "scoring.label": "Placar",
    "scoring.title": "Matriz de pontuação",
    "score.col1": "Chamada / Aposta",
    "score.col2": "Pontos",
    "score.col3": "Contexto",
    "score.truco": "Truco (Aceito)",
    "score.trucoPts": "2 pontos",
    "score.trucoCtx": "Aposta base pela vitória das rodadas",
    "score.retruco": "Retruco (Aceito)",
    "score.retrucoPts": "3 pontos",
    "score.retrucoCtx": "Contra-aposta ao Truco",
    "score.vale4": "Vale 4 (Aceito)",
    "score.vale4Pts": "4 pontos",
    "score.vale4Ctx": "Escalada final da aposta",
    "score.declined": "Truco / Retruco (Recusado)",
    "score.declinedPts": "1/2 pontos",
    "score.declinedCtx": "Pontos vão para quem chamou",
    "score.envido": "Envido (Aceito)",
    "score.envidoPts": "2 pontos",
    "score.envidoCtx": "Melhor combinação de naipe",
    "score.realEnvido": "Real Envido",
    "score.realEnvidoPts": "3 pontos",
    "score.realEnvidoCtx": "Aposta elevada na comparação de par",
    "score.faltaEnvido": "Falta Envido",
    "score.faltaEnvidoPts": "Variável",
    "score.faltaEnvidoCtx": "Quem vence leva a partida",
    "score.flor": "Flor (Anunciada)",
    "score.florPts": "3 pontos",
    "score.florCtx": "Três cartas do mesmo naipe",
    "score.contraFlor": "Contra Flor",
    "score.contraFlorPts": "6 / 4 pontos",
    "score.contraFlorCtx": "Aceita: 6 ao vencedor · recusada: 4 ao chamador",

    "cta.body": "Agora que você conhece a hierarquia e as apostas, está pronto para reivindicar seu lugar à mesa.",
    "cta.final": "¡Quiero vale cuatro!"
  },

  es: {
    "brand": "Acampamento Farroupilha",
    "header.tag": "Campeonato de Truco",
    "music.play": "Clic para escuchar la explicación",
    "music.pause": "Pausar",
    "nav.foundations": "Fundamentos",
    "nav.howitplays": "Cómo se juega",
    "nav.envido": "Envido",
    "nav.flor": "Flor",
    "nav.scoring": "Puntuación",

    "hero.top": "El arte de la mentira",
    "hero.title": "Truco",
    "hero.lede": "El legendario juego latinoamericano de farol, valentía y cálculo rápido.",
    "hero.sub": "Domina las manillas y domina la mesa.",
    "hero.cta": "Comienza tu aprendizaje",

    "foundations.label": "Fundamentos",
    "foundations.title": "Plan rápido de inicio",
    "foundations.desc": "El Truco es más que un juego de suerte; es un campo de batalla táctico de guerra psicológica, donde una mano débil puede vencer a una mano fuerte por pura confianza.",

    "qs1.title": "Alianzas 2v2",
    "qs1.body": "Se juega en parejas. Coordínate en silencio con tu compañero al otro lado de la mesa usando expresiones faciales tradicionales.",
    "qs2.title": "Baraja española",
    "qs2.body": "Se juega con una baraja tradicional de 40 cartas (sin 8, 9 ni comodines). Cada carta tiene un peso único en la batalla.",
    "qs3.title": "Carrera a 30",
    "qs3.body": "Suma puntos a lo largo de varias manos. El primer equipo en llegar a 30 puntos se lleva el honor máximo de la mesa.",

    "hierarchy.title": "La jerarquía de la baraja",
    "hierarchy.body": "A diferencia de los juegos tradicionales, las cartas del Truco no siguen el orden numérico. Memorizar esta jerarquía inusual es la clave para sobrevivir a las rondas.",
    "hierarchy.note": "Las manillas en la cima son las cartas únicas del juego; los 3 y los 2 también son activos críticos.",

    "howitplays.label": "Cómo se juega",
    "rhythm.title": "El ritmo de la ronda",
    "rhythm.body": "Una mano consiste en hasta tres cartas jugadas en secuencia por cada jugador. Ganar rondas temprano da ventaja, pero guardar la carta correcta para el momento justo es lo que decide el juego.",

    "deal.title": "El reparto",
    "deal.body": "Cada jugador recibe 3 cartas, evaluadas para Envido y Flor.",
    "tricks.title": "Tres rondas",
    "tricks.body": "Gana la mano quien gane 2 de las 3 rondas.",
    "handwin.title": "Victoria de la mano",
    "handwin.body": "El ganador se lleva los puntos en disputa (o más, si hubo Truco).",

    "calling.title": "¡Cantando Truco!",
    "calling.body": "En cualquier momento durante una ronda, puedes cantar ¡Truco! para subir la apuesta. La escalera de escalada es una prueba de nervios.",
    "fold.title": "Rendirse (No quiero)",
    "fold.body": "La mano termina de inmediato. El equipo que se rinde concede los puntos.",
    "accept.title": "Aceptar (Quiero)",
    "accept.body": "La batalla continúa, y el ganador del desafío se lleva los puntos.",
    "reraise.title": "Subir (Retruco)",
    "reraise.body": "Contraataque a Retruco (3 pts) o Vale Cuatro (4 pts).",
    "flow.truco": "Truco",
    "flow.retruco": "Retruco",
    "flow.vale4": "Vale Cuatro",

    "envido.label": "La apuesta lateral",
    "envido.title": "Envido: sinergia de palos",
    "envido.body": "Los puntos se declaran y se cuentan antes de que comiencen las rondas de cartas.",
    "envido.calcTitle": "Cómo se calcula el Envido",
    "envido.calc1": "Dos cartas del mismo palo: Carta A + Carta B + 20",
    "envido.calc2": "Palos distintos: solo el valor de la carta más alta",
    "envido.calc3": "Las cartas 10, 11 y 12 no suman valor (valen 0).",
    "envido.tie": "Empate: gana el jugador mano (quien juega primero en la ronda).",
    "envido.examples": "Ejemplos",
    "ex.e1.value": "7 + 5 + 20 = 32",
    "ex.e1.note": "Dos cartas del mismo palo",
    "ex.e2.value": "7 + 6 + 20 = 33",
    "ex.e2.note": "Mayor Envido posible",
    "ex.e3.value": "3 + 0 + 20 = 23",
    "ex.e3.note": "El 12 no cuenta",
    "ex.e4.value": "0 puntos",
    "ex.e4.note": "Sin pareja: 10 y 11 valen cero",
    "flor.badge": "Privilegio raro",
    "flor.title": "La Flor sagrada",
    "flor.body": "Si recibes las tres cartas del mismo palo, anuncia de inmediato \"¡Flor!\" antes de que comience la ronda. La Flor vale 3 puntos y anula cualquier Envido. Si ambos lados tienen Flor, el equipo de la mejor Flor gana 3 puntos por cada Flor anunciada. En caso de empate en el valor, gana el jugador mano (misma lógica que el Envido). Contra Flor solo puede cantarse si ambos lados tienen Flor: si se acepta, 6 puntos al ganador; si se rechaza, 4 puntos para quien la cantó.",
    "flor.examples": "Ejemplos de Flor",
    "flor.ex1.value": "7 + 6 + 5 + 20 = 38",
    "flor.ex1.note": "Flor muy fuerte",
    "flor.ex2.value": "1 + 0 + 0 + 20 = 21",
    "flor.ex2.note": "10 y 12 valen cero",
    "flor.duel.wins": "gana",
    "flor.duel.note": "Ambas tienen Flor: gana la mayor, que se lleva 3 puntos por cada Flor anunciada.",

    "scoring.label": "Marcador",
    "scoring.title": "Matriz de puntuación",
    "score.col1": "Llamada / Apuesta",
    "score.col2": "Puntos",
    "score.col3": "Contexto",
    "score.truco": "Truco (Aceptado)",
    "score.trucoPts": "2 puntos",
    "score.trucoCtx": "Apuesta base por la victoria de las rondas",
    "score.retruco": "Retruco (Aceptado)",
    "score.retrucoPts": "3 puntos",
    "score.retrucoCtx": "Contraapuesta al Truco",
    "score.vale4": "Vale Cuatro (Aceptado)",
    "score.vale4Pts": "4 puntos",
    "score.vale4Ctx": "Escalada final de la apuesta",
    "score.declined": "Truco / Retruco (Rechazado)",
    "score.declinedPts": "1/2 puntos",
    "score.declinedCtx": "Los puntos van a quien cantó",
    "score.envido": "Envido (Aceptado)",
    "score.envidoPts": "2 puntos",
    "score.envidoCtx": "Mejor combinación de palo",
    "score.realEnvido": "Real Envido",
    "score.realEnvidoPts": "3 puntos",
    "score.realEnvidoCtx": "Apuesta elevada en la comparación de pareja",
    "score.faltaEnvido": "Falta Envido",
    "score.faltaEnvidoPts": "Variable",
    "score.faltaEnvidoCtx": "Quien gana se lleva la partida",
    "score.flor": "Flor (Declarada)",
    "score.florPts": "3 puntos",
    "score.florCtx": "Tres cartas del mismo palo",
    "score.contraFlor": "Contra Flor",
    "score.contraFlorPts": "6 / 4 puntos",
    "score.contraFlorCtx": "Aceptada: 6 al ganador · rechazada: 4 al que cantó",

    "cta.body": "Ahora que conoces la jerarquía y las apuestas, estás listo para reclamar tu lugar en la mesa.",
    "cta.final": "¡Quiero vale cuatro!"
  },

  en: {
    "brand": "Acampamento Farroupilha",
    "header.tag": "Truco Championship",
    "music.play": "Click to hear the explanation",
    "music.pause": "Pause",
    "nav.foundations": "Foundations",
    "nav.howitplays": "How it plays",
    "nav.envido": "Envido",
    "nav.flor": "Flor",
    "nav.scoring": "Scoring",

    "hero.top": "The art of lying",
    "hero.title": "Truco",
    "hero.lede": "The legendary Latin American game of bluffing, bravery, and rapid calculations.",
    "hero.sub": "Master the tricks and command the table.",
    "hero.cta": "Begin your apprenticeship",

    "foundations.label": "Foundations",
    "foundations.title": "Quick Start Blueprint",
    "foundations.desc": "Truco is more than a game of luck; it is a tactical battleground of psychological warfare where a weak hand can beat a strong hand through sheer confidence.",

    "qs1.title": "2v2 Alliances",
    "qs1.body": "Played in partnerships of two. Coordinate silently with your teammate across the table using traditional facial expressions.",
    "qs2.title": "Spanish Deck",
    "qs2.body": "Played with a traditional 40-card baraja deck (no 8s, 9s, or Jokers). Every card carries unique weight in battle.",
    "qs3.title": "Race to 30",
    "qs3.body": "Earn points across multiple hands. The first team to secure 30 points wins the ultimate honor of the table.",

    "hierarchy.title": "The Spanish Baraja Hierarchy",
    "hierarchy.body": "Unlike traditional games, cards in Truco do not follow numerical order. Memorizing this unusual hierarchy is the key to surviving the rounds.",
    "hierarchy.note": "The manilhas at the top are the game's unique cards; the 3s and 2s are critical assets too.",

    "howitplays.label": "How it plays",
    "rhythm.title": "Rhythm of the Trick",
    "rhythm.body": "A hand consists of up to three cards played sequentially by each player. Winning early tricks gives you advantage, but holding back the right card for the right moment is what decides the game.",

    "deal.title": "The Deal",
    "deal.body": "Each player receives 3 cards, evaluated for both Envido and Flor.",
    "tricks.title": "Three Tricks",
    "tricks.body": "Best of 3 tricks wins the hand.",
    "handwin.title": "The Hand Win",
    "handwin.body": "The winner takes the points in dispute (or more, if Truco was called).",

    "calling.title": "Calling \"Truco!\"",
    "calling.body": "At any point during a trick, you can call Truco! to raise the stakes. The escalation tree is a test of nerves.",
    "fold.title": "Fold (No Quiero)",
    "fold.body": "The hand ends immediately. The folding team concedes the points.",
    "accept.title": "Accept (Quiero)",
    "accept.body": "The battle continues, and the winner of the challenge takes the points.",
    "reraise.title": "Re-raise (Retruco)",
    "reraise.body": "Counter-challenge to Retruco (3 pts) or Vale Cuatro (4 pts).",
    "flow.truco": "Truco",
    "flow.retruco": "Retruco",
    "flow.vale4": "Vale Cuatro",

    "envido.label": "The side bet",
    "envido.title": "Envido: Suit Synergy",
    "envido.body": "Points are declared and scored before the tricks resolve.",
    "envido.calcTitle": "How Envido is Calculated",
    "envido.calc1": "Two cards of same suit: Card A + Card B + 20",
    "envido.calc2": "No matching suits: only the single highest card value",
    "envido.calc3": "The 10, 11 and 12 cards add no value (count as 0).",
    "envido.tie": "Tie: the hand player wins (whoever plays first in the round).",
    "envido.examples": "Examples",
    "ex.e1.value": "7 + 5 + 20 = 32",
    "ex.e1.note": "Two cards of the same suit",
    "ex.e2.value": "7 + 6 + 20 = 33",
    "ex.e2.note": "Highest possible Envido",
    "ex.e3.value": "3 + 0 + 20 = 23",
    "ex.e3.note": "The 12 doesn't count",
    "ex.e4.value": "0 points",
    "ex.e4.note": "No pair: 10 and 11 are worth zero",
    "flor.badge": "Rare privilege",
    "flor.title": "The Sacred \"Flor\"",
    "flor.body": "If you are dealt all three cards of the same suit, immediately call \"Flor!\" before the round begins. The Flor is worth 3 points and overrides any Envido. If both sides have a Flor, the team with the best Flor scores 3 points for each announced Flor. In case of a tie in value, the hand player wins (same rule as Envido). Contra Flor can only be called if both sides have a Flor: if accepted, 6 points to the winner; if rejected, 4 points to the caller.",
    "flor.examples": "Flor Examples",
    "flor.ex1.value": "7 + 6 + 5 + 20 = 38",
    "flor.ex1.note": "Very strong Flor",
    "flor.ex2.value": "1 + 0 + 0 + 20 = 21",
    "flor.ex2.note": "10 and 12 are worth zero",
    "flor.duel.wins": "wins",
    "flor.duel.note": "Both have a Flor: the higher one wins, taking 3 points for each announced Flor.",

    "scoring.label": "Scoring ledger",
    "scoring.title": "Scoring Summary Matrix",
    "score.col1": "Call / Bid",
    "score.col2": "Point Value",
    "score.col3": "Gameplay Context",
    "score.truco": "Truco (Accepted)",
    "score.trucoPts": "2 points",
    "score.trucoCtx": "Baseline bet for the tricks win",
    "score.retruco": "Retruco (Accepted)",
    "score.retrucoPts": "3 points",
    "score.retrucoCtx": "Counter-bet to Truco",
    "score.vale4": "Vale Cuatro (Accepted)",
    "score.vale4Pts": "4 points",
    "score.vale4Ctx": "Final escalation of the bet",
    "score.declined": "Truco / Retruco (Declined)",
    "score.declinedPts": "1/2 points",
    "score.declinedCtx": "Points go to the caller",
    "score.envido": "Envido (Accepted)",
    "score.envidoPts": "2 points",
    "score.envidoCtx": "Best matching-suit combination",
    "score.realEnvido": "Real Envido",
    "score.realEnvidoPts": "3 points",
    "score.realEnvidoCtx": "Raised bid for the suit-pair comparison",
    "score.faltaEnvido": "Falta Envido",
    "score.faltaEnvidoPts": "Variable",
    "score.faltaEnvidoCtx": "Winner takes the game",
    "score.flor": "Flor (Declared)",
    "score.florPts": "3 points",
    "score.florCtx": "Three cards of the same suit",
    "score.contraFlor": "Contra Flor",
    "score.contraFlorPts": "6 / 4 points",
    "score.contraFlorCtx": "Accepted: 6 to winner · rejected: 4 to caller",

    "cta.body": "Now that you know the hierarchy and the bids, you are ready to claim your place at the table.",
    "cta.final": "¡Quiero vale cuatro!"
  }
};

const CARD_PATH = "assets/cards/";

const rankGroups = [
  { title: { pt: "1 de espada", es: "1 de espada", en: "1 of Swords" }, cards: ["1-espada"] },
  { title: { pt: "1 de basto", es: "1 de basto", en: "1 of Clubs" }, cards: ["1-basto"] },
  { title: { pt: "7 de espada", es: "7 de espada", en: "7 of Swords" }, cards: ["7-espada"] },
  { title: { pt: "7 de ouro", es: "7 de oro", en: "7 of Coins" }, cards: ["7-oro"] },
  { title: { pt: "Todos os 3", es: "Todos los 3", en: "All 3s" }, cards: ["3-espada", "3-basto", "3-copa", "3-oro"] },
  { title: { pt: "Todos os 2", es: "Todos los 2", en: "All 2s" }, cards: ["2-espada", "2-basto", "2-copa", "2-oro"] },
  { title: { pt: "1 de copa e ouro", es: "1 de copa y oro", en: "1 of Cups & Coins" }, cards: ["1-copa", "1-oro"] },
  { title: { pt: "Todos os 12 (reis)", es: "Todos los 12 (reyes)", en: "All 12s (kings)" }, cards: ["12-espada", "12-basto", "12-copa", "12-oro"] },
  { title: { pt: "Todos os 11 (cavalos)", es: "Todos los 11 (caballos)", en: "All 11s (knights)" }, cards: ["11-espada", "11-basto", "11-copa", "11-oro"] },
  { title: { pt: "Todos os 10 (valetes)", es: "Todos los 10 (sotas)", en: "All 10s (jacks)" }, cards: ["10-espada", "10-basto", "10-copa", "10-oro"] },
  { title: { pt: "7 de copa e basto", es: "7 de copa y basto", en: "7 of Cups & Clubs" }, cards: ["7-copa", "7-basto"] },
  { title: { pt: "Todos os 6", es: "Todos los 6", en: "All 6s" }, cards: ["6-espada", "6-basto", "6-copa", "6-oro"] },
  { title: { pt: "Todos os 5", es: "Todos los 5", en: "All 5s" }, cards: ["5-espada", "5-basto", "5-copa", "5-oro"] },
  { title: { pt: "Todos os 4", es: "Todos los 4", en: "All 4s" }, cards: ["4-espada", "4-basto", "4-copa", "4-oro"] }
];

const LANGS = ["pt", "es", "en"];

function currentLang() {
  const saved = localStorage.getItem("lang");
  if (saved && LANGS.includes(saved)) return saved;
  return "pt";
}

let musicPlaying = false;

function updateMusicLabel(lang) {
  const label = document.getElementById("music-label");
  if (!label) return;
  const l = lang || currentLang();
  const key = musicPlaying ? "music.pause" : "music.play";
  label.textContent = translations[l][key];
}

function cardImage(name) {
  const img = document.createElement("img");
  img.src = `${CARD_PATH}${name}.png`;
  img.alt = name.replace("-", " de ");
  img.loading = "lazy";
  return img;
}

function renderCardStack(element) {
  const cards = (element.dataset.cards || "").split(",").map((c) => c.trim()).filter(Boolean);
  cards.forEach((c) => element.appendChild(cardImage(c)));
}

function renderRankGrid(lang) {
  const grid = document.querySelector("#rank-grid");
  if (!grid) return;

  grid.innerHTML = "";

  rankGroups.forEach((group, i) => {
    const item = document.createElement("article");
    item.className = "rank-card";

    const num = document.createElement("span");
    num.className = "num";
    num.textContent = String(i + 1).padStart(2, "0");

    const title = document.createElement("strong");
    title.textContent = group.title[lang];

    const cards = document.createElement("div");
    cards.className = "cards";

    group.cards.forEach((c) => cards.appendChild(cardImage(c)));

    item.append(num, title, cards);
    grid.appendChild(item);
  });
}

function applyLanguage(lang) {
  document.documentElement.lang = lang === "pt" ? "pt-BR" : lang;

  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    const value = translations[lang][key];
    if (value !== undefined) el.textContent = value;
  });

  document.querySelectorAll(".lang-toggle button").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === lang);
  });

  renderRankGrid(lang);

  updateMusicLabel(lang);

  localStorage.setItem("lang", lang);
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-cards]").forEach(renderCardStack);

  document.querySelectorAll(".lang-toggle button").forEach((btn) => {
    btn.addEventListener("click", () => applyLanguage(btn.dataset.lang));
  });

  const navToggle = document.querySelector(".nav-toggle");
  const mobileMenu = document.querySelector(".mobile-menu");

  function setMenu(open) {
    if (!navToggle || !mobileMenu) return;
    navToggle.classList.toggle("open", open);
    mobileMenu.classList.toggle("open", open);
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  if (navToggle && mobileMenu) {
    navToggle.addEventListener("click", () => {
      setMenu(!mobileMenu.classList.contains("open"));
    });

    mobileMenu.querySelectorAll("a").forEach((a) => {
      a.addEventListener("click", () => setMenu(false));
    });
  }

  const audio = document.getElementById("site-music");
  const musicToggle = document.getElementById("music-toggle");

  function setPlaying(state) {
    musicPlaying = state;
    musicToggle.classList.toggle("playing", state);
    musicToggle.setAttribute("aria-pressed", state ? "true" : "false");
    updateMusicLabel();
  }

  if (audio && musicToggle) {
    audio.volume = 0.6;

    audio.addEventListener("play", () => setPlaying(true));
    audio.addEventListener("pause", () => setPlaying(false));

    musicToggle.addEventListener("click", () => {
      if (audio.paused) {
        audio.play().catch(() => {});
      } else {
        audio.pause();
      }
    });

    updateMusicLabel();
  }

  applyLanguage(currentLang());
});
