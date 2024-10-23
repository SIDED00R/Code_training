n = int(input())
for num in map(int, input().split()):
    if num == 300:
        print(1, end = " ")
    elif num >= 275:
        print(2, end = " ")
    elif num >= 250:
        print(3, end = " ")
    else:
        print(4, end = " ")