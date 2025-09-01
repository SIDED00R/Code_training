a, b = map(int, input().split())
c, d = map(int, input().split())

h = a + c
y = b + d
if h > y:
    print('Yongdap')
elif h < y:
    print('Hanyang Univ.')
else:
    print('Either')