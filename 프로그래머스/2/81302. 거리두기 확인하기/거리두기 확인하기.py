def able(arr, idx):
    x, y = idx
    # 위쪽 확인
    if arr[x - 1][y] == "P":
        return False
    elif arr[x - 1][y] == "O":
        if arr[x - 1][y - 1] == "P":
            return False
        if arr[x - 2][y] == "P":
            return False
        if arr[x - 1][y + 1] == "P":
            return False
    
    # 오른쪽 확인
    if arr[x][y + 1] == "P":
        return False
    elif arr[x][y + 1] == "O":
        if arr[x - 1][y + 1] == "P":
            return False
        if arr[x][y + 2] == "P":
            return False
        if arr[x + 1][y + 1] == "P":
            return False
    
    # 왼쪽 확인
    if arr[x][y - 1] == "P":
        return False
    elif arr[x][y - 1] == "O":
        if arr[x - 1][y - 1] == "P":
            return False
        if arr[x][y - 2] == "P":
            return False
        if arr[x + 1][y - 1] == "P":
            return False
    
    # 아래쪽 확인
    if arr[x + 1][y] == "P":
        return False
    elif arr[x + 1][y] == "O":
        if arr[x + 1][y - 1] == "P":
            return False
        if arr[x + 2][y] == "P":
            return False
        if arr[x + 1][y + 1] == "P":
            return False
        
    return True

def solution(places):
    answer = []
    for place in places:
        
        # 배열로 만들기
        X_line = ["X" for _ in range(7)]
        arr = [X_line]
        for line in place:
            arr.append(["X"] + list(line) + ["X"])
        arr.append(X_line)
        
        # 위치별로 가능한지 확인
        cannot = False
        for i in range(1, 6):
            for j in range(1, 6):
                if arr[i][j] == "P":
                    if not able(arr, [i, j]):
                        answer.append(0)
                        cannot = True
                if cannot:
                    break
            if cannot:
                break
        if not cannot:
            answer.append(1)
            
    return answer