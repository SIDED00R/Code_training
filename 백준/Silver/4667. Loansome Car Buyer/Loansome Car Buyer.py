while True:
    month, give_money, price, n = map(float, input().split())
    month = int(month)
    if month < 0:
        break
    
    before_m = 0
    rate = [0] * (month + 1)
    for _ in range(int(n)):
        m, r = map(float, input().split())
        m = int(m)
        if m == 0:
            before_r = r
        else:
            rate[before_m:m] = [1 - before_r] * (m - before_m)
            before_r = r
            before_m = m
    rate[m:] = [1 - r] * (month - m + 1)
    
    car_price = price + give_money
    debt = price
    
    car_price *= rate[0]
    answer = 0
    while car_price <= debt:
        answer += 1
        car_price *= rate[answer]
        debt -= price / month
    if answer == 1:
        print(f"{answer} month")
    else:
        print(f"{answer} months")