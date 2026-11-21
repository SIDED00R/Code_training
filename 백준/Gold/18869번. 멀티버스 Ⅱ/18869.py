from collections import Counter

def make_fenwick(size):
	tree = [0] * (size + 1)
	
	def update(i):
		while i <= size:
			tree[i] += 1
			i += i & (-i)
			
	def query(i):
		s = 0
		while i > 0:
			s += tree[i]
			i -= i & (-i)
		return s

	return update, query

m, n = map(int, input().split())

sig_counter = Counter()

for _ in range(m):
	line = list(map(int, input().split()))

	sorted_unique = sorted(set(line))
	rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
	size = len(sorted_unique)

	update, query = make_fenwick(size)

	signature = []
	for now_node in line:
		x = rank[now_node]
		less = query(x - 1)
		total = query(x)
		equal = total - less
		signature.append(less)
		signature.append(equal)
		update(x)

	sig_counter[tuple(signature)] += 1

ans = 0
for cnt in sig_counter.values():
	ans += cnt * (cnt - 1) // 2

print(ans)