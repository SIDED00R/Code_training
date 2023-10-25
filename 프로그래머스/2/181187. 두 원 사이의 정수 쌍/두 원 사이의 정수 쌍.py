def count_dot(r, small):
    total = 0
    hight = r
    half = int(r / (2 ** 0.5) + 1)
    special = 0
    for i in range(half):
        while i ** 2 + hight ** 2 > r ** 2:
            hight -= 1
        if small and i ** 2 + hight ** 2 == r ** 2:
            special += 1
        total += hight + 1
    total -= special
    total = total * 2 - half ** 2
    return total * 4 - 4 * (r + 1) + 1
    
def solution(r1, r2):
    return count_dot(r2, False) - count_dot(r1, True) - 4

