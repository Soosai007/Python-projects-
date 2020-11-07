import cv2
 
img = cv2.imread('python.jpg') 
 
cv2.imshow('sample image',img)
 
cv2.waitKey(0) # waits until a key is pressed

cv2.destroyAllWindows()
