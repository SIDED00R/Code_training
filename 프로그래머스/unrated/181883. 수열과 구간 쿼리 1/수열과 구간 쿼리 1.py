def solution(arr, queries):
    for i, j in queries:
        for idx in range(i,j+1):
            arr[idx] += 1
        
    return arr