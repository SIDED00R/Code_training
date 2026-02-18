t = int(input())
for _ in range(t):
    n = int(input())
    stack = []
    visited = [False for _ in range(n)]
    for _ in range(n):
        stack.append(int(input()) - 1)
    count = 0
    now = 0
    visited[0] = True
    while True:
        count += 1
        now = stack[now]
        if now == n - 1:
            print(count)
            break
        elif visited[now]:
            print(0)
            break
        visited[now] = True