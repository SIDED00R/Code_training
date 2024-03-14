import sys
input = sys.stdin.readline
from collections import defaultdict

def make_list(arr):
    ans = []
    for i in range(len(arr)):
        now = arr[i]
        ans.append(now)
        for j in range(i + 1, len(arr)):
            now += arr[j]
            ans.append(now)
            
    return ans

def make_dic(arr):
    dic = defaultdict(int)
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            dic[total] += 1
            
    return dic

T = int(input())
n = int(input())
A = list(map(int, input().rstrip('\n').split()))
m = int(input())
B_list = list(map(int, input().rstrip('\n').split()))

A_list = sorted(make_list(A))
B_dict = make_dic(B_list)

answer = 0
for num in A_list:
    answer += B_dict[T - num]
    
print(answer)
