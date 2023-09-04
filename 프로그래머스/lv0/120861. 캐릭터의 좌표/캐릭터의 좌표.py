def solution(keyinput, board):
    i, j = 0, 0
    ni = board[0] // 2
    nj = board[1] // 2
    for key in keyinput:
        if key == "left" and i != -ni:
            i -= 1
        elif key == "right" and i != ni:
            i += 1
        elif key == "up" and j != nj:
            j += 1
        elif key == "down" and j != -nj:
            j -= 1
            
    return [i, j]