import re
from PIL import Image, ImageDraw
from visual import S, W, H, tracked, centered, font, GREEN, SOFT, INK, WHITE, EYE_TRACK, FOOT_TRACK, f_eye, f_foot
NB = "\u00a0"
def fr(s):
    s = s.replace("'", "’"); s = re.sub(r" ([?!:;»])", NB + r"\1", s); return s.replace("« ", "«" + NB)
LIGHT = (169, 199, 184); PALE = (233, 241, 236)

def wrap(text, f, maxw):
    lines, cur = [], ""
    for w in text.split(" "):
        t = (cur + " " + w).strip()
        if f.getlength(t) / S <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def typo(eyebrow, title, body=None, inverted=False, max_title=118, max_lines=4, body_size=34, maxw=900):
    bg = GREEN if inverted else WHITE
    c_eye, c_title, c_body, c_foot = (LIGHT, WHITE, PALE, LIGHT) if inverted else (SOFT, GREEN, INK, GREEN)
    img = Image.new("RGB", (W*S, H*S), bg); d = ImageDraw.Draw(img)
    title = fr(title)
    size = max_title
    while size > 40:
        ft = font(900, size); tl = title.split("\n") if "\n" in title else wrap(title, ft, maxw)
        if len(tl) <= max_lines and all(ft.getlength(l)/S <= maxw for l in tl): break
        size -= 2
    pitch = size * 1.02
    fb = font(400, body_size); bl = []
    if body:
        for para in body.split("\n"):
            bl += wrap(fr(para), fb, 860)
    bp = body_size * 1.5
    title_h = 0.73*size + (len(tl)-1)*pitch
    body_h = ((len(bl)-1)*bp + 0.73*body_size) if bl else 0
    total = 19 + 56 + title_h + ((64 + body_h) if bl else 0)
    top = 650 - total/2
    y = top + 19
    tracked(d, 540, y, fr(eyebrow), f_eye, c_eye, EYE_TRACK)
    y += 56 + 0.73*size
    for i, l in enumerate(tl): centered(d, 540, y + i*pitch, l, ft, c_title)
    y += (len(tl)-1)*pitch + 64 + 0.73*body_size
    for i, l in enumerate(bl): centered(d, 540, y + i*bp, l, fb, c_body)
    tracked(d, 540, 1277, "BROU PAULIN-XAVIER KADJO  |  CONSEIL EN STRATÉGIE DE MARQUE", f_foot, c_foot, FOOT_TRACK)
    return img.resize((W, H), Image.LANCZOS)

# ---------- gabarit E : Avant / Après (panneaux empilés) ----------
def avant_apres(eyebrow, titre_sec, avant, apres, note):
    img = Image.new("RGB", (W*S, H*S), WHITE); d = ImageDraw.Draw(img)
    tracked(d, 540, 106, fr(eyebrow), f_eye, SOFT, EYE_TRACK)
    centered(d, 540, 205, "AVANT / APRÈS", font(900, 78), GREEN)
    centered(d, 540, 262, fr(titre_sec), font(400, 30), INK)
    fq = font(500, 33); fl = font(600, 21)
    def panel(y0, label, text, fill, outline, c_label):
        lines = wrap(fr(text), fq, 820); h = 36 + 22 + 30 + len(lines)*49 + 36
        d.rounded_rectangle([80*S, y0*S, 1000*S, (y0+h)*S], radius=24*S, fill=fill, outline=outline, width=(3*S if outline else 0))
        tracked(d, 540, y0 + 36 + 18, label, fl, c_label, 4)   # étiquette centrée
        for i, l in enumerate(lines): d.text((120*S, (y0 + 36 + 22 + 30 + 36 + i*49 - 10)*S), l, font=fq, fill=INK, anchor="ls")
        return y0 + h
    y = panel(330, "AVANT", avant, (242,242,239), None, (110,110,102))
    y = panel(y + 36, "APRÈS", apres, WHITE, GREEN, GREEN)
    centered(d, 540, y + 56, fr(note), font(400, 23), (105,105,98))
    tracked(d, 540, 1277, "BROU PAULIN-XAVIER KADJO  |  CONSEIL EN STRATÉGIE DE MARQUE", f_foot, GREEN, FOOT_TRACK)
    return img.resize((W, H), Image.LANCZOS), y + 70
