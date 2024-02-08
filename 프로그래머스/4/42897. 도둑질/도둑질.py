def dp(arr):
    n = len(arr)
    case = [0] * n
    case[0] = arr[0]
    case[1] = arr[1]
    case[2] = arr[0] + arr[2]
    for idx in range(3, n):
        case[idx] = max(case[idx - 2], case[idx - 3]) + arr[idx]
    return max(case)    

def solution(money):
    if len(money) < 3:
        return max(money)
    elif len(money) == 3:
        return max(money[1], money[0] + money[2])
    else:
        include_first = money[:-1]
        uninclude_first = money[1:]  
        return max(dp(include_first), dp(uninclude_first))