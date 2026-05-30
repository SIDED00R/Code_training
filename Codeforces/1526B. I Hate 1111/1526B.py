def able(num):
    key = num % 11
    return 111 * key <= num
    
t = int(input())
for _ in range(t):
    num = int(input())
    if able(num):
        print("YES")
    else:
        print("NO")