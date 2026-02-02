def dfs(node, before):
    for key in sorted(node.keys()):
        print(f"{before}{key}")
        dfs(node[key], before + "--")

n = int(input())
dic = {}
for _ in range(n):
    line = list(input().split())
    node = dic
    for name in line[1:]:
        node = node.setdefault(name, {})

dfs(dic, "")
