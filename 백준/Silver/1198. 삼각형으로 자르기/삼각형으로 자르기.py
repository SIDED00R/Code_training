from itertools import combinations

n = int(input())
coordinate = []
for _ in range(n):
    coordinate.append(list(map(int, input().split())))
    
answer = 0
for case in combinations([i for i in range(n)], 3):
    x1, y1 = coordinate[case[0]]
    x2, y2 = coordinate[case[1]]
    x3, y3 = coordinate[case[2]]
    triangle = 0.5 * abs(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3)
    answer = max(answer, triangle)
    
print(answer)
    