def solution(board, h, w):
    answer = 0
    N = len(board)
    blank = ["no"] * (N + 2)
    board = [blank] + [["no"] + line + ["no"] for line in board] + [blank]
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    now = board[h + 1][w + 1]
    for i in range(4):
        if now == board[h + dh[i] + 1][w + dw[i] + 1]:
            answer += 1
        
    return answer