def possible(x, n, row):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True   

def nqueen(x, n, row, check, answer):
    if x == n:
        answer += 1
    else:
        for i in range(n):
            if check[i]:
                continue
            row[x] = i
            if possible(x, n, row):
                check[i] = True
                answer = nqueen(x + 1, n, row, check, answer)
                check[i] = False
    return answer

def solution(n):
    row = [0 for _ in range(n)]
    check = [False for _ in range(n)]
    answer = 0
    return nqueen(0, n, row, check, answer)