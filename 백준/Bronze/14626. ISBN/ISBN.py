num = input()
answer = 0
keep = -1
for idx, n in enumerate(num):
    if n == '*':
        keep = idx
        continue
    else:
        if idx % 2 == 0:
            answer += int(n)
        else:
            answer += int(n) * 3
            
for able in range(10):
    if keep % 2 == 0:
        if (able + answer) % 10 == 0:
            print(able)
    else:
        if (answer + 3 * able) % 10 == 0:
            print(able)