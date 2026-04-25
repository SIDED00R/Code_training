from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

def div(num, prime_list):
    dic = defaultdict(int)
    for p in prime_list:
        while num % p == 0:
            dic[p] += 1
            num //= p
    if num != 1:
        dic[num] += 1
    return dic


prime = [0 for _ in range(1000)]
for i in range(2, 1000):
    for j in range(i * i, 1000, i):
        prime[j] = 1

prime[0] = 1
prime[1] = 1

prime_list = []
for idx in range(len(prime)):
    if prime[idx] == 0:
        prime_list.append(idx) 
        
now = defaultdict(int)
count = 0
for _ in range(n):
    a = int(input())
    d = div(a, prime_list)
    for k, v in d.items():
        if v % 2 == 0:
            continue
        else:
            if now[k] == 1:
                now[k] = 0
                count -= 1
            else:
                now[k] = 1
                count += 1
    if count == 0:
        print("DA")
    else:
        print("NE")
    