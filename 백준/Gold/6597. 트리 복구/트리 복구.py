answer = ""

def postorder(root,start,end):
    global answer
    if start>end:
        return

    for i in range(start,end):
        if preorder[root]==inorder[i]:
            postorder(root+1,start,i)
            postorder(root+1+(i-start),i+1,end)
            answer += preorder[root]

while True:
    try:
        preorder,inorder=input().split()
        preorder=list(preorder)
        inorder=list(inorder)
        postorder(0,0,len(preorder))
        print(answer)
        answer = ""
    except:
        break