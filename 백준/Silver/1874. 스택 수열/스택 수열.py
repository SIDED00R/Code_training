a=int(input())
b=list(range(0,a+1,1))
c=[]
d=[]
find=True
for i in range(a):
  c.append(int(input()))
pointer=0
for j in c:
  for p in range(j+10):
    if b[pointer]==j:
      d.append('-')
      b.pop(pointer)
      pointer-=1
      break
    elif b[pointer]<j:
      d.append('+')
      pointer+=1
    else:
      find=False
      break
if find:
  for i in d:
    print(i)
else:
  print("NO")
