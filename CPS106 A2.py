from PIL import *
from PIL import Image
from math import sqrt
#move program to same directory as images or it won't work

#creating image objects
#canvas to paste images to
canvas = Image.new("RGB", (500,500), (0,0,0))
caterpillar = Image.open("caterpillar.jpg")
horse = Image.open("horse.jpg")
temple = Image.open("temple.jpg")

#created function to seperate file into 4 borders
def split4(canvas: Image, color: tuple):
    w,h = canvas.size
    map = canvas.load()
    #splitting canvas into 4 equal parts
    for x in range(w):
        for y in range(h):
            if x == h//2 or y == w//2:
                map[x,y] = color

#created function which copies the input x and y of the image given onto the canvas
def openCropAndPaste(image: Image, canvas: Image, x1:int, x2:int, y1:int, y2:int, shiftx: int, shifty:int, output: str):
    #loaded image map
    map = image.load()
    #loaded canvas map
    canvasMap = canvas.load()

    #nested for loop to run through the parts of the image input
    for x in range(x1,x2 + 1):
        for y in range(y1,y2 + 1):
            #the pixel value given by map[x,y] is input into the canvas map with the shift value given
            canvasMap[x + shiftx,y + shifty] = map[x,y]

    #to save image if we want to save the output
    if output != "":
        canvas.save(output)

#created function to mirror image vertically
def mirrorVertical(image: Image, canvas: Image, x1:int, x2:int, y1:int, y2:int, shiftx:int, shifty:int):
    #loaded map and size
    map = image.load()
    w, h = image.size
    canvasMap = canvas.load()
    #nested for loop to run through the image
    for x in range(x1,x2):
        for y in range(y1,y2 + 1):
            #the map at width - 1 - x will give us the values starting from the right side of the image and will run to the left
            #this value is then put on canvasMap along with the shift
            canvasMap[x + shiftx,y + shifty] = map[ w - 1 - x,y]

#created function for mirroring image horizontally
def mirrorHorizontal(image: Image, canvas: Image, x1:int, x2:int, y1:int, y2:int, shiftx:int, shifty:int):
    #loaded maps and size
    map = image.load()
    w,h = image.size
    canvasMap = canvas.load()

    #nested for loop to run through the image with the given inputs
    for x in range(x1,x2):
        for y in range(y1, y2):
            #the y subtracted by the height - 1 is the map[x,y] from the bottom of the image
            #this map[x,y] value is then put on the canvas with the shift value
            canvasMap[x + shiftx,y + shifty] = map[x,h - 1 - y]
    pass

#distance between two colors function which returns an int value
def distance(color1:tuple, color2:tuple) -> int:
    r1,g1,b1 = color1
    r2,g2,b2 = color2
    return sqrt(((r2 - r1)**2 + (g2 - g1)**2 +(b2-b1)**2))

#created function for substituting the color that is given by another color given at the x and y values given
#this substituted image is then cropped and put on the canvas along with the shift
def backgroundSubstitution(image: Image, canvas: Image, substitute: tuple, substituteTo: tuple, x1:int, x2:int, y1:int, y2:int, shiftx:int, shifty:int):
    #loaded maps
    map = image.load()
    canvas = canvas.load()

    #nested for loop to go through the image with the given values
    for x in range(x1,x2):
        for y in range(y1,y2):
            #if the distance between the current pixel and the pixel we are looking for is less than 50 then replace the pixel with the one given by input
            if distance(map[x,y],substitute) < 50:
                canvas[x + shiftx,y + shifty] = substituteTo

            #if the distance between the current pixel and the one we are searching for is less than 50 then paste that pixel without any modifications to it onto the canvas
            else:
                canvas[x + shiftx, y + shifty] = map[x,y]
    
    pass

#creating function for greyscaleing
def greyscale(image: Image, canvas:Image, x1:int, x2:int, y1:int, y2:int, shiftx:int,shifty:int):
    #loaded map and size
    map = image.load()
    w,h = image.size
    canvasMap = canvas.load()
    #nested for loop to iterate through image
    for x in range(x1,x2):
        for y in range(y1,y2):
            #the greyscale value is calculated by taking the average of the RGB values and then rounding it
            r,g,b = map[x,y]
            grey = int((r + g + b) / 3)
            canvasMap[x + shiftx,y + shifty] = (grey,grey,grey)

def blur(image: Image, canvas: Image, x1: int, x2: int, y1: int, y2: int, shiftx: int, shifty: int):
    # Loaded map and size
    map = image.load()
    w, h = image.size
    canvasMap = canvas.load()
    cw, ch = canvas.size
    
    # Nested for loop to iterate through the specified region of the image
    for x in range(x1, x2):
        for y in range(y1, y2):
            total_r, total_g, total_b = 0, 0, 0
            count = 0
            
            # Iterating through neighboring pixels (3x3)
            for dx in range(-1, 2):  # -1, 0, 1
                for dy in range(-1, 2):  # -1, 0, 1
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        #adding all components of the pixels around to find the average after
                        r, g, b = map[nx, ny]
                        total_r += r
                        total_g += g
                        total_b += b
                        count += 1
            
            # Calculating the average color
            if count > 0:  # Avoid division by zero
                avgR = total_r // count
                avgG = total_g // count
                avgB = total_b // count

                # Set the blurred pixel on the canvas with shift
                canvas_x = x + shiftx
                canvas_y = y + shifty

                #checking if within canvas
                if 0 <= canvas_x < cw and 0 <= canvas_y < ch:
                    canvasMap[canvas_x, canvas_y] = (avgR, avgG, avgB)

#calling functions to create canvas
split4(canvas, (255,255,255))
openCropAndPaste(caterpillar, canvas, 0, 250, 0, 100, 0, 0, "")
backgroundSubstitution(caterpillar,canvas,(0,255,0), (0,0,0), 0,250,0,150, 0,99 )
mirrorVertical(horse, canvas, 50, 290, 200, 325, 201, -200)
mirrorHorizontal(horse, canvas, 50, 290, 200, 325, 205, -75)
greyscale(horse,canvas, 0, 249, 0, 100, 0,255)
greyscale(temple, canvas, 100,350,50,199,-100,300)
blur(caterpillar, canvas, 0, 300, 0, 150, 251, 251)
blur(horse, canvas, 150, 400, 100, 250, 100, 250)

#to show the canvas after all modifications are done
canvas.show()
#saving image as output.jpg file
canvas.save("output.jpg")