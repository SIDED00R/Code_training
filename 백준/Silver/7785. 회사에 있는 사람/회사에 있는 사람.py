N = int(input())
dic = {}
for _ in range(N):
    name, state = input().split()
    if state == "enter":
        dic[name] = 1
    else:
        dic[name] = 0
      
answer = []
for key, value in dic.items():
    if value == 1:
        answer.append(key)
for name in sorted(answer, reverse = True):
    print(name)