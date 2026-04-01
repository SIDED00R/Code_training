sample=int(input())
sip=sample//10
ill=sample%10
n=0
while True:
    a=sip+ill
    b=ill*10+a%10
    n=n+1
    if sample==b:
        break
    sip=b//10
    ill=b%10
print(n)
    
       