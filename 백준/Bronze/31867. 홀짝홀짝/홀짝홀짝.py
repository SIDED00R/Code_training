n = int(input())
k = input()
even = 0
odd = 0
for num in k:
    if int(num) % 2 == 0:
        even += 1
    else:
        odd += 1
        
if even > odd:
    print(0)
elif even < odd:
    print(1)
else:
    print(-1)