def insert(trie: dict, path: list[str]) -> None:
    node = trie
    for name in path:
        node = node.setdefault(name, {}) 

def dfs_print(node: dict, depth: int) -> None:
    for key in sorted(node.keys()):
        print("--" * depth + key)
        dfs_print(node[key], depth + 1)

N = int(input().strip())
trie: dict = {}

for _ in range(N):
    parts = input().split()
    k = int(parts[0])
    foods = parts[1:1 + k]
    insert(trie, foods)

dfs_print(trie, 0)
