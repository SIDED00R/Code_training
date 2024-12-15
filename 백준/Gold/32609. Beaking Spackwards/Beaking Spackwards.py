def find(left):
    first = 1
    last = left
    while first <= last:
        mid = (first + last) // 2
        if left < mid * (mid + 1) // 2:
            last = mid - 1
        else:
            first = mid + 1
    return last

n = int(input())
alp_list = ["a", "b", "c"]
answer = ""
idx = 0
while n != 0:
    now_num = find(n)
    answer += alp_list[idx] * now_num
    n -= (now_num * (now_num + 1) // 2)
    idx = (idx + 1) % 3

print(answer)