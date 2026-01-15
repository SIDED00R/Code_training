import sys
input = sys.stdin.readline

n, m = map(int, input().split())

house = []
for _ in range(n):
    p, c = map(int, input().split())
    house.append([p, c])

house.sort()

answer = 0
count = 0
for now in house:
    p, c = now
    answer += max(0, c - count)
    count = c

print(answer)