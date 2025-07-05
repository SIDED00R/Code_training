word = input()
answer = 0
for idx in range(len(word)):
    if word[idx] in ['a', 'e', 'i', 'o', 'u']:
        answer += 1
        
print(answer)