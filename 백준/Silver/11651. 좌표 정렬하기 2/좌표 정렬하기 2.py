import sys
n = int(sys.stdin.readline())
coordinate = []


for _ in range(n):
    coordinate.append(list(map(int, sys.stdin.readline().split())))

coordinate = sorted(coordinate, key = lambda x: [x[1], x[0]])

for num in coordinate:
    print(str(num[0]) + " " + str(num[1]))
