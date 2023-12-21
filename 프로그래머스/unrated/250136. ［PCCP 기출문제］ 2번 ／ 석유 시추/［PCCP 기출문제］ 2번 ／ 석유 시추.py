def solution(land):
    m, n = len(land[0]), len(land)
    num = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    oil_count = [0, 0]
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                count = 0
                num += 1
                stack = []
                stack.append([i, j])
                while stack:
                    now_i, now_j = stack.pop()
                    if land[now_i][now_j] == 1:
                        count += 1
                    land[now_i][now_j] = num
                    for idx in range(4):
                        next_i = now_i + dx[idx]
                        next_j = now_j + dy[idx]
                        if next_i >= 0 and next_i < n and next_j >= 0 and next_j < m and land[next_i][next_j] == 1:
                            stack.append([next_i, next_j])
                oil_count.append(count)
    answer = 0       
    for idx in range(m):
        case = set()
        for able in range(n):
            if land[able][idx] >= 2:
                case.add(land[able][idx])
        total_oil = 0
        for able_case in case:
            total_oil += oil_count[able_case]
        if total_oil > answer:
            answer = total_oil
    return answer

