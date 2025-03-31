import math

n = int(input())
machine = sorted(list(map(int, input().split())))
m = int(input())
box = sorted(list(map(int, input().split())))

if machine[-1] < box[-1]:
    print(-1)
    exit()
else:
    max_time = math.ceil(m / n)
    while max_time <= m:
        try:
            for i in range(n + 1):
                if machine[-(i + 1)] < box[-(i * max_time + 1)]:
                    max_time += 1
                    break
        except:
            print(max_time)
            exit()
