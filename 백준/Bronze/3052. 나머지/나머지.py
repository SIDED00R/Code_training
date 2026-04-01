a=[]
for i in range(10):
  b=int(input())
  a.append(b%42)


diff=set(a)
print(len(diff))