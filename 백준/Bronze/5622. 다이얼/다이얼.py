a=list(input())
g=0
for i in range(len(a)):
  if ord(a[i])<80:
    f=int((ord(a[i])+1)/3)-19
  elif ord(a[i])<87:
    f=int((ord(a[i])/4))-12
  else:
    f=10
  g=g+f
print(g)