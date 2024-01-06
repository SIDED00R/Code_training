import sys
input = sys.stdin.readline

C, N = map(int, input().split())
color_dic = {}
nickname_dic = {}
for _ in range(C):
    color_dic[input()[:-1]] = 0
for _ in range(N):
    nickname_dic[input()[:-1]] = 0

Q = int(input())
for _ in range(Q):
    team_name = input()[:-1]
    able_color = ""
    find = False
    for i in range(min(1000, len(team_name))):
        able_color += team_name[i]
        if able_color in color_dic:
            if team_name[i + 1:] in nickname_dic:
                find = True
                print("Yes")
                break
    if not find:
        print("No")