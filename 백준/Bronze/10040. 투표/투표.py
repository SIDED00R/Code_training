n, m = map(int, input().split())
fun = []
for _ in range(n):
    fun.append(int(input()))
weight = [0 for _ in range(n)]
for _ in range(m):
    w = int(input())
    for idx, num in enumerate(fun):
        if w >= num:
            weight[idx] += 1
            break
            
answer = 0
max_count = 0
for idx, count in enumerate(weight):
    if count > max_count:
        max_count = count
        answer = idx
        
print(answer + 1)