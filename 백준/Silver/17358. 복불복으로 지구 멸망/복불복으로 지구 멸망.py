n = int(input())
n -= 1
answer = 1
while n != 1:
    answer *= n
    n -= 2
    
print(answer % 1000000007)
    