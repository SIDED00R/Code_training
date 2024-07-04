total = input()
c_count = 0
d_count = 0
answer = 1

for case in total:
    if case == "c":
        if d_count != 0:
            digit = 10
            for _ in range(d_count - 1):
                digit *= 9
            answer *= digit
            d_count = 0
        c_count += 1
            
    else:
        if c_count != 0:
            digit = 26
            for _ in range(c_count - 1):
                digit *= 25
            answer *= digit
            c_count = 0
        d_count += 1
    answer %= 1000000009
   


if d_count != 0:
    digit = 10
    for _ in range(d_count - 1):
        digit *= 9
    answer *= digit
else:
    digit = 26
    for _ in range(c_count - 1):
        digit *= 25
    answer *= digit
print(answer % 1000000009)