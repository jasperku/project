from cvzone.HandTrackingModule import HandDetector
import cv2
import math

# 初始化手部检测器
detector = HandDetector(detectionCon=0.8, maxHands=1)

# 读取视频流
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    # 检测手部
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]  # 假设只检测到一个手

        # 获取手腕和食指指尖的坐标
        wrist = hand['lmList'][0]
        index_finger_tip = hand['lmList'][8]

        # 计算手的旋转角度
        angle = math.degrees(math.atan2(index_finger_tip[1] - wrist[1], index_finger_tip[0] - wrist[0]))
        angle = (angle + 360) % 360
        # 在图像上绘制旋转角度
        cv2.putText(img, f'旋轉角度: {int(angle)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # 显示图像
    cv2.imshow("手部追踪", img)

    # 检测按键，如果按下 'q' 键则退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
