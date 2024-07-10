# 偵測手部 
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#指定影像的寬
cap.set(3, 800)
#指定影像的高
cap.set(4,600)

detector= HandDetector(detectionCon=0.7) # confidence 的程度

# 載入圖片  例 Image/img1.jpg
pic1 = cv2.imread("img1.jpg")
# 告知載入的圖片要放在整個畫面的位置 
ox,oy = 150,150

# show image

while True:
    success, img = cap.read()
    # 翻轉影像 
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img, draw=True, flipType=False)
    
    # 放入我圖片的位置 h:height, w:weight, _: channel 
    h, w, _ = pic1.shape
    img[oy:oy+h, ox:ox+w ] = pic1
    
    # 我的攝影機抓到的畫面+載入的圖片
    cv2.imshow("Image",img)
    
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    
# 釋放我的資源, 關閉視窗
cap.release()
cv2.destroyAllWindows()

# 判斷 手與圖片是否有交集
# 如果有 判斷是否要移動圖片?  判斷條件: 中指指間與食指的指尖 間隔