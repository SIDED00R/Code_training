c = int(input())
for _ in range(c):
    n = int(input())
    answer = 1e10
    for a in range(1, int(n ** 0.5) + 1):
        if n % a != 0:
            continue
        else:
            left = n // a
        for b in range(1, int(left ** 0.5) + 2):
            if left % b != 0:
                continue
            else:
                c = left // b
                if a == min(a, b, c):
                    answer = min(answer, 2 * (a * b + b * c + c * a))
                    
    print(answer)
    