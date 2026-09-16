from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "assets" / "cards"
EXPORTS = ROOT / "exports"

W, H = 1654, 2339
M = 78

INK = (21, 17, 12)
MUTED = (66, 53, 38)
PAPER = (234, 215, 173)
PAPER_LIGHT = (247, 235, 203)
PANEL = (246, 231, 194)
RED = (166, 39, 34)
GREEN = (18, 101, 61)
YELLOW = (225, 179, 59)
CREAM = (250, 239, 209)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
FONT_REG = FONT_DIR / "DejaVuSans.ttf"
FONT_BOLD = FONT_DIR / "DejaVuSans-Bold.ttf"
FONT_SERIF = FONT_DIR / "DejaVuSerif-Bold.ttf"


def font(size: int, bold: bool = False, serif: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_SERIF if serif else (FONT_BOLD if bold else FONT_REG)
    return ImageFont.truetype(str(path), size)


F = {
    "title": font(194, True, True),
    "title_small": font(74, True, True),
    "h1": font(140, True, True),
    "h2": font(43, True, True),
    "h3": font(34, True),
    "body": font(31),
    "body_bold": font(31, True),
    "small": font(25),
    "small_bold": font(25, True),
    "tiny": font(21),
    "tiny_bold": font(21, True),
}


RANK_GROUPS = [
    (1, "1 de espada", ["1-espada"]),
    (2, "1 de basto", ["1-basto"]),
    (3, "7 de espada", ["7-espada"]),
    (4, "7 de ouro", ["7-oro"]),
    (5, "Todos os 3", ["3-espada", "3-basto", "3-copa", "3-oro"]),
    (6, "Todos os 2", ["2-espada", "2-basto", "2-copa", "2-oro"]),
    (7, "1 de copa e ouro", ["1-copa", "1-oro"]),
    (8, "Todos os 12 (reis)", ["12-espada", "12-basto", "12-copa", "12-oro"]),
    (9, "Todos os 11 (cavalos)", ["11-espada", "11-basto", "11-copa", "11-oro"]),
    (10, "Todos os 10 (valetes)", ["10-espada", "10-basto", "10-copa", "10-oro"]),
    (11, "7 de copa e basto", ["7-copa", "7-basto"]),
    (12, "Todos os 6", ["6-espada", "6-basto", "6-copa", "6-oro"]),
    (13, "Todos os 5", ["5-espada", "5-basto", "5-copa", "5-oro"]),
    (14, "Todos os 4", ["4-espada", "4-basto", "4-copa", "4-oro"]),
]


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def centered(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill=INK) -> None:
    x1, y1, x2, y2 = box
    tw, th = text_size(draw, text, fnt)
    draw.text((x1 + (x2 - x1 - tw) / 2, y1 + (y2 - y1 - th) / 2 - 3), text, font=fnt, fill=fill)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if text_size(draw, candidate, fnt)[0] <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, width: int, fill=INK, leading=8) -> int:
    x, y = xy
    line_height = text_size(draw, "Ag", fnt)[1] + leading
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_height
    return y


def page_base() -> Image.Image:
    random.seed(14)
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    for y in range(H):
        ratio = y / H
        r = int(PAPER_LIGHT[0] * (1 - ratio) + 211 * ratio)
        g = int(PAPER_LIGHT[1] * (1 - ratio) + 185 * ratio)
        b = int(PAPER_LIGHT[2] * (1 - ratio) + 135 * ratio)
        draw.line((0, y, W, y), fill=(r, g, b))

    noise = Image.effect_noise((W, H), 28).convert("L")
    noise_rgb = Image.merge("RGB", (noise, noise, noise))
    img = Image.blend(img, noise_rgb, 0.045)
    img = ImageEnhance.Color(img).enhance(0.92)
    draw = ImageDraw.Draw(img)

    for _ in range(90):
        x = random.randint(20, W - 20)
        y = random.randint(20, H - 20)
        rx = random.randint(10, 80)
        ry = random.randint(5, 45)
        fill = (105, 61, 26, random.randint(10, 28))
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        od.ellipse((x - rx, y - ry, x + rx, y + ry), fill=fill)
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        draw = ImageDraw.Draw(img)

    draw.rectangle((30, 30, W - 30, H - 30), outline=(58, 36, 19), width=16)
    draw.rectangle((52, 52, W - 52, H - 52), outline=INK, width=4)
    draw.rectangle((M - 12, M - 12, W - M + 12, H - M + 12), outline=(84, 59, 38), width=2)
    return img


