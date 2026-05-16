n = int(input())
dic = {}
for _ in range(n):
    request = input()
    if request not in dic:
        dic[request] = 0
        print("OK")
    else:
        dic[request] += 1
        print(f"{request}{dic[request]}")