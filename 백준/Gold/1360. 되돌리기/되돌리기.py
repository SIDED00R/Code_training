n = int(input())
total_stack = []
for _ in range(n):
    total_stack.append(list(input().split()))

answer = []
while total_stack:
    state, key, time = total_stack.pop()
    if state == 'type':
        answer.append(key)
    else:
        bound = int(time) - int(key)
        while total_stack:
            ls, lk, lt = total_stack[-1]
            if int(lt) >= bound:
                total_stack.pop()
            else:
                break


print("".join(answer[::-1]))