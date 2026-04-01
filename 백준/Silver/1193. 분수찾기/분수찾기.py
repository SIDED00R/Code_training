a=int(input())
b=0
for i in range(a+11):
  if a>b:
    b=b+i
  else:
    d=b-a+1
    e=i-d
    if i%2!=0:
      print('%d/%d'%(e,d))
      break
    else:
      print('%d/%d'%(d,e))
      break