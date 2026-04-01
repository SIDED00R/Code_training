a,b=map(int,input().split())
def sosu(x):
  if x==1:
    return False
  else:
    for i in range(2,int(x**0.5)+1):
      if x%i == 0:
        return False
    return True

for i in range(a,b+1):
  if sosu(i):
    print(i)
