n = int(input())
for _ in range(n):
    total_line = ""
    while True:
        line = input()
        if line == "":
            error = 0
            total = len(total_line)
            for letter in total_line:
                if letter == "#":
                    error += 1
            
            out = round((1 - error / total) * 100, 1)
            if out == int(out):
                print(f"Efficiency ratio is {int(out)}%.")
            else:
                print(f"Efficiency ratio is {round((1 - error / total) * 100, 1)}%.")
            break
        else:
            total_line += line