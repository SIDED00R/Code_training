answer = set()
for idx in range(1 << 10):
    result = []
    for i in range(10):
        if idx & (1 << i):
            result.append(9 - i) 
    result.sort(reverse=True)
    if not result:
        continue
    answer.add("".join(list(map(str, result))))

ans = sorted(list(map(int, answer)))
n = int(input())
try:
    print(ans[n - 1])
except:
    print(-1)