a,b=map(int,input().split())
c=list(map(int,input().split()))
fi=0
se=0
th=0
for first in c[:-2]:
  for second in c[c.index(first)+1:]:
    for third in c[c.index(second)+1:]:
      if first+second+third <= b and fi+se+th< first+second+third:
        fi=first
        se=second 
        th=third
print(fi+se+th)

