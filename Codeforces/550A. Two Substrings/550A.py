import sys
input = sys.stdin.readline

word = input()
ab_stack = []
ba_stack = []
length = len(word)
for idx in range(length):
    if word[idx] == "A" and idx < length - 1 and word[idx + 1] == "B":
        ab_stack.append([idx, idx + 1])
    if word[idx] == "B" and idx < length - 1 and word[idx + 1] == "A":
        ba_stack.append([idx, idx + 1])

for first_case in ab_stack:
    for second_case in ba_stack:
        if first_case[0] != second_case[1] and first_case[1] != second_case[0]:
            print("YES")
            exit()
print("NO")