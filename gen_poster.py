#!/usr/bin/env python3
"""Draw the 23 November 2026 front page (1024x1024, <= 1 MiB).

Layout follows the refined winner formula: masthead + strap, an exact-hour
UTC timeline, 3 illustrated hero panels, a "day in numbers" band, 11
medium panels, a dotted world map with numbered pins, a numbered ALSO ON
list, a DATE CHECK box and a one-line footer with the chip legend.
All content lives in stories.py. Vertical budget is fixed up front so
nothing can spill into the next band.
"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stories import (PANELS, NUMBERS, TIMELINE, ALSO_ON,
                     DATE_CHECK_EARLIER, DATE_CHECK_FUTURE, TOTAL_STORIES)

W, H = 1024, 1024
M = 18
CREAM = (246, 239, 224)
PAPER = (255, 253, 246)
INK = (26, 26, 26)
MUTED = (96, 89, 74)
RED = (176, 58, 46)
NAVY = (24, 38, 66)
GREEN = (38, 110, 66)
LINE = (182, 174, 154)
CHIP_BG = (233, 226, 208)
SEA = (168, 198, 224)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def F(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIFB = lambda s: F("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: F("DejaVuSerif.ttf", s)
SANS = lambda s: F("DejaVuSans.ttf", s)
SANSB = lambda s: F("DejaVuSans-Bold.ttf", s)


def wrap(d, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, text, font, width, leading, fill=INK, max_lines=None):
    lines = wrap(d, text, font, width)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def chip(d, x, y, label):
    f = SANSB(9)
    w = d.textlength(label, font=f) + 10
    d.rounded_rectangle([x, y, x + w, y + 14], 3, fill=CHIP_BG, outline=LINE)
    d.text((x + 5, y + 2), label, font=f, fill=(70, 62, 48))
    return w


# ---------------------------------------------------------------- scenes
def scene_ship(d, x, y, w, h):
    """Sea, a grey corvette, drone boats and a burst — panel 1."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 228, 240))
    horizon = y + int(h * 0.52)
    d.rectangle([x, horizon, x + w, y + h], fill=SEA)
    for i in range(5):
        yy = horizon + 7 + i * 8
        d.line([x + 8 + (i % 3) * 22, yy, x + 52 + (i % 3) * 22, yy],
               fill=(140, 175, 205), width=2)
    d.ellipse([x + w - 40, y + 7, x + w - 18, y + 29], fill=(244, 200, 90))
    hx, hy = x + int(w * 0.50), horizon - 4
    d.polygon([(hx, hy), (hx + 104, hy), (hx + 90, hy + 12), (hx + 12, hy + 12)],
              fill=(96, 104, 116))
    d.rectangle([hx + 25, hy - 14, hx + 63, hy], fill=(110, 118, 130))
    d.rectangle([hx + 38, hy - 25, hx + 50, hy - 14], fill=(110, 118, 130))
    d.line([hx + 44, hy - 25, hx + 44, hy - 35], fill=(70, 76, 86), width=2)
    for k in range(3):
        bx, by = x + 24 + k * 30, horizon + 14 + (k % 2) * 9
        d.polygon([(bx, by), (bx + 18, by), (bx + 13, by + 5), (bx + 4, by + 5)],
                  fill=(52, 58, 68))
    cx, cy = hx + 4, hy - 8
    for ang in range(0, 360, 30):
        r = 12 if ang % 60 == 0 else 8
        d.line([cx, cy, cx + r * math.cos(math.radians(ang)),
                cy + r * math.sin(math.radians(ang))], fill=(228, 110, 40),
               width=2)
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(240, 150, 50))
    for gx, gy, gr in ((hx + 58, hy - 40, 8), (hx + 74, hy - 47, 11),
                       (hx + 90, hy - 42, 7)):
        d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=(150, 150, 150))


