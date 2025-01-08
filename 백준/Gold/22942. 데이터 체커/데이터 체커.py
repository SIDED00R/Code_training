n = int(input())
stack = []
for _ in range(n):
    x, r = map(int, input().split())
    stack.append([x - r, x + r])

stack.sort()

now_stack = []
answer = True
for idx in range(n):
    if not answer:
        break
    l, r = stack[idx]

    while now_stack:
        if now_stack[-1][1] < l:
            now_stack.pop()
        else:
            break
        
    if not now_stack:
        now_stack.append([l, r])
    else:
        if now_stack[-1][1] > r:
            now_stack.append([l, r])
        else:
            answer = False

if answer:
    print("YES")
else:
    print("NO")

