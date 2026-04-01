front=[]
back=[]
for i in range(3):
  a,b=map(int,input().split())
  front.append(a)
  back.append(b)
midx=(max(front)+min(front))/2
midy=(max(back)+min(back))/2
x=4*midx-front[0]-front[1]-front[2]
y=4*midy-back[0]-back[1]-back[2]

print(int(x),int(y))
