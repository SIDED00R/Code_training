def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    student = [1 for _ in range(n)]
    for l in lost:
        student[l - 1] = 0
    for res in reserve:
        if student[res - 1] != 1:
            student[res - 1] = "r"
        elif student[max(res - 2, 0)] == 0:
            student[max(res - 2, 0)] = "r"
        elif student[min(res, n - 1)] == 0:
            student[min(res, n - 1)] = "r"
            
    return n - student.count(0)