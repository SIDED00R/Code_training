def gcd(first, second):
    while second != 0:
        first, second = second, first % second
    return first

N, M = map(int, input().split())

print(N * M // gcd(N, M))