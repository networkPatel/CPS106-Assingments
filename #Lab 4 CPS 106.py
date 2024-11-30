#Lab 4 CPS 106
from PIL import Image
image1 = Image.open(r"images.jfif")
#image.show()
#1. what is luminance? the brightness of a color
#2. Why is the maximum value for any color component 255? 8 bits is 1 byte 0-255 represents the 256 magnitude
#3. The color encoding we’re using is RGB. What does this mean, in terms of the amount of memory required to represent color? Is there a limit to the number of colors that we can represent? Are there enough colors representable in RGB?
#RPG file is RBG-24 bit file as JPG is already a pretty compressed file the RAM is used efficiently 256^3 different colors you could select from
#4. 

#write a function decreaseRed that decreases the red by 20%
# def decreaseRed(image):
#     w, h = image.size
#     map = image.load()
#     for x in range(w):
#         for y in range(h):
#             r, g, b = map[x, y]
#             r = int(r * 0.8)
#             map[x, y] = (r, g, b)
#     pass

#decrease blue by 10%
# def decreaseRed(image):
#     w, h = image.size
#     map = image.load()
#     for x in range(w):
#         for y in range(h):
#             r, g, b = map[x, y]
#             b = int(b*0.9)
#             map[x, y] = (r, g, b)
#     pass

#Write a function to swap the values of two colors, for example, swap the red value with the blue value
# def swapColours(image):
#     w, h = image.size
#     map = image.load()
#     for x in range(w):
#         for y in range(h):
#             r, g, b = map[x, y]
#             map[x,y] = (g,r,b)
#     pass

#write a function to set the red, green and blue values to 0
def setToZero(image):
    w, h = image.size
    map = image.load()
    for x in range(w):
        for y in range(h):
            (r, g, b) = map[x, y]
            map[x,y] = (0,0,0)
    pass

#write a function to set the red, green and blue values to 255
# def setToMax(image):
#     w, h = image.size
#     map = image.load()
#     for x in range(w):
#         for y in range(h):
#             r, g, b = map[x, y]
#             map[x,y] = (255,255,255)
#     pass

#4.9 set's the red value to 30% of original value
#4.12 increases the red, green and blue values by 10
#4.13 decreases the red, green and blue values by 20
#4.14 switches the red and blue values
#4.15 integer divides the rgb value by half
#4.16 integer divides the rgb value by a third
#4.17 sets the rgb value to double that it is

setToZero(image1)
image1.show()