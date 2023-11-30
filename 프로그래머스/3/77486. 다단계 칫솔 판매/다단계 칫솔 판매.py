def solution(enroll, referral, seller, amount):
    answer = {name: 0 for name in enroll}
    
    refer = {}
    for idx, people in enumerate(referral):
        refer[enroll[idx]] = people
            
    for num, sell in enumerate(seller):
        value = amount[num] * 100
        while value != 0:
            next_value = value // 10
            answer[sell] += value - next_value
            value = next_value
            sell = refer[sell]
            if sell == "-":
                break
        
    
    return [value for key, value in answer.items()]