letter = input()
answer = ""

count = 0
while True:
    num = ord(letter[0])
    if chr(num ^ count) == 'C':
        break
    else:
        count += 1

for alp in letter:
    num = ord(alp)
    answer += chr(num ^ count)
print(answer)