import sys
from bisect import bisect_right
input = sys.stdin.readline

def find(x):
    if x not in parent:
        return x
    parent[x] = find(parent[x])
    return parent[x]

N, M, K = map(int, input().split())
cards = sorted(map(int, input().split()))
cheolsu = list(map(int, input().split()))

parent = {} 

out = []
for num in cheolsu:
    i = bisect_right(cards, num)  
    i = find(i)         
    out.append(str(cards[i]))
    parent[i] = find(i + 1)     

sys.stdout.write("\n".join(out))
