import numpy as np

answer = []

def reduce(arr):
    
    sum1 = np.sum(arr, axis=0)
    total = int(np.sum(sum1))
    
    length = len(arr)
    
    if total == 0:
        answer.append(0)
    elif total == length ** 2:
        answer.append(1)
    else:
        reduce(arr[:length // 2,:length // 2])
        reduce(arr[:length // 2,length // 2:])
        reduce(arr[length // 2:,:length // 2])
        reduce(arr[length // 2:,length // 2:])

def solution(arr):
    arr = np.array(arr)
    reduce(arr)
    
    return [answer.count(0), answer.count(1)]