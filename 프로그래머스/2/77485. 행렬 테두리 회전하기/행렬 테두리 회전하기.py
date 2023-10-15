def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns)] for _ in range(rows)]  
    for i in range(rows * columns):
        arr[i // columns][i % columns] = i + 1
        
    for query in queries:
        x1, y1, x2, y2 = query
        
        outside = []
        for l in range(x1 - 1, x2):
            outside.append(arr[l][y1 - 1])
        for d in range(y1, y2):
            outside.append(arr[x2 - 1][d])
        for r in range(x2 - 2, x1 - 2, -1):
            outside.append(arr[r][y2 - 1])
        for u in range(y2 - 2, y1 - 1, -1):
            outside.append(arr[x1 - 1][u])
        
        answer.append(min(outside))      
        a = outside.pop(0)
        outside.append(a)
        idx = 0
        for l in range(x1 - 1, x2):
            arr[l][y1 - 1] = outside[idx]
            idx += 1
        for d in range(y1, y2):
            arr[x2 - 1][d] = outside[idx]
            idx += 1 
        for r in range(x2 - 2, x1 - 2, -1):
            arr[r][y2 - 1] = outside[idx]
            idx += 1
        for u in range(y2 - 2, y1 - 1, -1):
            arr[x1 - 1][u] = outside[idx]
            idx += 1

    return  answer