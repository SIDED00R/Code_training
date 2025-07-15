def climb(l):
    count_list = [1]
    for idx in range(1, len(l)):
        if l[idx - 1] <= l[idx]:
            count_list.append(count_list[-1])
        else:
            count_list.append(count_list[-1] + 1)
    return count_list
    
n, m = map(int, input().split())
height_list = list(map(int, input().split()))
range_list = []
for _ in range(m):
    l, r = map(int, input().split())
    range_list.append([l, r])

straight = climb(height_list)
back = climb(height_list[::-1])

for now_case in range_list:
    answer = 0
    l, r = now_case
    if l != 1:
        answer += straight[l - 2]
        if height_list[l - 2] <= height_list[r - 1]:
            answer -= 1
    if r != n:
        answer += straight[-1] - straight[r] + 1
        if height_list[r] >= height_list[l - 1]:
            answer -= 1
    answer += back[-l] - back[-r] + 1
    
    print(answer)