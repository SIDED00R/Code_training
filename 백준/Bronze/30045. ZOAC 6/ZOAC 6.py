n = int(input())
answer = 0
for _ in range(n):
    line = input()
    if "01" in line or "OI" in line:
        answer += 1
        
print(answer)