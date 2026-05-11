import math

n, m = map(int, input().split())
avg = n // m
left = n % m

less_case = m - left

max_case = n - m + 1

print(math.comb(avg, 2) * less_case + math.comb(avg + 1, 2) * left, math.comb(max_case, 2))