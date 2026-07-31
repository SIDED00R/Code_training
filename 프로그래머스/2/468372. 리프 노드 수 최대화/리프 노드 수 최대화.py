def solution(dist_limit, split_limit):
    D, S = dist_limit, split_limit

    def min_cost(A, a):                 # 진입폭 A 확보에 필요한 2-구간 최소 노드 수
        if a == 0:
            return 0 if A == 1 else None
        if A > (1 << a):
            return None
        n = -(-A // 2); T = n
        for _ in range(a - 1):
            n = -(-n // 2); T += n
        return T

    ans = 1
    a = 0
    while (1 << a) <= S:
        b = 0
        while (1 << a) * 3 ** b <= S:
            unit = (3 ** b - 1) // 2
            maxA, Tcap = 1 << a, (1 << a) - 1

            lo, hi = 1, maxA            # 예산을 다 쓸 수 있는 최소 진입폭
            while lo < hi:
                mid = (lo + hi) // 2
                t = min_cost(mid, a)
                if t is not None and t + mid * unit >= D:
                    hi = mid
                else:
                    lo = mid + 1

            for A in {1, maxA, lo, max(1, lo - 1), min(maxA, lo + 1)}:
                t0 = min_cost(A, a)
                if t0 is None or t0 > D:
                    continue
                T = max(t0, min(D, Tcap, D - A * unit))
                ans = max(ans, 1 + T + 2 * min(D - T, A * unit))
            b += 1
        a += 1
    return ans