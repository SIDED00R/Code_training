a=input()
b=list(a)
for i in range(26):
  if chr(97+i) in b:
    c=b.index(chr(97+i))
  else:
    c=-1
  print(c,end=' ')