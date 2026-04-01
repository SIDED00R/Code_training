a=int(input())
b=int(input())
c=int(input())
gop=a*b*c
d=[]
for i in range(100):
  d.append(gop%10)
  if gop//10==0:
    break
  else:
    gop=gop//10
for j in range(10):
  print(d.count(j))