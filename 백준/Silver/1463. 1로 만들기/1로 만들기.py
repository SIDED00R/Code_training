total = [0] * 1000001
N = int(input())
for i in range(1, N + 1):
    num = total[i]
    if (i + 1) <= 1e6 and (total[i + 1] == 0 or total[i + 1] > num + 1):
        total[i + 1] = num + 1
    if (i * 2) <= 1e6 and (total[i * 2] == 0 or total[i * 2] > num + 1):
        total[i * 2] = num + 1
    if (i * 3) <= 1e6 and (total[i * 3] == 0 or total[i * 3] > num + 1):
        total[i * 3] = num + 1
print(total[N])
