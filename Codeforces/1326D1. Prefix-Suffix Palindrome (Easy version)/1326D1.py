def manacher(s):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    r = [0] * n
    c = right = 0
    for i in range(n):
        if i < right:
            r[i] = min(right - i, r[2 * c - i])
        while (i - r[i] - 1 >= 0 and i + r[i] + 1 < n
               and t[i - r[i] - 1] == t[i + r[i] + 1]):
            r[i] += 1
        if i + r[i] > right:
            c, right = i, i + r[i]
    return t, r
 
def best_pref_suf(m):
    t, r = manacher(m)
    L = len(t)
    bp = bs = 0
    for i in range(L):
        if i - r[i] == 0:
            bp = max(bp, r[i])
        if i + r[i] == L - 1:
            bs = max(bs, r[i])
    return m[:bp] if bp >= bs else m[len(m) - bs:]
 
def solve(s):
    n = len(s)
    k = 0
    while k < n // 2 and s[k] == s[n - 1 - k]:
        k += 1
    return s[:k] + best_pref_suf(s[k:n - k]) + s[n - k:]
 
t = int(input())
for _ in range(t):
    word = input()
    print(solve(word))