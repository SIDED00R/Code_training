from itertools import product

def solution(users, emoticons):
    N = len(emoticons)
    rate = [10, 20, 30, 40]
    price_rate = list(product(rate, repeat = N))
    max_count = 0
    max_total = 0
    
    for case in price_rate:
        price = []
        for i in range(N):
            price.append((100 - case[i]) * emoticons[i] // 100)
        count = 0
        total = 0
        for user in users:
            buy = 0
            for idx in range(len(case)):
                if user[0] <= case[idx]:
                    buy += price[idx]
            if buy >= user[1]:
                buy = 0
                count += 1
            total += buy
            
        if count > max_count:
            max_count = count
            max_total = total
        elif count == max_count and max_total < total:
            max_total = total
        
    return [max_count, max_total]