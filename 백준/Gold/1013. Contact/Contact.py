import  re

pattern = r'((100+1+)|01)+'
n = int(input())
for _ in range(n):
    string = input()
    result = re.fullmatch(pattern, string)
    if result:
        print("YES")
    else:
        print("NO")