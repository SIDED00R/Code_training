n = int(input())

num = [0 for _ in range(n + 1)]
num[0] = 1
num[1] = 1

answer = 1

for idx in range(2, n + 1):
    if num[idx] == 0:
        for i in range(idx, n + 1, idx):
            num[i] = 1
        now = idx
        while now <= n:
            now  *= idx
        answer *= now
        answer //= idx
        answer %= 987654321

print(answer)