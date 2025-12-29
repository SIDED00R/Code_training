def check(num):
    straight = str(num)
    back = straight[::-1]
    if straight == back:
        return True
    return False
    
n = input()
length = len(n)
num = int(n)
if check(num + 1):
    print(num + 1)
elif check(num + 2):
    print(num + 2)
else:
    if length % 2 == 0:
        half = n[:length // 2]
        if int(half + half[::-1]) > num:
            print(int(half + half[::-1]))
        else:
            next_half = str(int(half) + 1)
            print(int(next_half + next_half[::-1]))
    else:
        half = n[:length // 2]
        mid = n[length // 2]
        if int(half + mid + half[::-1]) > num:
            print(int(half + mid + half[::-1]))
        else:
            if mid == "9":
                next_half = str(int(half) + 1)
                print(int(next_half + "0" + next_half[::-1]))
            else:
                print(int(half + str(int(mid) + 1) + half[::-1]))