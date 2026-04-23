def check(word):
    for idx in range(len(word) // 2):
        if word[idx] == word[-idx - 1]:
            continue
        else:
            return False
    return True
    
s = input()
for i in range(len(s)):
    if check(s[i:]):
        print(len(s) + i)
        exit()