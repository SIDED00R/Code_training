a,b=map(int,input().split())
c=[]
for i in range(a):
  c.append(int(input()))
mi=1
ma=max(c)
mid=int((mi+ma)/2)
for i in range(ma):
  count=0
  for j in c:
    e=j//mid
    count+=e
  if count>=b:
    mi=mid+1
    mid=int((mi+ma)/2)
    if mi>ma:
      print(ma)
      break
  else:
    ma=mid-1
    mid=int((mi+ma)/2)
    if mi>ma:
      print(ma)
      break


