n = int(input())

tree = [0]
for _ in range(n):
    tree.append(int(input()))
tree.append(0)


for num in range(1, n + 1):
    if tree[num - 1] <= tree[num] and tree[num + 1] <= tree[num]:
        print(num)