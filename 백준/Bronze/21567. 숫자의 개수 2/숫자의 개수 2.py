total = 1
for _ in range(3):
    total *= int(input())
    
s = str(total)
stack = [0 for _ in range(10)]
for num in s:
    stack[int(num)] += 1
    
for idx in range(10):
    print(stack[idx])
    