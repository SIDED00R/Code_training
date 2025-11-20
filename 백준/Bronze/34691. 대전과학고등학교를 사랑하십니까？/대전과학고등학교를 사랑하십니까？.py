dic = {"animal": "Panthera tigris", 'flower':'Forsythia koreana', 'tree': 'Pinus densiflora'}
while True:
    now = input()
    if now == "end":
        break
    else:
        print(dic[now])