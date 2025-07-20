import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
line = sorted(list(map(int, input().split())))
dic = defaultdict(int)
for num in line:
    dic[num] += 1

answer = 0
while line:
    length = 0
    while line and dic[line[-1]] == 0:
        line.pop()
    if not line:
        break
    last = line.pop()
    last_num = last
    dic[last] -= 1
    length += 1
    while True:
        if dic[last - 1] != 0:
            dic[last - 1] -= 1
            last -= 1
            length += 1
        else:
            break
    answer += last_num * length

print(answer)