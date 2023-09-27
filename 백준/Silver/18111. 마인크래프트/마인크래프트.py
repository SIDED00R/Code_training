import sys
N, M, B = map(int, sys.stdin.readline().split())
ground = []
answer = int(1e9)
deep = 0

for _ in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))

for high in range(257):
    put = 0
    take = 0
    for i in range(N):
        g = ground[i]
        for j in range(M):
            if g[j] > high:
                take += g[j] - high
            else:
                put += high - g[j]
    if take + B < put:
        break
    
    time = take * 2 + put

    if time <= answer:
        answer = time
        deep = high

print(answer, deep)
