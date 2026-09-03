def count_combinations_optimized(x, y):
	if y >= (x * x) // 3:
		return x * (x - 1) * (x - 2) // 6

	total_count = 0
	for a in range(1, x - 1):
		max_b = min(x - a - 1, (y - a) // (a + 1))
		
		if max_b < 1:
			break
			
		for b in range(1, max_b + 1):
			limit1 = x - a - b
			limit2 = (y - a * b) // (a + b)
			
			total_count += min(limit1, limit2)
			
	return total_count

t = int(input())
for _ in range(t):
	n, x = map(int, input().split())
	print(count_combinations_optimized(x, n))