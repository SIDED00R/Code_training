def newmerge(numbers):
    if len(numbers) < 2:
        return numbers

    mid = len(numbers) // 2
    left = newmerge(numbers[:mid])
    right = newmerge(numbers[mid:])
    
    answer = []
    low, high = 0, 0

    while low < len(left) and high < len(right):
        l = left[low]
        r = right[high]
        
        if int(l + r) < int(r + l):
            answer.append(r)
            high += 1
        else:
            answer.append(l)
            low += 1

    answer += left[low:]
    answer += right[high:]
    
    return answer

def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers = newmerge(numbers)
    answer = "".join(numbers)
    return "0" if answer[0] == "0" else answer
