def check(binary, able):
    start = 0
    end = len(binary) - 1
    if able[0]:
        now = (start + end) // 2
        if binary[now] != 1:
            able[0] = False
            return
        else:
            if sum(binary[:now]) > 0:
                check(binary[:now], able)
            if sum(binary[now + 1:]) > 0:
                check(binary[now + 1:], able)
    
def solution(numbers):
    answer = []
    for number in numbers:
        binary = []
        while number != 0:
            binary.append(number % 2)
            number //= 2
        length = 1
        while len(binary) > length:
            length = length * 2 + 1
        binary += [0] * (length - len(binary))
        able = [True]
        check(binary, able)
        if able[0]:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer