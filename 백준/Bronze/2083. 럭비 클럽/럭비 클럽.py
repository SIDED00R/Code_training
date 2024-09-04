while True:
    n, age, weight = input().split()
    if n == "#":
        break
    if int(age) > 17 or int(weight) >= 80:
        print(f"{n} Senior")
    else:
        print(f"{n} Junior")