def solution(n):
    for num in range(2, n):
        if (n - 1) % num == 0:
            return num