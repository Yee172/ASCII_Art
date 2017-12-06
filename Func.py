#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/10/13'


from PIL import Image, ImageChops  
from PIL.GifImagePlugin import getheader, getdata
import argparse


TOPNG = 1

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=60)
parser.add_argument('--height', type=int, default=60)
args = parser.parse_args()
IMG = args.file
WIDTH = int(args.width * 1.8)
HEIGHT = int(args.height * 1)
if TOPNG:
    if args.output[-4] is not '.':
        OUTPUT = args.output + '.dot'
    elif args.output[-4:] == '.txt':
        OUTPUT = args.output[:-4] + '.dot'
    elif args.output[-4:] == '.dot':
        OUTPUT = args.output
    else:
        OUTPUT = args.output
else:
    OUTPUT = args.output


ascii_char = list('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI         ')
# █▓
# $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.
# BUN ███████████████████████████████████▓████████████████████████#██      

def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 257 / length
    return ascii_char[int(gray / unit)]


im = Image.open(IMG)
im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

txt = ''

for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j, i)))
    txt += '\n'

print(txt)

if OUTPUT:
    with open(OUTPUT, 'w') as f:
        if TOPNG:
            f.write('graph{node [shape=box, color=white, fontname="Menlo Regular"]"\n')
        f.write(txt)
        if TOPNG:
            f.write('"}\n')
