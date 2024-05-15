N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    line = list(map(int, list(input())))
    A.append(line)
for _ in range(N):
    line = list(map(int, list(input())))
    B.append(line)    

count = 0
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            count += 1
            for di in range(3):
                for dj in range(3):
                    A[di + i][dj + j] = [1, 0][A[di + i][dj + j]]
                    
if A == B:
    print(count)
else:
    print(-1)