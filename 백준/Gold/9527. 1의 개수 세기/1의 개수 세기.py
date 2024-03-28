import sys
input = sys.stdin.readline

def find(n):
    count = 0
    num = 2
    while n * 2 >= num:
        count += (n // num) * (num // 2)
        left = n % num
        count += max(left - num // 2 + 1, 0)
        num *= 2
    return count
A, B = map(int, input().split())
print(find(B) - find(A - 1))