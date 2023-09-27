while True:

    n = input()
    if n == ".":
        break

    stack = []
    for alp in n:
        if alp == "(" or alp == "[":
            stack.append(alp)
        elif alp == ")":
            if len(stack) == 0:
                print("no")
                break
            elif stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break

        elif alp == "]":
            if len(stack) == 0:
                print("no")
                break
            elif stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break


        elif alp == ".":
            if len(stack) == 0:
                print("yes")
            else:
                print("no")
            break