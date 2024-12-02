total = int(input())
r = int(input())
c = int(input())
matrix = []
for _ in range(r):
    matrix.append(list(input()))

answer = []
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for i in range(r):
    for j in range(c):
        if matrix[i][j] == ".":
            ans = 1
            matrix[i][j] = "I"
            stack = [[i, j]]
            while stack:
                i, j = stack.pop()
                for idx in range(4):
                    ni = i + di[idx]
                    nj = j + dj[idx]
                    if 0 <= ni < r and 0 <= nj < c and matrix[ni][nj] == ".":
                        ans += 1
                        matrix[ni][nj] = "I"
                        stack.append([ni, nj])
            answer.append(ans)

answer = sorted(answer)
count = 0
while answer:
    now = answer.pop()
    if total >= now:
        count += 1
        total -= now
    else:
        break
if count == 1:
    print(f"{count} room, {total} square metre(s) left over")
else:
    print(f"{count} rooms, {total} square metre(s) left over")