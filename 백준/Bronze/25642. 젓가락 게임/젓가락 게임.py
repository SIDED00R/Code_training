a, b = map(int, input().split())
while a <= 5 and b <= 5:
    b += a
    if b >= 5:
        break
    a += b
    
if a >= 5:
    print('yj')
else:
    print('yt')