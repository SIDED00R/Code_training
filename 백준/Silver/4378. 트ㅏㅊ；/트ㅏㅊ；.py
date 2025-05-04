while True:
    try:
        letter = input()
        letter = letter.replace("`", "").replace("Q", "").replace("A", "").replace("Z", "")
        in_word = "1234567890-=WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./"
        out_word = "`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,."

        answer = letter.maketrans(in_word, out_word)
        print(letter.translate(answer))
    except:
        break