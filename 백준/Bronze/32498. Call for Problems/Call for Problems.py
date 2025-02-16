n = int(input())
answer = 0
for _ in range(n):
    if int(input()) % 2 == 0:
        continue
    else:
        answer += 1
        
print(answer)