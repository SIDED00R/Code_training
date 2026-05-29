t = int(input())
for _ in range(t):
    n = int(input())
    a_list = list(map(int, input().split()))
    next_diff = [n + 10] * n
    before_idx = 0
    before_num = a_list[0]
    for idx, num in enumerate(a_list):
        if num != before_num:
            for i in range(before_idx, idx):
                next_diff[i] = idx
            before_idx = idx
            before_num = a_list[idx]
        
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        if next_diff[l] <= r:
            print(l + 1, next_diff[l] + 1)
        else:
            print(-1, -1)
    print()