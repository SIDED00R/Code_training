L, R = input().split()
count = 0

if len(L) == len(R):
    for i in range(len(L)):
        if L[i] == R[i] == "8":
            count += 1
            
        if L[i] != R[i]:
            break
        
print(count)