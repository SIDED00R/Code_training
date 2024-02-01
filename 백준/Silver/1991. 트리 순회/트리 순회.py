import sys
input = sys.stdin.readline

def preorder(tree, now):
    left, right = tree[now]
    print(now, end = "")
    if left != ".":
        preorder(tree, left)
    if right != ".":
        preorder(tree, right)

def inorder(tree, now):
    left, right = tree[now]
    if left != ".":
        inorder(tree, left)
    print(now, end = "")
    if right != ".":
        inorder(tree, right)
    
def postorder(tree, now):
    left, right = tree[now]
    if left != ".":
        postorder(tree, left)
    if right != ".":
        postorder(tree, right)
    print(now, end = "")
    
n = int(input())
tree = {}

for i in range(n):
    now, left, right = input().rstrip('\n').split()
    tree[now] = (left, right)
    
preorder(tree, "A")
print()
inorder(tree, "A")
print()
postorder(tree, "A")
print()
