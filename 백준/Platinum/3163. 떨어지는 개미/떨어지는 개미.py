t = int(input())
for _ in range(t):
    left = []
    right = []
    answer = []
    n, l, k = map(int, input().split())
    for _ in range(n):
        p, a = map(int, input().split())
        if a < 0:
            left.append([p, a])
        else:
            right.append([p, a])
        answer.append([a])
    for i in range(len(left)):
        answer[i].append(left[i][0])
    for j in range(len(right)):
        answer[-j - 1].append(l - right[-j - 1][0])

    ans = sorted(answer, key = lambda x: [x[1], x[0]])
    
    print(ans[k - 1][0])

