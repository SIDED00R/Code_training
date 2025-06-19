from collections import deque

n = int(input())
line = sorted(list(map(int, input().split())))
if n < 3:
    print(n)
else:
    answer = 0
    ans_list = deque()
    for num in line:
        while len(ans_list) >= 2 and ((ans_list[0] + ans_list[1]) <= num):
            ans_list.popleft()
        ans_list.append(num)
        answer = max(answer, len(ans_list))
    print(answer)
