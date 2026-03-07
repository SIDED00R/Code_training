MOD = 1000000007

p = int(input())
q = int(input())
n = int(input())
k = int(input())

if k == 0:
    print(0)
    exit()
elif k == n:
    print(1)
    exit()
elif q * 2 == p:
    a, b = k, n
else:
    up = p - q     
    down = q    
    a = pow(up, n - k, MOD) * (pow(up, k, MOD) - pow(down, k, MOD)) % MOD
    b = (pow(up, n, MOD) - pow(down, n, MOD)) % MOD
result = a * pow(b, MOD-2, MOD) % MOD
print(result)