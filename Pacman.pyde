path=os.getcwd()
x = 50
y = 50
speed = 1000
fillVal = color(156)

class Pacman:
    def __init__(self, x, y, r,F):
        self.x = x
        self.y = y
        self.dx= self.dx+1
        self.dy+=1
        self.r = r
        self.F=F
        self.f=0
        self.img=loadImage(path+'/Pacman1.png')
        #self.distance()
        
        
    def move(self, dx, dy):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        
        #add for how it goes to other side
        
    # def collision(self):
    #      for d in game.dots:
    #         if self.distance(d) < self.r + d.r:
    #             print("radius found")
    #             game.dots.remove(d)
    #             del d
    #             #insert sound here
    
    # def distance(self,target):
    #     return ((self.x-target.x)**2+(self.y-target.y)**2)**0.5
            
    
    def display(self):
        # ellipse(self.x, self.y, self.r, self.r)
        noFill()
        image(self.img, self.x,self.y,50,50,0,0,95,100)
        
        if self.dx != 0:
            self.f=(self.f+0.1)%self.F
        else:
            self.f=3
    
    #     if self.dir >= 0:
    #   image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
    # else:
    #   image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)
    
        
    

class Dot:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.img=loadImage(path+'/dot.png')
    
    def display(self):
        # ellipse(self.x, self.y, self.r * 2, self.r * 2)
        noFill()
        image(self.img,self.x,self.y,10,10)
        

class Game:
    def __init__(self):
        self.pacman = Pacman(205, 200, 20,3)
        self.dots = []
        self.fillDots(50,50,5,20,20)
        
    def fillDots(self,x,y,s,numRows,numCols):
        self.x=x
        self.y=y
        self.s=s
        self.numRows=numRows
        self.numCols=numCols
        for r in range(self.numRows):
            # for c in range(self.numCols):
            self.dots.append(Dot(self.x,self.y,self.s))
            self.x+=15
        self.dots.append(Dot(400, 400, 5))
        self.dots.append(Dot(100,100,5))
        self.dots.append(Dot(120,100,5))
        self.dots.append(Dot(140,100,5))
        self.dots.append(Dot(100,120,5))
       
    
    def distance(self,target):
        return ((self.pacman.x-target.x)**2+(self.pacman.y-target.y)**2)**0.5
    
    def collision(self):
        for d in self.dots:
            if self.distance(d) < self.pacman.r + d.r:
                print("radius found")
                self.dots.remove(d)
                del d
                #insert sound here
    
   
    def display(self):
        self.pacman.display()
        for d in self.dots:
            d.display()


    
   
    
   
        
g = Game()
# pacman = Pacman(50, 50, 49)
# dots = []
# dots.append(Dot(650, 650, 30))
    
def setup():
    size(500,500)
    stroke(238,232,170)
    fill(fillVal)
    background(0)
    # g = Game()#created object of game

def draw(): #display b/c gets called 30 times a second
    background(0)
    # pacman.display()
    # for dott in dots:
    #     dott.display() 
    g.display()
    
def keyPressed():
    global x, y, fillVal
    if key == CODED:
        if keyCode == LEFT:
            g.pacman.move(-5, 0)
            g.collision()
        elif keyCode == RIGHT:
            g.pacman.move(5, 0)
            g.collision()
        elif keyCode == UP:
            g.pacman.move(0, -5)
            g.collision()
        elif keyCode == DOWN:
            g.pacman.move(0, 5)
            g.collision()
        else:
            print("invalid key pressed")    