def brush(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, size: int = 43) -> None:
    x1, y1, x2, y2 = box
    points = [
        (x1 + 8, y1 + 4),
        (x2 - 12, y1),
        (x2 - 3, y1 + (y2 - y1) // 2),
        (x2 - 14, y2 - 2),
        (x1 + 4, y2),
        (x1, y1 + (y2 - y1) // 2),
    ]
    draw.polygon(points, fill=INK)
    centered(draw, box, title.upper(), font(size, True, True), fill=CREAM)


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str | None = None) -> None:
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=PANEL, outline=INK, width=4)
    draw.rectangle((x1 + 7, y1 + 7, x2 - 7, y2 - 7), outline=(109, 83, 55), width=1)
    if title:
        bw = min(x2 - x1 - 50, max(320, int(text_size(draw, title.upper(), F["h2"])[0] + 120)))
        brush(draw, (x1 + (x2 - x1 - bw) // 2, y1 - 31, x1 + (x2 - x1 + bw) // 2, y1 + 35), title)


def bullet_list(draw: ImageDraw.ImageDraw, items: list[str], x: int, y: int, width: int, fnt=None, gap=11) -> int:
    fnt = fnt or F["body"]
    bullet_font = font(fnt.size + 2, True)
    line_height = text_size(draw, "Ag", fnt)[1] + 7
    for item in items:
        lines = wrap(draw, item, fnt, width - 38)
        draw.text((x, y), "•", font=bullet_font, fill=INK)
        yy = y
        for line in lines:
            draw.text((x + 34, yy), line, font=fnt, fill=INK)
            yy += line_height
        y = yy + gap
    return y


def table(draw: ImageDraw.ImageDraw, rows: list[tuple[str, str]], box: tuple[int, int, int, int], fnt=None) -> None:
    fnt = fnt or F["body_bold"]
    x1, y1, x2, y2 = box
    row_h = (y2 - y1) // len(rows)
    split = x1 + int((x2 - x1) * 0.47)
    for i, (left, right) in enumerate(rows):
        y = y1 + i * row_h
        if i:
            draw.line((x1, y, x2, y), fill=(95, 72, 48), width=2)
        draw.text((x1 + 10, y + 8), left, font=fnt, fill=INK)
        draw.text((split + 10, y + 8), right, font=fnt, fill=INK)


def draw_rs_flag(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=YELLOW, outline=INK, width=3)
    draw.polygon([(x1, y1), (x2, y1), (x1, y2)], fill=GREEN)
    draw.polygon([(x1, y2), (x2, y1), (x2, y1 + int((y2 - y1) * 0.38)), (x1 + int((x2 - x1) * 0.18), y2)], fill=RED)
    draw.polygon([(x1 + int((x2 - x1) * 0.18), y2), (x2, y1 + int((y2 - y1) * 0.38)), (x2, y2)], fill=YELLOW)
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    r = int((y2 - y1) * 0.32)
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=CREAM, outline=INK, width=3)
    centered(draw, (cx - r, cy - r, cx + r, cy + r), "RS", font(max(20, r), True, True), fill=INK)


def draw_cuia(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float = 1.0) -> None:
    w = int(150 * scale)
    h = int(190 * scale)
    draw.line((x + int(92 * scale), y + int(12 * scale), x + int(48 * scale), y + int(112 * scale)), fill=INK, width=max(5, int(9 * scale)))
    draw.ellipse((x + int(22 * scale), y + int(48 * scale), x + int(128 * scale), y + int(84 * scale)), fill=CREAM, outline=INK, width=max(4, int(7 * scale)))
    draw.ellipse((x + int(45 * scale), y + int(57 * scale), x + int(105 * scale), y + int(76 * scale)), fill=(91, 58, 28))
    draw.pieslice((x + int(28 * scale), y + int(66 * scale), x + int(122 * scale), y + h), 0, 180, fill=INK)
    draw.polygon([(x + int(37 * scale), y + int(72 * scale)), (x + int(113 * scale), y + int(72 * scale)), (x + int(95 * scale), y + int(168 * scale)), (x + int(55 * scale), y + int(168 * scale))], fill=INK)
    draw.line((x + int(55 * scale), y + int(116 * scale), x + int(98 * scale), y + int(116 * scale)), fill=CREAM, width=max(3, int(5 * scale)))
    draw.line((x + int(60 * scale), y + int(137 * scale), x + int(92 * scale), y + int(137 * scale)), fill=CREAM, width=max(3, int(5 * scale)))
    return None


def draw_trophy(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    cx = (x1 + x2) // 2
    draw.rounded_rectangle((cx - 35, y1 + 12, cx + 35, y1 + 85), radius=8, fill=INK)
    draw.arc((cx - 88, y1 + 20, cx - 12, y1 + 105), 275, 85, fill=INK, width=9)
    draw.arc((cx + 12, y1 + 20, cx + 88, y1 + 105), 95, 265, fill=INK, width=9)
    draw.rectangle((cx - 10, y1 + 82, cx + 10, y1 + 126), fill=INK)
    draw.rectangle((cx - 48, y1 + 124, cx + 48, y1 + 145), fill=INK)
    draw.line((cx - 70, y1 + 156, cx + 70, y1 + 156), fill=INK, width=11)


def load_card(name: str, height: int) -> Image.Image:
    img = Image.open(CARDS / f"{name}.png").convert("RGBA")
    ratio = height / img.height
    return img.resize((int(img.width * ratio), height), Image.Resampling.LANCZOS)


def paste_card(base: Image.Image, name: str, x: int, y: int, height: int, angle: float = 0) -> tuple[int, int]:
    card = load_card(name, height)
    shadow = Image.new("RGBA", (card.width + 16, card.height + 16), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((8, 8, card.width + 8, card.height + 8), radius=9, fill=(0, 0, 0, 80))
    shadow = shadow.filter(ImageFilter.GaussianBlur(4))
    shadow.alpha_composite(card, (0, 0))
    if angle:
        shadow = shadow.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    base.alpha_composite(shadow, (x, y))
    return shadow.width, shadow.height


def card_fan(base: Image.Image, cards: list[str], x: int, y: int, height: int, overlap: int = 42) -> None:
    start = x
    angles = [-13, -5, 4, 12, 18]
    for i, name in enumerate(cards):
        paste_card(base, name, start + i * overlap, y + abs(2 - i) * 3, height, angles[i % len(angles)])


def rank_grid(base: Image.Image, draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    cols = 7
    gap = 12
    cell_w = (x2 - x1 - gap * (cols - 1)) // cols
    cell_h = 231
    for idx, (number, title, cards) in enumerate(RANK_GROUPS):
        col = idx % cols
        row = idx // cols
        cx = x1 + col * (cell_w + gap)
        cy = y1 + row * (cell_h + gap)
        draw.rounded_rectangle((cx, cy, cx + cell_w, cy + cell_h), radius=8, fill=(249, 238, 209), outline=INK, width=3)
        draw.ellipse((cx + 10, cy + 9, cx + 55, cy + 54), fill=INK)
        centered(draw, (cx + 10, cy + 9, cx + 55, cy + 54), str(number), F["small_bold"], CREAM)
        lines = wrap(draw, title, F["tiny_bold"], cell_w - 70)
        ty = cy + 10
        for line in lines[:2]:
            draw.text((cx + 65, ty), line, font=F["tiny_bold"], fill=INK)
            ty += 25

        card_h = 126
        total_w = 55 + (len(cards) - 1) * 31
        sx = cx + (cell_w - total_w) // 2
        for i, card in enumerate(cards):
            paste_card(base, card, sx + i * 31, cy + 77, card_h)


def footer(draw: ImageDraw.ImageDraw, page_no: str, text: str) -> None:
    y = H - 136
    draw.line((M, y, W - M, y), fill=INK, width=4)
    draw.text((M, y + 18), page_no.upper(), font=F["h2"], fill=INK)
    label_w = text_size(draw, page_no.upper(), F["h2"])[0]
    draw.text((M + label_w + 70, y + 28), text, font=F["small_bold"], fill=INK)


def header(draw: ImageDraw.ImageDraw, title: str, eyebrow: str, icon: str = "flag") -> None:
    draw.text((M, 80), eyebrow.upper(), font=F["h2"], fill=INK)
    draw.text((M, 120), title.upper(), font=F["h1"], fill=INK)
    draw.line((M, 285, W - M, 285), fill=INK, width=5)
    if icon == "flag":
        draw_rs_flag(draw, (W - M - 410, 96, W - M, 175))
    elif icon == "cuia":
        draw_cuia(draw, W - M - 190, 70, 0.82)


def page_cover() -> Image.Image:
    img = page_base().convert("RGBA")
    draw = ImageDraw.Draw(img)

    draw_cuia(draw, 96, 82, 1.05)
    draw_wrapped(draw, (78, 278), "Aqui o truco é sério, mas a parceria vem primeiro.", F["small_bold"], 250)

    centered(draw, (360, 72, 1290, 145), "CAMPEONATO DE", F["title_small"], INK)
    centered(draw, (270, 138, 1388, 330), "TRUCO", F["title"], INK)
    draw_rs_flag(draw, (525, 342, 1125, 405))
    centered(draw, (300, 420, 1350, 478), "AMIZADE, RESPEITO E BOAS JOGADAS", F["h2"], INK)
    card_fan(img, ["1-espada", "1-basto", "7-espada", "7-oro"], 1248, 88, 178, 48)
    draw.rounded_rectangle((1236, 285, 1568, 420), radius=8, fill=(220, 181, 118), outline=INK, width=4)
    centered(draw, (1236, 295, 1568, 410), "TRUCO\nRETRUCO\nVALE 4", font(42, True), INK)

    panel(draw, (M, 535, 926, 835), "Regras gerais")
    bullet_list(
        draw,
        [
            "Jogo em duplas: 2 contra 2.",
            "Baralho espanhol de 40 cartas, sem 8, 9 e coringas.",
            "Cada jogador recebe 3 cartas.",
            "Há três formas de pontuar: Flor, Envido e Truco.",
            "Depois de Flor e Envido, a mão tem 3 rodadas.",
            "Vence a mão quem ganhar 2 das 3 rodadas.",
            "Vence a partida quem chegar primeiro a 30 pontos.",
        ],
        M + 38,
        585,
        780,
        F["small"],
        gap=5,
    )

    panel(draw, (960, 535, W - M, 835), "Pontuação rápida")
    table(
        draw,
        [
            ("Sem truco", "1 ponto"),
            ("Truco", "2 pontos"),
            ("Retruco", "3 pontos"),
            ("Vale 4", "4 pontos"),
            ("Envido", "+2 pontos"),
            ("Real Envido", "+3 pontos"),
            ("Flor", "3 pontos"),
        ],
        (997, 590, W - M - 28, 806),
        F["small_bold"],
    )

    brush(draw, (410, 890, 1245, 955), "Ordem das cartas", 49)
    centered(draw, (540, 955, 1110, 995), "maior para menor", F["small_bold"], INK)
    rank_grid(img, draw, (M, 1010, W - M, 1485))

    panel(draw, (M, 1560, 615, 2095), "Duplas inscritas")
    x0, y0, x1, y1 = M + 28, 1618, 585, 2060
    row_h = (y1 - y0) // 8
    draw.rectangle((x0, y0, x1, y1), outline=INK, width=4)
    for i in range(8):
        y = y0 + i * row_h
        draw.rectangle((x0, y, x0 + 70, y + row_h), fill=INK)
        centered(draw, (x0, y, x0 + 70, y + row_h), str(i + 1), F["h3"], CREAM)
        if i:
            draw.line((x0, y, x1, y), fill=INK, width=2)

    panel(draw, (665, 1560, W - M, 2095), "Chave do torneio")
    for y, label in [(1645, "SEMIFINAL 1"), (1795, "SEMIFINAL 2")]:
        centered(draw, (710, y - 45, 1090, y - 10), label, F["h3"], INK)
        draw.rectangle((710, y, 1090, y + 78), outline=INK, width=3)
        centered(draw, (710, y, 1090, y + 78), "________  X  ________", F["h3"], INK)
    draw.line((1090, 1685, 1160, 1685), fill=INK, width=4)
    draw.line((1090, 1835, 1160, 1835), fill=INK, width=4)
    draw.line((1160, 1685, 1160, 1835), fill=INK, width=4)
    draw.line((1160, 1760, 1215, 1760), fill=INK, width=4)
    centered(draw, (1235, 1600, 1515, 1645), "FINAL", F["h3"], INK)
    draw.rectangle((1225, 1660, 1530, 1748), outline=INK, width=3)
    centered(draw, (1225, 1660, 1530, 1748), "______  X  ______", F["h3"], INK)
    draw_trophy(draw, (1285, 1768, 1472, 1935))
    brush(draw, (1238, 1952, 1518, 2015), "Campeões", 38)

    footer(draw, "Truco é cultura", "Jogue limpo, respeite a parceria e aproveite a resenha.")
    return img.convert("RGB")


def detail_common(title: str, eyebrow: str, icon: str = "flag") -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = page_base().convert("RGBA")
    draw = ImageDraw.Draw(img)
    header(draw, title, eyebrow, icon)
    return img, draw


def draw_flow(draw: ImageDraw.ImageDraw, labels: list[str], box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    gap = 24
    w = (x2 - x1 - gap * (len(labels) - 1)) // len(labels)
    for i, label in enumerate(labels):
        x = x1 + i * (w + gap)
        draw.rounded_rectangle((x, y1, x + w, y2), radius=8, fill=CREAM, outline=INK, width=4)
        centered(draw, (x + 8, y1 + 8, x + w - 8, y2 - 8), label.upper(), F["small_bold"], INK)
        if i < len(labels) - 1:
            cy = (y1 + y2) // 2
            draw.line((x + w, cy, x + w + gap, cy), fill=INK, width=4)
            draw.polygon([(x + w + gap, cy), (x + w + gap - 12, cy - 7), (x + w + gap - 12, cy + 7)], fill=INK)


def example_cards(base: Image.Image, draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], cards: list[str], calc: str, note: str) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=8, fill=CREAM, outline=INK, width=4)
    card_fan(base, cards, x1 + 45, y1 + 28, 170, 78 if len(cards) == 2 else 61)
    centered(draw, (x1 + 10, y1 + 238, x2 - 10, y1 + 287), calc, F["h3"], INK)
    centered(draw, (x1 + 12, y1 + 288, x2 - 12, y2 - 12), note, F["small"], MUTED)


def page_envido() -> Image.Image:
    img, draw = detail_common("Envido", "Pontuação e disputa", "flag")

    panel(draw, (M, 355, 810, 655), "Quando pedir")
    y = draw_wrapped(draw, (M + 35, 405), "No início da mão, no turno do jogador, antes das cartas serem disputadas.", F["body"], 660)
    draw_wrapped(draw, (M + 35, y + 20), "Se o Truco já foi aceito, Envido não pode ser pedido. Antes do aceite, o adversário pode chamar Envido sobre o Truco, anulando aquela chamada; depois disso o Truco pode voltar.", F["small"], 660, MUTED)

    panel(draw, (850, 355, W - M, 655), "Respostas")
    bullet_list(
        draw,
        [
            "Quero: aceita a aposta.",
            "Envido: aumenta em 2 pontos.",
            "Real Envido: aumenta em 3 pontos.",
            "Falta Envido: se aceito, quem vence ganha a partida.",
            "Não quero: recusa a última aposta.",
        ],
        890,
        405,
        625,
        F["small"],
        gap=8,
    )

    panel(draw, (M, 735, W - M, 945), "Sequência das apostas")
    draw_flow(draw, ["Sem aposta", "Envido", "Real Envido", "Falta Envido"], (125, 795, W - 125, 870))
    draw_wrapped(draw, (125, 890), "Quem aumenta não volta para aposta menor. Real Envido e Falta Envido só aparecem uma vez.", F["tiny_bold"], W - 250, MUTED)

    panel(draw, (M, 1020, 825, 1355), "Como calcular")
    bullet_list(
        draw,
        [
            "Duas cartas do mesmo naipe: some as duas cartas e acrescente 20.",
            "10, 11 e 12 contam como zero.",
            "Três naipes diferentes: vale a maior carta da mão.",
            "Maior Envido: 33, com 7 + 6 do mesmo naipe.",
            "Menor Envido: 0, quando só há figuras sem valor útil.",
        ],
        M + 38,
        1075,
        685,
        F["small"],
        gap=8,
    )

    panel(draw, (865, 1020, W - M, 1355), "Desempate")
    draw_wrapped(draw, (905, 1080), "Se dois jogadores empatarem no valor do Envido, vence o jogador mão, ou seja, quem joga primeiro naquela mão.", F["body"], 600)
    draw.rectangle((905, 1230, W - M - 35, 1315), fill=(245, 219, 177), outline=RED, width=4)
    draw_wrapped(draw, (928, 1248), "Dica de torneio: deixe claro quem é o mão antes de iniciar cada rodada.", F["small_bold"], 550, INK)

    brush(draw, (440, 1440, 1215, 1505), "Exemplos rápidos", 49)
    example_cards(img, draw, (M, 1555, 535, 1975), ["7-oro", "6-oro"], "7 + 6 + 20 = 33", "Maior Envido possível")
    example_cards(img, draw, (590, 1555, 1065, 1975), ["3-copa", "12-copa"], "3 + 0 + 20 = 23", "Figuras valem zero")
    example_cards(img, draw, (1120, 1555, W - M, 1975), ["10-basto", "11-espada", "12-copa"], "0 ponto", "Sem par de naipe útil")

    footer(draw, "Página 2", "Envido decide no cálculo. Empate decide no mão.")
    return img.convert("RGB")


def page_flor() -> Image.Image:
    img, draw = detail_common("Flor", "Três cartas do mesmo naipe", "cuia")

    panel(draw, (M, 355, 810, 650), "O que é")
    y = draw_wrapped(draw, (M + 35, 408), "Flor acontece quando as 3 cartas do jogador são do mesmo naipe.", F["body"], 660)
    draw_wrapped(draw, (M + 35, y + 24), "Quem tem Flor deve anunciar dizendo \"Flor\". Se mais de uma Flor for anunciada, compara-se o valor das Flores.", F["body"], 660)

    panel(draw, (850, 355, W - M, 650), "Pontuação")
    table(
        draw,
        [
            ("Flor simples", "3 pontos"),
            ("Cada Flor", "3 p/ melhor Flor"),
            ("Contra aceita", "6 pontos"),
            ("Contra recusada", "4 pontos"),
        ],
        (890, 410, W - M - 30, 610),
        F["small_bold"],
    )

    panel(draw, (M, 730, W - M, 945), "Como calcular")
    draw_wrapped(draw, (125, 790), "Use a mesma lógica do Envido: some os valores das três cartas e acrescente 20. As cartas 10, 11 e 12 não somam valor.", F["body"], W - 250)
    draw.rounded_rectangle((180, 865, 1005, 918), radius=8, fill=INK)
    centered(draw, (180, 865, 1005, 918), "FLOR = CARTA 1 + CARTA 2 + CARTA 3 + 20", F["small_bold"], CREAM)
    draw.rounded_rectangle((1030, 865, 1472, 918), radius=8, fill=INK)
    centered(draw, (1030, 865, 1472, 918), "10, 11 E 12 = 0", F["small_bold"], CREAM)

    brush(draw, (440, 1030, 1215, 1095), "Exemplos rápidos", 49)
    example_cards(img, draw, (M, 1145, 535, 1565), ["7-basto", "6-basto", "5-basto"], "7 + 6 + 5 + 20 = 38", "Flor muito forte")
    example_cards(img, draw, (590, 1145, 1065, 1565), ["1-copa", "10-copa", "12-copa"], "1 + 0 + 0 + 20 = 21", "Figuras não aumentam")
    example_cards(img, draw, (1120, 1145, W - M, 1565), ["3-oro", "6-oro", "11-oro"], "3 + 6 + 0 + 20 = 29", "Boa Flor para disputar")

    panel(draw, (M, 1660, 810, 2020), "Contra Flor")
    draw_wrapped(draw, (M + 35, 1718), "Só pode ser chamada quando os dois lados têm Flor. Se for aceita, a melhor Flor leva 6 pontos. Se for recusada, quem chamou leva 4 pontos.", F["body"], 660)

    panel(draw, (850, 1660, W - M, 2020), "Desempate")
    draw_wrapped(draw, (890, 1718), "Quando duas Flores tiverem o mesmo valor, use o critério do jogador mão para o torneio, mantendo a mesma lógica de desempate indicada para o Envido.", F["body"], 620)
    draw.rectangle((890, 1900, W - M - 35, 1980), fill=(245, 219, 177), outline=RED, width=4)
    draw_wrapped(draw, (912, 1915), "Regra editável: ajuste este bloco se o torneio usar outro critério.", F["small_bold"], 560)

    footer(draw, "Página 3", "Flor deve ser anunciada. Contra Flor só existe se os dois lados tiverem Flor.")
    return img.convert("RGB")


def page_truco() -> Image.Image:
    img, draw = detail_common("Truco", "A disputa das cartas", "flag")
    card_fan(img, ["1-espada", "1-basto", "7-espada"], W - M - 410, 175, 150, 56)

    panel(draw, (M, 355, 810, 670), "Como funciona")
    bullet_list(
        draw,
        [
            "Depois de Flor e Envido, a mão é jogada em 3 rodadas.",
            "Em cada rodada, cada jogador baixa uma carta.",
            "A carta mais forte vence a rodada.",
            "Vence a mão quem ganhar 2 rodadas.",
            "Se ninguém pedir Truco, a mão vale 1 ponto.",
        ],
        M + 38,
        410,
        665,
        F["small"],
        gap=10,
    )

    panel(draw, (850, 355, W - M, 670), "Apostas")
    table(
        draw,
        [
            ("Truco", "2 pontos"),
            ("Retruco", "3 pontos"),
            ("Vale 4", "4 pontos"),
        ],
        (900, 420, W - M - 45, 565),
        F["body_bold"],
    )
    draw_wrapped(draw, (900, 590), "A aposta pode ser aceita, recusada ou aumentada na ordem abaixo.", F["small_bold"], 600, MUTED)

    panel(draw, (M, 750, W - M, 1010), "Sequência das apostas")
    draw_flow(draw, ["Sem aposta", "Truco", "Retruco", "Vale 4"], (125, 810, W - 125, 885))
    bullet_list(
        draw,
        [
            "Quero: aceita e joga pelos pontos em disputa.",
            "Não quero: recusa e entrega os pontos.",
        ],
        125,
        920,
        690,
        F["small"],
        gap=4,
    )
    bullet_list(
        draw,
        [
            "Aumentar: sobe para o próximo nível.",
            "Envido sobre Truco: anula antes do aceite.",
        ],
        840,
        920,
        630,
        F["small"],
        gap=4,
    )

    brush(draw, (465, 1090, 1190, 1155), "As 3 rodadas", 49)
    x = M
    card_w = (W - 2 * M - 40) // 3
    for i, (label, text) in enumerate(
        [
            ("Primeira", "Começa a disputa. Guarde quem venceu ou se ficou parda."),
            ("Segunda", "Se alguém fizer 2 vitórias, a mão termina aqui."),
            ("Terceira", "Resolve a mão quando ainda não há vencedor."),
        ]
    ):
        cx = x + i * (card_w + 20)
        draw.rounded_rectangle((cx, 1215, cx + card_w, 1438), radius=8, fill=CREAM, outline=INK, width=4)
        draw.ellipse((cx + card_w // 2 - 34, 1240, cx + card_w // 2 + 34, 1308), fill=INK)
        centered(draw, (cx + card_w // 2 - 34, 1240, cx + card_w // 2 + 34, 1308), str(i + 1), F["h3"], CREAM)
        centered(draw, (cx + 10, 1320, cx + card_w - 10, 1362), label.upper(), F["h3"], INK)
        draw_wrapped(draw, (cx + 28, 1372), text, F["small"], card_w - 56, MUTED)

    panel(draw, (M, 1530, 920, 2025), "Desempates")
    draw_wrapped(draw, (M + 38, 1588), "O arquivo de regras do repo não detalha a regra de parda. Para torneio, deixe combinado antes do primeiro jogo.", F["small_bold"], 765, MUTED)
    bullet_list(
        draw,
        [
            "Empate na 1ª: quem vencer a 2ª leva a vantagem.",
            "Empate na 2ª: vale a vantagem de quem venceu a 1ª.",
            "Empate na 3ª: vale a vantagem de quem venceu a 1ª.",
            "Três empates: vence o jogador mão.",
        ],
        M + 38,
        1708,
        765,
        F["small"],
        gap=10,
    )

    panel(draw, (960, 1530, W - M, 2025), "Lembrete rápido")
    card_fan(img, ["1-espada", "1-basto", "7-espada", "7-oro"], 1035, 1605, 172, 58)
    draw_wrapped(draw, (1008, 1845), "As quatro cartas mais fortes são: 1 de espada, 1 de basto, 7 de espada e 7 de ouro.", F["body_bold"], 500)

    footer(draw, "Página 4", "Truco é aposta, memória das rodadas e leitura da ordem das cartas.")
    return img.convert("RGB")


def main() -> None:
    EXPORTS.mkdir(exist_ok=True)
    pages = [page_cover(), page_envido(), page_flor(), page_truco()]
    for i, page in enumerate(pages, 1):
        final_path = EXPORTS / f"pagina-{i}.png"
        tmp_path = EXPORTS / f".pagina-{i}.tmp.png"
        page.save(tmp_path, format="PNG", compress_level=6)
        with Image.open(tmp_path) as check:
            check.load()
        tmp_path.replace(final_path)

    pdf_path = EXPORTS / "cartilha-truco.pdf"
    pages[0].save(pdf_path, "PDF", resolution=200.0, save_all=True, append_images=pages[1:])
    print(f"Exportados {len(pages)} PNGs e 1 PDF em {EXPORTS}")


if __name__ == "__main__":
    main()
