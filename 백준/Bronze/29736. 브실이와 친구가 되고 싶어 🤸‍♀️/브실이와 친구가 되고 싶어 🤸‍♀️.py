a, b = map(int, input().split())
k, x = map(int, input().split())

min_value = k - x
max_value = k + x
answer = min(b, max_value) - max(a, min_value) + 1

if answer >= 1:
    print(answer)
else:
    print('IMPOSSIBLE')
