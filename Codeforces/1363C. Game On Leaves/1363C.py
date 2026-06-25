from collections import defaultdict
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    route = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        route[u].append(v)
        route[v].append(u)
    if len(route[x]) <= 1:
        print("Ayush")
    elif n % 2 == 0:
        print("Ayush")
    else:
        print("Ashish")