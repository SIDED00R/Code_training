def check(matrix, m):
    line = [0] * (7 * m)
    for i in range(7):
        for j in range(m):
            line[7 * j + i] = matrix[i][j]

    line.append('X')

    long = 0 # 최장길이
    now_long = 0 # 국소 최장 길이
    
    freeze_count = 0 # 프리즈 개수
    now_freeze_count = 0 # 국소 프리즈 개수
    not_added_freeze = 0
    
    start_idx = 0
    start_idx_keep = 0
    
    fail_count = 0
    
    start = False # 스트릭이 이미 시작 했는지 여부
    for idx in range(7 * m + 1):
        now = line[idx]
        if now == 'O':
            if start:
                now_long += 1
                now_freeze_count += not_added_freeze
                not_added_freeze = 0
            else:
                start = True
                now_long = 1
                start_idx_keep = idx
        elif now == 'F':
            if start:
                not_added_freeze += 1
            else:
                continue
        else:
            fail_count += 1
            if start:
                start = False
                not_added_freeze = 0
                if long < now_long:
                    long = now_long
                    freeze_count = now_freeze_count
                    start_idx = start_idx_keep
                elif long == now_long:
                    if freeze_count > now_freeze_count:
                        freeze_count = now_freeze_count
                        start_idx = start_idx_keep
                now_long = 0
                now_freeze_count = 0
            else:
                continue
    return [long, freeze_count, start_idx, fail_count]

n, m = map(int, input().split())
answer = []
for _ in range(n):
    name = input()
    now_matrix = []
    for _ in range(7):
        now_matrix.append(list(input()))

    answer.append(check(now_matrix, m) + [name])

answer = sorted(answer, key = lambda x: [-x[0], x[1], x[2], x[3]])
j = 0
for i, now in enumerate(answer):
    if i == 0:
        print(f'{i + 1}. {now[-1]}')
    else:
        if answer[i][:-1] == answer[i - 1][:-1]:
            j += 1
        print(f'{i + 1 - j}. {now[-1]}')