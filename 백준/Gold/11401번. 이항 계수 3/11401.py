MOD = 1_000_000_007
N, r = map(int, input().split()) 

fact = [1] * (N + 1)
for i in range(1, N + 1):
	fact[i] = fact[i - 1] * i % MOD

inv_fact = [1] * (N + 1)
inv_fact[N] = pow(fact[N], MOD - 2, MOD)
for i in range(N, 0, -1):
	inv_fact[i - 1] = inv_fact[i] * i % MOD

def comb(n, r):
	if r < 0 or r > n:
		return 0
	return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

print(comb(N, r))