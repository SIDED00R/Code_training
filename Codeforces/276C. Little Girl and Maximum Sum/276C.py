n, q = map(int, input().split())
line = list(map(int, input().split()))
p_sum = [0] * (n + 2)
for _ in range(q):
	l, r = map(int, input().split())
	p_sum[l] += 1
	p_sum[r + 1] -= 1
	
stack = []
for idx in range(1, n + 2):
	p_sum[idx] += p_sum[idx - 1]
	stack.append(p_sum[idx])
sort_stack = sorted(stack[:-1])
sort_line = sorted(line)
answer = 0
for idx in range(n):
	answer += sort_stack[idx] * sort_line[idx]
print(answer)