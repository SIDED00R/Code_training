import sys

n = int(input())

answer = 0
for i in range(1, n):
    a = i
    find = i
    while a != 0:
        r = a % 10
        a //= 10
        find += r
    if find == n:
        answer = i
        break
print(answer)
