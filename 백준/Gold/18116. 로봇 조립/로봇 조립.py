import sys
input = sys.stdin.readline

def find(num, parents):
    if parents[num] != num:
        parents[num] = find(parents[num], parents)
    return parents[num]

def union(first, second, parents, total):
    num1 = find(first, parents)
    num2 = find(second, parents)
    if num1 < num2:
        parents[num2] = num1
        total[num1] += total[num2]
    elif num1 > num2:
        parents[num1] = num2
        total[num2] += total[num1]
    

n = int(input())
parents = [i for i in range(int(1e6) + 1)]
total = [1 for i in range(int(1e6) + 1)]
for _ in range(n):
    line = list(input().split())
    if line[0] == "I":
        first = int(line[1])
        second = int(line[2])
        union(first, second, parents, total)
    else:
        num = int(line[1])
        node = find(num, parents)
        print(total[node])
