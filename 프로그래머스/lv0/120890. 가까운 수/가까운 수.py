def solution(array, n):
    array.sort()
    mi = array[0]
    mx = array[-1]
    for num in array:
        if num <= n:
            mi = num
        else:
            mx = num
            break
    if n - mi > mx - n:
        return mx
        
            
    return mi