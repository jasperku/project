# get image
import cv2
# import image
img = cv2.imread("1.png", cv2.IMREAD_GRAYSCALE)

normalized_image = img.astype('float32') / 255.0

# show image
cv2.imshow("windows",normalized_image)
cv2.waitKey(0)
cv2.destroyWindow("windows" )