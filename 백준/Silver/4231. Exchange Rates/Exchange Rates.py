import math

while True:
    n = int(input())
    c = [0] * (n + 1)
    u = [0] * (n + 1)
    c[0] = 1000
    if n == 0:
        break
    else:
        for i in range(1, n + 1):
            num = float(input())
            c[i] = max(c[i - 1], math.floor(u[i - 1] * num * 0.97 * 100) / 100)
            u[i] = max(u[i - 1], math.floor(c[i - 1] / num * 0.97 * 100) / 100)
    print(format(c[-1], '.2f'))