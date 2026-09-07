import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n = int(input())
	a_list = list(map(int, input().split()))

	total_sum = 0
	min_plus_p = min_plus_m = float('inf')
	max_minus_p = max_minus_m = -float('inf')
	for idx in range(n):
		now_weight = a_list[idx]
		i = idx + 1
		if i % 2 == 1:
			total_sum += now_weight
			if 2 * now_weight + i < min_plus_p:
				min_plus_p = 2 * now_weight + i
			if 2 * now_weight - i < min_plus_m:
				min_plus_m = 2 * now_weight - i
		else:
			total_sum -= now_weight
			if 2 * now_weight + i > max_minus_p:
				max_minus_p = 2 * now_weight + i
			if 2 * now_weight - i > max_minus_m:
				max_minus_m = 2 * now_weight - i

	best = n - 1 if n % 2 == 1 else n - 2
	if best < 0:
		best = 0

	if n >= 2:
		best = max(best, max_minus_p - min_plus_p, max_minus_m - min_plus_m)

	print(total_sum + max(0, best))