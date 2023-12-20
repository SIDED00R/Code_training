import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    dic = {}
    answer = 1
    num = int(input())
    for j in range(num):
        cloth, where = input().split()
        if where in dic:
            dic[where] += 1
        else:
            dic[where] = 1
    for key, value in dic.items():
        answer *= (value + 1)
    print(answer - 1)
            
    
