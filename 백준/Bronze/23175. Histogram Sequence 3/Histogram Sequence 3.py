n=int(input())
a=[int(x) for x in input().split()]
c=[]
f=0
nfull=True
while nfull:
  c.append(a[f])
  d=a[f]
  f=f+d
  if f>=n:
    nfull=False
for i in range(len(c)):
  print(c[i],end=' ')