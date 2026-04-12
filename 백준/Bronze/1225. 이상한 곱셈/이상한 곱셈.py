from collections import Counter
a, b = input().split()
a_count = Counter(a)
b_count = Counter(b)
answer = 0
for a_k, a_v in a_count.items():
    for b_k, b_v in b_count.items():
        answer += int(a_k) * int(b_k) * a_v * b_v
print(answer)