def solution(line):
    answer = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            if A * D - B * C == 0:
                continue
            else:
                x = (B * F - E * D) / (A * D - B * C)
                y = (E * C - A * F) / (A * D - B * C)
            if x == int(x) and y == int(y):
                if answer == []:
                    xmin = xmax = int(x)
                    ymin = ymax = int(y)
                else:
                    if xmin > x:
                        xmin = int(x)
                    if xmax < x:
                        xmax = int(x)
                    if ymin > y:
                        ymin = int(y)
                    if ymax < y:
                        ymax = int(y)
                answer.append([int(x), int(y)])
                
    arr = [["." for _ in range(xmax - xmin + 1)] for _ in range(ymax - ymin + 1)]
    for x_idx, y_idx in answer:
        arr[ymax - y_idx][x_idx - xmin] = "*"
        
    return list(map("".join, arr))