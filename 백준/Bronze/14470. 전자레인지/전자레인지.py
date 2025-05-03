a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

answer = 0
if a < 0:
    answer += (-a) * c
    answer += d
    answer += b * e
    
else:
    answer += (b - a) * e
    
print(answer)