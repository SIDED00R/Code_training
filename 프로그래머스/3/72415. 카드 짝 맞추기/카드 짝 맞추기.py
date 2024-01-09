from collections import defaultdict, deque
from itertools import permutations
import copy

def cost(board, now_i, now_j, next_i, next_j):
    if now_i == next_i and now_j == next_j:
        return 0
    queue = deque([[now_i, now_j, 0]])
    visited = {(now_i, now_j)}
    while queue:
        i, j, c = queue.popleft()
        for di, dj in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            ni, nj = i + di, j + dj
            ci, cj = i, j
            while True:
                ci += di
                cj += dj
                if not (0 <= ci < 4 and 0 <= cj < 4):
                    ci -= di
                    cj -= dj
                    break
                elif board[ci][cj] != 0:
                    break
            if (ni == next_i and nj == next_j) or (ci == next_i and cj == next_j):
                return c + 1
            if (0 <= ni < 4 and 0 <= nj < 4) and (ni, nj) not in visited:
                queue.append([ni, nj, c + 1])
                visited.add((ni, nj))
            if (ci, cj) not in visited:
                queue.append([ci, cj, c + 1])
                visited.add((ci, cj))
    
def check(board, dic, now_i, now_j, case, count):
    if len(case) == 0:
        return count
    first_num = case[0]
    case1 = cost(board, now_i, now_j, dic[first_num][0][0], dic[first_num][0][1]) + cost(board, dic[first_num][0][0], dic[first_num][0][1], dic[first_num][1][0], dic[first_num][1][1])
    case2 = cost(board, now_i, now_j, dic[first_num][1][0], dic[first_num][1][1]) + cost(board, dic[first_num][1][0], dic[first_num][1][1], dic[first_num][0][0], dic[first_num][0][1])

    new_board = copy.deepcopy(board)
    new_board[dic[first_num][0][0]][dic[first_num][0][1]] = 0
    new_board[dic[first_num][1][0]][dic[first_num][1][1]] = 0
    
    if case1 >= case2:
        return check(new_board, dic, dic[first_num][0][0], dic[first_num][0][1], case[1:], count + case2 + 2)
    else:
        return check(new_board, dic, dic[first_num][1][0], dic[first_num][1][1], case[1:], count + case1 + 2)


def solution(board, r, c):
    dic = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dic[board[i][j]].append([i, j])
    cards = []
    for key, values in dic.items():
        cards.append(key)   
    total_case = list(permutations(cards))
    
    answer = 1000000
    for case in total_case:
        answer = min(answer, check(board, dic, r, c, case, 0))  
    return answer