n, k, l = map(int, input().split())
hambuger = list(map(int, input().split()))
cock = list(map(int, input().split()))
storage = 0
cock_length = [0 for _ in range(n + 1)]

for idx in cock:
    cock_length[idx] += 1
    if idx + l <= n:
        cock_length[idx + l] -= 1
for i in range(n):
    cock_length[i + 1] += cock_length[i]

sort_cock_length = sorted(cock_length[1:], reverse = True)
sort_hambuger = sorted(hambuger, reverse = True)

for i in range(n):
    storage += int(sort_hambuger[i] / 2 ** sort_cock_length[i])

print(storage)