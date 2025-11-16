from itertools import permutations

n = int(input())
num = list(input().split())
simbol = list(map(int, input().split()))

sim_list = []
dic = {0:"+", 1:"-", 2:"*", 3:"//"}
for idx in range(4):
    for _ in range(simbol[idx]):
        sim_list.append(dic[idx])

max_answer = -1e20
min_answer = 1e20

for now_case in set(permutations(sim_list, n - 1)):
    before_num = num[0]
    for idx in range(1, n):
        now_num = num[idx]
        if int(before_num) < 0 and now_case[idx - 1] == "//":
            before_num = "-" + str(eval(before_num[1:] + now_case[idx - 1] + now_num))
        else:
            before_num = str(eval(before_num + now_case[idx - 1] + now_num))
    max_answer = max(max_answer, int(before_num))
    min_answer = min(min_answer, int(before_num))

print(max_answer)
print(min_answer)