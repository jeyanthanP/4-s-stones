#THIS GAME ABOUT TO FIND 4 STONES BY SHOOTING  IT BEFORE THE ENEMY REACHES THE DESIRED POSITION
import pygame
import random
import math
from pygame.locals import*
from pygame import mixer
pygame.init()
fps = pygame.time.Clock()
 
# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("4's stones")
icon=pygame.image.load("index.png")
pygame.display.set_icon(icon)

#background
background_image=pygame.image.load("800-600.jpeg").convert()
mixer.music.load('background music.mp3')
mixer.music.play(-1)

#player
player=pygame.image.load("archer-girl1.png")
playerx=100
playery=400
playerx_speed=0
playery_speed=0

#enemy1
enemyimg=[]
enemyx=[]
enemyy=[]
enemyxchange=[]
enemyychange=[]
num_of_enemies =3

#enemy2
enemy1=[]
enemyx1=[]
enemyy1=[]
enemyxchange1=[]
enemyychange1=[]
num_of_enemies=3

#enemy3
enemyimg3=[]
enemyx3=[]
enemyy3=[]
enemyxchange3=[]
enemyychange3=[]
num_of_enemy=3

#finding stone
coinimg=[]
coinx=[]
coiny=[]
coinxchange=[]
coinychange=[]
num_of_coins=4

#list of enemy1
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('chipeur.png'))
    enemyx.append(random.randint(0,700))
    enemyy.append(random.randint(200,250))
    enemyxchange.append(0.3) 
    enemyychange.append(40)
    
#list of enemy2
for j in range(num_of_enemies):
    enemy1.append(pygame.image.load('enemy2.png')) 
    enemyx1.append(random.randint(0,700))
    enemyy1.append(random.randint(300,350))
    enemyxchange1.append(0.3) 
    enemyychange1.append(40)

#list of enemy3    
for l in range(num_of_enemy):
    enemyimg3.append(pygame.image.load("enemy5.png"))
    enemyx3.append(random.randint(340,440))
    enemyy3.append(random.randint(90,90))
    enemyxchange3.append(0.3)
    enemyychange3.append(40)

#list of finding stone
for k in range(num_of_coins):
    coinimg.append(pygame.image.load("carrom board-coins2.png"))
    coinx.append(random.randint(100,400))
    coiny.append(random.randint(300,370))
    coinxchange.append(0.3)
    coinychange.append(40)

#arrow
arrow=pygame.image.load("arrow2.png")
arrowx=200
arrowy=0
arrowxchange=10
arrowychange=0
arrow_state="ready"

#game over text
over_font= pygame.font.Font('freesansbold.ttf',63)
def game_over_text():
  over_text=over_font.render("GAME OVER",True,(0,0,0))
  screen.blit(over_text,(400,300))

#winner text
winner_font= pygame.font.Font('freesansbold.ttf',63)
def game_winner_text():
  winner_text=winner_font.render("WINNER",True,(0,0,0))
  screen.blit(winner_text,(400,300))  

#arrow shooting
def fire_arrow(x,y):
  global arrow_state
  arrow_state = "fire"
  screen.blit(arrow,(x+20,y+38))


#check collision
def iscollision(enemyx,enemyy,arrowx,arrowy):
  distance = math.sqrt((math.pow(enemyx-arrowx,2))+ (math.pow(enemyy-arrowy,2)))
  if distance < 27:
    return True
  else:
    return False  

#game loop
running=True
while running:
 screen.blit(background_image,[0,0])
 for event in pygame.event.get():
   if event.type==KEYDOWN:
       if event.key==K_ESCAPE:
         running=False
   elif event.type==QUIT:
       running=False
     
   if event.type==pygame.KEYDOWN:
       if event.key==pygame.K_LEFT:
         playerx_speed=-3
       if event.key==pygame.K_RIGHT:
         playerx_speed=3  
       if event.key==pygame.K_UP:
         playery_speed=-3
       if event.key==pygame.K_DOWN:
         playery_speed=3
       if event.key==pygame.K_SPACE:
         if arrow_state is "ready":
           arrowsound= mixer.Sound('arrow shooting effect.wav')
           arrowsound.play()
           arrowy =playery
           fire_arrow(arrowx,arrowy)         

   if event.type==pygame.KEYUP:
       if event.key==pygame.K_LEFT:
         playerx_speed=0
       if event.key==pygame.K_RIGHT:
         playerx_speed=0  
       if event.key==pygame.K_UP:
         playery_speed=0
       if event.key==pygame.K_DOWN:
         playery_speed=0
     
