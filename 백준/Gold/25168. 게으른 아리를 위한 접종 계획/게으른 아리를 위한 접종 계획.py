n, m = map(int, input().split())
cases = [0] * (n + 1)
for i in range(m):
    s, e, w = map(int, input().split())
    if cases[s] == 0:
        cases[s] = 1
    if w >= 7:
        cases[e] = max(cases[e], cases[s] + w + 1)
    else:
        cases[e] = max(cases[e], cases[s] + w)
        
print(max(cases))
