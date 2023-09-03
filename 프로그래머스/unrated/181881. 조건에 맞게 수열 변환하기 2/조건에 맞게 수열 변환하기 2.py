def solution(arr):
    beforarr = []
    count = 0
    while beforarr != arr:
        beforarr = arr[:]
        for idx, num in enumerate(arr):       
            if num >= 50 and num % 2 == 0:
                arr[idx] //= 2
            elif num < 50 and num % 2 == 1:
                arr[idx] = arr[idx] * 2 + 1
        count += 1
                
    return count - 1