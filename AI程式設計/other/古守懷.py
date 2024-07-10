import pyautogui as pyg
import webbrowser
# 指定要打开的网站的URL
url = "https://santatracker.google.com/intl/zh-TW/matching.html"

# 使用webbrowser库打开网站
webbrowser.open(url)

# 等待2秒鐘
pyg.sleep(2)

# 初始化布林值
lodingc_bool = False 
game_over = False

# 定義绿色的颜色代碼
gDoor = (0, 139, 68)

# 鼠標移動的時間延遲
DUR = 0.01
'''
x1=425;x2=635;x3=840;x4=1050;x5=1255;x6=1465
y1=600;y2=880
endgame = (920,620)
'''
#學校電腦位置

x1=485;x2=670;x3=855;x4=1040;x5=1225;x6=1410
y1=580;y2=830
endgame = (920,620)


# 定義卡片位置，這裡使用串列來紀錄多張卡片的位置
door_positions = [[(x1, y1), (x2, y1), (x3, y1), (x4, y1), (x5, y1), (x6, y1)],
                  [(x1, y2), (x2, y2), (x3, y2), (x4, y2), (x5, y2), (x6, y2)]]
# 初始化列表以跟蹤門的顏色和背景顏色
Doorg = [[(0,0,0)]*6,[(0,0,0)]*6] 
bgcDoor = [[(0,0,0)]*6,[(0,0,0)]*6] 
# 識別綠色卡片的函數
def green_card():
    checkg = pyg.screenshot()
    #print("green")
    for r in range(2):
        for c in range(6):
            #pyg.moveTo(door_positions[r][c][0], door_positions[r][c][1], duration=DUR)
            # 獲取當前門位置處的像素顏色
            dc = checkg.getpixel(door_positions[r][c])
            # 檢查顏色 (dc) 是否與 'gDoor' 的顏色匹配
            if dc == gDoor:
                # 如果顏色匹配，將 'Doorg' 陣列中的值設置為 'gDoor'
                # 這表示當前位置具有 'gDoor' 的顏色
                Doorg[r][c] = gDoor
       
# 檢查背景顏色的函數   
def check_bg():
    for r in range(2):
        for c in range(6):
            # 檢查 'Doorg' 陣列中的值是否等於 'gDoor'
            if Doorg[r][c] == gDoor:
                # 如果值匹配 'gDoor'，則移動滑鼠到該門位置，點擊滑鼠
                pyg.moveTo(door_positions[r][c][0], door_positions[r][c][1], duration=DUR)
                pyg.click()
                # 獲取當前門位置的螢幕截圖並檢查其像素顏色
                bgcDoor[r][c] = pyg.screenshot().getpixel(door_positions[r][c])
                # 如果當前門位置的像素顏色與前一個門位置相同，則將它們的像素顏色設置為 (0,0,0)
                if bgcDoor[r][c] == bgcDoor[r][c-1]:
                    bgcDoor[r][c] = (0,0,0)
                    bgcDoor[r][c-1] = (0,0,0)
                #print("bgcDoor:", bgcDoor[r][c], "door_positions:", door_positions[r][c])
                # 執行 'loding' 函數
                loding()
                #print("----------------------")
                
# 點擊匹配顏色的函數
def click_sam_color():
    for r in range(2):
        for c in range(6):
                # 檢查 'bgcDoor' 陣列中的值是否不等於 (0, 0, 0)
                if bgcDoor[r][c] != (0, 0, 0):
                    
                    #print("bgcDoor",bgcDoor[r][c], "r:", r, "c:", c)
                    
                    for rc in range(2):
                        for cc in range(6):
                            
                            #print("bgcDoorc",bgcDoor[rc][cc], "rc:", rc, "cc:", cc)
                            # 略過相同的位置
                            if rc == r and cc == c:
                                continue
                            # 檢查是否有相同的像素顏色且不為 (0, 0, 0)
                            if bgcDoor[r][c] == bgcDoor[rc][cc] and bgcDoor[rc][cc] != (0,0,0):
                                #print("click")
                                # 移動滑鼠到第一個門位置並點擊
                                pyg.moveTo(door_positions[r][c],duration=DUR)
                                pyg.click()
                                # 將相關的像素顏色設置為 (0, 0, 0)
                                bgcDoor[r][c] = (0, 0, 0)
                                # 移動滑鼠到第二個門位置並點擊
                                pyg.moveTo(door_positions[rc][cc],duration=DUR)
                                pyg.click()
                                # 將相關的像素顏色設置為 (0, 0, 0)
                                bgcDoor[rc][cc] = (0, 0, 0)
                                # 執行 'loding' 函數
                                loding()
                                break
                            
# 重置遊戲狀態的函數
def reset():
    for r in range(2):
        for c in range(6):
            # 將 'Doorg' 陣列中的值設置為 (0, 0, 0)，表示重新初始化門的狀態
            Doorg[r][c] = (0, 0, 0)
            # 將 'bgcDoor' 陣列中的值設置為 (0, 0, 0)，表示重新初始化像素顏色狀態
            bgcDoor[r][c] = (0, 0, 0)
            
# 檢查加載屏幕的函數       
def loding():
    # 無限迴圈，直到退出
    while True:
        # 等待一段時間，以降低迴圈速度
        pyg.sleep(0.08)
        # 獲取坐標 (100, 450) 處的像素顏色
        lodingc = pyg.screenshot().getpixel((100, 450))
        #print(lodingc)
        # 檢查像素顏色是否不等於 (168, 224, 249)
        if lodingc != (168,224,249):
            # 如果顏色匹配，可以執行某些操作，例如重置或設置標誌
            #print("loding")
            # 重置相關狀態
            reset()
            # 全局變數 lodingc_bool
            global lodingc_bool
            # 設置 lodingc_bool 為 True，表示加載完成
            lodingc_bool = True 
            # 退出迴圈
            break
        # 如果顏色不匹配，可以執行其他操作
        else:
            #print("not loding")
            # 退出迴圈
            break
        
# 檢查遊戲是否結束的函數
def gameEndc():
    # 獲取坐標 (941, 604) 處的像素顏色
    endc = pyg.screenshot().getpixel(endgame)
    print(endc)
    if endc == (173,0,173):
        global lodingc_bool
        lodingc_bool = True 
        # 如果顏色匹配，將全局變數 game_over 設置為 True，表示遊戲結束
        global game_over
        game_over = True 
        
# 主遊戲循環
while not game_over:
    # 獲取坐標 (100, 450) 處的像素颜色
    lodingc = pyg.screenshot().getpixel((100, 450))
    
    if lodingc != (168,224,249):
        # 如果像素颜色不匹配，繼續等待
        continue
    
    else:
        # 如果像素颜色匹配，將 lodingc_bool 設置為 False，表示加載完成
        lodingc_bool = False
        #print("lodingc_bool:",lodingc_bool)

    while not lodingc_bool:
        green_card()  # 檢查綠色卡片
        check_bg()  # 檢查背景顏色
        click_sam_color()  # 點擊匹配的顏色
        #gameEndc()  # 檢查遊戲是否結束
        