N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input().split(".")[1]))

answer = 0
find = False
while not find:
    answer += 1
    find = True
    for score in scores:
        low = score * answer
        high = (score + 1) * answer
        if low <= round(low, -3) < high or low <= round(high, -3) < high:
            continue
        else:
            find = False
            break
        
print(answer)