from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui
import time


def move_mouse(hand_info, img_width, img_height, screen_width, screen_height):
    index_finger_tip = hand_info['lmList'][8]  # 食指指尖

    cursor_x = index_finger_tip[0]  # 获取食指指尖的 x 坐标
    cursor_y = index_finger_tip[1]  # 获取食指指尖的 y 坐标

    # 假设 cursor_x 和 cursor_y 是手部追踪得到的坐标
    cursor_percentage_x = round(cursor_x / img_width, 3)  # x 坐标的百分比
    cursor_percentage_y = round(cursor_y / img_height, 3)  # y 坐标的百分比

    target_x = int(cursor_percentage_x * screen_width)
    target_y = int(cursor_percentage_y * screen_height)

    # 获取当前鼠标位置
    current_x, current_y = pyautogui.position()

    # 計算食指指尖移動距離
    distance = ((target_x - current_x) ** 2 + (target_y - current_y) ** 2) ** 0.5

    # 如果移動距離超過15，則移動鼠標
    if distance > 15:
        # 计算鼠标移动方向
        delta_x = target_x - current_x
        delta_y = target_y - current_y

        # 移动鼠标
        pyautogui.move(delta_x, delta_y)
        time.sleep(0.15)

def check_and_click(hand_info):
    thump_tip = hand_info['lmList'][4]  # 母指指尖
    index_finger_pip = hand_info['lmList'][6]  # 食指第三關節
    
    # 使用 findDistance 方法计算食指第三關節和母指指尖之间的距离
    length, _, _ = detector.findDistance(index_finger_pip[:2], thump_tip[:2])
    
    # 判断是否在节点4和节点6的范围内
    if length < 31:  # 假设节点4在节点6上面
        pyautogui.click()  # 模拟鼠标左键点击
        time.sleep(0.5)
        print("click")

# CAP_DSHOW is for windows speed up
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)  # 指定補抓影像的寬
cap.set(4, 480)  # 指定補抓影像的高

detector = HandDetector(detectionCon=0.70)

# 禁用安全模式
# pyautogui.FAILSAFE = False

while True:
    success, img = cap.read()
    if not success or img is None:
        # 检查图像是否为空，如果为空则终止循环
        print("Error reading image from camera.")
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False, draw=False)

    if hands and len(hands) > 0:
        hand = hands[0]
        
        img_width, img_height = cap.get(3), cap.get(4)
        screen_width, screen_height = pyautogui.size()
        
        move_mouse(hand, img_width, img_height, screen_width, screen_height)
        check_and_click(hand)

    #cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()