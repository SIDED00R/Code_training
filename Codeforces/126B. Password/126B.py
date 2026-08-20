s = input()
n = len(s)
pi = [0] * n
k = 0
for i in range(1, n):
    while k > 0 and s[i] != s[k]:
        k = pi[k - 1]
    if s[i] == s[k]:
        k += 1
    pi[i] = k

if n < 3:
    ans = 0
else:
    m = max(pi[:-1])
    ans = pi[-1]
    while ans > m:
        ans = pi[ans - 1]
if ans == 0:
    print("Just a legend")
else:
    print(s[-ans:])