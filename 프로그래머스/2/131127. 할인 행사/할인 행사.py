def solution(want, number, discount):
    answer = 0
    dic = {}
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for j in range(len(discount) - 9):
        check = {}
        arr = discount[j:j + 10]
        for i in range(10):
            if arr[i] in check:
                check[arr[i]] += 1
            else:
                check[arr[i]] = 1 
        if dic == check:
            answer += 1
    return answer