n = int(input())
for _ in range(n):
    g = int(input())
    student = []
    for _ in range(g):
        student.append(int(input()))
    find = True
    answer = len(student)
    while find:
        find = False
        dic = {}
        for s in student:
            d = s % answer
            if d in dic:
                answer += 1
                find = True
                break
            else:
                dic[d] = 1
                
    print(answer)