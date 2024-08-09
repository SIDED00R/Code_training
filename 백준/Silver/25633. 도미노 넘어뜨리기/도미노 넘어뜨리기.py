
def check(lists):
    answer = []
    for i in range(len(lists)):
        find = False
        for j in range(len(lists)):
            if i == j:
                continue
            if lists[i][0] <= lists[j][0] and lists[i][1] <= lists[j][1]:
                find = True
            if find:
                break
        if find:
            continue
        else:
            answer.append(lists[i][:])
    return answer
        

n = int(input())
line = list(map(int, input().split()))
dp = [[] for _ in range(n)]
dp[0].append([line[0], 1])
for idx in range(1, n):
    for case in dp[idx - 1]:
        total, count = case
        if total >= line[idx]:
            dp[idx].append([total + line[idx], count + 1])
        else:
            dp[idx].append([total, count])
    dp[idx].append([line[idx], 1])
    dp[idx] = check(dp[idx])
    
max_count = 0
for case in dp[-1]:
    if case[1] > max_count:
        max_count = case[1]
        
print(max_count)