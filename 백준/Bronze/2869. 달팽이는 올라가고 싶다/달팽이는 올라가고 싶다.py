a,b,v=map(int,input().split())
c=int((v-a)/(a-b))
if c==((v-a)/(a-b)):
  print(c+1)
else:
  print(c+2)