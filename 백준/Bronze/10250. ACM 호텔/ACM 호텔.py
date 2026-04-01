a=int(input())
for i in range(a):
  a,b,c=map(int,input().split())
  d=int(c/a)
  e=c%a
  if e==0:
    e=a
    d=d-1
  if d+1<10:
    print('%d0%d'%(e,d+1))
  else:
    print('%d%d'%(e,d+1))