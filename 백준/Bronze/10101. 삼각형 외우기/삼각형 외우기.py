answer = []
for _ in range(3):
    answer.append(int(input()))
  
if sum(answer) != 180:
    print("Error")
elif answer[0] == answer[1] and answer[0] == answer[2]:
    print("Equilateral")
elif answer[0] == answer[1] or answer[0] == answer[2] or answer[1] == answer[2]:
    print("Isosceles")
else:
    print("Scalene")