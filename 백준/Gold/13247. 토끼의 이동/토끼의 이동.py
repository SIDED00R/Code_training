from itertools import combinations

def move(l, board):
    length = len(l)
    next_l = [[0, -1] for _ in range(length - 1)]
    for idx in range(length):
        able, before = l[idx]
        if able == 0:
            continue
        if idx in [length - 1, length - 2]:
            if next_l[idx - 1] == [0, -1]:
                next_l[idx - 1] = [1, idx]
            else:
                next_l[idx - 1] = [2, idx]
        elif idx == 0:
            if next_l[1] == [0, -1]:
                next_l[1] = [1, idx]
            else:
                next_l[1] = [2, idx]
        else:
            simbol = board[idx]
            if simbol == 'W':
                if next_l[idx - 1] == [0, -1]:
                    next_l[idx - 1] = [1, idx]
                else:
                    next_l[idx - 1] = [2, idx]
            elif simbol == 'B':
                if next_l[idx + 1] == [0, -1]:
                    next_l[idx + 1] = [1, idx]
                else:
                    next_l[idx + 1] = [2, idx]
            else:
                if before == -1:
                    if next_l[idx - 1] == [0, -1]:
                        next_l[idx - 1] = [1, idx]
                    else:
                        next_l[idx - 1] = [2, idx]
                else:
                    if next_l[before] == [0, -1]:
                        next_l[before] = [1, idx]
                    else:
                        next_l[before] = [2, idx]
    for idx in range(length - 1):
        now_case = next_l[idx]
        if now_case[0] == 2:
            next_l[idx] = [0, -1]
    return next_l
    

board = list(input())
length = len(board)
r = int(input())
total_count = 0
answer = 0
for now_case in combinations(range(length), r):
    total_count += 1
    rabbit = [[0, -1] for _ in range(length)]
    for idx in now_case:
        rabbit[idx] = [1, -1]

    while len(rabbit) > 2:
        rabbit = move(rabbit, board)
    for now_case in rabbit:
        if now_case[0] == 1:
            answer += 1
print(answer / total_count)