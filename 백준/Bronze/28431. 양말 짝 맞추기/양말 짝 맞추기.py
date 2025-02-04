from collections import defaultdict
socks = defaultdict(int)
for _ in range(5):
    n = int(input())
    socks[n] += 1
    
for k, v in socks.items():
    if v % 2 != 0:
        print(k)
    