n = int(input())
line = list(map(int, input().split()))
even = odd = 0
for num in line:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
        
if even > odd:
    print("Happy")
else:
    print("Sad")