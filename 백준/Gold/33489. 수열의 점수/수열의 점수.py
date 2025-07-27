t = int(input())
answer_list = []
a, b = 1, 1
while b <= 1e7:
    answer_list.append([a, b])
    a, b = a + b, a
    
for _ in range(t):
    x, y = map(int, input().split())
    for nx, ny in answer_list:
        if x < nx or y < ny:
            print(ny, nx - ny)
            break
    