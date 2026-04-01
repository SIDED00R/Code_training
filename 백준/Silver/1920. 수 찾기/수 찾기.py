a=int(input())
b=sorted(list(map(int,input().split())))
c=int(input())
d=list(map(int,input().split()))
for i in d:
  min=0
  max=a-1
  for j in range(a+1):
    mid=(min+max)//2
    if min>max:
      found=False
      break
    if i>b[mid]:
      min=(min+max)//2+1
    elif i<b[mid]:
      max=(min+max)//2-1
    else:
      found=True
      break
  if found:
    print(1)
  else:
    print(0)