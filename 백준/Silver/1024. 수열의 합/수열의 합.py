n, l = map(int, input().split())

not_find = True
answer = [-1]
while not_find and (l <= 100):
    a = (2 * n / l + 1 - l) / 2
    int_a = int(a)
    if a == int_a:
        if a < 0:
            answer = [-1]
            break
        answer = [i for i in range(int(a), int(a) + l)]
        not_find = False
    l += 1
    
for num in answer:
    print(num, end = ' ')
    