#importing modules
import PIL
from PIL import Image


#making the function with the required parameters
def makeSquare(image, sidelength,):

    #creating an image variable
    #picture = Image.open("apple1.jpg")
    #picture = Image.open(r"apple2.jpg")
    picture = Image.open(image)

    #display of Image previous to image manipulation
    picture.show()

    #getting the size of the image and the map
    w, h = picture.size
    #loading image map
    map = picture.load()

    # if the image is a perfect square and has the same dimensions as length and width
    if(w == h):
        #nested loop to run though the image
        for x in range(w):
            for y in range(h):
                #if the x value is the size of the width and height of the square indicated from the center then paint the square
                if  x >= (h//2 - sidelength) and x <= (h//2 + sidelength) and y >= (w//2 - sidelength) and y <= (w//2 + sidelength):
                    map[x,y] = (255, 255, 255)

    #if the image is not a perfect square and has different length and width dimensions
    else:
        #same nested loop as above
        for x in range(w):
            for y in range(h):
                #if the image is a rectangle then create a rectangle from the center with the side length that was input
                if  x >= (w//2 - sidelength) and x <= (w//2 + sidelength) and y >= (h//2 - sidelength) and y <= (h//2 + sidelength):
                                    map[x,y] = (255, 255, 255)
    #end of function to show the edited version of the picture
    picture.show()

    pass

#image file input
imageInput = input("Please put the name of the image and the file type that you want to manipulate. Please ensure that the image you want to manipulate is in the same directory as this file: ")
while True:
    userInput = input("What is the sidelength of the square you want to put in the center of the picture or type \"stop\" to stop:")
    #keeps editing the image until the user says stop and breaks out of the loop
    if userInput == "stop":
        break

    #if the user enters a valid number
    try:
        #if the user enters a valid int
        intString = int(userInput)
        #call the function
        makeSquare(imageInput, intString)
    #if the user doesn't enter a valid number throw an error and try input again
    except ValueError:
        print("Please enter a number")
