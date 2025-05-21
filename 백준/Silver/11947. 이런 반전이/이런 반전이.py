t = int(input())
for _ in range(t):
    n = input()
    length = len(n)
    num = int(n)
    key = 10 ** length // 2
    if num >= key:
        print(key * (key - 1))
    else:
        print(num * (key * 2 - num - 1))
    
    