def solution(arr):
    col = len(arr)
    row = len(arr[0])
    if col > row:
        num = col - row
        for _ in range(num):
            for c in arr:
                c.append(0)
        return arr
    elif col < row:
        num = row - col
        for _ in range(num):
            arr.append([0] * row)
        return arr
    else:
        return arr