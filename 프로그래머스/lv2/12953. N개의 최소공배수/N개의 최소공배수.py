def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def lcd(num1, num2):
    if num1 > num2:
        g = gcd(num1, num2)
    else:
        g = gcd(num2, num1)
    return num1 * num2 // g
    

def solution(arr):
    answer = 1
    for i in arr:
        if answer % i != 0:
            answer = lcd(answer, i)
             
    return answer