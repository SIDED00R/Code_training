while True:
    line = input()
    if line == ".":
        break
    answer = ""
    count = 0
    keep = []
    keep_simbol = 0

    for s in line:
        if s == "-":
            count -= 1
        elif s == "+":
            count += 1
        elif s == "[":
            keep_simbol += 1
            keep.append("pin")
        elif s == "]":
            keep_simbol -= 1
            reverse_letter = ""
            while keep:
                now_out = keep.pop()
                if now_out == "pin":
                    break
                reverse_letter += now_out[::-1]
            if keep_simbol != 0:
                keep.append(reverse_letter)
            else:
                answer += reverse_letter
        elif s.isalpha():
            now_letter = chr((ord(s) + count - 65) % 26 + 65)
            if keep_simbol:
                keep.append(now_letter)
            else:
                answer += now_letter
            count = 0
        elif s == "?":
            if keep_simbol:
                keep.append("A")
            else:
                answer += "A"
            count = 0

    print(answer)
