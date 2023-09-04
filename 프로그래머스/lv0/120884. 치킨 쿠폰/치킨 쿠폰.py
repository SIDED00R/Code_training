def solution(chicken):
    answer = 0
    coupon = True
    while coupon != 0:    
        coupon = chicken // 10
        answer += coupon
        chicken = coupon + chicken % 10
    return answer