from collections import defaultdict

try:
    while True:
        n = int(input())
        dic = defaultdict(int)
        while True:
            line = input()
            if line == "EndOfText":
                break
            now_letter = ""
            for alp in line:
                if alp.isalpha():
                    now_letter += alp.lower()
                else:
                    dic[now_letter] += 1
                    now_letter = ""
            if now_letter != "":
                dic[now_letter] += 1
        answer = []
        for k, v in dic.items():
            if v == n:
                answer.append(k)
        if answer:
            for ans in sorted(answer):
                print(ans)
        else:
            print("There is no such word.")
        print()
except:
    exit()