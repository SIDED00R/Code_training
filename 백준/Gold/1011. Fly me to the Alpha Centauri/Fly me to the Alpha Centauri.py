a=int(input())
for i in range(a):
  c,d=map(int,input().split())
  e=d-c
  gan=1
  for j in range(1,d+10):
    if e<=gan:
      print(j)
      break
    gan=gan+j//2+1
