from collections import defaultdict

n = int(input())
stack = []
for _ in range(n):
    stack.append(input())
    
answer = 0
for idx in range(len(stack[0])):
    dic = defaultdict(int)
    for now_num in stack:
        dic[now_num[idx:]] += 1
    if len(dic) == n:
        answer = idx
    else:
        break
        
print(len(stack[0]) - answer)