dic = {'e': 'a', 'o': 'i', 'u': 'y', 'a': 'e', 'i': 'o', 'y': 'u', 'p': 'b', 'v': 'k', 'j': 'x', 'q': 'z', 't': 'n', 's': 'h', 'r': 'd', 'l': 'c', 'm': 'w', 'f': 'g', 'b': 'p', 'k': 'v', 'x': 'j', 'z': 'q', 'n': 't', 'h': 's', 'd': 'r', 'c': 'l', 'w': 'm', 'g': 'f'}

while True:
    try:
        line = input()
        answer = ""
        for letter in line:
            if letter.isalpha():
                if letter.isupper():
                    now_letter = letter.lower()
                    next_letter = dic[now_letter]
                    answer += next_letter.upper()
                else:
                    answer += dic[letter]
            else:
                answer += letter
        print(answer)
    except:
        break