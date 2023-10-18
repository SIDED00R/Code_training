def solution(m, n, startX, startY, balls):
    answer = []
    
    for x, y in balls:
        ans = 1e9
        
        #위로 반사
        if x != startX or startY > y:
            y1 = 2 * n - y
            if ans > (startX - x) ** 2 + (startY - y1) ** 2:
                ans = (startX - x) ** 2 + (startY - y1) ** 2
                
        #아래로 반사
        if x != startX or startY < y:
            y2 = -y
            if ans > (startX - x) ** 2 + (startY - y2) ** 2:
                ans = (startX - x) ** 2 + (startY - y2) ** 2
        
        #오른쪽 반사
        if y != startY or startX > x:
            x1 = 2 * m - x
            if ans > (startX - x1) ** 2 + (startY - y) ** 2:
                ans = (startX - x1) ** 2 + (startY - y) ** 2
                
        #왼쪽 반사
        if y != startY or startX < x:
            x2 = -x
            if ans > (startX - x2) ** 2 + (startY - y) ** 2:
                ans = (startX - x2) ** 2 + (startY - y) ** 2
        answer.append(ans)
        
    return answer