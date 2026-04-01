a=int(input())
b=int(input())
suma=[]
sumb=[]
def prime(sam,x):
  for i in range(2,x):
    if x%i == 0:
      return
  sam.append(x)
def primea(x):
  if x==1:
    return False
  for i in range(2,x):
    if x%i==0:
      return False
  return True
for i in range(a):
  if i+1 != 1:
    prime(suma,i+1)
for i in range(b):
  if i+1 != 1:
    prime(sumb,i+1)
if a>b:
  print(-1)
elif sumb==suma and not primea(a):
  print(-1)
else:
  if primea(a):
    print(sum(sumb)-sum(suma)+a)
    print(a)
  else:
    print(sum(sumb)-sum(suma))
    print(sumb[len(suma)])