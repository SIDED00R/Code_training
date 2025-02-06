n = int(input())
line = input()
count = 0
for letter in line:
    if letter in ["a", "e", "i", "o", "u"]:
        count += 1
        
print(count)