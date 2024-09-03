while True:
    line = input()
    if line == "#":
        break
    answer = 0
    for letter in line.lower():
        if letter in ["a", "e", "i", "o", "u"]:
            answer += 1
    print(answer)