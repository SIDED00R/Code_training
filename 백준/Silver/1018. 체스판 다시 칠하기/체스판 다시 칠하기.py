a,b=map(int,input().split())
c=[]
count=0
mincount=64
for i in range(a):
  c.append(list(input()))
for ga in range(a-7):
  for se in range(b-7):
    for j in range(ga,ga+8):
      for k in range(se,se+8):
        if (j+k)%2==0 and c[j][k]!='W':
          count += 1
        elif (j+k)%2==1 and c[j][k]!='B':
          count += 1
    if count<mincount:
      mincount=count
    count=0
for ga in range(a-7):
  for se in range(b-7):
    for j in range(ga,ga+8):
      for k in range(se,se+8):
        if (j+k)%2==0 and c[j][k]!='B':
          count += 1
        elif (j+k)%2==1 and c[j][k]!='W':
          count += 1
    if count<mincount:
      mincount=count
    count=0
print(mincount)