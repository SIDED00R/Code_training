n = int(input())
for i in range(n - 1):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))
print("*" * (2 * n - 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))