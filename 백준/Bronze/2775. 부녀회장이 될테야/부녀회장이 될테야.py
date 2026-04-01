a=int(input())
for i in range(a):
  
  e=list(range(1,15))
  b=int(input())
  c=int(input())
  for j in range(b):
    d=0
    for k in range(c):
      d=d+e[k]
      e[k]=d
  print(e[c-1])
