import sys
sys.setrecursionlimit(100000)

def find(room):
    global hash
    if room not in hash:
        hash[room] = room + 1
        return room
    else:
        next_room = find(hash[room])
        hash[room] = next_room
        return next_room

def solution(k, room_number):
    global hash
    answer = []
    hash = {}
    for room in room_number:
        answer.append(find(room))
    return answer