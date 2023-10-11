def calculate(num, first, second, third): 
    total = []
    number = ""
    for letter in num:
        if letter.isnumeric():
            number += letter
        else:
            total.append(int(number))
            number = ""
            total.append(letter)
    total.append(int(number))
    
    for simbol in [first, second, third]:
        new = []
        sim = ""
        for i in range(len(total)):
            if sim =="":
                if total[i] == simbol:
                    sim = total[i]
                else:
                    new.append(total[i])
            else:    
                if simbol == "+":
                    new[-1] += total[i]
                elif simbol == "-":
                    new[-1] -= total[i]
                elif simbol == "*":
                    new[-1] *= total[i]
                sim = ""
        total = new[:]
    return total[0]
            
def solution(expression):
    answer = []
    answer.append(calculate(expression, "+", "-", "*"))
    answer.append(calculate(expression, "+", "*", "-"))
    answer.append(calculate(expression, "-", "+", "*"))
    answer.append(calculate(expression, "-", "*", "+"))
    answer.append(calculate(expression, "*", "+", "-"))
    answer.append(calculate(expression, "*", "-", "+"))
    return max(max(answer), -min(answer))