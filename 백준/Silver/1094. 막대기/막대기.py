X = str(bin(int(input())))
count = 0
for num in X:
    if num == "1":
        count += 1
print(count)
