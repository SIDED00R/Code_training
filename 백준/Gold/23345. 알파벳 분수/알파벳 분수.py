def find(up, down):
    now_stack = []
    now_num = up[-1]
    if len(up) == 1:
        now_stack.append(up[0])
        while down:
            out = down.pop()
            now_stack.append(out)
        answer_stack.append(now_stack)
        return
    up_out = up.pop()
    now_stack.append(up_out)
    while len(down) > 1:
        if now_num + 2 == down[-2]:
            down_out = down.pop()
            now_stack.append(down_out)
            now_num += 1
        else:
            break
    answer_stack.append(now_stack)
    find(down, up)
                    
up, down = input().split("/")
up = sorted(up, reverse = True)
down = sorted(down, reverse = True)
if up[-1] != "A" or down[-1] != "B":
    print("None")
    exit()
up = list(map(ord, up))
down = list(map(ord, down))

answer_stack = []
find(up, down)

answer = []
for now_case in answer_stack:
    if len(now_case) == 1:
        answer.append(chr(now_case[0]))
    else:
        front = chr(now_case[0])
        for num in now_case[1:]:
            front = "(" + front + "/" + chr(num) + ")"
        answer.append(front)

back = answer[-1]
for now_case in answer[::-1][1:]:
    back = "(" + now_case + "/" + back + ")"
print(back)
