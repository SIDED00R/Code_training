people = list(map(int, input().split()))
x, y, r = map(int, input().split())
for idx in range(len(people)):
    if people[idx] == x:
        print(idx + 1)
        exit()
        
print(0)