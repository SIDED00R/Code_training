from collections import defaultdict

n = int(input())
x_route = defaultdict(list)
y_route = defaultdict(list)
dic = {}
for _ in range(n):
    x, y = map(int, input().split())
    dic[(x, y)] = 0
    x_route[x].append(y)
    y_route[y].append(x)
    
answer = -1
for k, v in dic.items():
    if v == 1:
        continue
    else:
        answer += 1
        dic[k] = 1
        stack = [k]
        while stack:
            x, y = stack.pop()
            for now_y in x_route[x]:
                if dic[(x, now_y)] == 1:
                    continue
                dic[(x, now_y)] = 1
                stack.append([x, now_y])
            for now_x in y_route[y]:
                if dic[(now_x, y)] == 1:
                    continue
                dic[(now_x, y)] = 1
                stack.append([now_x, y])
                
print(answer)