dic = {'k':0, 'p':1, 'n':3, 'b':3, 'r':5, 'q':9, '.':0}
answer = 0
for _ in range(8):
    line = list(input())
    for chess in line:
        if chess.isupper():
            answer += dic[chess.lower()]
        else:
            answer -= dic[chess]
print(answer)