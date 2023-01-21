from PIL import Image
import colorsys
import math

cx = 0.7885
cy = 0
R = (1 + (1 + 4 * (cx ** 2 + cy ** 2) ** 0.5) ** 0.5) / 2 + 0.001
max_iteration = 200

w, h, zoom = 1000, 1000, 1


def julia(cx, cy, R, max_iteration, x, y, minx, maxx, miny, maxy):
    zx = (x - minx) / (maxx - minx) * 2 * R - R
    zy = (y - miny) / (maxy - miny) * 2 * R - R
    i = 0
    while zx ** 2 + zy ** 2 < R ** 2 and i < max_iteration:
        temp = zx ** 2 - zy ** 2
        zy = 2 * zx * zy + cy
        zx = temp + cx
        i += 1
    return i


def gen_julia_image(sequence, cx, cy):
    bitmap = Image.new("RGB", (w, h), "white")
    pix = bitmap.load()
    for x in range(w):
        for y in range(h):
            c = julia(cx, cy, R, max_iteration, x, y, 0, w - 1, 0, h - 1)
            r, g, b = colorsys.hsv_to_rgb(c / max_iteration, 1, 0.9)
            r = min(255, round(r * 255))
            g = min(255, round(g * 255))
            b = min(255, round(b * 255))
            pix[x, y] = int(b) + (int(g) << 8) + (int(r) << 16)
    bitmap.save(f"./data/julia_{sequence}.jpg")


for i in range(360):
    cx = 0.7885 * math.cos(i * math.pi / 180)
    cy = 0.7885 * math.sin(i * math.pi / 180)
    gen_julia_image(i, cx, cy)
