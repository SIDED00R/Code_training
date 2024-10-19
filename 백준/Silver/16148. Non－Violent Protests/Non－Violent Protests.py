import sys

k = int(input())
for i in range(k):
    n = int(input())
    total = [0] * (n + 1)
    for num in list(map(int, sys.stdin.readline().split())):
        try:
            total[num] += 1
        except:
            continue
    answer = 0
    for idx in range(n + 1):
        answer += total[idx]
        if answer <= idx:
            break
    print(f"Data Set {i + 1}:")
    print(answer)
    print()