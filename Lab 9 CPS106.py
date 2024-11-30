from PIL import Image
import PIL

image = Image.new("RGB", (400,600), (0,0,0))

w,h = image.size
map = image.load()
def drawline(p1:tuple, p2:tuple, color:tuple):
    x1,y1 = p1
    x2,y2 = p2
    m = (y2-y1)//(x2-x1)
    m2 = m*(-1)

    for x in range(x1,x2):
        for y in range(y1,y2):
            if y == y1+ m*(x-x1) or y == y2 + m2*(x-x1):
                if 0<x<w and 0<y<h:
                    map[x,y] = color

for a in range (0,h//4,20):
    drawline((0,a), (w,w+a), (255,255,255))

def house(p0: tuple, W: int):
    x1,y1 = p0
    start_x = x1 - W//2
    final_x = x1 + W//2
    roof_y = y1 - W//2

    


image.show()
