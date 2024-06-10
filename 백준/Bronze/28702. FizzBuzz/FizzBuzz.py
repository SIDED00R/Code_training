words = []
for i in range(3):
    line = input()
    words.append(line)
    if line.isnumeric():
        num = int(line) + 3 - i
        
answer = ""
if num % 3 == 0:
    answer += "Fizz"
    
if num % 5 == 0:
    answer += "Buzz"

if answer == "":
    print(num)
else:
    print(answer)