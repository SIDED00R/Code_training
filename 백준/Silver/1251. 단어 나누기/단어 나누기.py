word = input()
n = len(word)
answer = ""
for i in range(1, n - 1):
    for j in range(i + 1, n):
        first = word[:i]
        second = word[i:j]
        third = word[j:]
        test = "".join([first[::-1], second[::-1], third[::-1]])
        if answer == "":
            answer = test
        elif answer > test:
            answer = test
            
print(answer)