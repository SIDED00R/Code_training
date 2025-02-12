t, e, f = map(int, input().split())
first = 3 * t + 20 * e + 120 * f

t, e, f = map(int, input().split())
second = 3 * t + 20 * e + 120 * f

if first > second:
    print("Max")
elif first == second:
    print("Draw")
else:
    print("Mel")