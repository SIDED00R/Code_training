N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
i, j = 0, 0
answer = []
while True:
    if A[i] > B[j]:
        answer.append(B[j])
        j += 1
        if j == M:
            answer += A[i:]
            break
    else:
        answer.append(A[i])
        i += 1
        if i == N:
            answer += B[j:]
            break
        
for num in answer:
    print(num, end = ' ')