from fractions import Fraction

def change(m1, m2, v1, v2):
    u1 = v1
    u2 = v2
    first_m = Fraction(m1 - m2, m1 + m2)
    second_m = Fraction(2 * m2, m1 + m2)
    third_m = Fraction(2 * m1, m1 + m2)
    v1 = first_m * u1 + second_m * u2
    v2 = third_m * u1 - first_m * u2
    return v1, v2

n = int(input())

m1 = 1
m2 = n ** 2
v1 = 0
v2 = 10

answer = 0
while True:
    answer += 1
    v1, v2 = change(m1, m2, v1, v2)
    if v1 > 0:
        v1 = -v1
        answer += 1
    if v2 < 0 and abs(v2) >= abs(v1):
        break

print(answer)