import sys
input = sys.stdin.readline
n = int(input())
stack = [1, 1]
total_sum = [1, 2]
for _ in range(n):
    sim, x, y = map(int, input().split())
    if sim == 1:
        if (total_sum[y] - total_sum[x - 1]) == y - x + 1:
            now_ans = 1
        else:
            now_ans = 0
    else:
        if (total_sum[y] - total_sum[x - 1]) == 0:
            now_ans = 1
        else:
            now_ans = 0
    stack.append(now_ans)
    total_sum.append(total_sum[-1] + now_ans)

for idx in range(2, len(stack)):
    if stack[idx] == 1:
        print('Yes')
    else:
        print('No')