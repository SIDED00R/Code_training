def find(r, l, first, d):
    r_d = r // d
    l_d = max(l - 1, first - 1) // d
    return max(r_d - l_d, 0)

l = int(input())
r = int(input())
k = int(input())

if k == 2:
    print(max(0, r - max(l, 3) + 1))
elif k == 3:
    print(find(r, l, 6, 3))
elif k == 4:
    answer = find(r, l, 10, 2)
    if l <= 12 <= r:
        answer -= 1
    print(answer)
else:
    print(find(r, l, 15, 5))
    
