from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui
import random

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

    # 计算鼠标移动方向
    delta_x = target_x - current_x
    delta_y = target_y - current_y

    # 移动鼠标
    pyautogui.move(delta_x, delta_y)

def check_and_click(hand_info, circles):
    index_finger_tip = hand_info['lmList'][8]  # 食指指尖
    thump_tip = hand_info['lmList'][4]  # 母指指尖
    index_finger_pip = hand_info['lmList'][6]  # 食指第三關節

    # 使用 findDistance 方法計算食指第三關節和母指指尖之間的距離
    length, _, _ = detector.findDistance(index_finger_pip[:2], thump_tip[:2])

    # 判斷是否在節點4和節點6的範圍內
    if length < 31:  # 假設節點4在節點6上面
        # 檢查列表是否為空
        if circles:
            # 檢查食指指尖是否在圓點的範圍內
            circle_x, circle_y = circles[0]
            if (
                circle_x - 20 < index_finger_tip[0] < circle_x + 20 and
                circle_y - 20 < index_finger_tip[1] < circle_y + 20
            ):
                # 點擊到了，增加分數並移除被點擊的圓點
                circles.pop(0)
                return True
    return False


# 创建一个空列表来存储圆点的信息
circles = []

def generate_circle(screen_width, screen_height):
    # 生成一个随机的圆点坐标
    circle_x = random.randint(50, screen_width - 50)
    circle_y = random.randint(50, screen_height - 50)
    return circle_x, circle_y

def draw_circles(img, circles):
    for circle in circles:
        cv2.circle(img, circle[:2], 20, (0, 255, 0), cv2.FILLED)

# CAP_DSHOW is for windows speed up
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)  # 指定補抓影像的寬
cap.set(4, 480)  # 指定補抓影像的高

detector = HandDetector(detectionCon=0.70)

# 禁用安全模式
#pyautogui.FAILSAFE = False

score = 0

# 主循環中的一部分
while True:
    success, img = cap.read()
    if not success or img is None:
        # 檢查圖像是否為空，如果為空則終止循環
        print("Error reading image from camera.")
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False, draw=True)

    if hands and len(hands) > 0:
        hand = hands[0]

        img_width, img_height = cap.get(3), cap.get(4)
        screen_width, screen_height = pyautogui.size()

        #move_mouse(hand, img_width, img_height, screen_width, screen_height)

        # 检查是否点击到圆点并增加分数
        if check_and_click(hand, circles):
            score += 1
            print(f"Score: {score}")

    # 在這裡確保這兩個變數是定義的
    screen_width, screen_height = pyautogui.size()

    # 以一定的概率生成新的圆点
    if random.random() < 0.02:
        circles.append(generate_circle(screen_width, screen_height))

    # 繪制所有的圆点
    draw_circles(img, circles)

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