def scene_chip_chart(d, x, y, w, h):
    """A microchip beside a surging line chart — panel 2."""
    d.rectangle([x, y, x + w, y + h], fill=(226, 236, 224))
    cx, cy, s = x + 24, y + int(h * 0.28), 50
    d.rounded_rectangle([cx, cy, cx + s, cy + s], 6, fill=(40, 44, 52))
    d.rounded_rectangle([cx + 12, cy + 12, cx + s - 12, cy + s - 12], 3,
                        outline=(120, 220, 160), width=2)
    for i in range(4):
        px = cx + 8 + i * 12
        d.line([px, cy - 7, px, cy], fill=(40, 44, 52), width=3)
        d.line([px, cy + s, px, cy + s + 7], fill=(40, 44, 52), width=3)
        py = cy + 8 + i * 12
        d.line([cx - 7, py, cx, py], fill=(40, 44, 52), width=3)
        d.line([cx + s, py, cx + s + 7, py], fill=(40, 44, 52), width=3)
    gx, gy = x + 104, y + h - 16
    for i in range(4):
        yy = gy - i * 15
        d.line([gx, yy, x + w - 12, yy], fill=(196, 208, 196), width=1)
    pts = [(gx, gy - 5), (gx + 34, gy - 11), (gx + 62, gy - 9),
           (gx + 92, gy - 27), (gx + 122, gy - 31), (gx + 150, gy - 56)]
    d.line(pts, fill=GREEN, width=3)
    ax, ay = pts[-1]
    d.polygon([(ax, ay), (ax - 11, ay + 1), (ax - 2, ay + 10)], fill=GREEN)
    d.text((gx + 2, y + 6), "+31%", font=SANSB(17), fill=GREEN)


