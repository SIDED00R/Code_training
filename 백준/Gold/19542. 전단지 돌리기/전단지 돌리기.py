from collections import defaultdict

n ,s, d = map(int, input().split())
connect_node = defaultdict(list)
connect_count = defaultdict(int)
for _ in range(n - 1):
    x, y = map(int, input().split())
    connect_node[x].append(y)
    connect_node[y].append(x)
    connect_count[x] += 1
    connect_count[y] += 1

end_node = []
for k, v in connect_count.items():
    if v == 1:
        if k == s:
            continue
        end_node.append(k)

for _ in range(d):
    new_end_node = []
    for node in end_node:
        del(connect_count[node])
        for parent_node in connect_node[node]:
            if parent_node == s:
                continue
            if parent_node in connect_count:
                connect_count[parent_node] -= 1
                if connect_count[parent_node] == 1:
                    new_end_node.append(parent_node)
    end_node = new_end_node[:]

print(len(connect_count) * 2 - 2)





