import cv2
def subtract_foreground(image_path, threshold=100):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    foreground = cv2.bitwise_and(img, img, mask=mask)
    return foreground
image_path = "C:/Users/kamini/Downloads/images/fox.jpg"
result = subtract_foreground(image_path)

cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Foreground', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
