n = int(input())
line = list(map(int, input().split()))
sort_line = sorted(line)
start = -1
end = -1

for idx in range(n):
    if line[idx] != sort_line[idx]:
        if start == -1:
            start = idx
        else:
            end = idx
if start == -1:
    print("yes")
    print(1, 1)
    exit()
new_line = line[:start] + line[start:end + 1][::-1] + line[end + 1:]
if sort_line == new_line:
    print("yes")
    print(start + 1, end + 1)
else:
    print("no")