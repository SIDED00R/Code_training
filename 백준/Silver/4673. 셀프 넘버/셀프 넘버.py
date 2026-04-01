sample=list(range(1,10001))
rem=[]
sam=0
for i in range(1,10001):
  a=i
  for j in range(10000):
    if int(a/10)==0:
      sam=sam+a
      break
    else:
      sam=sam+a%10
      a=int(a/10)
  

  b=i+sam
  if b>10000:
    sam=0
  else:
    rem.append(b)
    sam=0
for i in set(rem):
  sample.remove(i)
for i in sample:
  print(i)