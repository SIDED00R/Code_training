import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
prime_idx = [False for _ in range(N + 1)]
prime = []
for i in range(2, N + 1):
    if not prime_idx[i]:
        prime.append(i)
        for idx in range(i, N + 1, i):
            prime_idx[idx] = True

prime = sorted(prime, reverse = True)
stack = deque()
total = 0
answer = 0
while prime:
    now = prime.pop()
    stack.append(now)
    total += now
    while total >= N:
        if total == N:
            answer += 1
        out = stack.popleft()
        total -= out
        
print(answer)
        
