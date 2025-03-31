n = int(input())
tree = list(map(int, input().split()))
dic = {i:[] for i in range(n)}

for idx in range(n):
    t = tree[idx]
    if t == -1:
        continue
    dic[t].append(idx)

e = int(input())

stack = [e]
next_stack = [e]
while next_stack:
    out = next_stack.pop()
    next_list = dic[out]
    stack.extend(next_list)
    next_stack.extend(next_list)

for s in stack:
    del dic[s]

answer = 0
for k, v in dic.items():
    count = 0
    for idx in v:
        if idx in dic:
            count += 1
    if count == 0:
        answer += 1

print(answer)
