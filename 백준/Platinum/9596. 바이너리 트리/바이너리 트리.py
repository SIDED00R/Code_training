n = int(input())
for i in range(n):
    answer = 0
    first = input()
    second = input()
    start = 1
    for alp in first:
        if alp == "L":
            start *= 2
        elif alp == "R":
            start = start * 2 + 1
        else:
            start = max(1, start // 2)

    dic = {0:1, 1:0, 2:0, 3:0} # 0:자식없, 1: 왼자식, 2:오자식, 3:쌍자식
    for alp in second:
        new_dic = {}
        if alp == "L":
            new_dic[0] = (dic[0] + dic[2]) % 21092013
            new_dic[1] = (dic[0] + dic[1]) % 21092013
            new_dic[2] = 0
            new_dic[3] = (dic[3] + dic[2]) % 21092013
            dic = new_dic
        elif alp == "R":
            new_dic[0] = (dic[0] + dic[1]) % 21092013
            new_dic[1] = 0
            new_dic[2] = (dic[2] + dic[0]) % 21092013
            new_dic[3] = (dic[3] + dic[1]) % 21092013
            dic = new_dic
        else:
            if start == 1:
                continue
            else:
                if start % 2 == 0:
                    dic[1] += 1
                else:
                    dic[2] += 1
                start //= 2
    for k, v in dic.items():
        answer += v
    answer %= 21092013
    print(f"Case {i + 1}: {answer}")