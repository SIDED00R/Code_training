num = input()
if "7" in num:
    if int(num) % 7 == 0:
        print(3)
    else:
        print(2)
else:
    if int(num) % 7 == 0:
        print(1)
    else:
        print(0) 