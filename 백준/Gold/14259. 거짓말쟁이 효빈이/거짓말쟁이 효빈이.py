import sys
input = sys.stdin.readline

def find(num):
    front = 0
    back = len(front_stack) - 1
    while front <= back:
        mid = (front + back) // 2
        now_num = front_stack[mid][0]
        if num >= now_num:
            front = mid + 1
        else:
            back = mid - 1
    return back

def able_count(a, length):
    return (length + 1) // (a + 1)

n, k, a = map(int, input().split())
m = int(input())
line = list(map(int, input().split()))
front_stack = [[1, n]]
max_count = able_count(a, n)
find_answer = False
for answer, num in enumerate(line):
    idx = find(num)
    f_stack = front_stack[:idx]
    b_stack = front_stack[idx + 1:]
    before_front, before_back = front_stack[idx]
    length = before_back - before_front + 1
    if length == 1:
        max_count -= able_count(a, length)
        next_stack = []
    elif num == before_front:
        next_stack = [[before_front + 1, before_back]]
        max_count = max_count - able_count(a, length) + able_count(a, length - 1)
    elif num == before_back:
        next_stack = [[before_front, before_back - 1]]
        max_count = max_count - able_count(a, length) + able_count(a, length - 1)
    else:
        next_stack = [[before_front, num - 1], [num + 1, before_back]]
        max_count = max_count - able_count(a, length) + able_count(a, num - before_front) + able_count(a, before_back - num)
    front_stack = f_stack + next_stack + b_stack
    if max_count < k:
        find_answer = True
        break
if not find_answer:
    print(-1)
else:
    print(answer + 1)