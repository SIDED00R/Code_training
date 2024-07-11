now_temp = float(input())
while True:
    next_temp = float(input())
    if next_temp == 999:
        break
    print(format(next_temp - now_temp, ".2f"))
    now_temp = next_temp