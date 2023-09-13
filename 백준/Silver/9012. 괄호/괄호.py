num = input()
for _ in range(int(num)):
    letter = input()
    count = 0
    if letter[0] == ")":
        print("NO")
    else:
        for l in letter:
            if l == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
                break
        if count == 0:
            print("YES")
        else:
            print("NO")
