"""Render a rotating view of the first four levels with Pillow."""
from math import cos, sin, pi
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
NAVY, TEXT, FAINT = "#142b40", "#eaf1f4", "#a2b3bf"
TEAL, GOLD = "#63d8c7", "#f3bd73"
DEPTH = 4


def position(level, index):
    return ((2 * index + 1) / (2**level) - 1, level / 2 - 1,
            (level % 2) * 0.86 - 0.43)


def project(point, angle):
    x, y, z = point
    u = x*cos(angle) - y*sin(angle)
    v = x*sin(angle) + y*cos(angle)
    return (350 + 172*u, 220 + 62*v - 112*z)


def frame(angle):
    image = Image.new("RGB", (700, 392), NAVY)
    draw = ImageDraw.Draw(image)
    title = ImageFont.load_default(size=22)
    caption = ImageFont.load_default(size=15)
    draw.text((20, 16), "Nested disk addresses and their scale", font=title, fill=TEXT)
    draw.text((20, 49), "Horizontal spread separates addresses; height records the dilation.", font=caption, fill=FAINT)
    for level in range(1, DEPTH+1):
        for idx in range(2**level):
            child = project(position(level, idx), angle)
            parent = project(position(level-1, idx//2), angle)
            draw.line([parent, child], fill="#57728b", width=2)
    for level in range(DEPTH+1):
        for idx in range(2**level):
            x, y = project(position(level, idx), angle)
            color = GOLD if level % 2 else TEAL
            draw.ellipse((x-4,y-4,x+4,y+4), fill=color)
    draw.text((20,363), "Scale 1   |   even levels", font=caption, fill=TEAL)
    draw.text((260,363), "Scale 2   |   odd levels", font=caption, fill=GOLD)
    draw.text((524,363), "Radius not to scale", font=caption, fill=FAINT)
    return image


if __name__ == "__main__":
    frames = [frame(2*pi*i/48) for i in range(48)]
    frames[0].save(ROOT/"construction.gif", save_all=True, append_images=frames[1:],
                   duration=100, loop=0, optimize=True)
