n, m = map(int, input().split())
total = 1e9
div = n // 6
left = n % 6
min_six = 1e9
min_one = 1e9
for _ in range(m):
    six, one = map(int, input().split())
    min_six = min(min_six, six)
    min_one = min(min_one, one)
    
if left == 0:
    all_div = div
else:
    all_div = div + 1
total = min(total, min_one * n, all_div * min_six, div * min_six + left * min_one)
print(total)