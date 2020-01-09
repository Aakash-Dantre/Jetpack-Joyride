
from threading import Timer
import sys
import tty
import termios
from select import select
import time
def getch():
    fd = sys.stdin.fileno()
    old_setting = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
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
    if ch == "p":
        PauseKey=True
    if ch == "q":
        QuitKey=True

def mandalorian():
    global UpKey,DownKey,LeftKey,RightKey,PauseKey,QuitKey

    STEP = 0.1

    t=0
    while True:
        t+=1
        # key event
        time.sleep(STEP) 
        key_pressed()

        if UpKey:
            UpKey=False
            print("UP")
        if RightKey:
            RightKey=False
            print("RIGHT")
        if LeftKey:
            LeftKey=False
            print("LEFT")
        if QuitKey:
            print("quit")
            return  
    




if __name__ == "__main__":
    UpKey= False
    DownKey= False
    LeftKey= False
    RightKey= False
    PauseKey= False
    QuitKey= False

    mandalorian()
