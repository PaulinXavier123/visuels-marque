from PIL import Image, ImageDraw
import visual as V
from visual import S, W, H, tracked, centered, font, GREEN, SOFT, INK, WHITE, EYE_TRACK, FOOT_TRACK, TITLE_SIZE, BODY_SIZE, f_eye, f_foot

def make_photo(eyebrow, title_lines, sub_lines, photo_path):
    img = Image.new("RGB", (W*S, H*S), WHITE); d = ImageDraw.Draw(img)
    tracked(d, 540, 106, eyebrow, f_eye, SOFT, EYE_TRACK)
    f_t = font(900, TITLE_SIZE); pitch = TITLE_SIZE*1.01
    b = 240
    for i,t in enumerate(title_lines): centered(d, 540, b + i*pitch, t, f_t, GREEN)
    last = b + (len(title_lines)-1)*pitch
    f_n = font(600, BODY_SIZE); f_b = font(400, BODY_SIZE)
    y = last + 72
    for i,(t,wt) in enumerate(sub_lines):
        centered(d, 540, y + i*46, t, f_n if wt=="n" else f_b, INK)
    y_end = y + (len(sub_lines)-1)*46
    tracked(d, 540, 1277, "BROU PAULIN-XAVIER KADJO  |  CONSEIL EN STRATÉGIE DE MARQUE", f_foot, GREEN, FOOT_TRACK)
    base = img.resize((W, H), Image.LANCZOS)
    px0, px1, py0, py1 = 80, 1000, int(y_end + 62), 1220
    w, h = px1-px0, py1-py0
    ph = Image.open(photo_path).convert("RGB")
    cw = round(ph.height * w / h)
    ph = ph.crop((0, 0, cw, ph.height)).resize((w, h), Image.LANCZOS)
    m = Image.new("L", (w*4, h*4), 0)
    ImageDraw.Draw(m).rounded_rectangle([0,0,w*4-1,h*4-1], radius=24*4, fill=255)
    m = m.resize((w, h), Image.LANCZOS)
    base.paste(ph, (px0, py0), m)
    return base, (px0, py0, px1, py1, cw)

if __name__ == "__main__":
    im, info = make_photo("PRÉSENTATION", ["UNE MARQUE SE","CONSTRUIT PAR","DES DÉCISIONS."],
        [("Brou Paulin-Xavier KADJO","n"),("Conseil en stratégie de marque et communication","r")],
        "/mnt/user-data/uploads/1001021046.jpg")
    im.save("/mnt/user-data/outputs/J1_LinkedIn_visuel_final.png", optimize=True)
    print("cadre", info, im.size)
