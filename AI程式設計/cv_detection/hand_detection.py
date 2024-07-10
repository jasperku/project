from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#指定影像的寬
cap.set(3, 1280)
#指定影像的高
cap.set(4,720)

detector= HandDetector(detectionCon=0.7) # confidence 的程度

while True:
    success, img = cap.read()
    # 翻轉影像 
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img, draw=True, flipType=False)
    #print(hands)
    
    cv2.namedWindow('Camera')
    cv2.moveWindow('Camera',0,0)
    cv2.imshow('Camera',img)
    
    # 完成攝影機的呈現, 離開視窗
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    
# 釋放我的資源, 關閉視窗
cap.release()
cv2.destroyAllWindows()