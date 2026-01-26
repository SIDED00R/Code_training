n, k = map(int, input().split())
stack = []

for _ in range(n):
    idx, g, s, b = map(int, input().split())
    stack.append([g, s, b])
    if idx == k:
        answer = [g, s, b]
    
stack.sort()
find = False
for i, now in enumerate(stack):
    if now == answer:
        print(i + 1)
        break