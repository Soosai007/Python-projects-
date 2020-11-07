
import cv2

capture = cv2.VideoCapture(0) #0 for webcam and 1 for usb cam 
 
while(True):
     
    ret, frame = capture.read() #reading videos frame by frames
     
    cv2.imshow('video', frame)
     
    if cv2.waitKey(1) == 27: #if esc key is pressed camera will be closed 
        break
 
capture.release()
cv2.destroyAllWindows()

