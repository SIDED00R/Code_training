a, b = map(int, input().strip().split(' '))
for _ in range(b):
    line = ""
    for _ in range(a):
        line += "*"
    print(line)