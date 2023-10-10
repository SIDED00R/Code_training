import sys

N = int(input())

line = list(map(int, sys.stdin.readline().split()))

line = sorted(line, reverse = True)

answer = 0
for i in range(len(line)):
    answer += line[i] * (1 + i)
print(answer)
