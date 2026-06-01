from collections import defaultdict
n = int(input())
dic = defaultdict(int)
stack = []
for _ in range(n):
    name, score = input().split()
    stack.append([name, int(score)])
    dic[name] += int(score)

max_name = []
max_score = 0

for k, v in dic.items():
    if v > max_score:
        max_score = v
        max_name = [k]
    elif v == max_score:
        max_name.append(k)
        
if len(max_name) == 1:
    print(max_name[0])
else:
    answer_dic = defaultdict(int)
    for now_case in stack:
        name, score = now_case
        if name in max_name:
            answer_dic[name] += score
            if answer_dic[name] >= max_score:
                print(name)
                exit()