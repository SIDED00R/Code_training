import sys
input = sys.stdin.readline

t = int(input())
for t_num in range(t):
    w, n = map(int, input().split())
    line = list(map(int, input().split()))
    line.sort()

    mid_idx = (w - 1) // 2
    mid_num = line[mid_idx]
    now_sum = 0

    for idx in range(w):
        num = line[idx]
        now_sum += abs(mid_num - num)
        line.append(num + n)

    answer = now_sum
    for idx in range(w):
        mid_num = line[mid_idx]
        mid_idx += 1
        a = mid_num - line[idx]
        b = line[idx] + n - mid_num

        if w % 2 == 0:
            now_sum = now_sum - a + b - (line[mid_idx] - mid_num) * 2
        else:
            now_sum = now_sum - a + b - (line[mid_idx] - mid_num)
        answer = min(answer, now_sum)

    print(f"Case #{t_num + 1}: {answer}")