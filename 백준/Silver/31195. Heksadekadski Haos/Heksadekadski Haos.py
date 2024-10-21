answer = ["0000"] * 8
l = input().split(":")
if len(l) == 8:
    for idx, num in enumerate(l):
        added = 4 - len(num)
        answer[idx] = "0" * added + num
else:
    for idx, num in enumerate(l):
        if num == "":
            break
        else:
            added = 4 - len(num)
            answer[idx] = "0" * added + num
    count = 0
    while True:
        count -= 1
        if l[count] == "":
            break
        else:
            num = l[count]
            added = 4 - len(num)
            answer[count] = "0" * added + num
ans = ":".join(answer)
print(ans)
