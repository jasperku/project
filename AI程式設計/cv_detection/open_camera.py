import cv2 

# get camera
cap = cv2.VideoCapture(0)

# 是否有正確打開攝影機 
while (cap.isOpened()):
    ret, frame = cap.read()
    # show the camera data to users through a window
    cv2.imshow("Camera",frame)
    
    # 完成攝影機的呈現, 離開視窗
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

# 釋放我的資源, 關閉視窗
cap.release()
cv2.destroyAllWindows()