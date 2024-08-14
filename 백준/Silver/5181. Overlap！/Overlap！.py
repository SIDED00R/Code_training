k = int(input())

def change_time(t):
    start, end = t.split("-")
    sh, sm = start.split(":")
    eh, em = end.split(":")
    start_time = int(sh) * 60 + int(sm)
    end_time = int(eh) * 60 + int(em)
    return start_time, end_time

dic = {"M":0, "T":1, "W":2, "TH":3, "F":4}

for idx in range(k):
    answer = 0
    m, n = map(int, input().split())
    subjects = {}
    peoples = []
    for _ in range(m):
        class_name, day, time = input().split()
        start, end = change_time(time)
        subjects[class_name] = [day, start, end]
    for _ in range(n):
        time_table = [[0 for _ in range(60 * 24)] for _ in range(5)]
        now = list(input().split())
        for c in now:
            day, start, end = subjects[c]
            today = dic[day]
            time_table[today][start] += 1
            time_table[today][end] -= 1
        find = False
        for i in range(5):
            for j in range(1, 60 * 24):
                time_table[i][j] += time_table[i][j - 1]
                if time_table[i][j] >= 2:
                    answer += 1
                    find = True
                    break
            if find:
                break
        
        
    print(f"Data Set {idx + 1}:")
    print(answer)