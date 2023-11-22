import cv2 
img = cv2.imread("C:/Users/kamini/Downloads/images/humaneye.jpg") 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
smile_cascade = cv2.CascadeClassifier("C:/Users/kamini/Downloads/images/smile.xml") 
smile= smile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) 
for (x, y, w, h) in smile: 
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) 
cv2.imshow('Smile Detected', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
