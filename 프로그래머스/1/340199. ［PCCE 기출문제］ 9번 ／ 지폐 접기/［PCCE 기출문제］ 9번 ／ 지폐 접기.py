def solution(wallet, bill):
    min_w = min(wallet)
    max_w = max(wallet)
    min_bill = min(bill)
    max_bill = max(bill)
    answer = 0
    while min_w < min_bill or max_w < max_bill:
        answer += 1
        max_bill //= 2
        if max_bill > min_bill:
            continue
        else:
            max_bill, min_bill = min_bill, max_bill
    return answer