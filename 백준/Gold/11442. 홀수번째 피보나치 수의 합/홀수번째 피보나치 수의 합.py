def matrix_mul(A, B):
    answer = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j] += A[i][k] * B[k][j]
                answer[i][j] %= 1000000007
    return answer
                

def mul(n):
    if n == 1:
        return [[1, 1], [1, 0]]
    if n % 2 == 1:
        temp = mul(n - 1)
        return matrix_mul(temp, [[1, 1], [1, 0]])
    else:
        temp = mul(n // 2)
        return matrix_mul(temp, temp)
        
n = int(input())
if n % 2 == 1:
    n += 1

print(mul(n-1)[0][0])