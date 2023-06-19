import tkinter as tk
import tkinter.messagebox

def choose_mode():
    global player
    root.withdraw()
    mode_window = tk.Toplevel(root)
    mode_window.title('選擇遊戲模式')
    two_player_button = tk.Button(mode_window, text='兩人遊戲', command=lambda: start_game(mode_window, 'two_player'))
    two_player_button.pack()
    ai_button = tk.Button(mode_window, text='AI 對戰', command=lambda: start_game(mode_window, 'ai'))
    ai_button.pack()

def start_game(mode_window, mode):
    global player
    root.deiconify()
    mode_window.destroy()
    player = 'X'
    for i in range(3):
        for j in range(3):
            b[i][j] = tk.Button(root, font=('Arial', 60), width=4, height=2,
                                command=lambda i=i, j=j: on_click(i,j))
            b[i][j].grid(row=i,column=j)
            board[i][j] = 0
    if mode == 'ai':
        ai_move()

def ai_move():
    # 在這裡添加 AI 的程式碼
    pass

def on_click(i, j):
    global player
    if board[i][j] == 0:
        if player == 'X':
            b[i][j].configure(text='X')
            board[i][j] = 'X'
            player = 'O'
        else:
            b[i][j].configure(text='O')
            board[i][j] = 'O'
            player = 'X'
        winner = check_winner()
        if winner:
            tk.messagebox.showinfo(title='遊戲結束', message=f'{winner} 玩家獲勝！')
            reset_board()
            choose_mode()
        elif is_tie():
            tk.messagebox.showinfo(title='遊戲結束', message='平局！')
            reset_board()
            choose_mode()

def reset_board():
    global board
    for i in range(3):
        for j in range(3):
            b[i][j].configure(text='')
            board[i][j] = 0

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    return None

def is_tie():
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True

root = tk.Tk()
root.title('圈圈叉叉遊戲')
player = 'X'
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = [[None, None, None], [None, None, None], [None, None, None]]
for i in range(3):
    for j in range(3):
        b[i][j] = tk.Button(root, font=('Arial', 60), width=4, height=2,
                            command=lambda i=i, j=j: on_click(i,j))
        b[i][j].grid(row=i,column=j)

choose_mode()
root.mainloop()
