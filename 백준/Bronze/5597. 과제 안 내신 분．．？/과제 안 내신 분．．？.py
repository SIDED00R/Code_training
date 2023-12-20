arr = ["X"] * 31
for _ in range(28):
    num = int(input())
    arr[num] = "O"
for check in range(1, len(arr)):
    if arr[check] == "X":
        print(check)
    