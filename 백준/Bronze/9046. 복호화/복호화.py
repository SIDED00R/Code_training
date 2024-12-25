from collections import defaultdict
n = int(input())
for _ in range(n):
    letter = input()
    dic = defaultdict(int)
    for alpha in letter:
        if alpha == " ":
            continue
        else:
            dic[alpha] += 1
    max_num = 0
    max_idx = ""
    for k, v in dic.items():
        if v > max_num:
            max_num = v
            max_idx = k
        elif v == max_num:
            max_idx = "?"
    print(max_idx)
            