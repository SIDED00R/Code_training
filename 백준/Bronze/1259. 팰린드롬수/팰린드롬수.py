a=list(map(int,input()))
while a!=[0]:
  b=list(reversed(a))
  if a==b:
    print("yes")
  else:
    print("no")
  a=list(map(int,input()))
  