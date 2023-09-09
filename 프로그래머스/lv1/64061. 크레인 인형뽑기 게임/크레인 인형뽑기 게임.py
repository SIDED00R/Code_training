def solution(board, moves):
    board = list(map(list, zip(*board[::-1])))
    box = []
    answer = 0
    for move in moves:
        if len(board[move - 1]) == 0:
            continue
        while board[move - 1][-1] == 0 and len(board[move - 1]) != 0:
            board[move - 1].pop()
        doll = board[move - 1].pop()
        box.append(doll)
        if len(box) > 1:
            if box[-1] == box[-2]:
                box.pop()
                box.pop()
                answer += 2

    return answer