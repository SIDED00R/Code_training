count = 0
while True:
    count += 1
    n = int(input())
    if n == 0:
        break
    get_back = [True] * n
    name_list = []
    total = 0
    for _ in range(n):
        name_list.append(input())
    for _ in range(2 * n - 1):
        num, simbol = input().split()
        num = int(num)
        if get_back[num - 1]:
            get_back[num - 1] = False
            total += num
        else:
            total -= num
            
    print(count, name_list[total - 1])
    
    