"""Système de design de la marque : icônes, illustrations, gabarits à icônes (rendu PIL, suréchantillonné x2)."""
import math
from PIL import Image, ImageDraw
from visual import S, W, H, tracked, centered, font, GREEN, SOFT, INK, WHITE, EYE_TRACK, FOOT_TRACK, f_eye, f_foot
from render import fr, wrap, LIGHT, PALE

# ---------------------------------------------------------------- géométrie
def _bez(p0, p1, p2, n=8):
    return [((1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0], (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]) for t in [i/n for i in range(n+1)]]
def rounded_poly(pts, r, closed=True):
    if r <= 0: return list(pts) + ([pts[0]] if closed else [])
    n = len(pts); out = []
    for i in range(n):
        if not closed and i in (0, n-1): out.append(pts[i]); continue
        p0, p1, p2 = pts[i-1], pts[i], pts[(i+1) % n]
        l1 = math.dist(p0, p1); l2 = math.dist(p1, p2); rr = min(r, l1/2, l2/2)
        a = (p1[0]+(p0[0]-p1[0])/l1*rr, p1[1]+(p0[1]-p1[1])/l1*rr)
        b = (p1[0]+(p2[0]-p1[0])/l2*rr, p1[1]+(p2[1]-p1[1])/l2*rr)
        out += _bez(a, p1, b)
    return out + ([out[0]] if closed else [])
def _eye():
    top = [(2+20*t, 12-6.6*math.sin(math.pi*t)**0.85) for t in [i/20 for i in range(21)]]
    bot = [(2+20*t, 12+6.6*math.sin(math.pi*t)**0.85) for t in [i/20 for i in range(20, -1, -1)]]
    return top + bot
def _user():
    return [(12-7.5*math.cos(t), 21-6.5*math.sin(t)) for t in [math.pi*i/16 for i in range(17)]]

# ---------------------------------------------------------------- icônes (grille 24, style trait arrondi)
ICONS = {
 "eye":     [("curve", _eye(), False), ("circle", 12, 12, 3.2)],
 "check":   [("circle", 12, 12, 9.5), ("curve", [(7.8,12.4),(10.8,15.4),(16.4,9.4)], False)],
 "target":  [("circle", 12, 12, 9.5), ("circle", 12, 12, 5.5), ("disc", 12, 12, 1.7)],
 "bubble":  [("poly", [(3,4),(21,4),(21,16),(13,16),(8.5,20.5),(8.5,16),(3,16)], True, 2.6)],
 "clock":   [("circle", 12, 12, 9.5), ("poly", [(12,6.5),(12,12),(15.8,14.2)], False, 0)],
 "layers":  [("poly", [(12,3),(22,8.5),(12,14),(2,8.5)], True, 0.8), ("poly", [(2,12.5),(12,18),(22,12.5)], False, 0), ("poly", [(2,16.5),(12,22),(22,16.5)], False, 0)],
 "search":  [("circle", 10.5, 10.5, 6.8), ("poly", [(15.5,15.5),(21,21)], False, 0)],
 "user":    [("circle", 12, 8, 3.9), ("curve", _user(), False)],
 "arrow":   [("poly", [(3.5,12),(20,12)], False, 0), ("poly", [(13.5,5.5),(20,12),(13.5,18.5)], False, 0)],
 "x":       [("poly", [(6,6),(18,18)], False, 0), ("poly", [(18,6),(6,18)], False, 0)],
 "pencil":  [("poly", [(16.5,3.5),(20.5,7.5),(8,20),(3.5,20.5),(4,16)], True, 0.6), ("poly", [(14,6),(18,10)], False, 0)],
 "mark":    [("poly", [(3.5,3.5),(20.5,3.5),(20.5,20.5),(3.5,20.5)], True, 4), ("circle", 12, 12, 4)],
 "sparkle": [("poly", [(12,2.5),(14,10),(21.5,12),(14,14),(12,21.5),(10,14),(2.5,12),(10,10)], True, 1.2)],
}
def icon(d, name, cx, cy, size, color, sw=1.9):
    k = size*S/24.0; ox = cx*S - 12*k; oy = cy*S - 12*k; lw = max(2, int(round(sw*k)))
    P = lambda x, y: (ox+x*k, oy+y*k)
    def dots(pp):
        for p in pp: d.ellipse([p[0]-lw/2, p[1]-lw/2, p[0]+lw/2, p[1]+lw/2], fill=color)
    for prim in ICONS[name]:
        t = prim[0]
        if t == "circle":
            _, x, y, r = prim; d.ellipse([*P(x-r, y-r), *P(x+r, y+r)], outline=color, width=lw)
        elif t == "disc":
            _, x, y, r = prim; d.ellipse([*P(x-r, y-r), *P(x+r, y+r)], fill=color)
        elif t == "poly":
            _, pts, closed, rad = prim; pp = [P(*p) for p in rounded_poly(pts, rad, closed)]
            d.line(pp, fill=color, width=lw, joint="curve"); dots(pp)
        elif t == "curve":
            _, pts, closed = prim; pp = [P(*p) for p in pts]
            if closed: pp.append(pp[0])
            d.line(pp, fill=color, width=lw, joint="curve"); dots(pp)

