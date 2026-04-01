a=int(input())
b=input()
c=list(b)
sum=0
for i in range(a):
  c[i]=int(c[i])
  sum=sum+c[i]
print(sum)