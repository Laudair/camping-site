# Cartilha de Truco - Torneio

Kit editável para gerar uma cartilha visual de torneio de truco em PNG e PDF.

## Arquivos principais

- `index.html`: textos, paginas e blocos editaveis.
- `src/styles.css`: visual, cores, tamanhos e layout A4.
- `src/cartilha.js`: ordem das cartas e grupos usados na pagina 1.
- `assets/cards/`: imagens das cartas do repositorio `maxogod/Truco`.
- `assets/gauderia/`: bandeira do RS, cuia e trofeu em SVG.
- `exports/`: PNGs e PDF gerados.

## Como editar

Abra `index.html` para alterar textos, pontuacoes, nomes de secoes ou frases do torneio.

Para alterar a ordem visual das cartas, edite o array `rankGroups` em `src/cartilha.js`.

## Como exportar

No terminal, dentro desta pasta:

```bash
npm run export
```

Se estiver em outro computador e o Playwright não estiver instalado:

```bash
npm install
npm run export
```

Se você não tiver um navegador/Chromium disponível, use o exportador estático:

```bash
npm run export:static
```

## Referencias usadas

- Regras: https://github.com/maxogod/Truco/blob/main/docs/RULES.md
- Cartas: https://github.com/maxogod/Truco/tree/main/truco-front/src/assets/Cards

Observação: o `RULES.md` não detalha a regra de "parda" no Truco. A página de Truco deixa esse trecho marcado como critério de torneio editável.
