def check_birth(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 0
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 1
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 2
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 3
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return 4
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return 5
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 6
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 7
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 8
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        return 9
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return 10
    else:
        return 11
    
member_birth = []
for _ in range(7):
    member_birth.append(list(map(int, input().split())))
    
check = [0] * 12
for month, day in member_birth:
    check[check_birth(month, day)] = 1
    
n = int(input())
people_birth = []
for _ in range(n):
    month, day = map(int, input().split())
    if check[check_birth(month, day)] == 1:
        continue
    else:
        people_birth.append([month, day])
        
if people_birth:
    people_birth = sorted(people_birth)
    for month, day in people_birth:
        print(month, day)
else:
    print("ALL FAILED")