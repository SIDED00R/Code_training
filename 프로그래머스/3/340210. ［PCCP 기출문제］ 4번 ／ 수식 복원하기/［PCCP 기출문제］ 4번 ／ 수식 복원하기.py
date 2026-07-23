def revert(num, digit):
    answer = []
    while num != 0:
        answer.append(str(num % digit))
        num //= digit
    if not answer:
        answer = ["0"]
    return "".join(answer[::-1])


def solution(lines):
    before_answer = []
    for now in range(2, 10):
        answer = []
        able = True
        for line in lines:
            try:
                first, simbol, second, _, ans = line.split()
                first_d = int(first, now)
                second_d = int(second, now)
                if ans != 'X':
                    ans = int(ans, now)
                    if eval(str(first_d) + simbol + str(second_d)) != ans:
                        able = False
                        break
                else:
                    now_ans = eval(str(first_d) + simbol + str(second_d))
                    answer.append(f"{first} {simbol} {second} = {revert(now_ans, now)}")
            except:
                able = False
                break
        if able:
            if not before_answer:
                before_answer = answer[:]
            else:
                for idx, now_case in enumerate(before_answer):
                    if answer[idx] == now_case:
                        continue
                    else:
                        first, si, second, eql, ans = before_answer[idx].split()
                        before_answer[idx] = f"{first} {si} {second} = ?"
                    
    return before_answer
