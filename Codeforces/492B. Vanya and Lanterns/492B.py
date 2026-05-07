n, l = map(int, input().split())
light = sorted(list(map(int, input().split())))

answer = light[0]
for idx in range(1, n):
    answer = max(answer, (light[idx] - light[idx - 1]) / 2)
    
answer = max(answer, l - light[-1])
print(answer)