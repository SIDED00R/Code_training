from bisect import bisect_left, bisect_right
import sys

def get_cost(X, P, i, j, k):
    left_cost = (k - i + 1) * X[k] - (P[k] - P[i - 1])
    right_cost = (P[j] - P[k - 1]) - (j - k + 1) * X[k]
    return left_cost + right_cost

def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())

    X = [0] * (n + 1)
    P = [0] * (n + 1)

    # --- 여기만 수정: X를 여러 줄에서 모아서 n개 채우기 ---
    vals = []
    while len(vals) < n:
        vals.extend(map(int, input().split()))
    for i in range(1, n + 1):
        X[i] = vals[i - 1]
        P[i] = P[i - 1] + X[i]
    # -------------------------------------------------------

    # (필요하다면 보장 차원에서 정렬 전제 확인/정렬)
    # X[1:n+1]이 정렬 전제일 경우 아래 주석 해제 금지. 문제에서 이미 정렬이라고 보장하면 불필요.
    # if not all(X[i] <= X[i+1] for i in range(1, n)):
    #     raise ValueError("X[1..n] must be non-decreasing for bisect to work.")

    for _ in range(q):
        l, r = map(int, input().split())
        lo = bisect_left(X, l, 1, n + 1)
        hi = bisect_right(X, r, 1, n + 1) - 1

        if lo >= hi:
            print(0)
        else:
            max_stress = max(get_cost(X, P, lo, hi, lo),
                             get_cost(X, P, lo, hi, hi))
            min_stress = get_cost(X, P, lo, hi, (lo + hi) // 2)
            print(max_stress - min_stress)

if __name__ == "__main__":
    main()
