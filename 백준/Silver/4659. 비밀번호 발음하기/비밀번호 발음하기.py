def same(word):
    for idx in range(1, len(word)):
        if word[idx - 1] == word[idx] and word[idx] not in ["o", "e"]:
            return False
    return True
        
def three_same(word):
    for idx in range(2, len(word)):
        if all(alp in ["a", "e", "i", "o", "u"] for alp in word[idx - 2:idx + 1]) or all(ch not in ["a", "e", "i", "o", "u"] for ch in word[idx - 2:idx + 1]): 
            return False
    return True

while True:
    word = input()
    if word == "end":
        break
    if any(alp in word for alp in ["a", "e", "i", "o", "u"]) and same(word) and three_same(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")