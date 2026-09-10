def find(num, p):
	count = 0
	now_num = num
	for r in p:
		while now_num % r == 0:
			count += 1
			now_num //= r
	if now_num != 1:
		count += 1
	return count

total_p = [0 for _ in range(40000)]
p = []
for idx in range(2, 40000):
	if total_p[idx] == 0:
		p.append(idx)
		for i in range(idx, 40000, idx):
			total_p[i] = 1	
			
t = int(input())
for _ in range(t):
	a, b, k = map(int, input().split())
	if k == 1:
		if (a % b == 0 or b % a == 0) and a != b:
			print("YES")
		else:
			print("NO")
	else:
		a_count = find(a, p)
		b_count = find(b, p)
		if a_count + b_count < k:
			print("NO")
		else:
			print("YES")