n = int(input())
light = list(map(int, input().split()))
num = int(input())

change = {1:0, 0:1}

for _ in range(num):
    s, idx = map(int, input().split())
    idx -= 1
    if s == 1:
        for i in range(idx, n, idx + 1):
            light[i] = change[light[i]]
    else:
        front, back = idx, idx
        while 0 <= front and n > back and light[front] == light[back]:
            if front == back:
                light[front] = change[light[front]]
            else:
                light[front] = change[light[front]]
                light[back] = change[light[back]]
            front -= 1
            back += 1

for sp in range(1 + (n - 1) // 20):
    print(" ".join(list(map(str, light[sp * 20:(sp + 1) * 20]))))


