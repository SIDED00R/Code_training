import heapq

n = int(input())
answer = []
for _ in range(n):
    b, p, q, r = map(int, input().split())
    heapq.heappush(answer, [p * q * r, p + q + r, b])

for _ in range(3):
    print(heapq.heappop(answer)[2], end = " ")