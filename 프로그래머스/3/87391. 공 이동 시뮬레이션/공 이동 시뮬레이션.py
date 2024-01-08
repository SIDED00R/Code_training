def solution(n, m, x, y, queries):
    # 0: 왼쪽->오른쪽, 1: 오른쪽->왼쪽, 2: 위쪽->아래쪽, 3: 아래쪽->위쪽(반대 방향으로 생각함)
    now_up_left = [x, y]
    now_down_right = [x, y]
    while queries:
        command, dx = queries.pop()
        if command == 0:
            if now_up_left[1] != 0:
                now_up_left[1] += dx
            now_down_right[1] += dx
        elif command == 1:
            now_up_left[1] -= dx
            if now_down_right[1] != m - 1:
                now_down_right[1] -= dx
        elif command == 2:
            if now_up_left[0] != 0:
                now_up_left[0] += dx
            now_down_right[0] += dx
        elif command == 3:
            now_up_left[0] -= dx
            if now_down_right[0] != n - 1:
                now_down_right[0] -= dx
        if now_up_left[0] >= n or now_up_left[1] >= m or now_down_right[0] < 0 or now_down_right[1] < 0:
            return 0
        else:
            now_up_left[0] = max(0, now_up_left[0])
            now_up_left[1] = max(0, now_up_left[1])
            now_down_right[0] = min(n - 1, now_down_right[0])
            now_down_right[1] = min(m - 1, now_down_right[1])
    return (now_down_right[0] - now_up_left[0] + 1) * (now_down_right[1] - now_up_left[1] + 1)