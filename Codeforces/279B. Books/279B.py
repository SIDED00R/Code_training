n, t = map(int, input().split())
line = list(map(int, input().split()))
first = -1
second = -1
now = 0
answer = 0
while second < n - 1:
    second += 1
    now += line[second]
    while now > t:
        first += 1
        now -= line[first]
    answer = max(answer, second - first)
print(answer)