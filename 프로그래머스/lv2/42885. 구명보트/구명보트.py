def solution(people, limit):
    people = sorted(people)
    i, j = 0, len(people) - 1
    answer = 0
    
    while i <= j:
        total = 0
        
        if total + people[j] <= limit:
            total += people[j]
            j -= 1
        
        if total + people[i] <= limit:
            total += people[i]
            i += 1
        
        answer += 1
        
    return answer