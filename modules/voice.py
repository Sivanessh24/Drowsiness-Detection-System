import time
import pyttsx3 as p
from threading import Thread
def vva(intp):
    engine=p.init()
    voices = engine.getProperty('voices')
    if intp=='1':
        engine.setProperty('voice', voices[2].id)
        engine.setProperty('rate',150)
        engine.say('wake up sir')
        
    elif intp=='2':
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate',150)
        engine.say('Welcome to drowssiness detection system')
        time.sleep(0.2)
        
    elif intp=='5':
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate',150)
        engine.say('We hope you had a safe and happy journey')
        engine.say('powering off')
    try:
        engine.runAndWait()
        x=1
    except:
        er=True
        time.sleep(2)
        while er:
            try:
                engine.runAndWait()
                er=False
            except:
                pass
               
