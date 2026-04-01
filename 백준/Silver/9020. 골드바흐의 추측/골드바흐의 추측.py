import math
def prime(x):
  for i in range(2,int(math.sqrt(x))+1):
    if x%i==0:
      return False
  return True
sosu=[]
for i in range(2,10000):
  if prime(i):
    sosu.append(i)

a=int(input())
for i in range(a):
  num=int(input())
  a=num//2
  for k in range(num):
    if a in sosu:
      break
    else:
      a-=1
  idx=sosu.index(a)
  for j in range(10000):
    if num-sosu[idx] in sosu:
      x1=sosu[idx]
      x2=num-sosu[idx]
      break
    else:
      idx-=1
  print("%d %d"%(x1,x2))