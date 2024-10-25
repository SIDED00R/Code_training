def find(num, parents):
    if parents[num] != num:
        parents[num] = find(parents[num], parents)
    return parents[num]

def union(first, second, parents):
    num1 = find(first, parents)
    num2 = find(second, parents)
    if num1 < num2:
        parents[num2] = num1
    else:
        parents[num1] = num2

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]

for _ in range(m):
    first, second = map(int, input().split())
    union(first, second, parents)

order = list(map(int, input().split()))
answer = 0
before_node = order[0]
for node in order[1:]:
    if find(node, parents) == find(before_node, parents):
        continue
    else:
        answer += 1
    before_node = node

print(answer)