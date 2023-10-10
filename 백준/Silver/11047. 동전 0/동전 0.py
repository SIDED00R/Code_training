N, K = map(int,input().split())

coin = []

for i in range(N):
    c = int(input())
    coin.append(c)

answer = 0
for ablecoin in coin[::-1]:
    count = K // ablecoin
    if count > 0:
        answer += count
        K = K - count * ablecoin

print(answer)

