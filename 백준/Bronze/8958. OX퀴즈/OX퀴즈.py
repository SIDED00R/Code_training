n=int(input())
for j in range(n):
  b=input()
  a=list(b)
  sum=0
  c=0
  for i in a:
    if i=='O':
      c+=1
      sum+=c
    else:
      c=0
  print(sum)