import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(num, parents):
    if parents[num] != num:
        parents[num] = find(parents[num], parents)
    return parents[num]

def union(first, second, parents):
    num1 = find(first, parents)
    num2 = find(second, parents)
    if num1 < num2:
        parents[num2] = num1
    else:
        parents[num1] = num2

n , m = map(int, input().split())
parents = [i for i in range(n + 1)]

for _ in range(m):
    case, a, b = map(int, input().split())
    if case:
        num1 = find(a, parents)
        num2 = find(b, parents)
        if num1 == num2:
            print("YES")
        else:
            print("NO")
    else:
        union(a, b, parents)
    