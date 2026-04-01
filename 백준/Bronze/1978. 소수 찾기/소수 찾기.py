def prime(x):
  for i in range(2,x):
    if x%i==0:
      return False
  return True
b=input()
a=list(map(int,input().split()))
count=0
for i in a:
  if i!=1:
    if prime(i):
      count +=1
print(count)