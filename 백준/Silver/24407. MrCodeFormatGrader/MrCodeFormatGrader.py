def printer(symbol, l):
    print(f"{symbol}: ", end = "")
    if len(l) > 1:
        for now_case in l[:-2]:
            start, end = now_case
            if start == end:
                print(f"{start}, ", end = "")
            else:
                print(f"{start}-{end}, ", end = "")
        start, end = l[-2]
        if start == end:
            print(start, end = "")
        else:
            print(f"{start}-{end}", end = "")
        print(" and ", end = "")
    start, end = l[-1]
    if start == end:
        print(start)
    else:
        print(f"{start}-{end}")
    
n, m = map(int, input().split())
line = list(map(int, input().split()))

error = []
correct = []

error_start = line[0]
now_error = line[0]
for idx in range(1, m):
    if line[idx] == now_error + 1:
        now_error += 1
    else:
        error.append([error_start, now_error])
        error_start = line[idx]
        now_error = line[idx]
error.append([error_start, now_error])


if error[0][0] != 1:
    correct.append([1, error[0][0] - 1])
correct_start = error[0][1] + 1
for i in range(1, len(error)):
    correct.append([correct_start, error[i][0] - 1])
    correct_start = error[i][1] + 1
if correct_start <= n:
    correct.append([correct_start, n])


printer("Errors", error)
printer("Correct", correct)