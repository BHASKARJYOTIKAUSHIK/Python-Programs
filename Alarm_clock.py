from playsound import playsound as pd
import time

CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"
def alarm(sec):
    t=0
    print(CLEAR)
    while t<sec:
        
        time.sleep(1)
        
        
        t+=1
        time_left=sec-t
        min_left=time_left//60
        sec_left=time_left%60

        print(f"{CLEAR_AND_RETURN}Time lelt:{min_left:02d}:{sec_left:02d}")
    pd("mixkit-morning-clock-alarm-1003.wav")
        
s=int(input("Enter sec to wait:"))
m=int(input("Enter min to wait:"))
ts=s+m*60
alarm(ts)