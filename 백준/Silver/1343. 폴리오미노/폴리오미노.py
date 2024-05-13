line = input()

def change(count, answer):
    if count % 2 == 1:
        return -1
    answer += "AAAA" * (count // 4)
    answer += "BB" * ((count % 4) // 2)
    return answer

count = 0
answer = ""
for  letter in line:
    if letter == ".":
        if count % 2 == 1:
            answer = -1
            break
        answer = change(count, answer)
        answer += "."
        count = 0
    else:
        count += 1
answer = change(count, answer)   
print(answer)
