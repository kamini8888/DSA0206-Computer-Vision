import cv2 
path = "C:/Users/kamini/Downloads/images/puppy.jpg" 
image = cv2.imread(path) 
window_name = 'Image'
font = cv2.FONT_HERSHEY_SIMPLEX 
org = (50, 50) 
fontScale = 1
color = (255, 0, 0) 
thickness = 2
image = cv2.putText(image, 'puppy', org, font, fontScale, color, thickness, cv2.LINE_AA) 
cv2.imshow(window_name, image) 
