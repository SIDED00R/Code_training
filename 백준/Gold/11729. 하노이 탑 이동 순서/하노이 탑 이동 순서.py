import sys
input = sys.stdin.readline

count = 0

def hanoi(n, a, b, c):
    global count
    count += 1
    if n == 1:
        total.append([a, c])
        return
    hanoi(n - 1, a, c, b)
    total.append([a, c])
    hanoi(n - 1, b, a, c)
    return

total = []
K = int(input())
hanoi(K, 1, 2, 3)
print(count)
for l in total:
    print(l[0], l[1])