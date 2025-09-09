from collections import defaultdict
n = int(input())
line = list(map(int, input().split()))
dic = defaultdict(int)
for num in line:
    dic[num] += 1

max_num = 0
for k, v in dic.items():
    max_num = max(max_num, v)
print(max_num)