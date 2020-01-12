
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
from persons import person,sprite,magnets,dragon,spr

def is_data():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def getch():
    ch='l'
    if is_data():
        ch = sys.stdin.read(1)
    return ch 
    

def key_pressed():
    global UpKey,DownKey,LeftKey,RightKey,PauseKey,QuitKey
    ch = getch()
    if ch == "w":
        UpKey=True
    if ch == "a":
        LeftKey=True
    if ch == "d":
        RightKey=True
    if ch == 's':
        DownKey=True
    if ch == "p":
        PauseKey=True
    if ch == "q":
        QuitKey=True
def createobs(ob):
    ra_y = randint(3,32)
    r= randint(0,3)
    if r==0:
        for i in range(4,-1,-1):    
            ob.append(spr(138-2*i,ra_y,"O"))
    elif r==1:
        for i in range(4,-1,-1):    
            ob.append(spr(138-i,ra_y-i,"O"))
    elif r==2:
        for i in range(4,-1,-1):    
            ob.append(spr(134+i,ra_y-i,"O"))
    else:
        for i in range(4,-1,-1):    
            ob.append(spr(138,ra_y+i,"O"))                


def createcoins(co):
    ra_y = randint(3,32)
    for i in range(2,-1,-1):
        for j in range(5,-1,-1):
            co.append(spr(138-2*j,ra_y+i,'C'))

def createpower(sh,ch):
    ra_y=randint(3,32)
    for i in range(2,0,-1):
        for j in range(2,0,-1):
            sh.append(spr(138-2*j,ra_y+i,ch))  

def mandalorian():
    global UpKey,DownKey,LeftKey,RightKey,PauseKey,QuitKey,DownKey
    tik =TicToc()
    tik.tic()
    STEP = 0.0001
    me = person(50,9)
    score=0
    lives=3
    co=[]
    ob=[]
    mag=[]
    dra=[]
    drag=[]
    sh=[]
    sp=[]
    shstart=0
    spstart=0
    dragonp=0
    sheildp=0
    speed=1
    speedp=0
    time = 60
    # for j in range(3):
    #     for i in range(5):
    #         ob.append(obstacles(80+2*i,10+j,'O'))
    createpower(dra,'D')
    # mag.append(magnets(140,20))
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
            if dragonp:
                me.dr-=0.02
        if RightKey:
            RightKey=False
            me.velx+=0.1
        if LeftKey:
            LeftKey=False
            me.velx-=0.1 
        if DownKey:
            if dragonp:
                me.dr+=0.02


        # if t%25==0:
        #     if t%75==0:createobs(ob)   
        #     elif (t+25)%75==0:createcoins(co)
        #     else:
        #         i=randint(0,2)
        #         if i==0:createpower(sh,'S')
        #         if i==1:createpower(sp,'P')
        #         if i==2:createpower(dra,'D')

        if speedp==1:
            speed=2
        else: speed=0.5    

        if dragonp==0:
            me.update()
            me.printp()
        else:
            me.updatex()
            if t%10>4:drag.append(dragon(me.x,me.y+t%5,"D"))
            else: drag.append(dragon(me.x,me.y+4-t%5,"D"))
 
        #coins print
        all=[co,ob,sh,sp,dra]
        for j in all:
            for i in j:        
                i.update(speed) 
                if i.valid:
                    i.printsp()
                else:
                    j.remove(i)     

        #coin select
        for i in co:
            if abs(me.x-i.x)<1 and abs(me.y-i.y)<1:
                score+=1
                co.remove(i)
        
        #collision
        for i in ob:
            if sheildp==1:
                continue
            if abs(me.x-i.x)<1 and abs(me.y-i.y)<1:
                ob.remove(i)
                if dragonp==0:
                    lives-=1
                dragonp=0

        #powerup
        for i in sh:
            if abs(me.x-i.x)<1 and abs(me.y-i.y)<1:
                sh.remove(i)
                shstart=int(tik.elapsed)
                sheildp=1

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
            i.printsp()
            disx=i.x-me.x
            disy=i.y-me.y
            dis=floor(sqrt(disx**2+disy**2))        
            if dis!=0:
                me.velx+=(disx//dis)*3
                me.vely+=(disy//dis)*3
            i.update(speed)
            
        #dragon
        for i in drag:
            if i.valid==0:
                drag.remove(i)
                continue
            i.printsp()
            i.update()
        if dragonp==0:
            drag=[]
                    


        #sky and ground
        print("\033[2;12f")
        for i in range(150):
            print("S",end="")
        print("\033[41;0f")
        for i in range(150):
            print("G",end="")

                
        if lives==0:
            print("GAME OVER")
            return      
        tik.toc()
        ct=int(tik.elapsed)
        # print("\033[41;0f {},{}".format(me.x,me.y))
        print("\033[42;0f {},{}".format(me.velx,me.vely))
        print("\033[1;0f score:{}".format(score))
        print("\033[2;0f lives:{}".format(lives))
        if sheildp==1:
            if 20-(ct-shstart)>=0:
                print("\033[3;0f sheild:{} ({})".format(sheildp,20-(ct-shstart)))
            else:
                sheildp=0    
        else:
            print("\033[3;0f sheild:{}".format(sheildp))
        
        if speedp:
            if 20-(ct-spstart)>=0:
                print("\033[4;0f speed:{} ({})".format(speedp,20-(ct-spstart)))
            else:
                speedp=0
        else:
            print("\033[4;0f speed:{}".format(speedp))

        print("\033[5;0f dragon:{}".format(dragonp))
  
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

    mandalorian()
