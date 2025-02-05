n = int(input())
for _ in range(n):
    time_list = []
    answer = 0
    while True:
        s, f = map(int, input().split())
        if s == 0 and f == 0:
            break
        else:
            time_list.append([f - s, s, f])
    time_list.sort()
    able_time = [0] * 10
    for now_case in time_list:
        diff, s, f = now_case
        find = True
        for idx in range(s, f):
            if able_time[idx] == 1:
                find = False
                break
        if find:
            for idx in range(s, f):
                able_time[idx] = 1
            answer += 1
    print(answer)