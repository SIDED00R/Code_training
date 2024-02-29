n = int(input())

coordinate = []
for _ in range(n):
    x, y = map(float, input().split())
    coordinate.append([x, y])

coordinate = coordinate + [coordinate[0]]

answer = 0
for i in range(len(coordinate) - 1):
    front_x, front_y = coordinate[i]
    back_x, back_y = coordinate[i + 1]
    answer += (front_x * back_y - back_x * front_y)
    
print(round(abs(answer) / 2, 1))
    