#importing modules
import cv2

#reading image
img=cv2.imread("../DATA/00-puppy.jpg")

while True:
    cv2.imshow("my puppy ",img)
    if cv2.waitKey(1) & 0xFF==27: # 0xFF==ord('q') for q and 27 for esc key 
        break
    
cv2.destroyAllWindows()
    