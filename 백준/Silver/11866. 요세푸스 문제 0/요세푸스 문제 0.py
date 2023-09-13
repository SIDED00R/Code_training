a, b = input().split()
a, b = int(a), int(b)
nk = [i for i in range(1, a + 1)]
idx = 0
answer = []

while len(nk) != 0:
    idx += b
    while idx > len(nk):
        idx -= len(nk)
    num = nk.pop(idx - 1)
    idx -= 1
    answer.append(num)
sol = "<"
for num in answer[:-1]:
    sol += f"{num}, "
print(sol + f"{answer[-1]}>")

