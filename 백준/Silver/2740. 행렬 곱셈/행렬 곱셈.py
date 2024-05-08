N, M = map(int, input().split())
A = []
for _ in range(N):
    line = list(map(int, input().split()))
    A.append(line)
M, K = map(int, input().split())
B = []
for _ in range(M):
    line = list(map(int, input().split()))   
    B.append(line)
    
answer = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        for k in range(K):
            answer[i][k] += A[i][j] * B[j][k]

for i in range(N):
    for j in range(K):
        print(answer[i][j], end = " ")
    print()