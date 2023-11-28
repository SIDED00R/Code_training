def rotate_key(key):
    new_key = list(map(list, zip(*key[::-1])))
    return new_key

def find(key, lock):
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if key[i][j] + lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    keys = []
    for _ in range(4):
        keys.append(key)
        key = rotate_key(key)
        
    N = len(key)    
    M = len(lock)
    min_i, min_j, max_i, max_j = M, M, 0, 0
    for i in range(M):
        for j in range(M):
            if lock[i][j] == 0:
                if i < min_i:
                    min_i = i
                if i > max_i:
                    max_i = i
                if j < min_j:
                    min_j = j
                if j > max_j:
                    max_j = j
    
    x = max_j - min_j
    y = max_i - min_i
    if y >= N or x >= N:
        return False
    else:
        new_lock = [[col for col in row[min_j : max_j + 1]] for row in lock[min_i : max_i + 1]]
        for k in keys:
            for k_i in range(N - y):
                for k_j in range(N - x):
                    new_key = [[col for col in row[k_j:k_j + x + 1]] for row in k[k_i:k_i + y + 1]]
                    if find(new_key, new_lock):
                        return True
    
    return False