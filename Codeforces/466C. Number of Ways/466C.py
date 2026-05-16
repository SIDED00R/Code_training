from collections import defaultdict
import bisect
import math

n = int(input())
line = list(map(int, input().split()))
total = sum(line)
if total % 3 != 0:
    print(0)
    exit()
bound = total // 3
p_sum = [0]
idx = 0
dic = defaultdict(list)
for num in line:
    idx += 1
    p_sum.append(p_sum[-1] + num)
    if p_sum[-1] in [bound, bound * 2]:
        dic[p_sum[-1]].append(idx)
if bound == 0:
    if len(dic[0]) >= 3:
        print(math.comb(len(dic[0]) - 1, 2))
    else:
        print(0)
    exit()
first_point = 0
f_list = dic[bound]
s_list = dic[bound * 2]
answer = 0
while first_point < len(f_list):
    first_idx = f_list[first_point]
    answer += len(s_list) - bisect.bisect_right(s_list, first_idx)
    first_point += 1
print(answer)