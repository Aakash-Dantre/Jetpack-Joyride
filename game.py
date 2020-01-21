
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
    te=list()
    if r==0:
        for i in range(5,-1,-1):    
            te.append(spr(135-2*i,ra_y,"="))
    elif r==1:
        for i in range(5,-1,-1):    
            te.append(spr(135-i,ra_y-i,"\\\\"))
    elif r==2:
        for i in range(5,-1,-1):    
            te.append(spr(134+i,ra_y-i,"//"))
    else:
        for i in range(5,-1,-1):    
            te.append(spr(135,ra_y+i,"||"))                
    ob.append(te)

def createcoins(co):
    ra_y = randint(5,32)
    for i in range(0,3):
        for j in range(5,-1,-1):
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
    STEP = 0.0001;    me = person(50,9);    bsp = boss();    score=0;    lives=5;    co=[];    ob=[];    mag=[];    dra=[];    drag=[];    bu=[];    sp=[];    shstart=0;    spstart=0;    dragonp=0;    sheildp=0;    sheildav=1;    bossm=0;    bb=[];    speed=1;    speedp=0;    time = 60;    bossh=100;    t=0;
    bt=2000
    
    while True:
        tty.setcbreak(sys.stdin.fileno())

        t+=1
        sleep(0.1)
        system('clear')
        # key event
        key_pressed()
        if UpKey:
            UpKey=False
            me.upy(-0.2)
            # if dragonp:                     #on for dragon movement
            #     me.dr-=0.02
        if RightKey:
            RightKey=False
            me.upx(0.1)
        if LeftKey:
            LeftKey=False
            me.upx(-0.1) 
        if Bullet:
            Bullet=False
            bu.append(spr(me.getx()+2,me.gety(),'>'))
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

        if t%33==0 and bossm==0:
            if t%99==0:createobs(ob)   
            elif (t+33)%99==0:createcoins(co)
            else:
                i=randint(0,2)
                if i==0:createobs(ob)
                elif i==1:createpower(sp,'P')
                else:createpower(dra,'D')
        
        if t%100==0:
            mag.append(spr(135,randint(5,35),'M'))
        

        if t>bt:                         ## boss mode on
            bossm=1
                
        if speedp==1:
            speed=2.5
        else: speed=1.5   
        
        if dragonp==0:
            me.update()
            me.printp(sheildp)
        else:
            me.updatex()
            if t%10>4:drag.append(dragon(me.getx(),me.gety()+t%5,"D"))
            else: drag.append(dragon(me.getx(),me.gety()+4-t%5,"D"))
        
        if bossm:                           ## boss mocd on
            # bb have boss bullets
            if t%4==0:
                bx=95-me.getx()
                by=25-me.gety()
                dis = floor(sqrt((bx)**2+(by)**2))
                vx=(bx/dis)*2+1
                vy=(by/dis)*2
                bb.append(bull(95,bsp.gety(),vx,vy,'*'))
            d =0
            if me.gety()-bsp.gety() > 0:d=1
            bsp.update(d)
            bsp.printb()
            
            for i in bu:  # bullet cause it have differt direct
                i.update(-2)
                if i.gety()>35:
                	bu.remove(i)
                if i.getx()>143:
                	bu.remove(i)
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
                if abs(me.getx()-i.getx())<2 and abs(me.gety()-i.gety())<1:
                    bb.remove(i)
                    lives-=1
            # me hit boss
            for i in bu:
                k=(i.gety()-bsp.gety())
                if abs(95-i.getx())<=2 and k<8 and k>=0 :
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
            for j in ob:
                for i in j:
                    i.update(speed) 
                    if i.valid:
                        i.printsp(color.BOLD+color.RED)
                    else:
                        ob.remove(j)
                        break

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
                if i.gety()>35:
                	bu.remove(i)
                if i.getx()>143:
                 	bu.remove(i)
                if i.valid:
                    i.printsp(color.PURPLE)
                else:
                    bu.remove(i)

            #coin select
            for i in co:
                if abs(me.getx()-i.getx())<2 and abs(me.gety()-i.gety())<1:
                    score+=1
                    co.remove(i)
            
            #collision
            for j in ob:
                for i in j:
                    if sheildp==1:
                        continue
                    if abs(me.getx()-i.getx())<2 and abs(me.gety()-i.gety())<1:
                        ob.remove(j)
                        if dragonp==0:
                            lives-=1
                        dragonp=0
                        break

            #bullet with obstacls
            for k in bu:    
                for j in ob:
                    for i in j:
                        if abs(k.getx()-i.getx())<1 and (k.gety()-i.gety()<1):
                            ob.remove(j)
                            break

            #powerup
            for i in sp:
                if abs(me.getx()-i.getx())<1 and abs(me.gety()-i.gety())<1:
                    sp.remove(i)
                    spstart=int(tik.elapsed)
                    speedp=1        
            
            for i in dra:
                if abs(me.getx()-i.getx())<1 and abs(me.gety()-i.gety())<1:
                    dra.remove(i)
                    dragonp=1         
            #magnet effect
            for i in mag:
                if i.valid==0:
                    mag.remove(i)
                    continue
                i.printsp(color.DARKCYAN)
                disx=i.getx()-me.getx()
                disy=i.gety()-me.gety()
                dis=floor(sqrt(disx**2+disy**2))        
                if dis!=0:
                    me.upx((disx//dis)*2)
                    me.upy((disy//dis)*2)
                i.update(speed)
                
            #dragon if it come
            for i in drag:
                if i.valid==0:
                    drag.remove(i)
                    continue
                i.printsp(color.GREEN)
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
        # print("\033[42;0f {},{}".format(me.velx,me.vely))
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
                print("\033[10;80f YOU SAVED BABY YODA! :)")
                return
          
        
        time=200-ct
        if time == 0:
            print("TIME OVER")
            return
        print("\033[6;0f time:{}".format(time))
        if bossm==0:
        	print("\033[3;50f percentage:{}".format(int((t*100)/bt)))

if __name__ == "__main__":
    system('clear')
    UpKey= False;DownKey= False;LeftKey= False;RightKey= False;PauseKey= False;QuitKey= False;Bullet=False;sheildkey=False
    mandalorian()
