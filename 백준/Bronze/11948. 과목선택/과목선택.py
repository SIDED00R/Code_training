first = []
second = []
for _ in range(4):
    num = int(input())
    first.append(num)
for _ in range(2):
    num = int(input())
    second.append(num)
    
first.sort()
second.sort()
print(sum(first[1:]) + second[-1])