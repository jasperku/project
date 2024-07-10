import pyautogui as pyg

pyg.sleep(5)
posx,posy=200,650
#障礙物的顏色
obstacleColor = (83,83,83)

# 滑鼠移動到開始的位置 
pyg.moveTo(posx,posy, duration=1)
#啟動遊戲
pyg.click()

# 定義障礙物
def isObstacle(im):
    for i in range(140):
        c = im.getpixel((posx+i,posy))
        if c == obstacleColor:
            return True
    return False

def isObstaclebirds(im):
    for i in range(140):
        c = im.getpixel((220+i,580))
        if c == obstacleColor:
            return True
    return False

while True:
    #先擷取目前的畫面 以作為等一下判斷有沒有障礙物
    im = pyg.screenshot()
    
    if isObstacle(im):
        pyg.keyDown('up')
        pyg.keyUp('up')
    if isObstaclebirds(im):
        pyg.keyDown('down')
        pyg.keyUp('down')