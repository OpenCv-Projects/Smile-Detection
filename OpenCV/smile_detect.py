#import opencv library
import cv2

# Including face,eye and smile haar-cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
# face_cascade =cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


#Detecting face
# face=face_cascade.detectMultiScale(gray,1.3,5)

def detect(gray, frame):
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)# FOR face- scaling factor=1.3 no. of nearest neighbors=5
	
	for (x, y, w, h) in faces:		#x,y are upper left part of face   w,h-width and height
		cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) #rectangle draws a rectangle outline
		roi_gray = gray[y:y + h, x:x + w]
		roi_color = frame[y:y + h, x:x + w]
		smiles = smile_cascade.detectMultiScale(roi_gray, 3.8, 15)#FOR SMILE
		eyes=eye_cascade.detectMultiScale(roi_gray,1.4,4)#FOR EYES
		for (sx, sy, sw, sh) in smiles: 
			cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)

		# for (sx, sy, sw, sh) in eyes: 
		# 	cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 255,0), 2)
				
	return frame




video_capture = cv2.VideoCapture(0)

while video_capture.isOpened():
# Captures video_capture frame by frame
	_, frame = video_capture.read()

	# To capture image in monochrome					
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# calls the detect() function	
	canvas = detect(gray, frame)

	# Displays the result on camera feed					
	cv2.imshow('Video', canvas)

	# The control breaks once q key is pressed						
	if cv2.waitKey(1) & 0xff == ord('q'):			
		break

# Release the capture once all the processing is done.
video_capture.release()								
cv2.destroyAllWindows()

