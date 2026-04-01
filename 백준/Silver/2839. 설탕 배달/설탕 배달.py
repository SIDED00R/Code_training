a=int(input())
if int(a/5)!=a/5:
  for i in range(3):
    b=a-5*(i)
    if b<0:
      break
    if b/3==int(b/3):
      if b>=15:
        five=int(b/15)*3+i
        thr=(b%15)/3
        found=True
        break
      else:
        five=i
        thr=b/3
        found=True
        break
    else:
      found=False
  if found:
    print(int(five+thr))
  else:
    print(-1)
else:
  print(int(a/5))