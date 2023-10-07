def solution(record):
    ans = []
    answer = []
    people = {}
    
    # info[0] : event, info[1] : user_id, info[2] : name
    
    for i in record:
        info = i.split()
        if info[0] !="Leave":
            people[info[1]] = info[2]
        ans.append([info[0], info[1]])
    
    for i in ans:
        if i[0] == "Change":
            continue
        answer.append(f"{people[i[1]]}님이 {'들어왔' if i[0] == 'Enter' else '나갔'}습니다.")
    
    return answer