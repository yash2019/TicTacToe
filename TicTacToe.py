import pygame
import random
import time
from pygame.locals import *

pygame.init()    
screen=pygame.display.set_mode((700, 700))
pygame.display.set_caption("Tic Tac Toe")
screen.fill((255,255,255))
pygame.display.update()

BLACK =(0,0,0)
BLACKt =(0,0,0,228)
WHITE =(255,255,255)
RED   =(255,0,0)
PINK  =(255,0,255)
YELLOW=(255,255,0)
GREEN =(0,255,0)
BLUE  =(0,0,255)
TEAL  =(0,255,255)
clist=[RED,GREEN,BLUE,TEAL,PINK,YELLOW,BLACK,WHITE]
bo=0

D={1:"_",2:"_",3:"_",4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
A=1
permit=1

def display(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
def display2(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",100)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
def display3(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",24)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
    
print('Game History')
def Game():
    global bo
    while True:
#Menu
        screen.fill((255,255,255))
        pygame.draw.rect(screen,BLACK,(350,0,350,700))
        display('Start',225,350,BLACK)
        display('Quit',425,350,WHITE)
        display3('Created by: Yash Jain',650,850,WHITE)
        pygame.draw.rect(screen,BLACK,(215,350,75,35),5)
        pygame.draw.rect(screen,WHITE,(415,350,70,35),5)
        display('Settings',582,10,WHITE)
        pygame.draw.rect(screen,WHITE,(582,10,120,35),5)
        pygame.display.update()

#Game start   
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    x=event.pos[0]
                    y=event.pos[1]

                    if 350<=x<=515 and 350<=y<=385:
                        time.sleep(0.5)
                        import Main

                    
                        
                    if 215<=x<=285 and 350<=y<=385:
                        if permit==1:
                            pygame.draw.rect(screen,WHITE,(0,0,700,700))
                            D={1:"_",2:"_",3:"_",4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
                            A=1

                            while True:
                                pygame.draw.rect(screen,BLACK,(0,0,700,700),5)

                                pygame.draw.line(screen,BLACK,(233,0),(233,700),3)
                                pygame.draw.line(screen,BLACK,(466,0),(466,700),3)
                                pygame.draw.line(screen,BLACK,(0,233),(700,233),3)
                                pygame.draw.line(screen,BLACK,(0,466),(700,466),3)

                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        import Main
                                    elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:

                                        x=event.pos[0]
                                        y=event.pos[1]

                                        x=int(x)
                                        y=int(y)
#Square 1
                                        if 0<=x<=233 and 0<=y<=233:
                                            if A==1 and D[1]=='_':
                                                D[1]='x'
                                                pygame.draw.line(screen,BLACK,(0,0),(233,233),3)
                                                pygame.draw.line(screen,BLACK,(233,0),(0,233),3)
                                                A=0
                                            elif A==0 and D[1]=='_':
                                                pygame.draw.circle(screen,BLACK,(116,116),116,3)
                                                D[1]='o'
                                                A=1

                                            
#Square 2
                                        if 233<=x<=466 and 0<=y<=233:
                                            if A==1 and D[2]=='_':
                                                D[2]='x'
                                                pygame.draw.line(screen,BLACK,(233,0),(466,233),3)
                                                pygame.draw.line(screen,BLACK,(466,0),(233,233),3)
                                                A=0
                                            elif A==0 and D[2]=='_':
                                                pygame.draw.circle(screen,BLACK,(350,116),116,3)
                                                D[2]='o'
                                                A=1

#Square 3
                                        if 466<=x<=700 and 0<=y<=233:
                                            if A==1 and D[3]=='_':
                                                D[3]='x'
                                                pygame.draw.line(screen,BLACK,(466,0),(700,233),3)
                                                pygame.draw.line(screen,BLACK,(700,0),(466,233),3)
                                                A=0
                                            elif A==0 and D[3]=='_':
                                                pygame.draw.circle(screen,BLACK,(582,116),116,3)
                                                D[3]='o'
                                                A=1


#Square 4
                                        if 0<=x<=233 and 233<=y<=466:
                                            if A==1 and D[4]=='_':
                                                D[4]='x'
                                                pygame.draw.line(screen,BLACK,(0,233),(233,466),3)
                                                pygame.draw.line(screen,BLACK,(233,233),(0,466),3)
                                                A=0
                                            elif A==0 and D[4]=='_':
                                                pygame.draw.circle(screen,BLACK,(116,350),116,3)
                                                D[4]='o'
                                                A=1
                                
                                       
#Square 5
                                        if 233<=x<=466 and 233<=y<=466:
                                            if A==1 and D[5]=='_':
                                                D[5]='x'
                                                pygame.draw.line(screen,BLACK,(233,233),(466,466),3)
                                                pygame.draw.line(screen,BLACK,(466,233),(233,466),3)
                                                A=0
                                            elif A==0 and D[5]=='_':
                                                pygame.draw.circle(screen,BLACK,(350,350),116,3)
                                                D[5]='o'
                                                A=1


#Square 6
                                        if 466<=x<=700 and 233<=y<=466:
                                            if A==1 and D[6]=='_':
                                                D[6]='x'
                                                pygame.draw.line(screen,BLACK,(466,233),(700,466),3)
                                                pygame.draw.line(screen,BLACK,(700,233),(466,466),3)
                                                A=0
                                            elif A==0 and D[6]=='_':
                                                pygame.draw.circle(screen,BLACK,(582,350),116,3)
                                                D[6]='o'
                                                A=1
                                            

#Square 7
                                        if 0<=x<=233 and 466<=y<=700:
                                            if A==1 and D[7]=='_':
                                                D[7]='x'
                                                pygame.draw.line(screen,BLACK,(0,466),(233,700),3)
                                                pygame.draw.line(screen,BLACK,(233,466),(0,700),3)
                                                A=0
                                            elif A==0 and D[7]=='_':
                                                pygame.draw.circle(screen,BLACK,(116,582),116,3)
                                                D[7]='o'
                                                A=1



#Square 8
                                        if 233<=x<=466 and 466<=y<=700:
                                            if A==1 and D[8]=='_':
                                                D[8]='x'
                                                pygame.draw.line(screen,BLACK,(233,466),(466,700),3)
                                                pygame.draw.line(screen,BLACK,(466,466),(233,700),3)
                                                A=0
                                            elif A==0 and D[8]=='_':
                                                pygame.draw.circle(screen,BLACK,(350,582),116,3)
                                                D[8]='o'
                                                A=1

#Square 9
                                        if 466<=x<=700 and 466<=y<=700:
                                            if A==1 and D[9]=='_':
                                                D[9]='x'
                                                pygame.draw.line(screen,BLACK,(466,466),(700,700),3)
                                                pygame.draw.line(screen,BLACK,(700,466),(466,700),3)
                                                A=0
                                            elif A==0 and D[9]=='_':
                                                pygame.draw.circle(screen,BLACK,(582,582),116,3)
                                                D[9]='o'
                                                A=1

                                        pygame.display.update()


                                        if (D[1]=='x' and D[2]=='x' and D[3]=='x') or (D[4]=='x' and D[5]=='x' and D[6]=='x') \
                                        or (D[7]=='x' and D[8]=='x' and D[9]=='x') or (D[1]=='x' and D[4]=='x' and D[7]=='x') \
                                        or (D[2]=='x' and D[5]=='x' and D[8]=='x') or (D[3]=='x' and D[6]=='x' and D[9]=='x') \
                                        or (D[1]=='x' and D[5]=='x' and D[9]=='x') or (D[3]=='x' and D[5]=='x' and D[7]=='x'):
                                            time.sleep(0.5)
                                            pygame.draw.rect(screen,WHITE,(0,0,700,700))
                                            display2('PLAYER X WINS',15,350,BLACK)  
                                            pygame.display.update()
                                            time.sleep(1)
                                            print('Player x wins')
                                            pygame.draw.rect(screen,WHITE,(0,0,700,700))
                                            D={1:"_",2:"_",3:"_",4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
                                            bo=0
                                            A=1
                                            Conc=1
                                            event.button=0
                                            pygame.display.update()
                                            Game()
                                                                                
                                        if (D[1]=='o' and D[2]=='o' and D[3]=='o') or (D[4]=='o' and D[5]=='o' and D[6]=='o') \
                                        or (D[7]=='o' and D[8]=='o' and D[9]=='o') or (D[1]=='o' and D[4]=='o' and D[7]=='o') \
                                        or (D[2]=='o' and D[5]=='o' and D[8]=='o') or (D[3]=='o' and D[6]=='o' and D[9]=='o') \
                                        or (D[1]=='o' and D[5]=='o' and D[9]=='o') or (D[3]=='o' and D[5]=='o' and D[7]=='o'):
                                            time.sleep(0.5)
                                            pygame.draw.rect(screen,WHITE,(0,0,700,700))
                                            display2('PLAYER O WINS',15,350,BLACK)  
                                            pygame.display.update()
                                            time.sleep(1)
                                            print('Player o wins')
                                            pygame.draw.rect(screen,WHITE,(0,0,700,700))
                                            D={1:"_",2:"_",3:"_",4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
                                            bo=0
                                            A=1
                                            Conc=1
                                            event.button=0
                                            pygame.display.update()
                                            Game()

                                        bo=bo+1
                                        if bo==9:
                                            time.sleep(0.5)
                                            pygame.draw.rect(screen,WHITE,(0,0,700,700))
                                            display2('TIE',15,350,BLACK)  
                                            pygame.display.update()
                                            time.sleep(1)
                                            print('Player o wins')
                                            pygame.draw.rect(screen,WHITE,(0,0,700,700))
                                            D={1:"_",2:"_",3:"_",4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
                                            A=1
                                            Conc=1
                                            event.button=0
                                            pygame.display.update()
                                            Game()
                                            
                                    pygame.display.update()
                                    
while True:
    Game()
    pygame.display.update()
    permit=0
    
    
    


