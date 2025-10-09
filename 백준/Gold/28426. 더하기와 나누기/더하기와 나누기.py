n = int(input())
answer = ["2"]
for i in range(1, n):
    answer.append(f"{4 * i}")
    
print(" ".join(answer))
    