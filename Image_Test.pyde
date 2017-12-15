img = ""

def setup():
    global img
    size(800,600)
    background(125)
    img = loadImage("test.png")
    
def draw():
    # image(img,200,0,304,600)
    image(img,100,100,152,176,152,176,304,0)
    