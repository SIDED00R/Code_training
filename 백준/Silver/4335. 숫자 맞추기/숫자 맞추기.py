lie = False
able = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
while True:
    n = int(input())
    if n == 0:
        break
    ans = input()
    if ans == "too high":
        able = able & set(range(1, n))
    elif ans == "too low":
        able = able & set(range(n + 1, 11))
    else:
        able = able & set([n])
        if len(able) == 0:
            lie = True
        if lie:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        lie = False
        able = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])