s = int(input())
ma, f, mb = map(int, input().split())

air = ma + f + mb

if s <= 240 or s <= air:
    print('high speed rail')
    
else:
    print('flight')