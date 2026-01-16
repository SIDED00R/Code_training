line = input()
num_list = sorted(map(int, set(line)))
if num_list[0] == 0:
    num_list = num_list[1:]

count = 0
d = 0
while True:
    if count >= 10 ** d:
        count = 0
        d += 1
    now_num = int(line) * 10 ** d + count
    count += 1
    find = True
    for num in num_list:
        if now_num % num != 0:
            find = False
            break
    if find:
        print(now_num)
        break
    