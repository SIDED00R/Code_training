def is_win(simbol, arr):
    for i in range(3):
        if arr[i] == simbol * 3:
            return True
        row = [line[i] for line in arr]
        if "".join(row) == simbol * 3:
            return True
    if arr[0][0] == simbol and arr[1][1] == simbol and arr[2][2] == simbol:
        return True
    if arr[2][0] == simbol and arr[1][1] == simbol and arr[0][2] == simbol:
        return True

def solution(board):
    o = 0
    x = 0
    
    for line in board:
        o += line.count("O")
        x += line.count("X")
        
    if x > o:
        return 0
    
    if o - 2 >= x:
        return 0
    
    if is_win("O", board) and is_win("X", board):
        return 0
    
    elif is_win("X", board) and o > x:
        return 0
    
    elif is_win("O", board) and o == x:
        return 0
    
    return 1