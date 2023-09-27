import sys
n = int(sys.stdin.readline())

peoples = []
answer = []

for _ in range(n):
    peoples.append(list(map(int, sys.stdin.readline().split())))

for people in peoples:
    count = 0
    for p in peoples:
        if people[0] < p[0] and people[1] < p[1]:
            count += 1
    answer.append(str(count + 1))

print(" ".join(answer))
