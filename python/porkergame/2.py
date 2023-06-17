import tkinter as tk
from tkinter import messagebox

root= tk.Tk()
root.geometry('300x200')

def ExitApp():
    MsgBox = tk.messagebox.askquestion ('Exit App','Really Quit?',icon = 'error')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Welcome Back','Welcome back to the App')
        
buttonEg = tk.Button (root, text='Exit App',command=ExitApp)
buttonEg.pack()
  
root.mainloop()