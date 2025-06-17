num_list = []
for _ in range(9):
    num_list.append(int(input()))

total = sum(num_list)
for i in range(9):
    for j in range(i + 1, 9):
        now_ans = total - num_list[i] - num_list[j]
        if now_ans == 100:
            for idx in range(i):
                print(num_list[idx])
            for idx in range(i + 1, j):
                print(num_list[idx])
            for idx in range(j + 1, 9):
                print(num_list[idx])
            exit()