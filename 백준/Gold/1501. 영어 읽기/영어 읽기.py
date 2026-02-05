from collections import defaultdict

dic = defaultdict(lambda: defaultdict(int))
single = defaultdict(int)

n = int(input())
for _ in range(n):
    line = list(input())
    if len(line) == 1:
        single[line[0]] += 1
    else:
        stack_dic = defaultdict(int)
        for alp in line[1:-1]:
            stack_dic[alp] += 1
        key = tuple(sorted(stack_dic.items()))
        dic[(line[0], line[-1])][key] += 1

m = int(input())
for _ in range(m):
    line = list(input().split())
    total = 1
    for word in line:
        if len(word) == 1:
            total *= single.get(word, 0)
        else:
            stack_dic = defaultdict(int)
            for alp in word[1:-1]:
                stack_dic[alp] += 1
            key = tuple(sorted(stack_dic.items()))
            if (word[0], word[-1]) in dic and key in dic[(word[0], word[-1])]:
                total *= dic[(word[0], word[-1])][key]
            else:
                total *= 0

    print(total)