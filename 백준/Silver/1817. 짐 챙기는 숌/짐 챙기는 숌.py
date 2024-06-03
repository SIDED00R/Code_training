N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    line = list(map(int, input().split()))
    answer = 1
    total = 0
    for num in line:
        if total + num > M:
            answer += 1
            total = num
        else:
            total += num
            
    print(answer)