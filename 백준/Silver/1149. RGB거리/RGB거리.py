import sys
input = sys.stdin.readline

N = int(input())

red_dp = [0]
green_dp = [0]
blue_dp = [0]

for _ in range(N):
    r, g, b = map(int, input().rstrip('\n').split())
    red_now = r + min(green_dp[-1], blue_dp[-1])
    green_now = g + min(red_dp[-1], blue_dp[-1])
    blue_now = b + min(green_dp[-1], red_dp[-1])
    red_dp.append(red_now)
    green_dp.append(green_now)
    blue_dp.append(blue_now)
    
print(min(red_dp[-1], green_dp[-1], blue_dp[-1]))