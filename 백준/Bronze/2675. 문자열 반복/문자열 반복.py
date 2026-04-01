for i in range(int(input())):
  a,b=input().split()
  a=int(a)
  c=''
  for j in range(len(b)):
    c=c+b[j]*a
  print(c)