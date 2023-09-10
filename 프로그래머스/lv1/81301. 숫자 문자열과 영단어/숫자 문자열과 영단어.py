def solution(s):
    word = ""
    answer = ""
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for letter in s:
        if letter.isdigit():
            answer += letter
        else:
            word += letter
            if word in number:
                answer += str(number.index(word))
                word = ""
    return int(answer)