def disc(d, cx, cy, diam, fill, outline=None, width=0):
    r = diam/2*S; d.ellipse([cx*S-r, cy*S-r, cx*S+r, cy*S+r], fill=fill, outline=outline, width=width*S)
def badge(d, cx, cy, diam, name, fill, ic_color, sw=1.9, ratio=0.5):
    disc(d, cx, cy, diam, fill); icon(d, name, cx, cy, diam*ratio, ic_color, sw)

# ---------------------------------------------------------------- base commune
def _palette(inv):
    return dict(bg=GREEN if inv else WHITE, eye=LIGHT if inv else SOFT, title=WHITE if inv else GREEN,
                body=PALE if inv else INK, foot=LIGHT if inv else GREEN,
                soft_fill=(24,94,66) if inv else (233,241,236), soft_ic=LIGHT if inv else SOFT,
                strong_fill=WHITE if inv else GREEN, strong_ic=GREEN if inv else WHITE)
def _title(d, lines, max_size, maxw, y_top, color):
    lines = [fr(l) for l in lines]; size = max_size
    while size > 40:
        ft = font(900, size)
        if all(ft.getlength(l)/S <= maxw for l in lines): break
        size -= 2
    pitch = size*1.02; y = y_top + 0.73*size
    for i, l in enumerate(lines): centered(d, 540, y + i*pitch, l, ft, color)
    return y + (len(lines)-1)*pitch, size
def _footer(d, c):
    tracked(d, 540, 1277, "BROU PAULIN-XAVIER KADJO  |  CONSEIL EN STRATÉGIE DE MARQUE", f_foot, c, FOOT_TRACK)
def _body(d, text, y, color, size=34, maxw=860, pitch=1.5):
    fb = font(400, size); lines = []
    for para in text.split("\n"): lines += wrap(fr(para), fb, maxw)
    for i, l in enumerate(lines): centered(d, 540, y + i*size*pitch, l, fb, color)
    return y + (len(lines)-1)*size*pitch
def _new(inv):
    p = _palette(inv); img = Image.new("RGB", (W*S, H*S), p["bg"]); return img, ImageDraw.Draw(img), p

# ---------------------------------------------------------------- gabarit « scène » : deux notions face à face
def scene(eyebrow, title, left, right, body=None, inverted=False, max_title=104):
    """left/right = (icône, légende)."""
    img, d, p = _new(inverted)
    tracked(d, 540, 106, fr(eyebrow), f_eye, p["eye"], EYE_TRACK)
    base, size = _title(d, title.split("\n"), max_title, 900, 160, p["title"])
    cy = base + 70 + 150
    badge(d, 270, cy, 300, left[0], p["soft_fill"], p["soft_ic"], 1.7, 0.46)
    badge(d, 810, cy, 300, right[0], p["strong_fill"], p["strong_ic"], 1.9, 0.46)
    icon(d, "arrow", 540, cy, 76, p["eye"], 1.9)
    fl = font(600, 27)
    tracked(d, 270, cy + 150 + 58, fr(left[1]), fl, p["eye"], 4)
    tracked(d, 810, cy + 150 + 58, fr(right[1]), fl, p["title"], 4)
    if body: _body(d, body, cy + 150 + 150, p["body"], 34)
    _footer(d, p["foot"]); return img.resize((W, H), Image.LANCZOS)

# ---------------------------------------------------------------- gabarit « liste à icônes »
def icon_list(eyebrow, title, rows, inverted=False, max_title=96):
    img, d, p = _new(inverted)
    tracked(d, 540, 106, fr(eyebrow), f_eye, p["eye"], EYE_TRACK)
    base, size = _title(d, title.split("\n"), max_title, 900, 160, p["title"])
    y = base + 110; fl = font(600, 40)
    for i, (ic, label) in enumerate(rows):
        cy = y + i*150
        badge(d, 190, cy, 104, ic, p["soft_fill"] if i % 2 == 0 else p["strong_fill"], p["soft_ic"] if i % 2 == 0 else p["strong_ic"], 1.9, 0.5)
        d.text((270*S, (cy + 14)*S), fr(label), font=fl, fill=p["body"], anchor="ls")
    _footer(d, p["foot"]); return img.resize((W, H), Image.LANCZOS)

