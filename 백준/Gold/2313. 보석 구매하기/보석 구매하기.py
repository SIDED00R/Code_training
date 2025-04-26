n = int(input())
answer = 0
keep_list = []
for _ in range(n):
    l = int(input())
    line = list(map(int, input().split()))
    sum_list = [0]
    total = 0
    for num in line:
        sum_list.append(total + num)
        total = sum_list[-1]
    
    ans = -10000000
    keep_idx = [1, 1]
    for idx in range(l):
        if line[idx] > ans:
            ans = line[idx]
            keep_idx = [idx + 1, idx + 1]

    front = 1
    back = 0
    now_max = sum_list[1]
    total_min = sum_list[0]
    keep_back = -1
    while True:
        while front < l and sum_list[front] < sum_list[front + 1]:
            front += 1
        now_max = sum_list[front]

        while back < front:
            if total_min >= sum_list[back]:
                total_min = sum_list[back]
                keep_back = back
            back += 1
        
        if ans < now_max - total_min:
            ans = now_max - total_min
            keep_idx = [keep_back + 1, front]
        elif ans == now_max - total_min:
            min_length = keep_idx[1] - keep_idx[0]
            if (front - (keep_back + 1)) < min_length:
                keep_idx = [keep_back + 1, front]
                min_length = front - (keep_back + 1) + 1

        if front == l:
            break
        else:
            front += 1
            now_max = sum_list[front]

    answer += ans
    keep_list.append(keep_idx)

print(answer)
for l in keep_list:
    for num in l:
        print(num, end = " ")
    print()

