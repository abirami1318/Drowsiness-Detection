# Drowsiness-Detection
Used to prevent accidents due to drowsiness of drivers during driving.It plays a alert sound to wake up when they are sleepy.
## How it works
The operation we need is to find the eye contour and check how many seconds the eyes are closed,if it is longer than the threshold sound,then we are playing an alert sound to wake them up.So initially we find the landmark of the faces in the frame,
![Image of FacialLandmark](https://github.com/abirami1318/Drowsiness-Detection/dataset/facelandmark.png)
there are 68 coordinates from that we extract the coordinates of eyes and find the eye aspect ratio for both the eyes.The formula of eye aspect ratio 
        
