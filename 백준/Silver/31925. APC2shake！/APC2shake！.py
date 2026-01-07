n = int(input())
stack = []
for _ in range(n):
    name, doing, reward, shake, score = input().split()
    shake, score = map(int, (shake, score)) 
    if doing == "jaehak" and reward == "notyet" and shake not in [1, 2, 3]:
        stack.append([score, name])
stack.sort()
print(min(len(stack), 10))
for score, name in sorted(stack[:10], key = lambda x:x[1]):
    print(name)