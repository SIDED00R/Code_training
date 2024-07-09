n, s = map(int, input().split())
m = int(input())
eat = n - s - m
times = []
for _ in range(m):
    times.append(int(input()))
    
if eat <= 0:
    print(n - s)   
    exit()
    
find = False
now_time = 0

while not find:
    now_time += 1    
    total = 0
    for t in times:
        total += now_time // t
    if total >= eat:
        find = True    

zeros = []
for idx, t in enumerate(times):
    if now_time % t == 0:
        zeros.append(idx)
left = total - eat + 1
print(zeros[-left] + 1)

        
