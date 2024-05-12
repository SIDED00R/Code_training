A, B, N = map(int, input().split())
left = A % B
for _ in range(N):
    answer = left * 10 // B
    left = left * 10 % B
    
print(answer)