import sys
count=0
for i in range(8):
    chess=list(sys.stdin.readline())
    if i%2==0:
        for j in range(4):
            if chess[2*j]=='F':
                count+=1
    else:
        for j in range(4):
            if chess[2*j+1]=='F':
                count+=1
print(count)