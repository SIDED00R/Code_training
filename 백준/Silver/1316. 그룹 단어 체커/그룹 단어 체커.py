a=int(input())
sum=0
for i in range(a):
  pas=True
  b=input()
  for j in range(len(b)-1):
    if b[j] !=b[j+1]:
      new=b[j+1:]
      if new.count(b[j])>0:
        pas=False
  if pas:
    sum+=1
print(sum)