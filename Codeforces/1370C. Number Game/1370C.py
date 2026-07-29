def find(num):
    answer = 0
    for i in range(2, int(num ** 0.5) + 1):
        count = 0
        while num % i == 0:
            count += 1
            num //= i
        if i % 2 == 1:
            answer += count
    if num != 1 and num % 2 == 1:
        answer += 1
    return answer
            
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print("FastestFinger")
    elif n == 2:
        print("Ashishgup")
    elif n % 2 == 1:
        print("Ashishgup")
    else:
        count = find(n)
        if n % 4 != 0:
            if count == 1:
                print("FastestFinger")
            else:
                print("Ashishgup")
        else:
            if count == 0:
                print("FastestFinger")
            else:
                print("Ashishgup")