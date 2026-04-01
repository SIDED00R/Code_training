a=input().upper()
b=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
max=0
for i in b:
  if i in a:
    memo=a.count(i)
  else:
    continue
  if max<memo:
    max=memo
    sekai=i
  elif max==memo:
    sekai='?'
print(sekai)