def prime(a, b):
    answer = 1
    for num in range(1, int(a ** 0.5) + 1):
        if a % num == 0:
            if num <= b:
                answer = max(answer, num)
            else:
                break
            if (a // num) <= b:
                answer = max(answer, a // num)
    return answer

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p = prime(n, k)
    print(n // p)