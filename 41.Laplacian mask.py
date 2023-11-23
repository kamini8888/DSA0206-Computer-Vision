import cv2
import numpy as np
image_path = "C:/Users/kamini/Downloads/images/demon.jpg"
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv2.imshow('Original Image', img)
cv2.imshow('Laplacian Filtered', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
