def find(idx):
    if parent[idx] == idx:
        return idx
    return find(parent[idx])

def union(first, second, group_num):
    first_parent = find(first)
    second_parent = find(second)
    if first_parent > second_parent:
        group_num -= 1
        parent[first_parent] = second_parent
    elif first_parent < second_parent:
        group_num -= 1
        parent[second_parent] = first_parent
    return group_num
    

n = int(input())

coordinate = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append([x, y])

distance = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = coordinate[i]
        x2, y2 = coordinate[j]
        distance.append([abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2, i, j])
distance.sort()

parent = [i for i in range(n)]
group_num = n

for now_case in distance:
    answer = now_case[0]
    group_num = union(now_case[1], now_case[2], group_num)
    if group_num == 1:
        break

print(answer)
