n = int(input())
real = list(map(int, input().split()))
m = int(input())
dream = list(map(int, input().split()))
first = real[0]

idx_list = []
for idx in range(m):
    if dream[idx] == first:
        idx_list.append(idx)
      
if not idx_list:
    print(-1)
    exit()
    
deep = 1
answer = []
while (n - 1) * deep + 1 <= m:
    able = False
    for idx in idx_list:
        if idx + (n - 1) * deep > m:
            break
        else:
            able = True
            if real == dream[idx:idx + deep * (n - 1) + 1:deep]:
                answer.append(deep)
    deep += 1
    
if answer:
    print(answer[0] - 1, answer[-1] - 1)
else:
    print(-1)


