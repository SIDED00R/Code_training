import sys
line=[]
pri=[]
n=int(input())
for i in range(n):
    line.append(list(sys.stdin.readline()))
for j in range(len(line[0])):
  bigyo=line[0][j]
  for k in range(n):
    if bigyo!=line[k][j]:
      bigyo='?'
      break
  pri.append(bigyo)
print(''.join(pri))
    
    