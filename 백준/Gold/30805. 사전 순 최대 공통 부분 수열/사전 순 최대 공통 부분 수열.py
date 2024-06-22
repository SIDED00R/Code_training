n = int(input())
a_line = list(map(int, input().split()))
m = int(input())
b_line = list(map(int, input().split()))

num = 100
answer = []
while num >= 1:
    if num in a_line and num in b_line:
        a_line = a_line[a_line.index(num) + 1:]
        b_line = b_line[b_line.index(num) + 1:]
        answer.append(num)
    else:
        num -= 1
        
print(len(answer))
for number in answer:
    print(number, end = " ")