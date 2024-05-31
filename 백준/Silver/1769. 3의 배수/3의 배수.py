N = list(map(int, list(input())))
count = 0

while len(N) != 1:
    count += 1
    total = str(sum(N))
    N = list(map(int, list(total)))

print(count)
print("YES" if N[0] % 3 == 0 else "NO")
    