from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('River crossing puzzle')
window.geometry("800x600")
window.resizable(width=0, height=0)
#     人狼楊蔡
#      0 1 2 3
judge=[0,0,0,0]

def humanmove():
    if(judge[0]==0):
        human.place(x=550,y=200)
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
        human.place(x=0,y=200)
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
    if(judge[0]==0 and judge[2]==0):
        human.place(x=550,y=200)
        sheep.place(x=650,y=250)
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
        human.place(x=0,y=200)
        sheep.place(x=100,y=250)
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
    if(judge[0]==0 and judge[3]==0):
        human.place(x=550,y=200)
        cabbage.place(x=700,y=250)
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
        human.place(x=0,y=200)
        cabbage.place(x=150,y=250)
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
    if(judge[0]==0 and judge[1]==0):
        human.place(x=550,y=200)
        wolf.place(x=750,y=250)
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
        human.place(x=0,y=200)
        wolf.place(x=200,y=250)
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

grass_gif = PhotoImage(file="Rivercrossingpuzzle\grass.gif")
human_gif = PhotoImage(file="Rivercrossingpuzzle\human.gif")
sheep_gif = PhotoImage(file="Rivercrossingpuzzle\sheep.gif")
wolf_gif = PhotoImage(file="Rivercrossingpuzzle\wolf.gif")
cabbage_gif = PhotoImage(file="Rivercrossingpuzzle\cabbage.gif")
sea_gif = PhotoImage(file="Rivercrossingpuzzle\sea.gif")

grass1=Label(window,image=grass_gif)
grass2=Label(window,image=grass_gif)
human=Label(window,image=human_gif)
sheep=Label(window,image=sheep_gif)
wolf=Label(window,image=wolf_gif)
cabbage=Label(window,image=cabbage_gif)
sea=Label(window,image=sea_gif)

sea.place(x=250,y=300)
grass1.place(x=0,y=300)
grass2.place(x=550,y=300)
human.place(x=0,y=200)
sheep.place(x=100,y=250)
wolf.place(x=200,y=250)
cabbage.place(x=150,y=250)

human_btn=Button(window,text="人",width=10,command=humanmove)
sheep_btn=Button(window,text="羊",width=10,command=sheepmove)
wolf_btn=Button(window,text="狼",width=10,command=wolfmove)
cabbage_btn=Button(window,text="菜",width=10,command=cabbagemove)

human_btn.place(x=50,y=100)
sheep_btn.place(x=150,y=100)
wolf_btn.place(x=250,y=100)
cabbage_btn.place(x=350,y=100)

window.mainloop()