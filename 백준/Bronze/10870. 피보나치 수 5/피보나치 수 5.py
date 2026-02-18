a=int(input())
f1=0
f2=1
if a==0:
  print(f1)
elif a==1:
  print(f2)
else:
  for i in range(a-1):
    f=f1+f2
    f1=f2
    f2=f
  print(f)