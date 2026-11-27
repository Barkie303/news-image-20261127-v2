#!/usr/bin/env python3
"""Draw entry.png: a newspaper front page summing up Friday 27 November 2026.

Own work, drawn with PIL from the sourced stories in SOURCES.md.
Output: 1024x1024 PNG, well under the 1 MiB gate.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (22, 22, 22)
RED = (168, 30, 38)
BLUE = (31, 78, 121)
GREY = (96, 92, 84)
CARD = (255, 253, 248)
BORDER = (216, 208, 189)
DARK = (28, 28, 28)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
MX = 28  # margin

# ---- Masthead ----
d.text((MX, 14), "THE WORLD", font=font(SERIF_B, 62), fill=INK)
d.text((MX, 84), "One day's news, from every time zone", font=font(SANS_I, 15), fill=GREY)
d.text((W - MX, 22), "FRIDAY", font=font(SANS_B, 16), fill=GREY, anchor="ra")
d.text((W - MX, 44), "27 NOVEMBER 2026", font=font(SANS_B, 30), fill=RED, anchor="ra")
d.text((W - MX, 84), "54 STORIES  ·  SOURCES IN REPO", font=font(SANS_B, 12), fill=GREY, anchor="ra")
d.rectangle([MX, 110, W - MX, 113], fill=INK)
d.rectangle([MX, 116, W - MX, 117], fill=INK)

# ---- Lead story ----
LY, LH = 128, 128
d.rectangle([MX, LY, W - MX, LY + LH], fill=(251, 238, 238), outline=BORDER)
d.rectangle([MX, LY, MX + 8, LY + LH], fill=RED)
d.text((MX + 22, LY + 10), "WAR IN THE GULF  —  00:00 UTC", font=font(SANS_B, 13), fill=RED)
d.text((MX + 22, LY + 32), "Drones kill two Italians in Kuwait", font=font(SERIF_B, 33), fill=INK)
d.text((MX + 22, LY + 72), "as Iran denies any role", font=font(SERIF_B, 33), fill=INK)
d.text((MX + 22, LY + 106), "Riyadh and Damascus blame Tehran; Trump says US victory is near — and gives Iran a chance to talk.",
       font=font(SANS, 14), fill=(60, 58, 52))

# ---- Grid of 8 panels ----
panels = [
    ("UKRAINE", RED, "02:14 UTC", "Zelenskyy warns of a new Russian mass strike",
     "Ballistic missiles hit Kyiv, wounding seven; Trump says he pressed Putin to pull back."),
    ("UNITED STATES", BLUE, "04:34 UTC", "Thanksgiving storms cut power to nearly a million",
     "Macy's parade postponed; 2,000 flights delayed; record tides flood the California coast."),
    ("NEW ZEALAND", BLUE, "01:41 UTC", "Coalition falls one seat short of a majority",
     "Luxon must court the centrist Opportunity Party after special votes cost two seats."),
    ("EUROPE", RED, "00:30 UTC", "De Cos chosen to lead the European Central Bank",
     "Ex-Bank of Spain chief succeeds Lagarde on 7 Feb; EU backs a €45bn loan to Ukraine."),
    ("AFRICA", RED, "04:06 UTC", "13 Niger soldiers killed in border attack",
     "Ebola passes 12,000 cases in DR Congo as fighting disrupts the aid response."),
    ("ECONOMY", BLUE, "06:25 UTC", "Amazon workers strike in 20+ countries",
     "Black Friday walkouts over pay; Asian shares rebound; Nasdaq futures jump 1%."),
    ("CYBER", RED, "01:07 UTC", "AFP platform offline after cyberattack",
     "Intrusion began at 00:30 GMT; France warns of an unprecedented threat level."),
    ("SPORT", BLUE, "05:31 UTC", "Thanksgiving NFL: three last-second thrillers",
     "Eagles 39–38 Cowboys; Bills 13–10 Chiefs; Bears 39–35 Lions."),
]
GX, GY = MX, 272
CW, CH, GAP = 476, 141, 16
for i, (cat, col, when, head, deck) in enumerate(panels):
    x = GX + (i % 2) * (CW + GAP)
    y = GY + (i // 2) * (CH + 10)
    d.rectangle([x, y, x + CW, y + CH], fill=CARD, outline=BORDER)
    d.rectangle([x, y, x + CW, y + 4], fill=col)
    d.text((x + 14, y + 12), cat, font=font(SANS_B, 12), fill=col)
    d.text((x + CW - 14, y + 12), when, font=font(SANS_B, 11), fill=GREY, anchor="ra")
    hl = wrap(d, head, font(SANS_B, 20), CW - 28)
    yy = y + 34
    for line in hl[:2]:
        d.text((x + 14, yy), line, font=font(SANS_B, 20), fill=INK)
        yy += 24
    dl = wrap(d, deck, font(SANS, 13), CW - 28)
    yy = y + 34 + 2 * 24 + 4
    for line in dl[:2]:
        d.text((x + 14, yy), line, font=font(SANS, 13), fill=(60, 58, 52))
        yy += 17

# ---- UTC timeline strip ----
TY, TH = 880, 92
d.rectangle([MX, TY, W - MX, TY + TH], fill=DARK)
d.text((MX + 14, TY + 8), "THE DAY IN UTC", font=font(SANS_B, 13), fill=(255, 255, 255))
events = [
    ("00:00", "Kuwait attack"),
    ("00:11", "Argentina bank"),
    ("00:47", "Hasina return"),
    ("01:07", "AFP attack"),
    ("01:41", "NZ result"),
    ("02:14", "Ukraine warn"),
    ("04:06", "Niger attack"),
    ("04:34", "US storms"),
    ("06:25", "Nasdaq +1%"),
]
cols = 5
cell = (W - 2 * MX - 28) // cols
for i, (t, label) in enumerate(events):
    row, c = divmod(i, cols)
    ex = MX + 14 + c * cell
    ey = TY + 30 + row * 30
    d.ellipse([ex, ey + 2, ex + 7, ey + 9], fill=RED)
    d.text((ex + 12, ey - 2), t, font=font(SANS_B, 12), fill=(255, 255, 255))
    d.text((ex + 58, ey - 2), label, font=font(SANS, 11), fill=(205, 200, 190))

# ---- Footer ----
d.text((W // 2, 986), "Friday, 27 November 2026  ·  54 sourced stories — full list in SOURCES.md  ·  Times are UTC",
       font=font(SANS, 12), fill=GREY, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
