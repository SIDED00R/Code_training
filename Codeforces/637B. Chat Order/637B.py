from collections import defaultdict

dic = defaultdict(int)

n = int(input())
for idx in range(n):
    name = input()
    dic[name] = idx
    
stack = []
for k, v in dic.items():
    stack.append([v, k])
    
for now in sorted(stack, reverse  = True):
    print(now[1])