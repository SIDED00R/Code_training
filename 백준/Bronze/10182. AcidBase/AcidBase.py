import math

n = int(input())
for _ in range(n):
    simbol, _, num = input().split()
    now = math.log10(float(num))
    if simbol == "H":
        print(format(-now, ".2f"))
    else:
        print(format(14 + now, ".2f"))