# ---------------------------------------------------------------- gabarit « couverture à icône »
def cover_icon(eyebrow, title, name, body=None, inverted=False, max_title=100, body_size=36):
    img, d, p = _new(inverted)
    lines = title.split("\n"); size = max_title
    while size > 40:
        ft = font(900, size)
        if all(ft.getlength(fr(l))/S <= 900 for l in lines): break
        size -= 2
    pitch = size*1.02; title_h = 0.73*size + (len(lines)-1)*pitch
    nb = len(_wrap_count(body, body_size)) if body else 0
    total = 200 + 64 + 19 + 56 + title_h + ((64 + (nb-1)*body_size*1.5 + 0.73*body_size) if body else 0)
    top = 640 - total/2
    badge(d, 540, top + 100, 200, name, p["strong_fill"], p["strong_ic"], 1.9, 0.5)
    y = top + 200 + 64 + 19
    tracked(d, 540, y, fr(eyebrow), f_eye, p["eye"], EYE_TRACK)
    base, _ = _title(d, lines, size, 900, y + 56, p["title"])
    if body: _body(d, body, base + 64 + 0.73*body_size, p["body"], body_size)
    _footer(d, p["foot"]); return img.resize((W, H), Image.LANCZOS)
def _wrap_count(text, size):
    fb = font(400, size); out = []
    for para in text.split("\n"): out += wrap(fr(para), fb, 860)
    return out

# ---------------------------------------------------------------- v2 : composition centrée verticalement
def _fit(lines, max_size, maxw=900):
    size = max_size
    while size > 40:
        ft = font(900, size)
        if all(ft.getlength(fr(l))/S <= maxw for l in lines): break
        size -= 2
    return size
def scene(eyebrow, title, left, right, body=None, inverted=False, max_title=104, diam=320):
    img, d, p = _new(inverted); lines = title.split("\n"); size = _fit(lines, max_title)
    title_h = 0.73*size + (len(lines)-1)*size*1.02
    nb = len(_wrap_count(body, 34)) if body else 0; body_h = ((nb-1)*34*1.5 + 0.73*34) if body else 0
    total = 19 + 56 + title_h + 70 + diam + 64 + ((80 + body_h) if body else 0)
    top = 650 - total/2
    tracked(d, 540, top + 19, fr(eyebrow), f_eye, p["eye"], EYE_TRACK)
    base, _ = _title(d, lines, size, 900, top + 19 + 56, p["title"])
    cy = base + 70 + diam/2
    badge(d, 270, cy, diam, left[0], p["soft_fill"], p["soft_ic"], 1.7, 0.46)
    badge(d, 810, cy, diam, right[0], p["strong_fill"], p["strong_ic"], 1.9, 0.46)
    icon(d, "arrow", 540, cy, 80, p["eye"], 1.9)
    fl = font(600, 28)
    tracked(d, 270, cy + diam/2 + 56, fr(left[1]), fl, p["eye"], 4)
    tracked(d, 810, cy + diam/2 + 56, fr(right[1]), fl, p["title"], 4)
    if body: _body(d, body, cy + diam/2 + 56 + 90, p["body"], 34)
    _footer(d, p["foot"]); return img.resize((W, H), Image.LANCZOS)
def icon_list(eyebrow, title, rows, inverted=False, max_title=96):
    img, d, p = _new(inverted); lines = title.split("\n"); size = _fit(lines, max_title)
    title_h = 0.73*size + (len(lines)-1)*size*1.02
    total = 19 + 56 + title_h + 96 + (len(rows)-1)*150 + 112
    top = 650 - total/2
    tracked(d, 540, top + 19, fr(eyebrow), f_eye, p["eye"], EYE_TRACK)
    base, _ = _title(d, lines, size, 900, top + 19 + 56, p["title"])
    y = base + 96 + 56; fl = font(600, 40)
    for i, (ic, label) in enumerate(rows):
        cy = y + i*150; soft = (i % 2 == 0)
        badge(d, 190, cy, 112, ic, p["soft_fill"] if soft else p["strong_fill"], p["soft_ic"] if soft else p["strong_ic"], 1.9, 0.5)
        d.text((276*S, (cy + 14)*S), fr(label), font=fl, fill=p["body"], anchor="ls")
    _footer(d, p["foot"]); return img.resize((W, H), Image.LANCZOS)
