from collections import defaultdict, deque

def find(weight, stack, time, road):
    while stack:
        out = stack.popleft()
        now_weight = weight[out]
        for next_node in road[out]:
            w = time[(out, next_node)]
            if weight[next_node] > w + now_weight:
                weight[next_node] = w + now_weight
                stack.append(next_node)
    return weight

n, m, k = map(int, input().split())
time = {}
road = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, input().split())
    time[(a, b)] = t
    time[(b, a)] = t
    road[a].append(b)
    road[b].append(a)

you_list = list(map(int, input().split()))

my_weight = [1e20 for _ in range(n + 1)]
your_weight = [1e20 for _ in range(n + 1)]
my_weight[1] = 0
for idx in you_list:
    your_weight[idx] = 0

my_weight = find(my_weight, deque([1]), time, road)
your_weight = find(your_weight, deque(you_list), time, road)

answer = []
for idx in range(2, n + 1):
    if my_weight[idx] < your_weight[idx]:
        answer.append(idx)
if answer:
    for num in sorted(answer):
        print(num)
else:
    print(0)