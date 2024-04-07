import sys
input = sys.stdin.readline

N = int(input())
k = 0
while N != 1:
    N //= 3
    k += 1
    
before = ["*"]

for _ in range(k):
    next_box = []
    for i in range(3):
        if i == 1:
            for line in before:
                next_box.append(line + " " * len(line) + line)
        else:
            for line in before:
                next_box.append(line * 3)
    before = next_box[:]

for l in before:
    print(l)