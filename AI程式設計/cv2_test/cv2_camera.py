import cv2

# current camera
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
   ret, frame = cap.read()
   cv2.imshow("Camera", frame)
   key = cv2.waitKey(1)
   # ESC
   if key == 27:
      break
cap.release()
cv2.destroyAllWindows()