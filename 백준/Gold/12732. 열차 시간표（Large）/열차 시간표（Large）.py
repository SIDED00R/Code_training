def time_change(l):
    stack_time = []
    for now_time in l:
        start, end = now_time.split()
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        stack_time.append([sh * 60 + sm, eh * 60 + em])
    return stack_time

def count(a_list, b_list, t):
    a_list = sorted(a_list)
    b_list = sorted(b_list, key = lambda x: x[1])
    a_pointer = 0
    b_pointer = 0
    c = 0
    while True:
        if a_pointer >= len(a_list) or b_pointer >= len(b_list):
            break
        if a_list[a_pointer][0] >= b_list[b_pointer][1] + t:
            c += 1
            a_pointer += 1
            b_pointer += 1
        else:
            a_pointer += 1
    return len(a_list) - c

n = int(input())
for idx in range(n):
    t = int(input())
    a, b = map(int, input().split())
    stack_a = []
    stack_b = []
    for _ in range(a):
        stack_a.append(input())
    for _ in range(b):
        stack_b.append(input())
    stack_a = time_change(stack_a)
    stack_b = time_change(stack_b)
    print(f"Case #{idx + 1}: {count(stack_a, stack_b, t)} {count(stack_b, stack_a, t)}")
