from itertools import product
import copy

def check(copy_map, i, j, count, N):
    if copy_map[i][j] == 0:
        return count
    elif copy_map[i][j] == 1:
        count += 3
        copy_map[i][j] = (copy_map[i][j] + 3) % 4
        copy_map[i + 1][j] = (copy_map[i + 1][j] + 3) % 4
        if i < N - 2:
            copy_map[i + 2][j] = (copy_map[i + 2][j] + 3) % 4
        if j > 0:
            copy_map[i + 1][j - 1] = (copy_map[i + 1][j - 1] + 3) % 4
        if j < N - 1:
            copy_map[i + 1][j + 1] = (copy_map[i + 1][j + 1] + 3) % 4
    elif copy_map[i][j] == 2:
        count += 2
        copy_map[i][j] = (copy_map[i][j] + 2) % 4
        copy_map[i + 1][j] = (copy_map[i + 1][j] + 2) % 4
        if i < N - 2:
            copy_map[i + 2][j] = (copy_map[i + 2][j] + 2) % 4
        if j > 0:
            copy_map[i + 1][j - 1] = (copy_map[i + 1][j - 1] + 2) % 4
        if j < N - 1:
            copy_map[i + 1][j + 1] = (copy_map[i + 1][j + 1] + 2) % 4
    elif copy_map[i][j] == 3:
        count += 1
        copy_map[i][j] = (copy_map[i][j] + 1) % 4
        copy_map[i + 1][j] = (copy_map[i + 1][j] + 1) % 4
        if i < N - 2:
            copy_map[i + 2][j] = (copy_map[i + 2][j] + 1) % 4
        if j > 0:
            copy_map[i + 1][j - 1] = (copy_map[i + 1][j - 1] + 1) % 4
        if j < N - 1:
            copy_map[i + 1][j + 1] = (copy_map[i + 1][j + 1] + 1) % 4
    return count

def solution(clockHands):
    N = len(clockHands)
    first_lines = list(product([0, 1, 2, 3], repeat = N))
    min_move = 4 * N * N
    
    for first_line in first_lines:
        now_move = 0
        copy_map = copy.deepcopy(clockHands)
        for idx, num in enumerate(first_line):
            if num == 0:
                continue
            elif num == 1:
                now_move += 3
                copy_map[0][idx] = (copy_map[0][idx] + 3) % 4
                copy_map[1][idx] = (copy_map[1][idx] + 3) % 4
                if idx > 0:
                    copy_map[0][idx - 1] = (copy_map[0][idx - 1] + 3) % 4
                if idx < N - 1:
                    copy_map[0][idx + 1] = (copy_map[0][idx + 1] + 3) % 4
            elif num == 2:
                now_move += 2
                copy_map[0][idx] = (copy_map[0][idx] + 2) % 4
                copy_map[1][idx] = (copy_map[1][idx] + 2) % 4
                if idx > 0:
                    copy_map[0][idx - 1] = (copy_map[0][idx - 1] + 2) % 4
                if idx < N - 1:
                    copy_map[0][idx + 1] = (copy_map[0][idx + 1] + 2) % 4
            elif num == 3:
                now_move += 1
                copy_map[0][idx] = (copy_map[0][idx] + 1) % 4
                copy_map[1][idx] = (copy_map[1][idx] + 1) % 4
                if idx > 0:
                    copy_map[0][idx - 1] = (copy_map[0][idx - 1] + 1) % 4
                if idx < N - 1:
                    copy_map[0][idx + 1] = (copy_map[0][idx + 1] + 1) % 4
                    
        for i in range(N - 1):
            for j in range(N):
                now_move = check(copy_map, i, j, now_move, N)
                
        if sum(copy_map[N - 1]) == 0:
            if min_move > now_move:
                min_move = now_move

    return min_move