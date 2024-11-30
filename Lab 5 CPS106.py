#Lab 5: Chapter 4 problems from guzdial and Ericson
#using nested loops to modify images

from PIL import *
from PIL import Image

def blue_to_white(image):
    w,h = image.size()
    map = image.load

    for x in range(w):
        for y in range(h):
            r,g,b = map[x,y]
            if b > 150:
                map[x,y] = (255,255,255)
    image.show()
    pass

def increase_blue(image):
    w,h = image.size()
    map = image.load

    for x in range(w):
        for y in range(h):
            r,g,b = map[x,y]
            map[x,y] = (r/2,g/2,b*2)
    image.show()
    pass


def increase_red(image):
    w,h = image.size()
    map = image.load

    for x in range(w):
        for y in range(h):
            r,g,b = map[x,y]
            map[x,y] = (r*2,b/2,g/2)
    image.show()
    pass

#not finished
def grey_negate(image):
    w,h = image.size()
    map = image.load
    grayscaleImage = image.convert("L")
    image.show()

    for x in range(w):
        for y in range(h):
            r,g,b = map[x,y]
            lum = int((r+g+b)/3)
            lum = 255- lum
            map[x,y] = (lum,lum,lum)
    image.show()
    pass

#not finished
def lighten_grey(image):
    w,h = image.size()
    map = image.load

    for x in range(w):
        for y in range(h):
            r,g,b = map[x,y]
            lum = int((r+g+b)/3)
            lum += 75
            map[x,y] = (lum,lum,lum)
    image.show()
    pass


def top_black(image):
    w,h = image.size()
    map = image.load

    for x in range(w):
        for y in range(h//2):
            map[x,y] = (0,0,0)
    image.show()
    pass

def bottom_to_top(image):
    w,h = image.size()
    map = image.load

    for x in range(w):
        for y in range(h//2,h):
            (r,g,b) = map[x,y]

            for i in range(h//2):
                map[x,i] = (r,g,b)
    image.show()
    pass