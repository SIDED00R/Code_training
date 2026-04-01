a=int(input())
b=int(input())
c=a
a=a//100
a=a%b
a=a*100
a1=a-a%100
for i in range(c):
    if a1<=b*i:
        if b*i-a1<10:
            print('0%d'%(b*i-a1))
            break
        else:
            print(b*i-a1)
            break
    