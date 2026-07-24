def solution(land, P, Q):
    heights = sorted(h for row in land for h in row)
    n = len(heights)

    prefix = [0] * (n + 1)
    for i, h in enumerate(heights):
        prefix[i + 1] = prefix[i] + h
    total = prefix[n]

    best = float('inf')
    for i, h in enumerate(heights):
        fill = P * (h * i - prefix[i])
        dig = Q * ((total - prefix[i]) - h * (n - i))
        best = min(best, fill + dig)

    return best