from bisect import bisect_left, bisect_right

def get_cost(X, P, i, j, k):
    left_cost = (k - i + 1) * X[k] - (P[k] - P[i - 1])
    right_cost = (P[j] - P[k - 1]) - (j - k + 1) * X[k]
    return left_cost + right_cost

def main():
    n, q = map(int, input().split())
    X = [0] * (n + 1)
    P = [0] * (n + 1)
    
    line = list(map(int, input().split()))
    for i in range(1, n + 1):
        X[i] = line[i - 1]
        P[i] = P[i - 1] + X[i]
    
    for _ in range(q):
        l, r = map(int, input().split())
        
        lo = bisect_left(X, l, 1, n + 1)
        hi = bisect_right(X, r, 1, n + 1) - 1
        
        if lo >= hi:
            print(0)
        else:
            max_stress = max(get_cost(X, P, lo, hi, lo), get_cost(X, P, lo, hi, hi))
            min_stress = get_cost(X, P, lo, hi, (lo + hi) // 2)
            print(max_stress - min_stress)

if __name__ == "__main__":
    main()
