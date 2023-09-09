def solution(n, arr1, arr2):
    map1 = []
    map2 = []

    for num1 in arr1:
        line = ""
        for i in range(n):
            if num1 % 2 == 1:
                line += "1"
            else:
                line += "0"
            num1 //= 2
        map1.append(line[::-1])
    
    for num2 in arr2:
        line = ""
        for i in range(n):
            if num2 % 2 == 1:
                line += "1"
            else:
                line += "0"
            num2 //= 2
        map2.append(line[::-1])

    for i in range(n):
        line = ""
        for j in range(n):
            if map1[i][j] == "0":
                line += " "
            else :
                line += "#"
        map1[i] = line
    
    for i in range(n):
        line = ""
        for j in range(n):
            if map2[i][j] == "0":
                line += " "
            else :
                line += "#"
        map2[i] = line

    map = []
    for i in range(n):
        line = ""
        for j in range(n):    
            if map1[i][j] == "#" or map2[i][j] == "#":
                line += "#"
            else:
                line += " " 
        map.append(line)
    return map