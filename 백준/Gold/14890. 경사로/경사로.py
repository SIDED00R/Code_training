def able(now_list, l):
    n = len(now_list)
    put_able = [True for _ in range(n)]
    for idx in range(1, n):
        if now_list[idx] == now_list[idx - 1]:
            continue
        elif now_list[idx] + 1 == now_list[idx - 1]:
            if n < idx + l:
                return 0
            key = now_list[idx]
            for now_i in range(idx, idx + l):
                if now_list[now_i] != key:
                    return 0
            for now_i in range(idx, idx + l):
                if put_able[now_i] != True:
                    return 0
                put_able[now_i] = False
        elif now_list[idx] - 1 == now_list[idx - 1]:
            if 0 > idx - l:
                return 0
            key = now_list[idx - 1]
            for now_i in range(idx - 1, idx - l - 1, -1):
                if now_list[now_i] != key:
                    return 0
            for now_i in range(idx - 1, idx - l - 1, -1):
                if put_able[now_i] != True:
                    return 0
                put_able[now_i] = False
        else:
            return 0
    return 1

n, l = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

answer = 0
for i in range(n):
    answer += able(matrix[i], l)
    now_l = []
    for j in range(n):
        now_l.append(matrix[j][i])
    answer += able(now_l, l)
print(answer)