#player movement     
 playerx += playerx_speed
 playery += playery_speed   

 if playerx <=0:
   playerx =0
 elif playerx >=700:
   playerx =700
 if playery <=190:
   playery =190
 elif playery >=500:
   playery =500

#enemy1 movement  
 for i in range(num_of_enemies):
   if enemyy[i] >277:
     for n in range (num_of_enemies):     
       enemyy[n] =2000
     game_over_text()
     break  
   
   enemyx[i] += enemyxchange[i]
   if enemyx[i] <=0:
     enemyxchange[i] = 0.3
     enemyy[i] +=enemyychange[i]
   elif enemyx[i] >=700:
     enemyxchange[i] = -0.3
     enemyy[i] +=enemyychange[i]
   collision = iscollision(enemyx[i],enemyy[i],arrowx,arrowy)
   if collision:
     explosionsound= mixer.Sound('explosion sound.wav')
     explosionsound.play()
     arrowx = 100
     arrow_state = "ready"
     enemyx[i]=random.randint(0,700)
     enemyy[i]=random.randint(200,250)
   screen.blit(enemyimg[i],(enemyx[i],enemyy[i]))

#enemy2 movement
 for j in range(num_of_enemies):
   if enemyy[i] >277:
     for m in range (num_of_enemies):
       enemyy[m] =2000
     game_over_text()
     break  
  
   enemyx1[j] += enemyxchange1[j]
   if enemyx1[j] <=0:
     enemyxchange1[j] = 0.3
     enemyy1[j] +=enemyychange1[j]
   elif enemyx1[j] >=700:
     enemyxchange1[j] = -0.3
     enemyy1[j] +=enemyychange1[j]
   collision = iscollision(enemyx1[j],enemyy1[j],arrowx,arrowy)
   if collision:
     explosionsound= mixer.Sound('explosion sound.wav')
     explosionsound.play()
     arrowx = 100
     arrow_state = "ready"
     enemyx1[j]=random.randint(0,700)
     enemyy1[j]=random.randint(300,350)
   screen.blit(enemy1[j],(enemyx1[j],enemyy1[j]))  

#enemy3 movement
 for l in range(num_of_enemy):
   if enemyy[i] >277:
     for v in range (num_of_enemies):
       enemyy[v] =2000
     game_over_text()
     break  
    
   enemyy3[l] += enemyychange3[l]
   if enemyy3[l] <= 0:
     enemyychange3[l]=0.3
     enemyy3[l] += enemyychange3[l]
   elif enemyy3 [l]>=180:
     enemyychange3[l] =-0.3
     enemyy3[l] += enemyychange3[l]
   collision = iscollision(enemyx3[l],enemyy3[l],arrowx,arrowy)
   if collision:
     explosionsound= mixer.Sound('explosion sound.wav')
     explosionsound.play()
     arrowx = 100
     arrow_state = "ready"
     enemyx3[l]=random.randint(340,440)
     enemyy3[l]=random.randint(90,90)
   screen.blit(enemyimg3[l],(enemyx3[l],enemyy3[l]))

#stone movement
 for k in range(num_of_coins):
   if coiny[i]>=500:
     for h in range (num_of_coins):
       coiny[h] =2000
     screen.blit(background_image,[0,0])
     game_winner_text()
     break
     
   collision = iscollision(coinx[k],coiny[k],arrowx,arrowy)
   if collision:
     explosionsound= mixer.Sound('explosion sound.wav')
     explosionsound.play()
     arrowx = 100
     arrowy =  260
     arrrow_state = "ready"
     coinx[k]=random.randint(400,420)
     coiny[k]=random.randint(500,520)
   screen.blit(coinimg[k],(coinx[k],coiny[k]))

#arrow movement
 if arrowx >= 800:
   arrowx =200
   arrow_state = "ready"
 if arrow_state is "fire":
   fire_arrow(arrowx,arrowy)
   arrowx +=arrowxchange
 
#player image
 screen.blit(player,(playerx,playery))
 pygame.display.update()

pygame.quit()
