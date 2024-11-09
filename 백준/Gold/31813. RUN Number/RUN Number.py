
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    str_num = str(k)
    count = 0
    answer = []
    while str_num != '0':
        count += 1
        now_num = int(str_num[0] * n)
        if k < now_num:
            if str_num[0] == 1:
                now_num = ("9" * (n - 1))
            else:
                now_num = int(str(int(str_num[0]) - 1) * n)
        k -= now_num
        str_num = str(k)
        n = len(str_num)
        answer.append(now_num)

    print(count)
    for num in answer:
        print(num, end = " ")
    print()