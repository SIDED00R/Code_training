import functools

def div(num, d):
    answer = 0
    while num % d == 0:
        answer += 1
        num //= d
    return answer

def check(a, b):
    if div(a, 3) > div(b, 3):
        return -1
    elif div(a, 3) == div(b, 3):
        if div(a, 2) > div(b, 2):
            return 1
        else:
            return -1
    else:
        return 1
        
n = int(input())
line = list(map(int, input().split()))

s_line = sorted(line, key = functools.cmp_to_key(check))
for num in s_line:
    print(num, end = " ")