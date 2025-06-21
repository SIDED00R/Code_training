def find(num):
    ans = 1
    while True:
        if ans >= num:
            break
        else:
            ans *= 2
    return ans

while True:
    g, t, a, d = map(int, input().split())
    if g == t == a == d == -1:
        break
    total_game = g * t * (t - 1) // 2
    now_team = g * a
    team_number = find(now_team + d)
    add_team = team_number - now_team - d
    print(f'{g}*{a}/{t}+{d}={total_game + team_number - 1}+{add_team}')