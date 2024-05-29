import sys
input = sys.stdin.readline

text = input().rstrip("\n")
check = input().rstrip("\n")
answer = 0
idx = 0
while idx < len(text):
    if text[idx:idx + len(check)] == check:
        idx += len(check)
        answer += 1
    else:
        idx += 1
        
print(answer)