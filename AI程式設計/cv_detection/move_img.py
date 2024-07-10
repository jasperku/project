from cvzone.HandTrackingModule import HandDetector
import cv2

# CAP_DSHOW is for windows speed up
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3, 1280) # 指定補抓影像的寬
cap.set(4, 720) # 指定補抓影像的高 

detector = HandDetector(detectionCon=0.65)

# insert image
pic1 = cv2.imread("img1.jpg")
ox,oy =200, 200

# height, weight, channel
h, w, _ = pic1.shape

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    
    if hands:
        lmList = hands[0]['lmList']
        #cursor = lmList[8]
        #lmList[8]: 指尖
        length, info, img = detector.findDistance(lmList[8][:2], lmList[12][:2], img)
        print(length)
        
        if length< 60:
            # two finger click 
            cursor = lmList[8]
            # check if in region?
            if ox < cursor[0] < ox + w and oy < cursor[1] < oy + h:
                ox,oy = cursor[0] - w//2, cursor[1] - h//2
       
    
    img[oy:oy+h, ox:ox+w ] =pic1
      
    cv2.imshow("Image", img)
    
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()