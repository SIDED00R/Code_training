dic = {'k':0, 'p':0, 'l':0}
for _ in range(3):
    name = input()
    if name[0] in dic:
        dic[name[0]] += 1
find = True
for k, v in dic.items():
    if v == 0:
        find = False
   
if find:
    print('GLOBAL')
else:
    print('PONIX')