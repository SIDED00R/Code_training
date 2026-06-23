import sys
input = sys.stdin.readline

word = input()
a_ab = False
a_ba = False
b_ab = False
b_ba = False
bab = False
aba = False
for idx in range(len(word)):
    if word[idx] == "A":
        if (idx > 0 and word[idx - 1] == "B") and (idx < len(word) - 1 and word[idx + 1] == "B"):
            if aba:
                a_ab = True
                a_ba = True
            else:
                aba = True
        elif idx > 0 and word[idx - 1] == "B":
            a_ba = True
        elif idx < len(word) - 1 and word[idx + 1] == "B":
            a_ab = True
    if word[idx] == "B":
        if (idx > 0 and word[idx - 1] == "A") and (idx < len(word) - 1 and word[idx + 1] == "A"):
            if bab:
                b_ab = True
                b_ba = True
            else:
                bab = True
        elif idx > 0 and word[idx - 1] == "A":
            b_ba = True
        elif idx < len(word) - 1 and word[idx + 1] == "A":
            b_ab = True
if a_ab and a_ba and b_ab and b_ba:
    print("YES")
else:
    print("NO")