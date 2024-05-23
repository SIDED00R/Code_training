for _ in range(3):
    N = int(input())
    answer = 0
    for _ in range(N):
        answer += int(input())
        
    if answer == 0:
        print("0")
    elif answer > 0:
        print("+")
    else:
        print("-")
        