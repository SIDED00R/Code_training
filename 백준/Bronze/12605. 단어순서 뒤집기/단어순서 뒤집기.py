n = int(input())
for i in range(n):
    line = list(input().split())
    print(f"Case #{i + 1}: {' '.join(line[::-1])}")