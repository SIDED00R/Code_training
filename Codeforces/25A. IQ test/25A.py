n = int(input())
line = list(map(int, input().split()))
even = 0
odd = 0
even_idx = -1
odd_idx = -1
for idx, num in enumerate(line):
    if num % 2 == 0:
        even += 1
        even_idx = idx
    else:
        odd += 1
        odd_idx = idx
        
if even == 1:
    print(even_idx + 1)
else:
    print(odd_idx + 1)