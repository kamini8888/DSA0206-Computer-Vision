import cv2
import numpy as np
image_path = "C:/Users/kamini/Downloads/images/demon.jpg"
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
gradient_magnitude = np.uint8(gradient_magnitude)
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Filtered', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
