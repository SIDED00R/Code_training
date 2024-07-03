n, h, w = map(int, input().split())
words = []
for _ in range(h):
    words.append(input())
    
answer = ""
for idx in range(n):
    alp = "?"
    find = False
    for i in range(w):
        if find:
            break
        for j in range(h):
            if words[j][i + idx * w] != "?":
                alp = words[j][i + idx * w]
                find = True
                break
            
    answer += alp
    
print(answer)