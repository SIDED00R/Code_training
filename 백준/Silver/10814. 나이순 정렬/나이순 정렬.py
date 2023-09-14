import sys
n = int(input())

memberlist = []
for _ in range(n):
    people = sys.stdin.readline().split()
    memberlist.append(people)

memberlist = sorted(memberlist, key = lambda x: int(x[0]))

for member in memberlist:
    print(" ".join(member))
