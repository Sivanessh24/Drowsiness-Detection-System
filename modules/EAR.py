from euclidean_distance import *

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
