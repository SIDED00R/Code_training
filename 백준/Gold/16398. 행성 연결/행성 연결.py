import heapq
import sys
input = sys.stdin.readline

def find(num):
    if check[num] == num:
        return num
    else:
        ans = find(check[num])
        check[num] = ans
        return ans
        
def union(first, second):
    f = find(first)
    s = find(second)
    if f == s:
        return 0
    elif f > s:
        check[f] = s
    else:
        check[s] = f
    return 1
    
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

heap = []
for i in range(n):
    for j in range(i + 1, n):
        heapq.heappush(heap, [matrix[i][j], i, j])

check = [i for i in range(n)]
count = 0
answer = 0
while count != n - 1:
    w, i, j = heapq.heappop(heap)
    if union(i, j):
        count += 1
        answer += w
print(answer)