k = int(input())
for i in range(k):
    dic = {}
    n, c, l = map(int, input().split())
    for _ in range(n):
        num, drink = input().split()
        if num not in dic:
            dic[num] = {"I": 0, "S": 0}
        dic[num][drink] += 1
    peoples = []
    for _ in range(c):
        num, people = input().split()
        peoples.append((num, int(people)))
    peoples.sort(key = lambda x : -x[1])
    for num, people in peoples:
        if num in dic and dic[num]["S"] >= 1:
            dic[num]["S"] -= 1
            dic[num]["I"] -= (people - 1)
            if dic[num]["I"] < 0:
                dic[num]["S"] += dic[num]["I"]
                dic[num]["I"] = 0
    ans = 0         
    for key, value in dic.items():
        for k, v in value.items():
            if v > 0:
                ans += v
        
    print(f"Data Set {i + 1}:")
    print(ans)
