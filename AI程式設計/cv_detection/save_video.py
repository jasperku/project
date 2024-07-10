# get camera, recorder , save to HD output.avi

import cv2 

# get camera
cap = cv2.VideoCapture(0)

# setup Video format
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640,480) )

# 是否有正確打開攝影機 
while (cap.isOpened()):
    ret, frame = cap.read()
    
    # ret == true: camera is open 
    if ret == True:
        # frame output 
        out.write(frame)
        cv2.imshow("Camera",frame)
        
        # 完成攝影機的呈現, 離開視窗
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break

# 釋放我的資源, 關閉視窗
cap.release()
out.release()
cv2.destroyAllWindows()