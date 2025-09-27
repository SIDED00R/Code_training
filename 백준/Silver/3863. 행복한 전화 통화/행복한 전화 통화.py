while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    test_stack = []
    for _ in range(n):
        source, destination, start, duration = map(int, input().split())
        test_stack.append((start, start + duration))

    call_stack = []
    for _ in range(m):
        start, duration = map(int, input().split())
        call_stack.append((start, start + duration))

    for now_node in call_stack:
        count = 0
        now_s, now_e = now_node
        for now_case in test_stack:
            test_s, test_e = now_case
            start = max(test_s, now_s)
            end = min(test_e, now_e)
            if start < end:
                count += 1
        print(count)
    