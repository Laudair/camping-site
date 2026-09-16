const CARD_PATH = "./assets/cards/";

const rankGroups = [
  { number: 1, title: "1 de espada", cards: ["1-espada"] },
  { number: 2, title: "1 de basto", cards: ["1-basto"] },
  { number: 3, title: "7 de espada", cards: ["7-espada"] },
  { number: 4, title: "7 de ouro", cards: ["7-oro"] },
  { number: 5, title: "Todos os 3", cards: ["3-espada", "3-basto", "3-copa", "3-oro"] },
  { number: 6, title: "Todos os 2", cards: ["2-espada", "2-basto", "2-copa", "2-oro"] },
  { number: 7, title: "1 de copa e ouro", cards: ["1-copa", "1-oro"] },
  { number: 8, title: "Todos os 12 (reis)", cards: ["12-espada", "12-basto", "12-copa", "12-oro"] },
  { number: 9, title: "Todos os 11 (cavalos)", cards: ["11-espada", "11-basto", "11-copa", "11-oro"] },
  { number: 10, title: "Todos os 10 (valetes)", cards: ["10-espada", "10-basto", "10-copa", "10-oro"] },
  { number: 11, title: "7 de copa e basto", cards: ["7-copa", "7-basto"] },
  { number: 12, title: "Todos os 6", cards: ["6-espada", "6-basto", "6-copa", "6-oro"] },
  { number: 13, title: "Todos os 5", cards: ["5-espada", "5-basto", "5-copa", "5-oro"] },
  { number: 14, title: "Todos os 4", cards: ["4-espada", "4-basto", "4-copa", "4-oro"] },
];

function cardImage(cardName, index = 0) {
  const img = document.createElement("img");
  img.src = `${CARD_PATH}${cardName}.png`;
  img.alt = cardName.replace("-", " de ");
  img.loading = "eager";
  img.style.setProperty("--i", index);
  return img;
}

function renderCardStack(element) {
  const cards = element.dataset.cards
    .split(",")
    .map((card) => card.trim())
    .filter(Boolean);

  cards.forEach((card, index) => element.appendChild(cardImage(card, index)));
}

function renderRankGrid() {
  const grid = document.querySelector("#rank-grid");
  if (!grid) return;

  rankGroups.forEach((group) => {
    const item = document.createElement("article");
    item.className = "rank-card";

    const header = document.createElement("header");
    const number = document.createElement("span");
    number.className = "rank-number";
    number.textContent = group.number;

    const title = document.createElement("strong");
    title.textContent = group.title;

    header.append(number, title);

    const cards = document.createElement("div");
    cards.className = "rank-card-stack";
    cards.dataset.cards = group.cards.join(",");

    item.append(header, cards);
    grid.appendChild(item);
    renderCardStack(cards);
  });
}

document.querySelectorAll("[data-cards]").forEach(renderCardStack);
renderRankGrid();
