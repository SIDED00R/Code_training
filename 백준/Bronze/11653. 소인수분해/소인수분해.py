a=int(input())
nanu=2
if a!=1:
  for i in range(a):
    if a%nanu==0:
      print(nanu)
      a=a//nanu
    else:
      nanu+=1
