n, x = map(int, input().split())
ans_s = -1
for _ in range(n):
    s, t = map(int, input().split())
    if x >= s + t:
        ans_s = max(ans_s, s)
        
print(ans_s)