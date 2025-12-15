def rotate(line):
    length = int(len(line) ** 0.5)
    answer = [0] * len(line)
    for i in range(length):
        for j in range(length):
            answer[i * length + j] = line[j * length + length - i - 1]
    return answer

n = int(input())
for _ in range(n):
    line = input()
    print("".join(rotate(line)))