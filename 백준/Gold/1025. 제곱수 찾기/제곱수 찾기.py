n, m = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(input())
    matrix.append(line)


total_case = set()      

for si in range(n):
    for sj in range(m):
        for di in range(n):
            for dj in range(m):
                if di == 0 and dj == 0:
                    total_case.add(matrix[si][sj])
                    continue
                else:
                    now_num = matrix[si][sj] 
                    for idx in range(1, max(n, m)):
                        if 0 <= si + di * idx < n and 0 <= sj + dj * idx < m:
                            now_num += matrix[si + di * idx][sj + dj * idx]
                            total_case.add(now_num)
                            total_case.add(now_num[::-1])
                        else:
                            break
                    
                    now_num = matrix[si][sj] 
                    for idx in range(1, max(n, m)):
                        if 0 <= si + di * idx < n and 0 <= sj - dj * idx < m:
                            now_num += matrix[si + di * idx][sj - dj * idx]
                            total_case.add(now_num)
                            total_case.add(now_num[::-1])
                        else:
                            break


l = sorted(list(set(map(int, total_case))))
while l:
    out = l.pop()
    if out == int(out ** 0.5) ** 2:
        print(out)
        exit()
print(-1)
