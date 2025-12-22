stack = []
while True:
    try:
        stack.extend(list(input().split()))
    except:
        break

new_stack = []
for num in stack[1:]:
    new_stack.append(num[::-1])

for num in sorted(map(int, new_stack)):
    print(num)