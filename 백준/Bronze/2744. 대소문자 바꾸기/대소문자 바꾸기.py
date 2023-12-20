word = input()
answer = ""
for letter in word:
    if letter.isupper():
        answer += letter.lower()
    else:
        answer += letter.upper()
print(answer)