def find(num, dic):
    length = len(num)
    if length == 1:
        for num in range(int(num) + 1):
            dic[num] += 1
        return dic
    first_num = int(num[0])
    for f_n in range(first_num):
        dic[f_n] += 10 ** (length - 1)
        for i in range(10):
            dic[i] += (length - 1) * 10 ** (length - 2)
    dic[first_num] += int(num[1:]) + 1
    return dic

def answer(n):
    dic = {i:0 for i in range(10)}
    dic[0] -= (10 ** len(n) - 1) // 9
    while n:
        dic = find(n, dic)
        n = n[1:]
    return dic

while True:
    a, b = input().split()
    if a == b == "0":
        break
    a = str(int(a) - 1)
    a_dic = answer(a)
    b_dic = answer(b)
    for i in range(10):
        print(b_dic[i] - a_dic[i], end = " ")
    print()