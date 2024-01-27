import sys
input = sys.stdin.readline

def check_digit(num, broken_numbers):
    if num == 0 and num in broken_numbers:
        return False
    while num:
        if num % 10 in broken_numbers:
            return False
        num //= 10
    return True

N = int(input())
M = int(input())
if M:
    broken_numbers = list(map(int, input().rstrip('\n').split()))
else:
    broken_numbers = []

min_count = abs(N - 100)

# upper case
for num in range(N, 1000000):
    if check_digit(num, broken_numbers):
        count = abs(N - num)
        if num == 0:
            count += 1
        while num:
            count += 1
            num //= 10
        if min_count > count:
            min_count = count 
        break
    
# lower case
for num in range(N, -1, -1):
    if check_digit(num, broken_numbers):
        count = abs(N - num)
        if num == 0:
            count += 1
        while num:
            count += 1
            num //= 10
        if min_count > count:
            min_count = count
        break
    
print(min_count)