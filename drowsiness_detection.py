from pygame import mixer
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import playsound
import imutils
import time
import dlib
import cv2
mixer.init()
def soundalarm(path):
    mixer.music.load(path)
    mixer.music.play()
def stop_song():
    mixer.music.stop()
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1],eye[5])
    B = dist.euclidean(eye[2],eye[4])
    C = dist.euclidean(eye[0],eye[3])
    ratio = (A+B) / (2.0*C)
    return ratio
def shape_to_np(shape):
    arr = np.zeroes(68,2)
    for i in range(68):
        arr[i] = [shape[i][0],shape[i][1]]
    return arr
eye_threshold = 0.3
no_frames = 10
counter = 0
alarm_on = False
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('D:/Abi/Project/Drowsiness_Detection/shape_predictor/shape_predictor_68_face_landmarks.dat')
(lstart,lend) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rstart,rend) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']
while True:
    vs = VideoStream(0).start()
    time.sleep(0.2)
    frame = vs.read()
    frame = imutils.resize(frame,width=450)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rects = detector(gray,0)
    for rect in rects:
        shape = predictor(gray,rect)
        shape = face_utils.shape_to_np(shape)
        lefteye = shape[lstart:lend]
        righteye = shape[rstart:rend]
        left_ratio = eye_aspect_ratio(lefteye)
        right_ratio = eye_aspect_ratio(righteye)
        ear = (left_ratio+right_ratio)/2
        lefteyehull = cv2.convexHull(lefteye)
        righteyehull = cv2.convexHull(righteye)
        cv2.drawContours(frame, [lefteyehull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [righteyehull], -1, (0, 255, 0), 1)
        if ear < eye_threshold:
            counter += 1
            print(True)
            if counter >= no_frames:
                print('ALARM')
                if not alarm_on:
                    alarm_on = True
                soundalarm('D:/Abi/Project/Drowsiness_Detection/alarm.mp3')
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            counter = 0
            stop_song()
            alarm_on = False
        cv2.putText(frame, "Ratio:{:.2f}".format(ear), (100, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow('Streaming',frame)
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
    print(counter)
cv2.destroyallWindows()
vs.stop()
