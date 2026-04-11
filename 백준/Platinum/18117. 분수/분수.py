import sys
input = sys.stdin.readline

def v_factor(x, f):
    cnt = 0
    while x % f == 0:
        x //= f
        cnt += 1
    return cnt, x
def get_block_coprime(num, den, start, length):
    if den == 1:
        return "0" * length
    rem = (num * pow(10, start - 1, den)) % den
    val = (rem * (10 ** length)) // den
    return str(val).zfill(length)
    
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    i, n = map(int, input().split())
    r = a % b
    p, temp = v_factor(b, 2)
    q, c = v_factor(temp, 5)
    m = max(p, q)
    prefix = []
    rem = r
    for _ in range(m):
        rem *= 10
        prefix.append(str(rem // b))
        rem %= b
    ans = []
    if i <= m:
        take = min(n, m - i + 1)
        ans.append(''.join(prefix[i - 1:i - 1 + take]))
        n -= take
        i += take
    if n > 0:
        if c == 1:
            ans.append("0" * n)
        else:
            d = (2 ** p) * (5 ** q)
            num2 = rem // d  
            start = i - m
            ans.append(get_block_coprime(num2, c, start, n))
    print(''.join(ans))