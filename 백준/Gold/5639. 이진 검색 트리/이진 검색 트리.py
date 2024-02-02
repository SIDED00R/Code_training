import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def postorder(tree, now):
    left, right = tree[now]
    if left != -1:
        postorder(tree, left)
    if right != -1:
        postorder(tree, right)
    print(now)

dic = {}
head = -1

while True:
    try:
        num = int(input())
        if head == -1:
            head = num
            dic[num] = [-1, -1]
        else:
            now = head
            while True:
                if now < num and dic[now][1] != -1:
                    now = dic[now][1]
                elif now > num and dic[now][0] != -1:
                    now = dic[now][0]
                elif now < num:
                    dic[now][1] = num
                    dic[num] = [-1, -1]
                    break
                elif now > num:
                    dic[now][0] = num
                    dic[num] = [-1, -1]
                    break
    except:
        break
    
postorder(dic, head)