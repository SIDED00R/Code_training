import sys
input = sys.stdin.readline
from collections import deque

def printer(arr, reverse):
    answer = "["
    if reverse:
        for num in arr[::-1]:
            answer += num
            answer += ","
    else:
        for num in arr:
            answer += num
            answer += ","
    if answer[-1] == ",":
        return answer[:-1] + "]"
    else:
        return answer + "]"

T = int(input())
for _ in range(T):
    reverse = False
    p = list(input().rstrip('\n'))
    n = int(input())
    if n:
        arr = deque(list(input().lstrip("[").rstrip("]\n").split(",")))
    else:
        arr = input()
        arr = []
    try:
        for case in p:
            if reverse and case == "D":
                arr.pop()
            elif not reverse and case == "D":
                arr.popleft()
            elif case == "R":
                if reverse:
                    reverse = False
                else:
                    reverse = True
        print(printer(list(arr), reverse))  
    except:
        print("error")
