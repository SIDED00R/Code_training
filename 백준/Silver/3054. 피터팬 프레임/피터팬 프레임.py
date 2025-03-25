def wendy(letter):
    fir = "..*.."
    sec = ".*.*."
    thi = f"*.{letter}.*"
    fou = ".*.*."
    fiv = "..*.."
    return fir, sec, thi, fou, fiv

def peter(letter):
    fir = ".#.."
    sec = "#.#."
    thi = f".{letter}.#"
    fou = "#.#."
    fiv = ".#.."
    return fir, sec, thi, fou, fiv

word = input()

answer = [".", ".", "#", ".", "."]

for idx in range(1, len(word) + 1):
    if idx % 3 == 0:
        fir, sec, thi, fou, fiv = wendy(word[idx - 1])
        answer[0] = answer[0][:-1] + fir
        answer[1] = answer[1][:-1] + sec
        answer[2] = answer[2][:-1] + thi
        answer[3] = answer[3][:-1] + fou
        answer[4] = answer[4][:-1] + fiv
    else:
        fir, sec, thi, fou, fiv = peter(word[idx - 1])
        answer[0] += fir
        answer[1] += sec
        answer[2] += thi
        answer[3] += fou
        answer[4] += fiv
        
for l in answer:
    print(l)
        