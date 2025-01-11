import sys
input = sys.stdin.readline

n = int(input())

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

l = sorted(l, key = lambda x: x[0] - x[1], reverse = True)

answer = 0
height = 0
for i in range(n):
    up, down = l[i]
    answer += height + up
    height += up - down

answer += min(0, height) * -n
print(answer)