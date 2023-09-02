def solution(numbers):
    number = ""
    answer = 0
    case = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for letter in numbers:
        number += letter
        if number in case:
            answer = answer * 10 + case.index(number)
            number = ""
    return answer