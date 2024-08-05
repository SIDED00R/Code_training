k = int(input())

two = 0
answer = 1

while k > 2:
    two = 0
    while 1 << two < k:
        two += 1
    if two % 2 != 0:
        left = 2 ** two - k
        k = 2 ** (two - 1) - left
        answer = answer ^ 1
    else:
        k = 2 ** two - k + 1
    
if k == 1:
    print(1 ^ answer)
else:
    print(answer)