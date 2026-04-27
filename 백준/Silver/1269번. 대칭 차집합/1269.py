a, b = map(int, input().split())
a_list = set(map(int, input().split()))
b_list = list(map(int, input().split()))
for num in b_list:
    a_list.add(num)
    
print(a + b - 2 * (b - len(a_list) + a))