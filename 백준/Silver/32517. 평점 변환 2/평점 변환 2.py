import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
answer = line[:]

total = line[0]
if answer[0] == 0:
    print(-1)
    exit()

for idx in range(1, n):
    if total > (line[idx] + 1) * idx:
        answer[idx] = line[idx] + 1
    elif total <= line[idx] * idx:
        answer[idx] = line[idx]
    else:
        print(-1)
        exit()
    total += answer[idx]

for num in answer:
    if 1 <= num <= 1e9:
        continue
    else:
        print(-1)
        exit()

ans = map(str, answer)
print(" ".join(ans))