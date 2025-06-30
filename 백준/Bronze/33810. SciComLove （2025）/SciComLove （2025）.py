word = 'SciComLove'
line = input()
answer = 0
for idx in range(len(word)):
    if word[idx] != line[idx]:
        answer += 1
        
print(answer)