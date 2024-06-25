n, k = map(int, input().split())
times = list(map(int, input().split()))

answer = 0
end_time = 0

for num in times:
    if num <= end_time:
        continue
    else:
        end_time = num + k
        answer += 1
        
print(answer)
    