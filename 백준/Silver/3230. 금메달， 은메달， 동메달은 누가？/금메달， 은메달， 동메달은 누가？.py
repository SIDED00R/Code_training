n, m = map(int, input().split())
stack = [0]
for i in range(1, n + 1):
    now = int(input())
    stack = stack[:now] + [i] + stack[now:]
    
new_stack = [0]
for num in stack[m:0:-1]:
    now = int(input())
    new_stack = new_stack[:now] + [num] + new_stack[now:]
    
for idx in range(3):
    print(new_stack[idx + 1])