import sys
input = sys.stdin.readline

MOD = 998244353
def inverse(q):
	return pow(q, -1, MOD)

n, m = map(int, input().split())
end_point = [[] for _ in range(m + 2)]
weight = [[] for _ in range(m + 2)]
total_p = [1] * (m + 2)
denominator = 1
for _ in range(n):
	l, r, p, q = map(int, input().split())
	d = (q - p) % MOD
	end_point[l].append(r)
	weight[l].append(p * inverse(d) % MOD)
	total_p[l] = total_p[l] * d % MOD
	denominator = denominator * q % MOD

f = [0] * (m + 2)
f[m + 1] = 1
for s in range(m, 0, -1):
	now = 0
	for idx in range(len(end_point[s])):
		now += weight[s][idx] * f[end_point[s][idx] + 1]
	f[s] = now % MOD

answer = f[1]
for i in range(1, m + 1):
	answer = answer * total_p[i] % MOD
print(answer * inverse(denominator) % MOD)