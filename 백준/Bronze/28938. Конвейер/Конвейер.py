n = int(input())
line = sum(list(map(int, input().split())))
if line == 0:
    print("Stay")
elif line > 0:
    print("Right")
else:
    print("Left")
