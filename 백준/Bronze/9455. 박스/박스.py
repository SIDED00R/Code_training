T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    box = []
    answer = 0
    for _ in range(m):
        box.append(list(map(int, input().split())))
    for j in range(n):
        count = 0
        for i in range(m):
            if box[i][j] == 0:
                answer += count
            elif box[i][j] == 1:
                count += 1
                
    print(answer)