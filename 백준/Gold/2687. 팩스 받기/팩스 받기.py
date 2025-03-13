def hex_to_bin(num):
    return bin(int(num, 16))[2:].zfill(8)

n = int(input())
for _ in range(n):
    b = int(input())
    line = ""
    for _ in range(b // 40 + 1):
        line += input()
    idx = 0
    answer = ""
    while idx < b * 2:
        trans = hex_to_bin(line[idx: idx + 2])
        if trans[0] == "0":
            length = int(trans[1:], 2) + 1
            answer += line[idx + 2: idx + 2 + 2 * length]
            idx += 2 + 2 * length
        else:
            repeat = int(trans[1:], 2) + 3
            answer += line[idx + 2: idx + 4] * repeat
            idx += 4

    ans_len = len(answer)
    print(ans_len // 2)
    i = 0
    while i * 80 < ans_len:
        print(answer[i * 80: i * 80 + 80])
        i += 1



