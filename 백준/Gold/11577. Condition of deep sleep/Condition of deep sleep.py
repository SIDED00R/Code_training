n, k = map(int, input().split())
line = list(map(int, input().split()))

xor_line = []
before = 0
change = {1:0, 0:1}

for num in line:
    xor_line.append((before + num) % 2)
    before = num

answer = 0
for idx, now_num in enumerate(xor_line):
    if now_num == 1:
        answer += 1
        if idx + k == n:
            continue
        elif idx + k > n:
            print("Insomnia")
            exit()
        else:
            xor_line[idx + k] = change[xor_line[idx + k]]

print(answer)