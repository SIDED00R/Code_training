N = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
total = 0
for s in size:
    total += s // t
    if s % t != 0:
        total += 1
        
print(total)
print(N // p, N % p)
