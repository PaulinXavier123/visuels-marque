from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
FD = "/home/claude/viz/fonts/Inter-%d.ttf"
GREEN=(12,72,48); SOFT=(76,124,104); INK=(36,36,36); WHITE=(255,255,255)
S = 2
W, H = 1080, 1350

def font(w, size): return ImageFont.truetype(FD % w, int(round(size*S)))
def fit(weight, text, target, lo=8, hi=220):
    for _ in range(40):
        mid = (lo+hi)/2
        if ImageFont.truetype(FD % weight, int(round(mid*S))).getlength(text)/S < target: lo = mid
        else: hi = mid
    return (lo+hi)/2

# --- calibrage sur le visuel de référence (largeurs mesurées en px à 1080) ---
TITLE_SIZE = fit(900, "UN BON PRODUIT", 784)
BODY_SIZE  = fit(400, "Si votre client ne comprend pas pourquoi vous choisir, il", 785)
EYE_SIZE = 26
f_eye = font(400, EYE_SIZE)
eye_ref = "STRATÉGIE DE MARQUE"
EYE_TRACK = (306 - f_eye.getlength(eye_ref)/S) / (len(eye_ref)-1)
FOOT_SIZE = 19
f_foot = font(500, FOOT_SIZE)
foot_ref = "PAULIN-XAVIER KADJO  |  CONSEIL EN STRATÉGIE DE MARQUE"
FOOT_TRACK = (587 - f_foot.getlength(foot_ref)/S) / (len(foot_ref)-1)

def tracked(d, cx, base, text, f, fill, track):
    adv = [f.getlength(c) for c in text]
    total = sum(adv) + track*S*(len(text)-1)
    x = cx*S - total/2
    for c,a in zip(text, adv):
        d.text((x, base*S), c, font=f, fill=fill, anchor="ls"); x += a + track*S
def centered(d, cx, base, text, f, fill):
    d.text((cx*S, base*S), text, font=f, fill=fill, anchor="ms")

def make(eyebrow, title_lines, sub_lines, label, label2):
    img = Image.new("RGB", (W*S, H*S), WHITE); d = ImageDraw.Draw(img)
    tracked(d, 540, 106, eyebrow, f_eye, SOFT, EYE_TRACK)
    f_t = font(900, TITLE_SIZE); pitch = TITLE_SIZE*1.01
    widths = [f_t.getlength(t)/S for t in title_lines]
    assert max(widths) <= 920, widths
    b = 240
    for i,t in enumerate(title_lines): centered(d, 540, b + i*pitch, t, f_t, GREEN)
    last = b + (len(title_lines)-1)*pitch
    f_n = font(600, BODY_SIZE); f_b = font(400, BODY_SIZE)
    y = last + 72
    for i,(t,wt) in enumerate(sub_lines):
        centered(d, 540, y + i*46, t, f_n if wt=="n" else f_b, INK)
    y_end = y + (len(sub_lines)-1)*46
    # --- cadre photo (emplacement du portrait) ---
    px0, px1 = 80, 1000
    py0 = int(y_end + 62); py1 = 1220
    pw, ph = (px1-px0)*S, (py1-py0)*S
    ph_img = Image.new("RGB", (pw, ph))
    g = ImageDraw.Draw(ph_img)
    for yy in range(ph):
        t = yy/ph; c = tuple(int(a+(b2-a)*t) for a,b2 in zip((240,236,227),(221,214,200)))
        g.line([(0,yy),(pw,yy)], fill=c)
    glow = Image.new("RGB", (pw, ph), (0,0,0)); gd = ImageDraw.Draw(glow)
    gd.ellipse([-pw*0.2, -ph*0.3, pw*0.55, ph*0.7], fill=(40,38,32))
    glow = glow.filter(ImageFilter.GaussianBlur(120*S/2))
    ph_img = Image.fromarray(__import__("numpy").clip(__import__("numpy").asarray(ph_img).astype(int)+__import__("numpy").asarray(glow).astype(int)//4, 0, 255).astype("uint8"))
    g = ImageDraw.Draw(ph_img)
    cx = pw*0.5; head_r = ph*0.14
    sil = (203,195,178)
    g.ellipse([cx-head_r, ph*0.2, cx+head_r, ph*0.2+2*head_r], fill=sil)
    g.ellipse([cx-ph*0.36, ph*0.2+2*head_r+ph*0.05, cx+ph*0.36, ph*1.25], fill=sil)
    mask = Image.new("L", (pw, ph), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0,0,pw-1,ph-1], radius=24*S, fill=255)
    img.paste(ph_img, (px0*S, py0*S), mask)
    # pastille d'indication
    d = ImageDraw.Draw(img)
    f_l = font(600, 20); f_l2 = font(400, 18)
    wl = sum(f_l.getlength(c) for c in label) + 3*S*(len(label)-1)
    bw, bh = int(max(wl, f_l2.getlength(label2))/S + 56), 84
    bx0 = 540 - bw/2; by0 = py1 - 36 - bh
    ov = Image.new("RGBA", img.size, (0,0,0,0)); od = ImageDraw.Draw(ov)
    od.rounded_rectangle([bx0*S, by0*S, (bx0+bw)*S, (by0+bh)*S], radius=16*S, fill=(255,255,255,235))
    img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB"); d = ImageDraw.Draw(img)
    tracked(d, 540, by0+34, label, f_l, SOFT, 3)
    centered(d, 540, by0+62, label2, f_l2, (95,95,88))
    tracked(d, 540, 1277, "BROU PAULIN-XAVIER KADJO  |  CONSEIL EN STRATÉGIE DE MARQUE", f_foot, GREEN, FOOT_TRACK)
    return img.resize((W, H), Image.LANCZOS)

if __name__ == "__main__":
    print("calibrage:", round(TITLE_SIZE,1), round(BODY_SIZE,1), round(EYE_TRACK,2), round(FOOT_TRACK,2))
    im = make("PRÉSENTATION",
              ["UNE MARQUE SE", "CONSTRUIT PAR", "DES DÉCISIONS."],
              [("Brou Paulin-Xavier KADJO","n"), ("Conseil en stratégie de marque et communication","r")],
              "PORTRAIT RÉEL À INSÉRER",
              "Photo de Brou Paulin-Xavier KADJO · lumière naturelle, fond clair")
    im.save("/mnt/user-data/outputs/J1_LinkedIn_visuel_test.png", optimize=True)
    print("ok", im.size)
