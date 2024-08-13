a, b = map(int, input().split())
a -= 1
b -= 1
a_r, a_q = a % 4, a // 4
b_r, b_q = b % 4, b // 4
answer = abs(a_r - b_r) + abs(a_q - b_q)
print(answer)