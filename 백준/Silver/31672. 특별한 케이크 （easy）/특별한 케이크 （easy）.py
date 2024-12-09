import sys
_ = input()
N = int(input())

check = [[False] * N for _ in range(N)]
student = [0] * N
cnt = 0

for i in range(N):
    M = int(input())
    students = list(map(int, input().split()))
    B = int(input())

    if B:
        for s in students:
            check[i][s - 1] = True
    else:
        for j in range(N):
            check[i][j] = True
        for s in students:
            check[i][s - 1] = False

for i in range(N):
    for j in range(N):
        if i != j:
            if check[j][i]:
                student[i] += 1
        else:
            if not check[j][i]:
                student[i] += 1
    if student[i] == N:
        cnt += 1

if cnt == 0:
    print("swi")
else:
    result = [str(i + 1) for i in range(N) if student[i] == N]
    print(" ".join(result))
