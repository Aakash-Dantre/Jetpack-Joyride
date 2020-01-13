
from ttictoc import TicToc
import select
import sys
import termios
import time
import tty
from math import fmod, sqrt,floor
from random import randint
from time import sleep
from os import system
import math
from persons import *
from sprite import *
from colorcode import color

def is_data():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def getch():
    ch='l'
    if is_data():
        ch = sys.stdin.read(1)
    return ch 
    
def sky():
    print(color.CYAN+"\033[3;12f")
    for i in range(150):
        print("S",end="")
    print(color.GREEN+"\033[41;0f")
    for i in range(150):
        print("G",end="")
    print(color.END)    
def key_pressed():
    global UpKey,DownKey,LeftKey,RightKey,PauseKey,QuitKey,Bullet,sheildkey
    ch = getch()
    if ch == "w":
        UpKey=True
    elif ch == "a":
        LeftKey=True
    elif ch == "d":
        RightKey=True
    elif ch == 's':
        DownKey=True
    elif ch == ' ':
        Bullet=True
    elif ch == "p":
        PauseKey=True
    elif ch == "q":
        QuitKey=True
    elif ch == "t":
        sheildkey=True

def createobs(ob):
    ra_y = randint(8,32)
    r= randint(0,3)
    if r==0:
        for i in range(4,-1,-1):    
            ob.append(spr(135-2*i,ra_y,"_"))
    elif r==1:
        for i in range(4,-1,-1):    
            ob.append(spr(135-i,ra_y-i,"\\"))
    elif r==2:
        for i in range(4,-1,-1):    
            ob.append(spr(134+i,ra_y-i,"/"))
    else:
        for i in range(4,-1,-1):    
            ob.append(spr(135,ra_y+i,"|"))                

def createcoins(co):
    ra_y = randint(5,32)
    for i in range(0,3):
        for j in range(4,-1,-1):
            co.append(spr(138-2*j,ra_y+i,'C'))

def createpower(sh,ch):
    ra_y=randint(5,32)
    for i in range(0,2):
        for j in range(1,-1,-1):
            sh.append(spr(138-2*j,ra_y+i,ch))  

