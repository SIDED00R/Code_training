n, k = map(int, input().split())
ans_list = []
for num in range(1, int(n ** 0.5) + 1):
	if n % num == 0:
		ans_list.append(num)
		if num != n // num:
			ans_list.append(n // num)
			
s_list = sorted(ans_list)
if len(s_list) < k:
	print(0)
else:
	print(s_list[k - 1])