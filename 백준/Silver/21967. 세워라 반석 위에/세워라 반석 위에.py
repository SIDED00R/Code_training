import sys
from collections import deque, defaultdict

n = int(input())
line = list(map(int, sys.stdin.readline().split()))
stack = deque([])
dic = defaultdict(int)
answer = 0
minimum = 11
maximum = 0

for num in line:
    stack.append(num)
    dic[num] += 1
    if minimum > num:
        minimum = num
    if maximum < num:
        maximum = num

    while maximum - minimum > 2:
        leftmost = stack.popleft()
        dic[leftmost] -= 1
        if dic[leftmost] == 0:
            del dic[leftmost]
        if leftmost == minimum:
            minimum = min(dic.keys(), default=float('inf'))
        if leftmost == maximum:
            maximum = max(dic.keys(), default=float('-inf'))
        
    answer = max(answer, len(stack))

print(answer)