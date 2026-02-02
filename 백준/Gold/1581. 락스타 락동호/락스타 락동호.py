ff, fs, sf, ss = map(int, input().split())
answer = 0
if fs > 0:
    answer += ff
    answer += ss
    if fs > sf:
        answer += sf * 2 + 1
    else:
        answer += fs * 2
elif ff > 0:
    answer = ff
else:
    answer = ss
    if sf > 0:
        answer += 1

print(answer)