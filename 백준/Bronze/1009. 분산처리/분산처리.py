n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a %= 10
    answer = a
    for i in range(1, b):
        answer *= a
        answer %= 10

    if answer == 0:
        answer = 10
        
    print(answer)
