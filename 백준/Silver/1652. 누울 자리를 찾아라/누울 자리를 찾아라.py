import copy

N = int(input())
room = []
for _ in range(N):
    room.append(list(input()))
    
count_r = 0
count_c = 0

room_c = copy.deepcopy(room)
for i in range(N):
    for j in range(N):
        find = False
        if room_c[i][j] ==".":
            next_i = i
            next_j = j + 1
            while 0 <= next_i < N and 0 <= next_j < N and room_c[next_i][next_j] == ".":    
                find = True
                room_c[next_i][next_j] = "X"
                next_j += 1
            if find:
                room_c[i][j] = "X"
                count_c += 1

                    
for i in range(N):
    for j in range(N):
        find = False
        if room[i][j] ==".":
                next_i = i + 1
                next_j = j
                while 0 <= next_i < N and 0 <= next_j < N and room[next_i][next_j] == ".":
                    find = True
                    room[next_i][next_j] = "X"
                    next_i += 1
                if find:
                    room[i][j] = "X"
                    count_r += 1
                    
print(count_c, count_r)