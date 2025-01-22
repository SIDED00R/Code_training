import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

first = line[0]
second = 0
answer = []

for idx in range(1, n):
    if line[idx] > first:
        first, second = line[idx], first
    elif second < line[idx]:
        second = line[idx]
    answer.append(second)

for num in answer:
    print(num, end = " ")

