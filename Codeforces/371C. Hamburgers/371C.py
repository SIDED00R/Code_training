from collections import defaultdict

dic = defaultdict(int)
for now in input():
	dic[now] += 1
b = dic["B"]
s = dic["S"]
c = dic["C"]
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())

able = int(input())

min_answer = 0
max_answer = int(1e20)
while min_answer <= max_answer:
	mid = (min_answer + max_answer) // 2
	now_b = max(b * mid - nb, 0)
	now_s = max(s * mid - ns, 0)
	now_c = max(c * mid - nc, 0)
	total = pb * now_b + ps * now_s + pc * now_c
	if total > able:
		max_answer = mid - 1
	else:
		min_answer = mid + 1
		
print(max_answer)