import numpy as np
import cv2
import time

cam=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('InvisbileCloak.avi' , fourcc, 20.0, (480,640))
time.sleep(2)
background = 0 #capturing background

for i in range(50):
    ret, background = cam.read()#capturing image
while(cam.isOpened()):
    ret, img = cam.read()
    
    if not ret:
        break
        
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower_red = np.array([0,120,70])
    # upper_red = np.array([10,255,255])
    # mask1 = cv2.inRange(hsv , lower_red , upper_red)
    
    lower_blue = np.array([95,67,60])
    upper_blue = np.array([138,215,255])
    mask1=cv2.inRange(hsv , lower_blue, upper_blue) #Setting a Range

    # lower_red = np.array([95,67,60])
    # upper_red = np.array([138,215,255])
    # # lower_red = np.array([161, 155, 84])
    # # upper_red = np.array([179, 255, 255])
    # mask2 = cv2.inRange(hsv , lower_red , upper_red)
    
    # mask1 = mask1 + mask2 #OR
    # red=cv2.bitwise_and(background, background, mask=mask1)

    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN ,np.ones((3,3) , np.uint8) , iterations=1)
        
    mask2=cv2.morphologyEx(mask1, cv2.MORPH_DILATE ,np.ones((3,3) , np.uint8) , iterations=2)
        
    mask2 = cv2.bitwise_not(mask1)
    
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    
    final_output = cv2.addWeighted(res1 , 1, res2 , 1, 0)
    
    cv2.imshow('Invisible' , final_output)
    k=cv2.waitKey(10)
    if k==27:
        break
cam.release()
cv2.destroyAllWindows()        
        


#     # Red color
#     low_red = np.array([161, 155, 84])
#     high_red = np.array([179, 255, 255])
#     red_mask = cv2.inRange(hsv_frame, low_red, high_red)
#     red = cv2.bitwise_and(frame, frame, mask=red_mask)

# Same for the other colors:

#     # Blue color
#     low_blue = np.array([94, 80, 2])
#     high_blue = np.array([126, 255, 255])
#     blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
#     blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

#     # Green color
#     low_green = np.array([25, 52, 72])
#     high_green = np.array([102, 255, 255])
#     green_mask = cv2.inRange(hsv_frame, low_green, high_green)
#     green = cv2.bitwise_and(frame, frame, mask=green_mask)

#     # Every color except white
#     low = np.array([0, 42, 0])
#     high = np.array([179, 255, 255])
#     mask = cv2.inRange(hsv_frame, low, high)
#     result = cv2.bitwise_and(frame, frame, mask=mask)        
