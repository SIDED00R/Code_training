import copy

n = int(input())

star = ["*"]
patterns = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0]]

for num in range(n):
    blank = " " * (5 ** num)
    next_star = []
    for i in range(5):
        pattern = patterns[i]
        for j in range(len(star)):
            line = ""
            for check in pattern:
                if check:
                    line += star[j]
                else:
                    line += blank
            next_star.append(line)
    star = copy.deepcopy(next_star)
        
for l in star:
    print(l)
        
    