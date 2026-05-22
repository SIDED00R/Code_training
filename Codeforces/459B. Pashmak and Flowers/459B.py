from collections import Counter
import math
n = int(input())
count_dic = Counter(map(int, input().split()))
num_list = sorted(count_dic)
if num_list[-1] != num_list[0]:
	print(num_list[-1] - num_list[0], count_dic[num_list[-1]] * count_dic[num_list[0]])
else:
    print(0, math.comb(count_dic[num_list[0]], 2))