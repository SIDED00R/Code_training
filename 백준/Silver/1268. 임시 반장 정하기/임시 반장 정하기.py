N = int(input())
student_class = []
for _ in range(N):
    line = list(map(int, input().split()))
    student_class.append(line)
  
    
max_count = 0
answer = 1
for i in range(N):
    now = set()
    for j in range(N):
        if i != j:
            for idx in range(5):
                if student_class[i][idx] == student_class[j][idx]:
                    now.add(j)
                    break
    if max_count < len(now):
        max_count = len(now)
        answer = i + 1
        
print(answer)