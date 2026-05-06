n = int(input())
stack = []
for _ in range(n):
    a, b = map(int, input().split())
    stack.append([a, b])
    
s_stack = sorted(stack)
answer = True
for i in range(1, n):
    if s_stack[i - 1][1] < s_stack[i][1]:
        continue
    else:
        answer = False
        
if not answer:
    print("Happy Alex")
else:
    print("Poor Alex")