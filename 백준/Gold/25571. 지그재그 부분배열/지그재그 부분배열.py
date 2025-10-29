import math

t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    count_list = []
    count = 0
    for i in range(1, n):
        if count == 0:
            if line[i] != line[i - 1]:
                count = 1
        else:
            if (line[i - 1] - line[i - 2]) * (line[i] - line[i - 1]) < 0:
                count += 1
            else:
                count_list.append(count)
                if line[i] != line[i - 1]:
                    count = 1
                else:
                    count = 0
    count_list.append(count)
    answer = 0
    for num in count_list:
        if num == 0:
            continue
        answer += math.comb(num + 1, 2)
    print(answer)
            
        
    