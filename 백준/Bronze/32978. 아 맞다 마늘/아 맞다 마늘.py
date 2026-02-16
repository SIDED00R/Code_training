n = int(input())
stack = list(input().split())
check = list(input().split())
while True:
    if stack[-1] in check:
        stack.pop()
    else:
        print(stack[-1])
        break