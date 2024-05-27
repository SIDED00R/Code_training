N = int(input())
platforms = []

for _ in range(N):
    Y, X1, X2 = map(int, input().split())
    platforms.append((Y, X1, X2))
platforms.sort()

total_pillar_length = 0
for i in range(N):
    Y, X1, X2 = platforms[i]
    left_support_height = 0
    right_support_height = 0

    for j in range(N):
        if j == i:
            continue
        Y2, X1_2, X2_2 = platforms[j]
        
        if X1_2 < X1 + 0.5 < X2_2 and Y > Y2:
            left_support_height = max(left_support_height, Y2)
        
        if X1_2 < X2 - 0.5 < X2_2 and Y > Y2:
            right_support_height = max(right_support_height, Y2)

    total_pillar_length += (Y - left_support_height)
    total_pillar_length += (Y - right_support_height)

print(total_pillar_length)
