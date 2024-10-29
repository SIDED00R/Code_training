n, k = map(int, input().split())
if n == 2:
    print("YES")
    for _ in range(5):
        print("swap 1 2")
elif n == 3:
    print("NO")
else:
    print("YES")
    if k == 1:
        print("swap 1 2")
        print(f"reverse 2 {n}")
        print(f"reverse 2 {n - 1}")
        print("swap 1 2")
        print("swap 1 2")
    elif k == n - 1:
        print(f"swap {n - 1} {n}")
        print(f"reverse 1 {n - 1}")
        print(f"reverse 2 {n - 1}")
        print("swap 1 2")
        print("swap 1 2")
    else:
        print(f"reverse 1 {k}")
        print(f"reverse {k + 1} {n}")
        print(f"reverse 1 {n}")
        print("swap 1 2")
        print("swap 1 2")