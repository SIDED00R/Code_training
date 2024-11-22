n = int(input())
young = list(map(int, input().split()))
old = list(map(int, input().split()))

answer = 0
for idx in range(n - 2):
    answer += abs(young[idx] - old[idx])

now_young = old[-2] + young[-1]
now_old = young[-2] + old[-1]

print(answer + abs(now_young - now_old))