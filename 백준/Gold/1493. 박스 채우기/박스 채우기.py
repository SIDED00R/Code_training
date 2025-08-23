from collections import defaultdict

total_case = defaultdict(int) # 나눠지는 경우 dict

def devide(l, w, h):
    global total_case
    min_length = min(l, w, h)
    if min_length == 1:
        total_case[1] += l * w * h
        return
    length = 1
    while length <= min_length:
        length *= 2
    length //= 2

    mul = (l // length) * (w // length) * (h // length)

    total_case[length] += mul

    left_l = l - (l // length) * length
    left_w = w - (w // length) * length
    left_h = h - (h // length) * length

    if left_l != 0:
        left_case.append((left_l, w, h))
    if left_w != 0:
        left_case.append((l - left_l, left_w, h))
    if left_h != 0:
        left_case.append((l - left_l, w - left_w, left_h))
        
l, w, h = map(int, input().split())
left_case = [(l, w, h)]
while left_case:
    l, w, h = left_case.pop()
    devide(l, w, h)

n = int(input())
cube_stack = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    length = 2 ** a
    cube_stack[length] = b

answer = 0
find = True
for length in sorted(total_case, reverse = True):
    left = total_case[length] # 해당 개수만큼 지워야함
    while left != 0:
        if length == 0:
            find = False
            break
        if left <= cube_stack[length]:
            answer += left
            cube_stack[length] -= left
            left = 0
        else:
            left -= cube_stack[length]
            answer += cube_stack[length]
            cube_stack[length] = 0
            left *= 8
            length //= 2
if find:
    print(answer)
else:
    print(-1)