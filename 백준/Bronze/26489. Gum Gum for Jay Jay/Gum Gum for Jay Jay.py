count = 0
while True:
    try:
        input()
        count += 1
    except:
        print(count)
        exit()