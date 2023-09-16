def hanoi(start, mid, end, n, move):
    if n == 1:
        move.append([start, end])
    else: 
        hanoi(start, end, mid, n - 1, move)
        hanoi(start, mid, end, 1, move)
        hanoi(mid, start, end, n - 1, move)
    return move

def solution(n):
    answer = []
        
    return hanoi(1, 2, 3, n, answer)