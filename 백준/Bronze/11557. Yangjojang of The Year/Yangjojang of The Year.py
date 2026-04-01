a=int(input())
for i in range(a):
  d=0
  b=int(input())
  for j in range(b):
    c,f=input().split()
    if d<int(f):
      d=int(f)
      e=c
  print(e)