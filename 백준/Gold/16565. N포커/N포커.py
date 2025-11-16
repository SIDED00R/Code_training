import math

n = int(input())

def fact(n):
    mod = 10007
    fact_list = [1]
    for i in range(1, n + 1):
        fact_list.append(fact_list[-1] * i % mod)

    inv_fact_list = [1 for _ in range(n + 1)]
    inv_fact_list[n] = pow(fact_list[-1], mod - 2, mod)
    for i in range(n, 0, -1):
        inv_fact_list[i - 1] = inv_fact_list[i] * i % mod

    return fact_list, inv_fact_list

def comb_mod(n, r, fact_list, inv_fact_list):
    return (fact_list[n] * inv_fact_list[r] * inv_fact_list[n - r]) % 10007

fact_list, inv_fact_list = fact(52)

answer = []
for i in range(1, 14):
    now = i * 4
    left = n - now
    if left < 0:
        break
    now_answer = 1
    now_answer *= math.comb(13, i)
    now_answer *= comb_mod(52 - now, left, fact_list, inv_fact_list)
    now_answer %= 10007
    answer.append(now_answer)

ans = 0
for idx, num in enumerate(answer):
    if idx % 2 == 0:
        ans += num
    else:
        ans -= num

print(ans % 10007)