h, m, s = map(int, input().split())
time = int(input())
ts = time % 60
time //= 60
tm = time % 60
th = time // 60

answer_s = s + ts
if answer_s >= 60:
    m += (answer_s // 60)
    answer_s %= 60
answer_m = m + tm
if answer_m >= 60:
    h += (answer_m // 60)
    answer_m %= 60
answer_h = (h + th) % 24

print(answer_h, answer_m, answer_s)