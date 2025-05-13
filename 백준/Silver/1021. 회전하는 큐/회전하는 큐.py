from collections import deque

n, m = map(int, input().split())
line = list(map(int, input().split()))
stack = [i for i in range(1, n + 1)]
answer = 0
for now_num in line:
    if stack[0] == now_num:
        stack = stack[1:]
    else:
        length = len(stack)
        for idx in range(length):
            if stack[idx] == now_num:
                break
        answer += min(idx, length - idx)
        stack = stack[idx + 1:] + stack[:idx]

print(answer)
        
