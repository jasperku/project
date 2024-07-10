import cv2

# current camera
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('capture', frame)

        key = cv2.waitKey(1)
        # ESC
        if key == 27:
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()