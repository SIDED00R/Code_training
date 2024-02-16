import sys
input = sys.stdin.readline

def extended_gcd(a, b):
    if a == 0:
        return (0, 1)
    else:
        x, y = extended_gcd(b % a, a)
        return (y - (b // a) * x, x)

M = int(input())
answer = 0
mod = 1000000007

for _ in range(M):
    N, S = map(int, input().rstrip('\n').split())
    x, y = extended_gcd(N, mod)
    answer += (x % mod) * S
    answer %= mod
    
print(answer)
