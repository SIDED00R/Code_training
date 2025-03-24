n = int(input())
total = 0
for num in range(1, n - 2):
    outside = n - 2 - num
    total += num * outside
    
print(total * n // 4)