import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())

jewel = []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jewel, (M, V))
    
bag = []
for _ in range(K):
    c = int(input())
    heapq.heappush(bag, c)

able_steal = []
answer = 0
while bag:
    now_bag = heapq.heappop(bag)
    while jewel and jewel[0][0] <= now_bag:
        heapq.heappush(able_steal, -heapq.heappop(jewel)[1])
    if able_steal:
        answer += -heapq.heappop(able_steal)
    else:
        continue
    
print(answer)