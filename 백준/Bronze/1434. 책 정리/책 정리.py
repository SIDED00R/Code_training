total = 0
n, m = map(int, input().split())
boxs = list(map(int, input().split()))
book = list(map(int, input().split()))

box_idx = 0
box = boxs[box_idx]
for idx in range(m):
    if box >= book[idx]:
        box -= book[idx]
    else:
        while True:
            total += box
            box_idx += 1
            box = boxs[box_idx]
            if box >= book[idx]:
                box -= book[idx]
                break
total += box
for i in range(box_idx + 1, n):
    total += boxs[i]
print(total)