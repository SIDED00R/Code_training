def before_total(first, second, third, num):
    if num == 1:
        return first
    elif num == 2:
        return second
    else:
        return third

def find(start, num, n, first, second, third):
    if n == 0:
        ans = [0, 0, 0]
        if num >= 0:
            ans[start - 1] = 1
        return ans
    
    num_list = []
    answer = [0, 0, 0]
    if num == -1:
        return answer
    if num == 0:
        num_list = [0 for _ in range(n)]
    while num != 0:
        num_list.append(num % 3)
        num //= 3
    while len(num_list) != n:
        num_list.append(0)

    dic = {1:[1, 3, 2], 2:[2, 1, 1], 3:[2, 3, 2]}
    now_pattern = dic[start]
    height = n
    for now_num in num_list[::-1]:
        height -= 1
        if now_num == 1:
            f, s, t = before_total(first, second, third, now_pattern[0])[height]
            answer[0] += f
            answer[1] += s
            answer[2] += t
        elif now_num == 2:
            f, s, t = before_total(first, second, third, now_pattern[0])[height]
            answer[0] += f
            answer[1] += s
            answer[2] += t
            f, s, t = before_total(first, second, third, now_pattern[1])[height]
            answer[0] += f
            answer[1] += s
            answer[2] += t
        if height == 0:
            answer[now_pattern[now_num] - 1] += 1
        now_pattern = dic[now_pattern[now_num]]
    return answer

start = int(input())
left = int(input())
right = int(input())
n = int(input())

first = [[1, 0, 0]]
second = [[0, 1, 0]]
third = [[0, 0, 1]]
for i in range(20):
    ff, fs, ft = first[i]
    sf, ss, st = second[i]
    tf, ts, tt = third[i]
    first.append([ff + 2 * fs, ff + fs + 2 * ft, ff + ft])
    second.append([sf + 2 * ss, sf + ss + 2 * st, sf + st])
    third.append([tf + 2 * ts, tf + ts + 2 * tt, tf + tt])

front = find(start, left - 1, n, first, second, third)
back = find(start, right, n, first, second, third)

print(back[0] - front[0], back[1] - front[1], back[2] - front[2])