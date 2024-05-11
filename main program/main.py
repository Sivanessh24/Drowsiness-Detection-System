from imutils.video import VideoStream#to veiw the video from the 
from imutils import face_utils
from threading import Thread #to perfome multitask
import numpy as np 
import imutils
import dlib
import cv2#edit content set the frame to display
import sys
import time
import pyttsx3 as p
from playsound import playsound
import math

def euclidean_dist(x,y):
    temp=[]
    for a,b in zip(x,y):
        z=a-b
        temp.append(z**2)
    dist=math.sqrt(sum(temp))
    return dist
#dist=math.sqrt(sum([(a-b)**2 for a,b in zip(x,y)]))



def vva(intp):
    engine=p.init()
    voices = engine.getProperty('voices')
#    engine.setProperty('voice', voices[0].id)
#    engine.setProperty('rate',145)
    if intp=='1':
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate',150)
        engine.say('wake up sir')
        
    elif intp=='2':
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate',150)
        engine.say('Welcome to drowssiness detection system sir')
        time.sleep(0.2)
        
    elif intp=='5':
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate',150)
        engine.say('We hope you had a safe and happy journey')
        engine.say('powering off')
       
    c123=0
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
               

#import tester
def sound():
 #   t1=Thread(target=vva,args='1')
 #   t1.start()
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


def eye_aspect_ratio(eye):
    A = euclidean_dist(eye[1], eye[5]) 
    B = euclidean_dist(eye[2], eye[4])
    C = euclidean_dist(eye[0], eye[3])
    
    ear = (A + B) / (2.0 * C)
    
    return ear

def final_ear(shape):
    rightEye = shape[36:42]
    leftEye = shape[42:48]
    mouth=shape[48:68]
    
    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)

    ear = (leftEAR + rightEAR) / 2.0
    return (ear, leftEye, rightEye)

def tml():
    t=list(time.localtime())
    t=[12,1,22]
    tm=''
    if t[0]<12:
        ap=' am'
    else:
        ap=' pm'
        if t[0]!=12:
            t[0]=t[0]-12
    for i in t:    
        if len(str(i))==1:
            t[t.index(i)]='0'+str(i)
    tm=str(t[0])+':'+str(t[1])+':'+str(t[2])+ap
    return tm

t1=Thread(target=vva,args='2')
t1.start()

print('\n                                       *****Welcome to drowssiness detection system*****')
print('                                              *****START_TIME__'+tml()+'*****'+'\n\n')

#ap = argparse.ArgumentParser()
#args=ap.add_argument("-w", "--webcam", type=int, default=0)
#args = vars(ap.parse_args())#{'webcam': 0}

args = {'webcam': 0}
E_A_R = 0.27#minimum eye ratio
EYE_FPS = 30#45/24=3seceonds
alarm_status = False
dlevel=0.00
COUNTER = 0

print("---preparing to launch...:)")

detector = dlib.get_frontal_face_detector()#helps to detect human face
predictor = dlib.shape_predictor(r"D:\clone\external sources\shape_predictor_68_face_landmarks.dat")#help to plot all the coorinates

time.sleep(2)

vs = VideoStream(src=args["webcam"]).start()

print("---webcam connected successfully")
print('\n\nEnter "q" to quit')

tp=0
while True:
    
    frame = vs.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#converting one colourspace to anthour
                                                    #in backend it converts to gray scale
    
    rects = detector(gray)#faces are dectected
    
    for rect in rects:
        
        x = rect.left()
        y = rect.top() #could be face.bottom() - not sure
        w = rect.right() - rect.left()
        h = rect.bottom() - rect.top()+10
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        shape = predictor(gray, rect)#all the cordinates have been collected and stored
        shape = face_utils.shape_to_np(shape)#all cordinates have been converted into an array 2D list
        
        eye = final_ear(shape)#function calling area
        ear = eye[0]#avg ear of both eye
        leftEye = eye [1]#all coordinates of left eye
        rightEye = eye[2]#all coordinates of right eye
        
         
        leftEyeHull = cv2.convexHull(leftEye)#invisble bountries are created in left eye
        rightEyeHull = cv2.convexHull(rightEye)#invisble bountries are created in right eye
        
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)#a green line is drawn along
                                                                #the boundry of left eye

        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)#a green line is drawn along
                                                                #the boundry of left eye
        
        cv2.putText(frame, 'EAR:'+str(int(ear*100)/100), (x+w, y+h+10),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,255,255), 1)
#        cv2.putText(frame, 'BLINKS:'+str(tp), (225, 300),
#                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,255,255), 1)

       # cv2.putText(frame,'EAR:'+str(int(ear*10)/10), (330, 25),
        #                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 1)

        cv2.putText(frame, 'DL:'+str(int(ear*100)/100), (x-65, y),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,255,255), 1)
        
        if  alarm_status ==True:
            cv2.putText(frame, "DROWSINESS ALERT!", (110, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
        if ear < E_A_R:#ear<0.3
            COUNTER += 1
            if COUNTER >= EYE_FPS:#COUNTER>=72/24
                tp+=1
                if alarm_status == False:
                    alarm_status = True
                    t=Thread(target=alarm,args='1')#only function name is enough
                    t.start()
        else:
            COUNTER = 0
            alarm_status = False
            alarm('0')
            
            
    cv2.imshow("drowsiness detection", frame)

    key=cv2.waitKey(1)
    if key == ord("q"):
        vs.stop()
        alarm_status = False
        alarm(0)
        print('STOP_TIME'+tml())
        print('\n                                --We hope you had a safe and happy journey..:)')
        cv2.destroyAllWindows()    
        vva('5')
        break
