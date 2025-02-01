n, w = map(int, input().split())
line = list(map(int, input().split()))
line.sort()

if line[-1] > w:
    print("-1")

elif n == 1:
    print(1)

elif line[0] + line[1] > w:
    print("-1")

else:
    count = 0
    for idx in range(1, n):
        if line[0] + line[idx] > w:
            count += 1

    answer = count * 4 + (n - count) * 2 - 3
    print(answer)