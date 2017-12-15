add_library('sound')
import os
path=os.getcwd()

class Tile:
    def __init__(self,r,c,v):
        self.r=r
        self.c=c
        self.v=v
        self.img=loadImage(path+"/Images/"+str(self.v)+".png")
    
    def display(self):
            if self.v != 15:
                image(self.img,self.c*100,self.r*100)
    
class Puzzle:
    def __init__(self,numRows,numCols):
        self.numRows=numRows
        self.numCols=numCols
        self.blank=15
        self.mlist=[]
        
    def createBoard(self):
        self.gameWin=False
        #self.gameSound=SoundFile(this,path+'/Sounds/banana.mp3')
        self.winSound=SoundFile(this,path+'/Sounds/TaDa.mp3')
        #self.gameSound.play()
        self.board=[]
        v=0
        for r in range(self.numRows):
            for c in range(self.numCols):
                self.board.append(Tile(r,c,v))
                v+=1
                
    def display(self):
        for t in self.board:
            t.display()

    def shuffle(m=0):
        if self.blank==15:
            self.mlist.append=[[0,1][-1,0][0,-1][1,0]]
            while random.choice(mlist):
            # for m in range(mlist):
            #     for n in range(mlist):
                    self.blank=board[randx][randy].v
                    board[x][y]=board[randx][randy]
                    return
                
            # for r in range(mlist):
        #     for c in range(mlist):
        #         random.choice()

        

    # def move(self,t):
    #     if t.x == 4 and t.y == 4:
            
            
             
            
pz = Puzzle(4,4)

def setup():
    size(pz.numCols*100,pz.numRows*100)
    background(0)
    pz.createBoard()

def draw():
    pz.display()
    
# def mouseClicked():
#     for t in pz.board:
#         if t.x*100 <= mouseX <= t.x*100+100 and t.y*52 <= mouseY <= t.y*100+100:
#             pz.move(t)
#             break




        
        