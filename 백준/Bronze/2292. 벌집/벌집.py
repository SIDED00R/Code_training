a=int(input())
a=a-1
b=0
for i in range(a+1):
  b=b+6*i
  if a<=b:
    print(i+1)
    break
