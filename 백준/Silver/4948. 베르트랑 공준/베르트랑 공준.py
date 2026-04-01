import math
def prime(x):
  for i in range(2,int(math.sqrt(x))+1):
    if x%i==0:
      return False
  return True
lis=[]
li=list(range(2,246913))
for j in li:
  if prime(j):
    lis.append(j)

while True:
  a=int(input())
  if a==0:
    break
  count=0
  for i in lis:
    if a<i and i<=a*2:
      count+=1
  print(count)
 