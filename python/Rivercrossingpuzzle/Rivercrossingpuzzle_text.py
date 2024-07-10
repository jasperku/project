import os
from tkinter import *
from tkinter import messagebox

# 创建Tk对象
window = Tk()
window.title('River crossing puzzle')
window.geometry("800x600")
window.resizable(width=0, height=0)

#     人狼楊蔡
#      0 1 2 3
judge=[0,0,0,0]

canvas = None  # 用于存储Canvas对象
human = None   # 用于存储人物图像对象

def humanmove():
    global human
    if(judge[0]==0):
        canvas.move(human, 550, 0)
        judge[0]=1
        if(judge==[1,0,0,0]):
            msgbox=messagebox.askokcancel("GAME OVER!","狼吃掉羊了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[0,1,1,0] or judge==[1,0,0,1]):
            msgbox=messagebox.askokcancel("GAME OVER!","狼吃掉羊了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[1,1,1,1]):
            msgbox=messagebox.askokcancel("GAME WIN!","恭喜把狼、羊、菜運過河了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[0,0,1,1] or judge==[1,1,0,0]):
            msgbox=messagebox.askokcancel("GAME OVER!","羊吃掉菜了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
    elif(judge[0]==1):
        canvas.move(human, -550, 0)
        judge[0]=0
        if(judge==[0,1,1,0] or judge==[1,0,0,1]):
            msgbox=messagebox.askokcancel("GAME OVER!","狼吃掉羊了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[1,1,1,1]):
            msgbox=messagebox.askokcancel("GAME WIN!","恭喜把狼、羊、菜運過河了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[0,0,1,1] or judge==[1,1,0,0]):
            msgbox=messagebox.askokcancel("GAME OVER!","羊吃掉菜了!\n確認是否離開")
            if msgbox == True:
                window.destroy()

def sheepmove():   
    global human, sheep
    if(judge[0]==0 and judge[2]==0):
        canvas.move(human, 550, 0)
        canvas.move(sheep, 550, 0)
        judge[0]=1
        judge[2]=1
        if(judge==[0,1,1,0] or judge==[1,0,0,1]):
            msgbox=messagebox.askokcancel("GAME OVER!","狼吃掉羊了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[1,1,1,1]):
            msgbox=messagebox.askokcancel("GAME WIN!","恭喜把狼、羊、菜運過河了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[0,0,1,1] or judge==[1,1,0,0]):
            msgbox=messagebox.askokcancel("GAME OVER!","羊吃掉菜了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
    elif(judge[0]==1 and judge[2]==1):
        canvas.move(human, -550, 0)
        canvas.move(sheep, -550, 0)
        judge[0]=0
        judge[2]=0
        if(judge==[0,1,1,0] or judge==[1,0,0,1]):
            msgbox=messagebox.askokcancel("GAME OVER!","狼吃掉羊了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[1,1,1,1]):
            msgbox=messagebox.askokcancel("GAME WIN!","恭喜把狼、羊、菜運過河了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[0,0,1,1] or judge==[1,1,0,0]):
            msgbox=messagebox.askokcancel("GAME OVER!","羊吃掉菜了!\n確認是否離開")
            if msgbox == True:
                window.destroy()

def cabbagemove():   
    global human, cabbage
    if(judge[0]==0 and judge[3]==0):
        canvas.move(human, 550, 0)
        canvas.move(cabbage, 550, 0)
        judge[0]=1
        judge[3]=1
        if(judge==[0,1,1,0] or judge==[1,0,0,1]):
            msgbox=messagebox.askokcancel("GAME OVER!","狼吃掉羊了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[1,1,1,1]):
            msgbox=messagebox.askokcancel("GAME WIN!","恭喜把狼、羊、菜運過河了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[0,0,1,1] or judge==[1,1,0,0]):
            msgbox=messagebox.askokcancel("GAME OVER!","羊吃掉菜了!\n確認是否離開")
            if msgbox == True:
                window.destroy()    
    elif(judge[0]==1 and judge[3]==1):
        canvas.move(human, -550, 0)
        canvas.move(cabbage, -550, 0)
        judge[0]=0
        judge[3]=0
        if(judge==[0,1,1,0] or judge==[1,0,0,1]):
            msgbox=messagebox.askokcancel("GAME OVER!","狼吃掉羊了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[1,1,1,1]):
            msgbox=messagebox.askokcancel("GAME WIN!","恭喜把狼、羊、菜運過河了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[0,0,1,1] or judge==[1,1,0,0]):
            msgbox=messagebox.askokcancel("GAME OVER!","羊吃掉菜了!\n確認是否離開")
            if msgbox == True:
                window.destroy()

def wolfmove():    
    global human, wolf
    if(judge[0]==0 and judge[1]==0):
        canvas.move(human, 550, 0)
        canvas.move(wolf, 550, 0)
        judge[0]=1
        judge[1]=1
        if(judge==[0,1,1,0] or judge==[1,0,0,1]):
            msgbox=messagebox.askokcancel("GAME OVER!","狼吃掉羊了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[1,1,1,1]):
            msgbox=messagebox.askokcancel("GAME WIN!","恭喜把狼、羊、菜運過河了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[0,0,1,1] or judge==[1,1,0,0]):
            msgbox=messagebox.askokcancel("GAME OVER!","羊吃掉菜了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
    elif(judge[0]==1 and judge[1]==1):
        canvas.move(human, -550, 0)
        canvas.move(wolf, -550, 0)
        judge[0]=0
        judge[1]=0
        if(judge==[0,1,1,0] or judge==[1,0,0,1]):
            msgbox=messagebox.askokcancel("GAME OVER!","狼吃掉羊了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[1,1,1,1]):
            msgbox=messagebox.askokcancel("GAME WIN!","恭喜把狼、羊、菜運過河了!\n確認是否離開")
            if msgbox == True:
                window.destroy()
        if(judge==[0,0,1,1] or judge==[1,1,0,0]):
            msgbox=messagebox.askokcancel("GAME OVER!","羊吃掉菜了!\n確認是否離開")
            if msgbox == True:
                window.destroy()

def load_images():
    try:
        # 获取当前脚本文件的绝对路径
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 定义图像对象
        window.grass_gif = PhotoImage(file=os.path.join(script_dir, "Rivercrossingpuzzle", "grass.gif"))
        window.human_gif = PhotoImage(file=os.path.join(script_dir, "Rivercrossingpuzzle", "human.gif"))
        window.sheep_gif = PhotoImage(file=os.path.join(script_dir, "Rivercrossingpuzzle", "sheep.gif"))
        window.wolf_gif = PhotoImage(file=os.path.join(script_dir, "Rivercrossingpuzzle", "wolf.gif"))
        window.cabbage_gif = PhotoImage(file=os.path.join(script_dir, "Rivercrossingpuzzle", "cabbage.gif"))
        window.sea_gif = PhotoImage(file=os.path.join(script_dir, "Rivercrossingpuzzle", "sea.gif"))
        
        return window.grass_gif, window.human_gif, window.sheep_gif, window.wolf_gif, window.cabbage_gif, window.sea_gif
    except TclError as e:
        print(f"TclError: {e}")
        
def create_canvas():
    global canvas
    canvas = Canvas(window, width=800, height=600)
    canvas.pack()
    return canvas

def create_image(canvas, x, y, image):
    return canvas.create_image(x, y, anchor=NW, image=image)

def main():
    global window
    global judge
    global canvas
    global human, sheep, wolf, cabbage
    
    grass_gif, human_gif, sheep_gif, wolf_gif, cabbage_gif, sea_gif = load_images()
    canvas = create_canvas()

    grass1 = create_image(canvas, 0, 300, grass_gif)
    grass2 = create_image(canvas, 550, 300, grass_gif)
    human = create_image(canvas, 0, 200, human_gif)
    sheep = create_image(canvas, 100, 250, sheep_gif)
    wolf = create_image(canvas, 200, 250, wolf_gif)
    cabbage = create_image(canvas, 150, 250, cabbage_gif)
    sea = create_image(canvas, 250, 300, sea_gif)

    human_btn = Button(window, text="人", width=10, command=humanmove)
    sheep_btn = Button(window, text="羊", width=10, command=sheepmove)
    wolf_btn = Button(window, text="狼", width=10, command=wolfmove)
    cabbage_btn = Button(window, text="菜", width=10, command=cabbagemove)

    human_btn.place(x=50, y=100)
    sheep_btn.place(x=150, y=100)
    wolf_btn.place(x=250, y=100)
    cabbage_btn.place(x=350, y=100)

    window.mainloop()

if __name__ == "__main__":
    main()