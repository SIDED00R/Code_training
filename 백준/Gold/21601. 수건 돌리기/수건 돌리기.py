def start_first(n, k):
    if (n + 1) // 2 >= k:
        return 2 * k - 1
    if n % 2 == 0:
        return 2 * start_first(n // 2, k - n // 2)
    else:
        return 2 * start_second(n // 2, k - n // 2)

def start_second(n, k):
    if n // 2 >= k:
        return 2 * k
    if n % 2 == 0:
        return start_second(n // 2, k - n // 2) * 2 - 1
    else:
        return start_first((n + 1) // 2, k - n // 2) * 2 - 1

n, k = map(int, input().split())
print(start_first(n, k))

