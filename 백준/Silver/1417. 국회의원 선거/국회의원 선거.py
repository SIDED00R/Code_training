import heapq

N = int(input())
vote = []
for _ in range(N):
    vote.append(-int(input()))
    if N == 1:
        print(0)
        exit()
dasom = vote[0]
left = vote[1:]
heapq.heapify(left)

count = 0
while -dasom <= -left[0]:
    count += 1
    top = heapq.heappop(left)
    dasom -= 1
    heapq.heappush(left, top + 1)
    
print(count)