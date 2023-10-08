def solution(skill, skill_trees):
    saved = list(skill)
    answer = 0
    for s in skill_trees:
        skill = saved[:]
        impossible = False
        for alp in s:
            print(skill)
            if alp == skill[0]:
                skill.pop(0)
            elif alp in skill[1:]:
                impossible = True
                break
            if len(skill) == 0:
                break
        if not impossible:
            answer += 1
            
    return answer