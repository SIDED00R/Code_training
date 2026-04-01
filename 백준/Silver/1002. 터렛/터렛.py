a=int(input())
for i in range(a):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    r=((x1-x2)**2+(y1-y2)**2)**0.5
    maxr=max(r1,r2)
    minr=min(r1,r2)
    if r1==r2 and r==0:
        print(-1)
    elif r==r1+r2 or maxr==minr+r:
        print(1)
    elif r<r1+r2 and r>maxr-minr:
        print(2)
    else:
        print(0)