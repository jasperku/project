import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置窗口和游戏参数
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Game")

# 定义颜色
white = (0, 0, 0)

# 加载音符图像
note_image = pygame.image.load("note.png")  # 请替换为你的音符图像

# 设置音符的初始位置和速度
note_x = random.randint(0, screen_width - note_image.get_width())
note_y = -note_image.get_height()
note_speed = 5

# 游戏循环
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 移动音符
    note_y += note_speed

    # 绘制背景和音符
    screen.fill(white)
    screen.blit(note_image, (note_x, note_y))

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

pygame.quit()
