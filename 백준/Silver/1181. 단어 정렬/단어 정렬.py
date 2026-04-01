a=int(input())
b=list()
for i in range(a):
  c=input()
  b.append(c)
b=set(b)
b=sorted(b, key=lambda x:(len(x), x))
for i in b:
  print(i)