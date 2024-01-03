import sys

input = sys.stdin.readline
N, r, c = map(int, input().split())

length = 2 ** N
check = []
front_di, front_dj = 0, 0
back_di, back_dj = length, length
for _ in range(N):
    middle_di = (front_di + back_di) // 2
    middle_dj = (front_dj + back_dj) // 2
    now = 0
    if middle_dj > c:
        back_dj = middle_dj
        now += 0
    else:
        front_dj = middle_dj
        now += 1
    if middle_di > r:
        back_di = middle_di
        now += 0
    else:
        front_di = middle_di
        now += 2
    check.append(now)

answer = 0
now_num = 2 ** (2 * N)
for num in check:
    now_num //= 4
    answer += num * now_num

print(answer)