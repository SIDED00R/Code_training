def solution(a):
    dic = {}
    for num in a:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    stack = []
    for key, value in dic.items():
        stack.append([key, value])
    stack = sorted(stack, key = lambda x : x[1])
    answer = 0
    while stack and answer < stack[-1][1]:
        now_num, _ = stack.pop()
        now_check = 0
        check = 0
        for check_num in a:
            if check_num == now_num and check == 0:
                check = 1
            elif check_num == now_num and check == 1:
                continue
            elif check_num != now_num and check == 1:
                now_check += 1
                check = 0
            elif check_num != now_num and check == 0:
                check = 2
            elif check_num == now_num and check == 2:
                now_check += 1
                check = 0
        if answer < now_check:
            answer = now_check   
    return answer * 2