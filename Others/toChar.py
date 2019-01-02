from PIL import ImageGrab
import os

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
WIDTH = 600
HEIGHT = 160

def get_char(pix):
    length = len(ascii_char)
    unit = (256 + 1) / length
    return ascii_char[int(pix/unit)]

while True:
    im = ImageGrab.grab(bbox=(10, 310, 670, 810))
    im = im.resize((WIDTH, HEIGHT)).convert('L')
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(im.getpixel((j, i)))
        txt += '\n'
    os.system('cls')
    print(txt)
