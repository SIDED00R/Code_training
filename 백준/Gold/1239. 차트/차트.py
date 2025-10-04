from itertools import permutations
from collections import deque

n = int(input())
line = list(map(int, input().split()))

answer = 0

for now_case in permutations(line, n):
    now_answer = 0
    total = 0
    double_count = False
    popout = False
    stack = deque()
    for num in now_case:
        total += num
        stack.append(num)
        while total > 50:
            out = stack.popleft()
            total -= out
            popout = True
        if total == 50:
            if not popout:
                double_count = True
            now_answer += 1
    if double_count:
        now_answer -= 1
    answer = max(answer, now_answer)
print(answer)
            