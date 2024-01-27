import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

N = int(input())
heap = []
dic = defaultdict(int)
for _ in range(N):
    num = int(input())
    if num == 0:
        try:
            out = heapq.heappop(heap)
            if dic[-out] != 0:
                dic[-out] -= 1
                print(-out)
            else:
                dic[out] -= 1
                print(out)
        except:
            print(0)
    else:
        dic[num] += 1
        if num < 0:
            heapq.heappush(heap, -num)
        else:
            heapq.heappush(heap, num)