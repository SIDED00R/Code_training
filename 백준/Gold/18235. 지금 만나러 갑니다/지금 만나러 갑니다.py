import copy

n, a, b = map(int, input().split())
a_stack = set([a])
b_stack = set([b])
answer = 0
while True:
    count = 2 ** answer
    next_a = set()
    for a_idx in a_stack:
        if 1 <= a_idx - count <= n:
            next_a.add(a_idx - count)
        if 1 <= a_idx + count <= n:
            next_a.add(a_idx + count)

    next_b = set()
    for b_idx in b_stack:
        if 1 <= b_idx - count <= n:
            next_b.add(b_idx - count)
        if 1 <= b_idx + count <= n:
            next_b.add(b_idx + count)
    answer += 1
    if len(next_a) == 0 or len(next_b) == 0:
        print(-1)
        break

    elif next_a & next_b:
        print(answer)
        break
    else:
        a_stack = next_a.copy()
        b_stack = next_b.copy()