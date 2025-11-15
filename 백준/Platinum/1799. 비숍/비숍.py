import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

black_cands = []
white_cands = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            if (i + j) % 2 == 0:
                black_cands.append((i, j))
            else:
                white_cands.append((i, j))

used1 = [False] * (2 * n)
used2 = [False] * (2 * n)

black_answer = 0
white_answer = 0

def dfs(cands, idx, cnt, is_black):
    global black_answer, white_answer

    if idx == len(cands):
        if is_black:
            if cnt > black_answer:
                black_answer = cnt
        else:
            if cnt > white_answer:
                white_answer = cnt
        return

    i, j = cands[idx]
    d1 = i + j
    d2 = i - j + (n - 1)
    if not used1[d1] and not used2[d2]:
        used1[d1] = used2[d2] = True
        dfs(cands, idx + 1, cnt + 1, is_black)
        used1[d1] = used2[d2] = False
    dfs(cands, idx + 1, cnt, is_black)

dfs(black_cands, 0, 0, True)

used1 = [False] * (2 * n)
used2 = [False] * (2 * n)

dfs(white_cands, 0, 0, False)

print(black_answer + white_answer)
