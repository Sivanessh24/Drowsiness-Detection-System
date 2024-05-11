from voice import *
from playsound import playsound
from threading import Thread
import time

def sound():
    playsound(r"D:\clone\external sources\alarm.wav")


def alarm(ast):
    global alarm_status
    if ast=='1':
        alarm_status=True
    else:
        alarm_status=False
    count=0
    while alarm_status:
        if count>=3 :
            sound()
        else:
            vva('1')
            count+=1