def scene_building(d, x, y, w, h):
    """A shattered apartment block over rubble — panel 3."""
    d.rectangle([x, y, x + w, y + h], fill=(228, 220, 206))
    bx, by, bw, bh = x + 84, y + 10, 104, int(h * 0.76)
    d.rectangle([bx, by, bx + bw, by + bh], fill=(168, 158, 142))
    for r in range(3):
        for c in range(4):
            wx, wy = bx + 9 + c * 24, by + 9 + r * 18
            dark = (r * 4 + c) % 5 == 0
            d.rectangle([wx, wy, wx + 14, wy + 11],
                        fill=(60, 56, 50) if dark else (238, 228, 200))
    d.polygon([(bx + bw - 32, by), (bx + bw, by), (bx + bw, by + 40),
               (bx + bw - 15, by + 27), (bx + bw - 28, by + 36)],
              fill=(228, 220, 206))
    d.polygon([(bx + bw - 32, by + 2), (bx + bw - 2, by + 36),
               (bx + bw - 17, by + 31)], fill=(90, 60, 44))
    for gx, gy, gr in ((bx + 62, by - 3, 9), (bx + 80, by - 10, 13),
                       (bx + 97, by - 5, 8)):
        d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=(150, 144, 130))
    base = by + bh
    for tx, tw, th in ((x + 26, 50, 13), (x + 92, 62, 17), (x + 168, 56, 11),
                       (x + 232, 42, 14)):
        d.polygon([(tx, base + 14), (tx + tw, base + 14),
                   (tx + tw // 2, base + 14 - th)], fill=(128, 118, 102))
    d.line([x + 16, base + 14, x + w - 12, base + 14], fill=(110, 100, 86),
           width=2)
    d.line([x + 26, y + 22, x + 58, y + 22], fill=RED, width=3)
    d.line([x + 42, y + 14, x + 42, y + 30], fill=RED, width=3)


SCENES = {1: scene_ship, 2: scene_chip_chart, 3: scene_building}

# ------------------------------------------------------- dotted world map
LAND = [
    [(-165, 68), (-140, 70), (-120, 71), (-100, 69), (-88, 67), (-80, 62),
     (-72, 58), (-66, 52), (-64, 47), (-70, 43), (-74, 39), (-77, 34),
     (-80, 30), (-81, 25), (-85, 21), (-88, 18), (-91, 15), (-95, 16),
     (-100, 18), (-104, 21), (-108, 25), (-112, 29), (-117, 33), (-122, 37),
     (-124, 43), (-128, 50), (-135, 58), (-152, 61), (-162, 64)],
    [(-92, 15), (-84, 11), (-79, 9), (-82, 8), (-89, 12), (-94, 14)],
    [(-78, 7), (-71, 11), (-64, 10), (-57, 7), (-51, 4), (-50, 0), (-44, -3),
     (-38, -6), (-39, -13), (-40, -20), (-46, -24), (-52, -30), (-57, -36),
     (-62, -40), (-65, -45), (-67, -51), (-69, -54), (-71, -54), (-73, -47),
     (-73, -39), (-71, -30), (-70, -21), (-71, -16), (-76, -11), (-79, -6),
     (-80, -1), (-79, 3)],
    [(-9, 37), (-9, 43), (-2, 44), (-1, 46), (-5, 48), (0, 49), (3, 51),
     (7, 54), (8, 57), (12, 56), (18, 56), (21, 60), (25, 66), (31, 70),
     (42, 67), (52, 65), (60, 62), (66, 65), (60, 58), (50, 53), (42, 50),
     (34, 47), (28, 46), (23, 44), (19, 42), (16, 40), (12, 42), (8, 44),
     (3, 43), (-1, 40), (-3, 37)],
    [(-17, 15), (-16, 21), (-13, 27), (-9, 31), (-6, 35), (0, 36), (10, 37),
     (19, 33), (27, 31), (32, 31), (35, 28), (39, 22), (43, 12), (48, 11),
     (51, 11), (47, 5), (42, -2), (40, -9), (38, -16), (36, -21), (34, -27),
     (29, -31), (24, -34), (19, -34), (16, -29), (14, -23), (13, -16),
     (12, -10), (10, -4), (9, 1), (6, 4), (0, 5), (-7, 5), (-12, 8)],
    [(28, 42), (36, 36), (36, 33), (40, 31), (44, 29), (48, 30), (52, 28),
     (56, 26), (60, 25), (66, 25), (72, 20), (74, 14), (77, 8), (80, 13),
     (84, 18), (88, 22), (91, 22), (93, 17), (96, 15), (98, 11), (100, 7),
     (103, 2), (105, 6), (107, 12), (109, 15), (112, 19), (118, 22),
     (121, 26), (126, 29), (130, 32), (135, 34), (139, 36), (141, 40),
     (142, 45), (149, 48), (156, 51), (162, 56), (170, 60), (178, 65),
     (172, 69), (158, 71), (142, 72), (125, 72), (108, 72), (92, 70),
     (78, 68), (68, 66), (60, 62), (52, 58), (46, 54), (38, 50), (32, 47)],
    [(95, 5), (100, -2), (105, -5), (110, -3), (115, -1), (120, -2),
     (126, -1), (132, -3), (138, -3), (143, -4), (147, -6), (142, -8),
     (136, -6), (130, -5), (124, -4), (118, -4), (112, -6), (106, -7),
     (100, -4), (96, 2)],
    [(113, -22), (114, -29), (116, -34), (122, -34), (129, -32), (134, -33),
     (137, -35), (141, -38), (146, -39), (150, -37), (153, -31), (153, -26),
     (150, -22), (146, -19), (143, -14), (142, -11), (140, -14), (139, -18),
     (136, -15), (135, -12), (131, -11), (127, -13), (123, -16), (119, -19),
     (115, -21)],
    [(167, -45), (172, -41), (175, -38), (177, -38), (174, -41), (169, -46)],
    [(-8, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 55), (-2, 51)],
    [(130, 31), (134, 34), (138, 35), (140, 37), (141, 41), (142, 44),
     (140, 44), (138, 39), (135, 35), (131, 33)],
]


def in_poly(lon, lat, poly):
    inside, n = False, len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > lat) != (y2 > lat):
            xi = x1 + (lat - y1) * (x2 - x1) / (y2 - y1)
            if lon < xi:
                inside = not inside
    return inside


def draw_map(d, x, y, w, h, pins):
    d.rectangle([x, y, x + w, y + h], fill=(250, 246, 233), outline=LINE)
    lon0, lon1, lat0, lat1 = -172, 192, 82, -58

    def px(lon):
        return x + (lon - lon0) / (lon1 - lon0) * w

    def py(lat):
        return y + (lat0 - lat) / (lat0 - lat1) * h

    lat = 80.0
    while lat > -56:
        lon = -170.0
        while lon < 188:
            if any(in_poly(lon, lat, p) for p in LAND):
                d.ellipse([px(lon) - 1, py(lat) - 1, px(lon) + 1, py(lat) + 1],
                          fill=(178, 168, 140))
            lon += 2.6
        lat -= 2.6
    for num, plat, plon in pins:
        cx, cy = px(plon), py(plat)
        d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=RED, outline=PAPER)
        t = str(num)
        tw = d.textlength(t, font=SANSB(10))
        d.text((cx - tw / 2, cy - 6), t, font=SANSB(10), fill=PAPER)


# ------------------------------------------------------------------ main
def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    counts = {}
    for p in PANELS:
        counts[p[5]] = counts.get(p[5], 0) + 1
    order = ["EUROPE", "AMERICAS", "ASIA", "AFRICA", "MIDDLE EAST",
             "OCEANIA", "WORLD"]
    region_bits = " · ".join("%s %d" % (r, counts[r]) for r in order
                             if r in counts)

    # ---- masthead (0..108)
    d.text((M, 8), "ONE DAY OF WORLD NEWS · ONE PICTURE", font=SANSB(12),
           fill=MUTED)
    right = "%d STORIES · %s" % (TOTAL_STORIES, region_bits)
    d.text((W - M - d.textlength(right, font=SANSB(12)), 8), right,
           font=SANSB(12), fill=MUTED)
    d.line([M, 27, W - M, 27], fill=INK, width=2)
    title = "Monday 23 November 2026"
    tf = SERIFB(42)
    d.text(((W - d.textlength(title, font=tf)) / 2, 32), title, font=tf,
           fill=INK)
    d.line([M, 84, W - M, 84], fill=INK, width=1)
    strap = ("Ukraine sinks a Russian corvette off Libya  ·  Nvidia's Huang "
             "returns and markets erupt  ·  COP31 falls, and the argument begins")
    sf = SERIF(13)
    d.text(((W - d.textlength(strap, font=sf)) / 2, 89), strap, font=sf,
           fill=(70, 62, 48))
    d.line([M, 108, W - M, 108], fill=LINE, width=1)

    # ---- timeline (114..150): label, then six slots beside it
    ty = 114
    d.text((M, ty), "THE DAY IN UTC", font=SANSB(11), fill=RED)
    tx0 = M + 116
    sw = (W - M - tx0) / 6
    for i, (t, txt) in enumerate(TIMELINE):
        sx = tx0 + i * sw
        if i:
            d.line([sx - 6, ty, sx - 6, ty + 34], fill=LINE, width=1)
        d.text((sx, ty), t, font=SANSB(12), fill=INK)
        text_block(d, sx, ty + 15, txt, SANS(9), sw - 12, 10.5, fill=MUTED,
                   max_lines=2)

    # ---- hero panels (156..354)
    hy, hh, hg = 156, 198, 10
    hw = (W - 2 * M - 2 * hg) / 3
    for i, p in enumerate(PANELS[:3]):
        num, tag, head, det, ch = p[0], p[1], p[2], p[3], p[4]
        x = M + i * (hw + hg)
        d.rectangle([x, hy, x + hw, hy + hh], fill=PAPER, outline=LINE)
        SCENES[num](d, x + 6, hy + 6, hw - 12, 78)
        d.text((x + 10, hy + 90), "%d  %s" % (num, tag), font=SANSB(10.5),
               fill=RED)
        yy = text_block(d, x + 10, hy + 103, head, SERIFB(15), hw - 20, 17,
                        max_lines=2)
        text_block(d, x + 10, yy + 2, det, SANS(9.5), hw - 20, 11.5,
                   fill=(52, 48, 40), max_lines=3)
        chip(d, x + 10, hy + hh - 20, ch)

    # ---- day in numbers (358..418)
    ny = 358
    d.rectangle([M, ny, W - M, ny + 60], fill=NAVY)
    d.text((M + 12, ny + 4), "THE DAY IN NUMBERS", font=SANSB(9.5),
           fill=(240, 220, 170))
    nw = (W - 2 * M - 24) / 6
    for i, (big, cap) in enumerate(NUMBERS):
        sx = M + 12 + i * nw
        d.text((sx, ny + 15), big, font=SERIFB(20), fill=(255, 250, 235))
        text_block(d, sx, ny + 41, cap, SANS(7.5), nw - 10, 9,
                   fill=(198, 206, 224), max_lines=2)

    # ---- medium panels (424..688): rows of 4, 4, 3
    my, rh, rgap = 424, 84, 6
    med = PANELS[3:]
    rows = [med[0:4], med[4:8], med[8:11]]
    for r, row in enumerate(rows):
        y = my + r * (rh + rgap)
        n = len(row)
        pw = (W - 2 * M - (n - 1) * rgap) / n
        for i, p in enumerate(row):
            num, tag, head, det, ch = p[0], p[1], p[2], p[3], p[4]
            x = M + i * (pw + rgap)
            d.rectangle([x, y, x + pw, y + rh], fill=PAPER, outline=LINE)
            d.text((x + 8, y + 5), "%d  %s" % (num, tag), font=SANSB(9),
                   fill=RED)
            yy = text_block(d, x + 8, y + 17, head, SERIFB(12), pw - 16, 13.5,
                            max_lines=2)
            text_block(d, x + 8, yy + 2, det, SANS(8.5), pw - 16, 10,
                       fill=(52, 48, 40), max_lines=2)
            chip(d, x + 8, y + rh - 17, ch)

    # ---- bottom (692..958): map left, also-on right
    by = 696
    d.line([M, by - 4, W - M, by - 4], fill=LINE, width=1)
    mapw = 452
    d.text((M, by), "WHERE IT HAPPENED", font=SANSB(11.5), fill=RED)
    pins = [(p[0], p[6], p[7]) for p in PANELS]
    draw_map(d, M, by + 18, mapw, 198, pins)
    d.text((M, by + 222), region_bits, font=SANSB(9.5), fill=MUTED)
    text_block(d, M, by + 236,
               "Pins mark the 14 panel stories, numbered as they appear "
               "above.", SANS(9), mapw, 11, fill=MUTED, max_lines=2)

    ax = M + mapw + 18
    aw = W - M - ax
    d.text((ax, by), "ALSO ON MONDAY", font=SANSB(11.5), fill=RED)
    yy = by + 17
    for i, (place, txt) in enumerate(ALSO_ON):
        d.text((ax, yy), "%d." % (15 + i), font=SANSB(9.5), fill=RED)
        yy = text_block(d, ax + 24, yy, place + " — " + txt, SANS(9.5),
                        aw - 24, 11.0, max_lines=1)
        yy += 0.1

    # ---- date check (962..996)
    dy = 962
    d.rectangle([M, dy, W - M, dy + 34], fill=(238, 230, 210), outline=LINE)
    d.text((M + 8, dy + 4), "DATE CHECK", font=SANSB(9.5), fill=RED)
    text_block(d, M + 76, dy + 2, DATE_CHECK_EARLIER, SANS(8.5),
               W - 2 * M - 84, 10, fill=(52, 48, 40), max_lines=2)
    text_block(d, M + 76, dy + 23, DATE_CHECK_FUTURE, SANS(8.5),
               W - 2 * M - 84, 10, fill=(52, 48, 40), max_lines=1)

    # ---- footer (1000..1016)
    d.line([M, 1000, W - M, 1000], fill=INK, width=1)
    foot = ("All stories happened or were first reported on Monday 23 Nov "
            "2026. CONFIRMED = 2+ sources · REPORTED = 1 named source · "
            "CLAIM = one side. Sources: Reuters, AP, BBC, CNN, WSJ, The "
            "Times, Al Jazeera, UN News, FIFA.")
    d.text((M, 1005), foot, font=SANS(8.5), fill=MUTED)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
