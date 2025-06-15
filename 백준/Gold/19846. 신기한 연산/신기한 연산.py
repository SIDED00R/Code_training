n, m, q = map(int, input().split())
num_list = [chr(97 + i) for i in range(n)]
answer = ''

for idx in range((m + 1) // 2):
    answer += num_list[idx % n] * 2

print(answer[:m])