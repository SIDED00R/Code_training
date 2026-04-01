a,b=map(int,input().split())
def GCD(x,y):
    while(y!=0):
        ai=x
        bi=y
        x=bi
        y=ai%bi
    return x  
def LCM(x,y):
    return (x*y)//GCD(x,y)
print(GCD(a,b))
print(LCM(a,b))