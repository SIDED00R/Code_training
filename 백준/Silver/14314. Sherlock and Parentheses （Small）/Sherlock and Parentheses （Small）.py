t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    min_num = min(l, r)
    answer = 0
    for num in range(min_num + 1):
        answer += num
    print(f"Case #{i + 1}: {answer}")