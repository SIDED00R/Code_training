n, m = map(int, input().split())
matrix = []
left_num = []
start_list = []
for _ in range(n):
    line = list(map(int, input().split()))
    count = line[0]
    check = line[1:]
    if count == m or count == 0:
        print('NO')
        exit()
    matrix.append(check)
    
    left_count = 0
    for idx, now_node in enumerate(check):
        if now_node == 1:
            left_count += 1
        elif now_node == -1:
            start_list.append(idx)
            break
    left_num.append(count - left_count)


able_case = []
for j in range(m):
    correct = False
    for i in range(n):
        if matrix[i][j] == 1:
            correct = True
    if not correct:
        able_case.append(j)

# start_list : -1이 시작
# able_case: 못맞출 가능성 있는 위치
# left_num: 맞출 가능성 있는 개수

for idx in range(n):
    if left_num[idx] != 0:
        num = left_num[idx]
        start = start_list[idx]
        if start <= able_case[0]:
            able_case = able_case[num:]
        else:
            print('NO')
            exit()
        if able_case == []:
            print('YES')
            exit()
if able_case == []:
    print('YES')
else:
    print('NO')