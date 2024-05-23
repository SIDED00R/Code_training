count = 0
while True:
    count += 1
    n = int(input())
    name_list = []
    idx_lists = []
    if n == 0:
        break
    print(f"Group {count}")
    for _ in range(n):
        line = list(input().split())
        name_list.append(line[0])
        idx_list = []
        for idx, symbol in enumerate(line[1:]):
            if symbol == "N":
                idx_list.append(idx)
        idx_lists.append(idx_list)
        
    able = True
    for i, case in enumerate(idx_lists):
        for num in case:
            able = False
            print(f"{name_list[(i - num - 1 + n) % n]} was nasty about {name_list[i]}")
                
    if able:
        print("Nobody was nasty")
        
    print()
        