import pyautogui as pyg
import time

pyg.sleep(2)


gDoor = (0, 139, 68)
DUR = 0.2
x1=485;x2=670;x3=855;x4=1040;x5=1225;x6=1410
y1=580;y2=830



# 定義卡片位置，這裡使用串列來紀錄多張卡片的位置 door1=480,580 dooor2=480,830 door3=670,580
card_positions = [[(x1, y1), (x2, y1), (x3, y1), (x4, y1), (x5, y1), (x6, y1)],
                  [(x1, y2), (x2, y2), (x3, y2), (x4, y2), (x5, y2), (x6, y2)]]

Doorc = [[(0,0,0)]*6,[(0,0,0)]*6] 
bgcDoor = [[(0,0,0)]*6,[(0,0,0)]*6] 

#opened_cards = []  # 用來存放已翻開的卡片的位置
def green_card():
    beforeim = pyg.screenshot()
    for r in range(2):
        for c in range(6):
            # 移動到 x, y 座標  door[r][c][x],door[r][c][y]
            dc = beforeim.getpixel(card_positions[r][c])
            if dc == gDoor:
            #滑鼠直接點擊
                pyg.moveTo(card_positions[r][c][0], card_positions[r][c][1], duration=DUR)
                pyg.click()
                check_bg(r,c)
            #print(dc)

def check_bg(row, col):
    # 滑鼠點開後 拍下他的背景顏色 
    afterim = pyg.screenshot()
    #取得滑鼠點擊位置 doors[r][c] 的rgb
    bgc = afterim.getpixel(card_positions[row][col])
    # 放入這個儲存的空間中 
    bgcDoor[row][col] = bgc

green_card()
print(bgcDoor)
