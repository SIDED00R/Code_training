def solution(a, b, g, s, w, t):
    min_time = 1
    max_time = 1e9 * 2 * 1e5 * 2
    while min_time + 1 < max_time:
        now_time = (min_time + max_time) // 2
        now_gold_max = 0
        now_silver_max = 0
        now_move_max = 0
        for i in range(len(g)):
            move_time = ((now_time // t[i]) + 1) // 2
            can_move = w[i] * move_time
            now_move_max += min(can_move, g[i] + s[i])
            now_gold_max += min(g[i], can_move)
            now_silver_max += min(s[i], can_move)
        if a <= now_gold_max and b <= now_silver_max and a + b <= now_move_max:
            max_time = now_time
        else:
            min_time = now_time
    return max_time