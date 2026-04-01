a=int(input())
for i in range(a):
  b=int(input())
  f1=0
  f2=1
  if b==0:
    f=f1
  elif b==1:
    f=f2
  else:
    for i in range(b-1):
      f=f1+f2
      f1=f2
      f2=f
  g1=1
  g2=0
  if b==0:
    g=g1
  elif b==1:
    g=g2
  else:
    for i in range(b-1):
      g=g1+g2
      g1=g2
      g2=g
  print('%d %d'%(g,f))