n = int(input())
now = []
for _ in range(n):
    command = input()
    if command == "pwd":
        answer = "/".join(now)
        if answer == "":
            print("/")
        else:
            print("/" + answer + "/")
    else:
        _, path = command.split()
        for now_case in path.split("/"):
            if now_case == "":
                now = []
            elif now_case == "..":
                now.pop()
            else:
                now.append(now_case)