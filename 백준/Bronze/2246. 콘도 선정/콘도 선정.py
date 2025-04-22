n = int(input())

total_list = []
for _ in range(n):
    d, c = map(int, input().split())
    total_list.append([d, c])
    
total_list = sorted(total_list)
answer = 1

before_d, before_c = total_list[0]
for idx in range(1, n):
    now_d, now_c = total_list[idx]
    if before_d == now_d:
        continue
    else:
        if before_c > now_c:
            answer += 1
            before_d, before_c = now_d, now_c
            
print(answer)