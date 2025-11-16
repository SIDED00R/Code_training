from decimal import getcontext, Decimal
getcontext().prec = 1100

def mul(num, n):
    if n == 1:
        return num
    if n % 2 == 0:
        return mul(num, n // 2) ** 2
    else:
        return mul(num, n // 2) ** 2 * num

num, n = input().split()
num = Decimal(num)
n = int(n)

ans = mul(num, n)
answer = format(ans, 'f')
print(answer)