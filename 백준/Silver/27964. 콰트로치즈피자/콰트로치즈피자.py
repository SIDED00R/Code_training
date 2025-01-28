n = int(input())

topping = list(input().split())
dic = {}
for cheese in topping:
    if cheese[-6:] == "Cheese":
        dic[cheese] = 1

if len(dic) >= 4:
    print("yummy")
else:
    print("sad")