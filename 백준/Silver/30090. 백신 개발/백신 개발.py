from itertools import permutations

n = int(input())
word = []
for _ in range(n):
    word.append(input())
    
    
length = 100
if n == 1:
    print(len(word[0]))
    exit()
for case in permutations(word, n):
    answer = case[0]
    for i in range(1, n):
        now = case[i]
        find = False
        for j in range(len(now)):
            if answer[-len(now) + j:] == now[:len(now) - j]:
                find = True
                answer += now[len(now) - j:]
                break
        if not find:
            break
    if not find:
        continue
    else:
        length = min(len(answer), length)
        
print(length)
                