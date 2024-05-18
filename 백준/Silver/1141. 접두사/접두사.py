N = int(input())
words = []
for _ in range(N):
    words.append(input())
   
words = sorted(words, key = lambda x: -len(x))
answer = []
for word in words:
    check = True
    for case in answer:
        if case[:len(word)] == word:
            check = False
            break
    if check:
        answer.append(word)
        
print(len(answer))