N, R1, C1, R2, C2 = map(int, input().split())
pattern = [chr(97 + num % 26) for num in range(N)]

n = 2 * N - 1
for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        i %= n
        j %= n
        dis = abs(N - 1 - i) + abs(N - 1 - j)
        if dis > N - 1:
            print(".", end = "")
        else:
            print(pattern[dis % 26], end = "")
    print()
        