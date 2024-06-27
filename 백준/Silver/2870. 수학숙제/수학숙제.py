import heapq

n = int(input())

stack = []
for _ in range(n):
    line = input()
    cases = ""
    for num in line:
        if num.isnumeric():
            cases += num
        else:
            if cases != "":
                heapq.heappush(stack, int(cases))
                cases = ""        
    if cases != "":
        heapq.heappush(stack, int(cases))
        
while stack:
    print(heapq.heappop(stack))