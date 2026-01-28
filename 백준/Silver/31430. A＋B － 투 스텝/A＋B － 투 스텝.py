t = int(input())
if t == 1:
    a, b = map(int, input().split())
    total = a + b
    stack = [0] * 13
    idx = 0
    while total:
        stack[idx] = total % 26
        total //= 26
        idx += 1
    answer = ""
    for i in range(13):
        answer += chr(stack[i] + 97)
    print(answer)

else:
    word = input()
    stack = []
    for alp in word:
        stack.append(ord(alp) - 97)
    answer = 0
    for i in range(13):
        answer += (26 ** i) * stack[i]
    print(answer)