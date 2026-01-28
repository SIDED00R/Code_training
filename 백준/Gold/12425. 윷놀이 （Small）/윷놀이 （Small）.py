def move(num, simbol, dic):
    if num == -1:
        num = 0
    move_num = dic[simbol]
    if num == 5:
        return 19 + move_num
    elif num == 10:
        if move_num <= 2:
            return 24 + move_num
        elif move_num == 3:
            return 22
        else:
            return 23 + move_num
    elif num in [20, 21, 23, 24]:
        now = num + move_num
        if now >= 25:
            add = now - 24
            return 14 + add
        else:
            return now
    elif num in [22]:
        return 26 + move_num
    elif num in [25, 26]:
        now = num + move_num
        if now == 27:
            return 22
        elif now < 27:
            return now
        else:
            return now - 1
    elif num in [15, 16, 17, 18, 19]:
        now = num + move_num
        if now == 20:
            return 29
        elif now > 20:
            return 30
        else:
            return now
    else:
        return num + move_num

t = int(input())
dic = {'Do': 1, 'Gae': 2, 'Gul': 3, 'Yut': 4, 'Mo':5}
for idx in range(1, t + 1):
    u, n, a, b = map(int, input().split())
    moving = list(input().split())
    a_map = input()
    b_map = input()
    if a_map:
        a_map = int(a_map)
    else:
        a_map = -1
    if b_map:
        b_map = int(b_map)
    else:
        b_map = -1
        
    turn = 0
    now_a = -1
    now_b = -1
    for now_move in moving:
        if now_a > 29 or now_b > 29:
            now_a = 999
            break
        if turn == 0:
            now_a = move(now_a, now_move, dic)
            turn = 1
            if now_move in ['Yut', 'Mo']:
                turn = 0
            if now_a == now_b:
                now_b = -1
                turn = 0
        else:
            now_b = move(now_b, now_move, dic)
            turn = 0
            if now_move in ['Yut', 'Mo']:
                turn = 1
            if now_b == now_a:
                now_a = -1
                turn = 1
    if now_a == 29:
        now_a = 0
    elif now_a > 29:
        now_a = -1
    if now_b == 29:
        now_b = 0
    elif now_b > 29:
        now_b = -1
        
    if a_map == now_a and b_map == now_b:
        print(f'Case #{idx}: YES')
    else:
        print(f'Case #{idx}: NO')