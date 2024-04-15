N = int(input())
having = {}
for num in map(int, input().split()):
    having[num] = 1

M = int(input())
for card in map(int, input().split()):
    if card in having:
        print(1, end = " ")
    else:
        print(0, end = " ")