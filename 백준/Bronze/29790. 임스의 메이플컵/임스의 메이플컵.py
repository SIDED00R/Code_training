n, u, l = map(int, input().split())
cond1 = (n >= 1000)
cond2 = (u >= 8000 or l >= 260)
if cond1 and cond2:
    print('Very Good')
elif cond1:
    print('Good')
else:
    print('Bad')