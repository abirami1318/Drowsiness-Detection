# Drowsiness-Detection
Used to prevent accidents due to drowsiness of drivers during driving.It plays a alert sound to wake up when they are sleepy.
## How it works
The operation we need is to find the eye contour and check how many seconds the eyes are closed,if it is longer than the threshold sound,then we are playing an alert sound to wake them up.So initially we find the landmark of the faces in the frame,
![Image of FacialLandmark](https://github.com/abirami1318/Drowsiness-Detection/blob/master/dataset/facelandmark.png)
there are 68 coordinates from that we extract the coordinates of eyes and find the eye aspect ratio for both the eyes.The formula of eye aspect ratio
![Image of Eye Aspect Ratio](https://github.com/abirami1318/Drowsiness-Detection/blob/master/dataset/ear.png)
if the average of left and right eye aspect ratio less than threshold EAR for the consecutive number of frames,then the alarm should turn on till the EAR greater than respected ratio.
## Prerequisites
!pip install pygame<br>
!pip install scipy<br>
!pip install imutils<br>
!pip install numpy<br>
!pip install dlib<br>
!pip install cv2
## How to run
python drowsiness_detection.py
