import sys
sys.setrecursionlimit(100005)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def go_preorder(in_from, in_to, post_from, post_to):
    root = postorder[post_to]
    print(root, end=' ')
    inorder_root_index = inorder.index(root)
    left_count = inorder_root_index - in_from
    right_count = in_to - inorder_root_index
    if left_count > 0:
        go_preorder(in_from, in_from + (left_count - 1), post_from, post_from + (left_count - 1))
    if right_count > 0:
        go_preorder(in_to - (right_count - 1), in_to, post_to - 1 - (right_count - 1), post_to - 1)


go_preorder(0, len(inorder) - 1, 0, len(postorder) - 1)