
add_library('sound')
import os
path=os.getcwd()

class Game:
  def __init__(self,w,h,g):
    self.w=w
    self.h=h
    self.g=g
    self.x=0
    self.mario=Mario(100,100,self.g,39,"marioRun.png",78,78,4)
    self.enemies=[]
    for i in range(2):
      self.enemies.append(Gomba(300+i*80,100,self.g,35,"gomba.png",70,70,5))
    self.enemies.append(Gomba(2200,100,self.g,35,"gomba.png",70,70,5))
    self.stars=[]
    for i in range(5):
      self.stars.append(Star(1000+50*i,300+50*i,self.g,20,"star.png",40,40,6))
    self.platforms=[]
    self.platforms.append(Platform(300,350,200,52))
    self.platforms.append(Platform(500,250,200,52))
    self.platforms.append(Platform(2000,400,200,52))
    self.music=SoundFile(this,path+'/Overworld.mp3')
    self.music.play()
    self.bg=[]
    for i in range(1,6):
      self.bg.append(loadImage(path+'/layer_0'+str(i)+".png"))
    
  def display(self):
#     stroke(255)
#     line(0,self.g,self.w,self.g)
    cnt=0
    for b in self.bg[::-1]:
      if cnt==0:
        x = (self.x//6)%self.w
      elif cnt == 1:
        x = (self.x//4)%self.w
      elif cnt == 2:
        x = (self.x//2)%self.w
      else:
        x = (self.x)%self.w
      cnt+=1
      image(b,0,0,self.w-x,self.h,x,0,self.w,self.h)
      image(b,self.w-x,0,x,self.h,0,0,x,self.h)
    
    textSize(32);
    text(str(self.mario.score), 30, 30) 
  
    for s in self.stars:
      s.display()
    for e in self.enemies:
      e.display()
    for p in self.platforms:
      p.display()
      
    self.mario.display()
    
class Creature:
  def __init__(self,x,y,g,r,img,w,h,F):
    self.x=x
    self.y=y
    self.r=r
    self.g=g
    self.vx=0
    self.vy=0
    self.img=loadImage(path+'/'+img)
    self.w=w
    self.h=h
    self.F=F
    self.f=0
    self.dir=1
    
  def gravity(self):
    if self.y+self.r < self.g:
      self.vy+=0.2
    else:
      self.vy=0
      
    if self.y+self.r+self.vy > self.g:
      self.vy = self.g-(self.y+self.r)
      
    for p in game.platforms:
      if self.x+self.r > p.x and self.x-self.r < p.x+p.w \
        and self.y+self.r <= p.y:
        self.g=p.y
        break
      self.g=game.g
      
      
  def update(self):   
    self.gravity()
      
    self.x+=self.vx
    self.y+=self.vy
    
  def display(self):
    self.update()
    stroke(255,0,0)
    noFill()
    #ellipse(self.x,self.y,2*self.r,2*self.r)
    stroke(0,255,0)
    line(self.x-self.r-game.x,self.g,self.x+self.r-game.x,self.g)
    
    if self.vx != 0:
      self.f=(self.f+0.1)%self.F
    else:
      self.f=3
    
    if self.dir >= 0:
      image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
    else:
      image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)
    
class Mario(Creature):
  def __init__(self,x,y,g,r,img,w,h,F):
    Creature.__init__(self,x,y,g,r,img,w,h,F)
    self.keyHandler={LEFT:False,RIGHT:False,UP:False}
    self.jumpSound=SoundFile(this,path+'/jump.wav') # windows \\
    self.killSound=SoundFile(this,path+'/kill.mp3') # windows \\
    self.gameOverSound=SoundFile(this,path+'/gameover.wav') # windows \\
    self.starSound=SoundFile(this,path+'/coin.mp3')
    self.starSound.amp(0.1)
    self.gameOver=False
    self.score=0
    
  def colission(self):
    for s in game.stars:
      if self.distance(s) < self.r+s.r:
        game.stars.remove(s)
        del s
        self.starSound.play()
    
    for e in game.enemies:
      if self.distance(e) <= self.r+e.r: # checking for colission
        if self.y+self.r < e.y and self.vy > 0:
          game.enemies.remove(e)
          del e
          self.killSound.play()
          self.vy=-6
          self.score+=100
        else:
          self.gameOver=True
          self.gameOverSound.play()
          self.vy=-10
          self.vx=0
          game.music.stop()
          
          

  def distance(self,target):
    return ((self.x-target.x)**2+(self.y-target.y)**2)**0.5
      
  def update(self):
    if not self.gameOver:
      self.gravity()
      self.colission()

      if self.keyHandler[LEFT]:
        self.vx=-5
        self.dir=-1
      elif self.keyHandler[RIGHT]:
        self.vx=5
        self.dir=1
      else:
        self.vx=0

      if self.keyHandler[UP] and self.vy==0:
        self.vy=-10
        self.jumpSound.play()
    else:
      self.vx=0
      self.vy+=0.2
      #restart game when Mario goes off screen
      if self.y-self.r > game.h:
        game.__init__(1280,720,585)
    
    self.x+=self.vx
    self.y+=self.vy
    
    if self.x >= game.w//2:
      game.x+=self.vx
      
    if self.x-self.r <= 0:
      self.x=self.r

class Gomba(Creature):
  def __init__(self,x,y,g,r,img,w,h,F):
    Creature.__init__(self,x,y,g,r,img,w,h,F)
    self.x1=self.x-100
    self.x2=self.x+100
    self.vx=1
    
  def update(self):
    self.gravity()
    
    if self.x < self.x1:
      self.vx=1
      self.dir=1
    elif self.x > self.x2:
      self.vx=-1
      self.dir=-1
      
    self.x+=self.vx
    self.y+=self.vy
    
class Platform:
  def __init__(self,x,y,w,h):
    self.x=x
    self.y=y
    self.w=w
    self.h=h
    self.img=loadImage(path+'/platform1.png')
  
  def display(self):
    #stroke(255)
    #noFill()
    #rect(self.x,self.y,self.w,self.h)
    image(self.img,self.x-game.x,self.y,self.w,self.h)
    
class Star(Creature):
  def __init__(self,x,y,g,r,img,w,h,F):
    Creature.__init__(self,x,y,g,r,img,w,h,F)
    self.vx=1
    self.vy=2
    self.y1=200
    self.y2=self.g-50
  
  def update(self):
    if self.y > self.y2:
      self.vy = -2
    elif self.y < self.y1:
      self.vy = 2
    self.y+=self.vy
    
game=Game(1280,720,585)
def setup():
  size(game.w,game.h)
  background(0)
  
def draw():
  background(0)
  game.display()
  
def keyPressed():
  if keyCode == LEFT:
    game.mario.keyHandler[LEFT]=True
  elif keyCode == RIGHT:
    game.mario.keyHandler[RIGHT]=True
  elif keyCode == UP:
    game.mario.keyHandler[UP]=True

def keyReleased():
  if keyCode == LEFT:
    game.mario.keyHandler[LEFT]=False
  elif keyCode == RIGHT:
    game.mario.keyHandler[RIGHT]=False
  elif keyCode == UP:
    game.mario.keyHandler[UP]=False

