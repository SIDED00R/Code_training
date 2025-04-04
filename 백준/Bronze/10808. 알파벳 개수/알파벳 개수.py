dic = {}
for i in range(26):
    dic[chr(i + 97)] = 0
word = input()
for letter in word:
    dic[letter] += 1
    
for k, v in dic.items():
    print(v, end = " ")
    