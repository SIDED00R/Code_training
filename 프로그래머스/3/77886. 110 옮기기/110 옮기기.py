def solution(s):
    answer = []
    for case in s:
        stack = []
        count = 0
        moved = []
        for num in case:
            if num == "1":
                count += 1
            if num == "0" and count >= 2:
                stack.pop()
                stack.pop()
                count -= 2
                moved += ["1", "1", "0"]
                continue
            elif num == "0":
                count = 0
            stack.append(num)
        check = 0
        for idx in range(len(stack)):
            if stack[idx] == "0":
                check = 0
                continue
            else:
                check += 1
                if check == 2:
                    stack = stack[:idx - 1] + moved + stack[idx - 1:]
                    break
        if check == 0:
            stack += moved
        elif check == 1:
            stack.pop()
            stack += moved
            stack.append("1")
        answer.append("".join(stack))
    return answer