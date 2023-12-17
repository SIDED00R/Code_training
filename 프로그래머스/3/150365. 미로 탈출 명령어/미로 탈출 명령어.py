def solution(n, m, x, y, r, c, k):
    answer = []
    row = r - x
    col = c - y
    left = k - abs(row) - abs(col)
    stack_r = []
    stack_u = []
    stack_l = []
    new_x = x
    new_y = y
    if left < 0 or left % 2 == 1:
        return "impossible"
    else:
        if row > 0:
            answer += ["d"] * (row)
            new_x = x + row
        if col < 0:
            new_y = y + col
            stack_l = ["l"] * (-col)
        if col > 0:
            stack_r = ["r"] * (col)
        if row < 0:
            stack_u = ["u"] * (-row)
            
        while left != 0 and new_x != n:
            new_x += 1
            left -= 2
            answer.append("d")
            stack_u.append("u")
        answer += stack_l
        while left != 0 and new_y != 1:
            new_y -= 1
            left -= 2
            answer.append("l")
            stack_r.append("r")
        while left != 0:
            left -= 2
            answer.append("r")
            answer.append("l")
        answer += stack_r
        answer += stack_u
        
        return "".join(answer)