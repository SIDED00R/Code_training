a=int(input())
min=100
sol=''
for i in range(a):
    b,c=input().split()
    if min>int(c):
        min=int(c)
        sol=b
print(sol)