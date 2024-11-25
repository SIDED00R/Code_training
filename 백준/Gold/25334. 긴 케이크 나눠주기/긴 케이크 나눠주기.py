import sys 
input = sys.stdin.readline

def precompute_factorials(max_n, mod):
    fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], mod - 2, mod)
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact

def comb(n, r, fact, inv_fact, mod):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    line = list(map(int, list(input())[:-1]))
    total = sum(line)
    if total == 0:
        fact, inv_fact = precompute_factorials(n, 1000000007)
        print(comb(n - 1, k - 1, fact, inv_fact, 1000000007) % 1000000007)
        continue
    count = total // k
    if total % k != 0:
        print(0)
        continue
    answer = []
    now_count = count
    find = False
    for num in line:
        if num == 1:
            if find:
                find = False
                answer.append(now_answer)
                now_count = count
            now_count -= 1
            if now_count == 0:
                find = True
                now_answer = 1
        else:
            if find:
                now_answer += 1
    
    ans = 1
    for num in answer:
        ans *= num
        ans %= 1000000007
    print(ans)

