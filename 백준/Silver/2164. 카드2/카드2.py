a=int(input())
if a==1:
  print(1)
for i in range(1,a):
  if a<=2**i:
    print((a-2**(i-1))*2)
    break