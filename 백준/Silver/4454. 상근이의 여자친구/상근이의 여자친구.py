from math import floor

while True:
    try:
        a, b, c, d, m, t = map(float, input().split())
        find = False
        first = 0
        second = 100000000
        while not find:
            mid = (first + second) / 2
            oil = a * mid ** 4 + b * mid ** 3 + c * mid ** 2 + d * mid
            if oil * m / mid < t:
                first = mid
            else:
                second = mid
            
            if floor(first * 100) == floor(second * 100):
                find = True
        print(f"{floor(first * 100) / 100:.2f}")
        
    except:
        exit()