def mandalorian():
    global UpKey,DownKey,LeftKey,RightKey,PauseKey,QuitKey,Bullet,sheildkey
    tik =TicToc()
    tik.tic()
    STEP = 0.0001
    me = person(50,9)
    bsp = boss()
    score=0
    lives=3
    co=[]
    ob=[]
    mag=[]
    dra=[]
    drag=[]
    bu=[]
    sp=[]
    shstart=0
    spstart=0
    dragonp=0
    sheildp=0
    sheildav=1
    bossm=0
    bb=[]
    speed=1.5
    speedp=0
    time = 60
    bossh=100
    t=0

    while True:
        tty.setcbreak(sys.stdin.fileno())

        t+=1
        sleep(0.1)
        system('clear')
        # key event
        key_pressed()
        if UpKey:
            UpKey=False
            me.vely-=0.2
            # if dragonp:                     #on for dragon movement
            #     me.dr-=0.02
        if RightKey:
            RightKey=False
            me.velx+=0.1
        if LeftKey:
            LeftKey=False
            me.velx-=0.1 
        if Bullet:
            Bullet=False
            bu.append(spr(me.x,me.y,'>'))
        # if DownKey:                         #on for dragon movement
        #     if dragonp:
        #         me.dr+=0.02

        if QuitKey:
            print("GAME OVER")
            return
       	if sheildkey:
       		sheildkey=False
       		if sheildav:
       			sheildp=1 
        		sheildav=0
        		shstart=int(tik.elapsed)
       	#########################################################

        if t%35==0 and bossm==0:
            if t%105==0:createobs(ob)   
            elif (t+35)%105==0:createcoins(co)
            else:
                i=randint(0,2)
                if i==1:createpower(sp,'P')
                if i==2:createpower(dra,'D')
        
        if t%500==0:
            mag.append(spr(135,randint(5,35),'M'))
        

        if t>2000:                         ## boss mode on
            bossm=1
                
        if speedp==1:
            speed=2.5
        else: speed=1.5   
        
        if dragonp==0:
            me.update()
            me.printp(sheildp)
        else:
            me.updatex()
            if t%10>4:drag.append(dragon(me.x,me.y+t%5,"D"))
            else: drag.append(dragon(me.x,me.y+4-t%5,"D"))
        
        if bossm:                           ## boss mocd on
            # bb have boss bullets
            if t%4==0:
                bx=100-me.x
                by=25-me.y
                dis = floor(sqrt((bx)**2+(by)**2))
                vx=(bx/dis)*2
                vy=(by/dis)*2
                bb.append(bull(100,bsp.y,vx,vy,'*'))
            d =0
            if me.y-bsp.y > 0:d=1
            bsp.update(d)
            bsp.printb()
            
            for i in bu:  # bullet cause it have differt direct
                i.update(-2)
                if i.valid:
                    i.printsp(color.PURPLE)
                else:
                    bu.remove(i)
            for i in bb:  #bossb
                i.update()
                if i.valid:
                    i.printsp(color.RED)
                else:
                    bb.remove(i)        
            
            #boss hit me
            for i in bb:
                if abs(me.x-i.x)<2 and abs(me.y-i.y)<1:
                    bb.remove(i)
                    lives-=1
            # me hit boss
            for i in bu:
                if abs(100-i.x)<1 and abs(bsp.y-i.y)<2:
                    bu.remove(i)
                    bossh-=5 
               
        else:            
            #coins/obstacles/powerup print
               
            for i in co:        
                i.update(speed) 
                if i.valid:
                    i.printsp(color.BOLD+color.YELLOW)
                else:
                    co.remove(i)     
            for i in ob:        
                i.update(speed) 
                if i.valid:
                    i.printsp(color.BOLD+color.RED)
                else:
                    ob.remove(i)  
            for i in sp:        
                i.update(speed) 
                if i.valid:
                    i.printsp(color.DARKCYAN)
                else:
                    sp.remove(i) 
            for i in dra:        
                i.update(speed) 
                if i.valid:
                    i.printsp(color.PURPLE)
                else:
                    dra.remove(i)                                                                     

            for i in bu:  # bullet cause it have differt direct
                i.update(-2)
                if i.valid:
                    i.printsp(color.PURPLE)
                else:
                    bu.remove(i)

            #coin select
            for i in co:
                if abs(me.x-i.x)<2 and abs(me.y-i.y)<1:
                    score+=1
                    co.remove(i)
            
            #collision
            for i in ob:
                if sheildp==1:
                    continue
                if abs(me.x-i.x)<2 and abs(me.y-i.y)<1:
                    ob.remove(i)
                    if dragonp==0:
                        lives-=1
                    dragonp=0

            #powerup
            for i in sp:
                if abs(me.x-i.x)<1 and abs(me.y-i.y)<1:
                    sp.remove(i)
                    spstart=int(tik.elapsed)
                    speedp=1        
            
            for i in dra:
                if abs(me.x-i.x)<1 and abs(me.y-i.y)<1:
                    dra.remove(i)
                    dragonp=1         
            #magnet effect
            for i in mag:
                if i.valid==0:
                    mag.remove(i)
                    continue
                i.printsp(color.DARKCYAN)
                disx=i.x-me.x
                disy=i.y-me.y
                dis=floor(sqrt(disx**2+disy**2))        
                if dis!=0:
                    me.velx+=(disx//dis)*3
                    me.vely+=(disy//dis)*3
                i.update(speed)
                
            #dragon if it come
            for i in drag:
                if i.valid==0:
                    drag.remove(i)
                    continue
                i.printsp()
                i.update()
            if dragonp==0:
                drag=[]
                    

        #sky and ground
        sky()

        if lives==0:
            print("GAME OVER")
            return      


        tik.toc()
        ct=int(tik.elapsed)
        # print("\033[41;0f {},{}".format(me.x,me.y))
        print("\033[42;0f {},{}".format(me.velx,me.vely))
        print("\033[1;0f score:{}".format(score))
        print("\033[2;0f lives:{}".format(lives))
        if sheildav==0:
            if 60-(ct-shstart)>=0:
                print("\033[3;0f sheild:{} ({})".format(sheildav,60-(ct-shstart)))
            else:
                sheildav=1    
        else:
            print("\033[3;0f sheild:{}  press t".format(sheildav))
        
        if sheildp:
        	if 10-(ct-shstart)<=0:
        		sheildp=0


        if speedp:
            if 20-(ct-spstart)>=0:
                print("\033[4;0f speed:{} ({})".format(speedp,20-(ct-spstart)))
            else:
                speedp=0
        else:
            print("\033[4;0f speed:{}".format(speedp))

        print("\033[5;0f dragon:{}".format(dragonp))
            
        if bossm:
            print("\033[3;90f BOSS HEALTH:{}".format(bossh))

            if bossh < 1 :
                print("\033[10;80f YOU SAVED BABY YODA! :){}")
                return
          
        
        time=200-ct
        if time == 0:
            print("TIME OVER")
            return
        print("\033[6;0f time:{}".format(time))

if __name__ == "__main__":
    system('clear')
    UpKey= False
    DownKey= False
    LeftKey= False
    RightKey= False
    PauseKey= False
    QuitKey= False
    Bullet=False
    sheildkey=False
    mandalorian()
