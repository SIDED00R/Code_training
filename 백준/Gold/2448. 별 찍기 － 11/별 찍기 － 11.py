import math
N = int(input())
k = int(math.log2(N // 3))
star = ["  *  ", " * * ", "*****"]
for i in range(k):
    next_star = []
    blank = " " * (3 * 2 ** i)
    for line in star:
        next_star.append(blank + line + blank)
    for line in star:
        next_star.append(line + " " + line)
    star = next_star[:]

for line in star:
    print(line)
    
