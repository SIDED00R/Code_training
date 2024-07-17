p, k = map(int, input().split())
find = False
for num in range(2, k):
    if p % num == 0:
        find = True
        small = num
        break

if find:
    print(f"BAD {small}")
else:
    print("GOOD")
