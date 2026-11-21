import sys
from collections import Counter

input = sys.stdin.readline

m, n = map(int, input().split())

sig_counter = Counter()

for _ in range(m):
	line = list(map(int, input().split()))

	sorted_unique = sorted(set(line))
	rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
	size = len(sorted_unique)

	tree = [0] * (size + 1)
	seen = [0] * (size + 1)

	signature = [0] * (2 * n)
	idx = 0
	for v in line:
		x = rank[v]
		less = 0
		i = x - 1
		while i > 0:
			less += tree[i]
			i -= i & (-i)

		equal = seen[x]

		signature[idx] = less
		signature[idx + 1] = equal
		idx += 2

		seen[x] += 1

		i = x
		while i <= size:
			tree[i] += 1
			i += i & (-i)

	sig_counter[tuple(signature)] += 1

ans = 0
for cnt in sig_counter.values():
	ans += cnt * (cnt - 1) // 2

print(ans)