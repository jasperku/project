import numpy as np

# 极大极小算法
def minimax(board, depth, maximizing_player):
    # 终止条件
    if depth == 0 or game_over(board):
        return evaluate(board)
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves(board):
            new_board = make_move(board, move, 'X')
            eval = minimax(new_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves(board):
            new_board = make_move(board, move, 'O')
            eval = minimax(new_board, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# 判断游戏是否结束
def game_over(board):
    # 检查行
    for i in range(15):
        for j in range(11):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4] != ' ':
                return True
    # 检查列
    for i in range(11):
        for j in range(15):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j] != ' ':
                return True
    # 检查对角线
    for i in range(11):
        for j in range(11):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4] != ' ':
                return True
            if board[i][j+4] == board[i+1][j+3] == board[i+2][j+2] == board[i+3][j+1] == board[i+4][j] != ' ':
                return True
    return False

# 评估当前棋盘局势
def evaluate(board):
    score = 0
    # 检查行
    for i in range(15):
        for j in range(11):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4] == 'X':
                score += 100  # 玩家X连成五子
            elif board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4] == 'O':
                score -= 100  # 玩家O连成五子
    # 检查列
    for i in range(11):
        for j in range(15):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j] == 'X':
                score += 100  # 玩家X连成五子
            elif board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j] == 'O':
                score -= 100  # 玩家O连成五子
    # 检查对角线
    for i in range(11):
        for j in range(11):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4] == 'X':
                score += 100  # 玩家X连成五子
            elif board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4] == 'O':
                score -= 100  # 玩家O连成五子
            if board[i][j+4] == board[i+1][j+3] == board[i+2][j+2] == board[i+3][j+1] == board[i+4][j] == 'X':
                score += 100  # 玩家X连成五子
            elif board[i][j+4] == board[i+1][j+3] == board[i+2][j+2] == board[i+3][j+1] == board[i+4][j] == 'O':
                score -= 100  # 玩家O连成五子
    return score


# 获取合法移动列表
def legal_moves(board):
    moves = []
    for i in range(15):
        for j in range(15):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# 在棋盘上放置棋子
def make_move(board, move, player):
    new_board = np.copy(board)
    new_board[move[0]][move[1]] = player
    return new_board

# 主程序
def play():
    board = np.array([[' ']*15 for _ in range(15)])
    depth = 3  # 搜索深度
    while True:
        print(board)
        if game_over(board):
            print("游戏结束")
            break
        move = None
        if input("你是X，请输入你的下棋位置(x, y):") == 'q':
            break
        while move not in legal_moves(board):
            x, y = map(int, input().split(','))
            move = (x, y)
        board = make_move(board, move, 'X')

        # AI下棋
        ai_move = None
        max_eval = float('-inf')
        for move in legal_moves(board):
            new_board = make_move(board, move, 'O')
            eval = minimax(new_board, depth - 1, False)
            if eval > max_eval:
                max_eval = eval
                ai_move = move
        board = make_move(board, ai_move, 'O')

play()