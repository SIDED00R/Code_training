import sys
n=int(input())
for i in range(n):
    a,b,c=map(int,sys.stdin.readline().split())
    d=a-c
    e=b%2
    if d<0:
        print("No")
    elif d%2 !=0  :
        print("No")
    elif e==1:
        if c !=0:
            print("Yes")
        elif a>=2:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
    