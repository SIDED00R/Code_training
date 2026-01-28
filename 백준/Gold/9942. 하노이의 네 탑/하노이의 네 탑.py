i = 0
while True:
    i += 1
    try:
        n = int(input())
        m = int(((8 * n + 1) ** 0.5 - 1) // 2)
        answer = pow(2, m) * (n - m * (m - 1) // 2 - 1) + 1
        print(f"Case {i}: {answer}")
    except:
        break